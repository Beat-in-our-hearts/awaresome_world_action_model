#!/usr/bin/env python3
"""Download arXiv papers into the repository paper layout.

This script supports:
- alias-based downloads through `scripts/paper_ids.py`
- track-aware storage under `docs/papers/embodied_robotics/` or
  `docs/papers/autonomous_driving/` or `docs/papers/foundational_works/`
- automatic track detection for known aliases and known arXiv IDs
- incremental updates that skip valid local files
- optional PDF-only or source-only refreshes

Examples:
    python3 scripts/paper_download.py dreamzero --proxy http://127.0.0.1:7890
    python3 scripts/paper_download.py driveva --proxy http://127.0.0.1:7890
    python3 scripts/paper_download.py serl --proxy http://127.0.0.1:7890
    python3 scripts/paper_download.py --from-file ids.txt --workers 4 --proxy http://127.0.0.1:7890
    python3 scripts/paper_download.py 2601.99999 --track embodied_robotics --proxy http://127.0.0.1:7890
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import gzip
import http.client
import json
import os
import re
import shutil
import sys
import tarfile
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path

from paper_ids import resolve_paper_id, resolve_paper_track


ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_ABS_PREFIX = "https://arxiv.org/abs/"
ARXIV_PDF_PREFIX = "https://arxiv.org/pdf/"
ARXIV_API_URL = "https://export.arxiv.org/api/query?id_list={id}"
ARXIV_SOURCE_URLS = (
    "https://export.arxiv.org/e-print/{id}",
    "https://arxiv.org/e-print/{id}",
)
DEFAULT_OUTPUT_ROOT = Path("docs/papers")
TRACK_CHOICES = ("embodied_robotics", "autonomous_driving", "foundational_works")
USER_AGENT = "awaresome-world-action-model-paper-downloader/1.0"


@dataclass
class PaperMetadata:
    arxiv_id: str
    title: str
    summary: str
    published: str
    updated: str
    authors: list[str]
    pdf_url: str
    abs_url: str


@dataclass
class DownloadTarget:
    raw_value: str
    arxiv_id: str
    track: str
    download_url: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download arXiv papers into docs/papers with incremental updates."
    )
    parser.add_argument("ids", nargs="*", help="arXiv IDs or arXiv abs URLs.")
    parser.add_argument(
        "--from-file",
        type=Path,
        help="Read arXiv IDs from a text file, one per line.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root directory for downloaded papers. Default: docs/papers",
    )
    parser.add_argument(
        "--track",
        choices=TRACK_CHOICES,
        default="embodied_robotics",
        help="Fallback track for papers not yet registered in scripts/paper_ids.py.",
    )
    parser.add_argument(
        "--proxy",
        help="Proxy URL such as http://127.0.0.1:7890. "
        "If omitted, standard HTTP(S)_PROXY env vars are used.",
    )
    parser.add_argument(
        "--pdf-only",
        action="store_true",
        help="Download only the PDF.",
    )
    parser.add_argument(
        "--source-only",
        action="store_true",
        help="Download only the arXiv source archive.",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Re-download even if local files already look valid.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of concurrent paper downloads.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=4,
        help="Retry count for unstable network requests.",
    )
    return parser.parse_args()


def normalize_arxiv_id(value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError("Empty arXiv ID.")
    value = re.sub(r"^arxiv:", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^https?://arxiv\.org/abs/", "", value)
    value = re.sub(r"^https?://www\.arxiv\.org/abs/", "", value)
    value = re.sub(r"v\d+$", "", value)
    if not re.fullmatch(r"([a-z\-]+/\d{7}|\d{4}\.\d{4,5})", value):
        raise ValueError(f"Unsupported arXiv ID format: {value}")
    return value


def is_direct_download_url(value: str) -> bool:
    parsed = urllib.parse.urlparse(value.strip())
    if parsed.scheme not in {"http", "https"}:
        return False
    return bool(Path(parsed.path).suffix)


def redirect_url_from_error(exc: urllib.error.HTTPError) -> str | None:
    if exc.code not in {301, 302, 303, 307, 308}:
        return None
    return exc.headers.get("Location")


def slugify(text: str) -> str:
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "paper"


def make_opener(proxy: str | None) -> urllib.request.OpenerDirector:
    handlers: list[urllib.request.BaseHandler] = []
    if proxy:
        handlers.append(
            urllib.request.ProxyHandler(
                {"http": proxy, "https": proxy}
            )
        )
    opener = urllib.request.build_opener(*handlers)
    opener.addheaders = [("User-Agent", USER_AGENT)]
    return opener


def request_bytes(
    opener: urllib.request.OpenerDirector, url: str, retries: int
) -> bytes:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with opener.open(url, timeout=60) as response:
                return response.read()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt == retries:
                break
            time.sleep(min(attempt, 3))
    raise RuntimeError(f"Failed to fetch {url}: {last_error}") from last_error


def fetch_metadata(
    opener: urllib.request.OpenerDirector, arxiv_id: str, retries: int
) -> PaperMetadata:
    url = ARXIV_API_URL.format(id=urllib.parse.quote(arxiv_id))
    raw = request_bytes(opener, url, retries)
    root = ET.fromstring(raw)
    entry = root.find("atom:entry", ATOM_NS)
    if entry is None:
        raise RuntimeError(f"No arXiv metadata found for {arxiv_id}")
    title = clean_text(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
    summary = clean_text(
        entry.findtext("atom:summary", default="", namespaces=ATOM_NS)
    )
    authors = [
        clean_text(node.findtext("atom:name", default="", namespaces=ATOM_NS))
        for node in entry.findall("atom:author", ATOM_NS)
    ]
    published = entry.findtext("atom:published", default="", namespaces=ATOM_NS)
    updated = entry.findtext("atom:updated", default="", namespaces=ATOM_NS)
    return PaperMetadata(
        arxiv_id=arxiv_id,
        title=title,
        summary=summary,
        published=published,
        updated=updated,
        authors=authors,
        pdf_url=f"{ARXIV_PDF_PREFIX}{arxiv_id}.pdf",
        abs_url=f"{ARXIV_ABS_PREFIX}{arxiv_id}",
    )


def clean_text(text: str) -> str:
    return " ".join(text.split())


def paper_dir_name(metadata: PaperMetadata) -> str:
    date_str = metadata.published[:10].replace("-", "")
    return f"{date_str}_{slugify(metadata.title)}"


def metadata_from_direct_download(download_url: str) -> PaperMetadata:
    parsed = urllib.parse.urlparse(download_url)
    filename = Path(urllib.parse.unquote(parsed.path)).name or "downloaded_paper.pdf"
    title = Path(filename).stem.replace("_", " ").replace("-", " ").strip()
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return PaperMetadata(
        arxiv_id="",
        title=title or "downloaded paper",
        summary=f"Downloaded directly from {download_url}.",
        published=now,
        updated=now,
        authors=[],
        pdf_url=download_url,
        abs_url=download_url,
    )


def looks_like_valid_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 1024:
        return False
    with path.open("rb") as handle:
        header = handle.read(8)
        if not header.startswith(b"%PDF-"):
            return False
        try:
            handle.seek(-2048, os.SEEK_END)
        except OSError:
            handle.seek(0)
        tail = handle.read()
    if b"%%EOF" not in tail:
        return False
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        _ = len(reader.pages)
    except ImportError:
        pass
    except Exception:  # noqa: BLE001
        return False
    return True


def safe_extract_tar(archive_path: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive_path) as tar:
        for member in tar.getmembers():
            member_path = destination / member.name
            if not str(member_path.resolve()).startswith(str(destination.resolve())):
                raise RuntimeError(f"Unsafe path in tar archive: {member.name}")
        tar.extractall(destination)


def sniff_archive_extension(path: Path) -> str:
    with path.open("rb") as handle:
        prefix = handle.read(4)
    if prefix.startswith(b"\x1f\x8b"):
        return ".gz"
    if prefix.startswith(b"%PDF"):
        return ".pdf"
    if tarfile.is_tarfile(path):
        return ".tar"
    return ".bin"


def try_extract_source(archive_path: Path, extract_dir: Path) -> str:
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir(parents=True, exist_ok=True)

    if tarfile.is_tarfile(archive_path):
        safe_extract_tar(archive_path, extract_dir)
        return "tar"

    with archive_path.open("rb") as raw_handle:
        signature = raw_handle.read(2)

    if signature == b"\x1f\x8b":
        decompressed_path = extract_dir / "source.tex"
        with gzip.open(archive_path, "rb") as gz_handle, decompressed_path.open(
            "wb"
        ) as out_handle:
            shutil.copyfileobj(gz_handle, out_handle)
        return "gzip"

    return "raw"


def download_with_resume(
    opener: urllib.request.OpenerDirector,
    url: str,
    dest: Path,
    retries: int,
) -> None:
    part_path = dest.with_suffix(dest.suffix + ".part")
    dest.parent.mkdir(parents=True, exist_ok=True)
    current_url = url

    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        existing_size = part_path.stat().st_size if part_path.exists() else 0
        headers = {}
        if existing_size > 0:
            headers["Range"] = f"bytes={existing_size}-"
        request = urllib.request.Request(current_url, headers=headers)
        try:
            with opener.open(request, timeout=60) as response:
                append = response.status == 206 and existing_size > 0
                mode = "ab" if append else "wb"
                if not append and part_path.exists():
                    part_path.unlink()
                with part_path.open(mode) as handle:
                    while True:
                        chunk = response.read(1024 * 256)
                        if not chunk:
                            break
                        handle.write(chunk)
                expected = response.headers.get("Content-Length")
                if expected is not None:
                    expected_size = int(expected) + (existing_size if append else 0)
                    if part_path.stat().st_size < expected_size:
                        raise RuntimeError(
                            f"Incomplete download for {url}: "
                            f"{part_path.stat().st_size} < {expected_size}"
                        )
                part_path.replace(dest)
                return
        except urllib.error.HTTPError as exc:
            last_error = exc
            redirect_url = redirect_url_from_error(exc)
            if redirect_url:
                current_url = urllib.parse.urljoin(current_url, redirect_url)
                if attempt < retries:
                    continue
            if exc.code == 429 and attempt < retries:
                time.sleep(min(5 * attempt, 20))
                continue
            if 400 <= exc.code < 500 and exc.code != 429:
                break
            if attempt == retries:
                break
            time.sleep(min(attempt, 3))
        except (
            RuntimeError,
            urllib.error.URLError,
            http.client.IncompleteRead,
            TimeoutError,
        ) as exc:
            last_error = exc
            if attempt == retries:
                break
            time.sleep(min(attempt, 3))
    raise RuntimeError(f"Failed to download {url}: {last_error}") from last_error


def write_metadata_files(
    paper_dir: Path,
    metadata: PaperMetadata,
    source_archive_name: str | None,
) -> None:
    code_dir = paper_dir / "paper_arxiv_code"
    code_dir.mkdir(parents=True, exist_ok=True)

    metadata_path = code_dir / "metadata.json"
    metadata_payload = asdict(metadata)
    metadata_payload["source_archive"] = source_archive_name
    metadata_path.write_text(
        json.dumps(metadata_payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    readme_path = code_dir / "README.md"
    authors = ", ".join(metadata.authors[:8])
    if len(metadata.authors) > 8:
        authors += ", et al."
    if not authors:
        authors = "not available"
    summary = textwrap.fill(metadata.summary, width=88)
    arxiv_id_line = (
        f"- arXiv ID: {metadata.arxiv_id}"
        if metadata.arxiv_id
        else "- arXiv ID: not available"
    )
    source_line = (
        f"- Source archive: {source_archive_name}"
        if source_archive_name
        else "- Source archive: not downloaded"
    )
    readme = (
        f"# {metadata.title}\n\n"
        f"{arxiv_id_line}\n"
        f"- Published: {metadata.published[:10]}\n"
        f"- Updated: {metadata.updated[:10]}\n"
        f"- Authors: {authors}\n"
        f"- PDF: {metadata.pdf_url}\n"
        f"- Abstract: {metadata.abs_url}\n"
        f"{source_line}\n\n"
        f"## Summary\n{summary}\n"
    )
    readme_path.write_text(readme, encoding="utf-8")


def should_download_pdf(pdf_path: Path, refresh: bool) -> bool:
    if refresh:
        return True
    return not looks_like_valid_pdf(pdf_path)


def should_download_source(code_dir: Path, refresh: bool) -> bool:
    if refresh:
        return True
    archive_files = list(code_dir.glob("source_archive.*"))
    return not archive_files


def download_source_archive(
    opener: urllib.request.OpenerDirector,
    metadata: PaperMetadata,
    code_dir: Path,
    retries: int,
) -> str:
    temp_path = code_dir / "source_archive.download"
    last_error: Exception | None = None
    for template in ARXIV_SOURCE_URLS:
        try:
            download_with_resume(
                opener,
                template.format(id=metadata.arxiv_id),
                temp_path,
                retries,
            )
            break
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if temp_path.exists():
                temp_path.unlink()
    else:
        raise RuntimeError(
            f"Failed to download arXiv source for {metadata.arxiv_id}: {last_error}"
        ) from last_error
    ext = sniff_archive_extension(temp_path)
    archive_path = code_dir / f"source_archive{ext}"
    if archive_path.exists():
        archive_path.unlink()
    temp_path.replace(archive_path)
    try_extract_source(archive_path, code_dir / "source")
    return archive_path.name


def read_ids(args: argparse.Namespace) -> list[DownloadTarget]:
    values: list[str] = list(args.ids)
    if args.from_file:
        for line in args.from_file.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                values.append(stripped)
    if not values:
        raise SystemExit("Please provide at least one arXiv ID or use --from-file.")
    result: list[DownloadTarget] = []
    seen_ids: set[str] = set()
    for value in values:
        resolved_value = resolve_paper_id(value)
        if is_direct_download_url(resolved_value):
            dedupe_key = resolved_value.strip()
            if dedupe_key in seen_ids:
                continue
            result.append(
                DownloadTarget(
                    raw_value=value,
                    arxiv_id=Path(urllib.parse.urlparse(resolved_value).path).name,
                    track=args.track,
                    download_url=resolved_value,
                )
            )
            seen_ids.add(dedupe_key)
            continue
        normalized = normalize_arxiv_id(resolved_value)
        track = resolve_paper_track(value) or args.track
        if normalized not in seen_ids:
            result.append(
                DownloadTarget(raw_value=value, arxiv_id=normalized, track=track)
            )
            seen_ids.add(normalized)
    return result


def process_one(target: DownloadTarget, args: argparse.Namespace) -> str:
    opener = make_opener(args.proxy)
    if target.download_url:
        if args.source_only:
            raise RuntimeError("Direct download links do not support --source-only.")
        metadata = metadata_from_direct_download(target.download_url)
    else:
        metadata = fetch_metadata(opener, target.arxiv_id, args.retries)
    paper_dir = args.output_root / target.track / paper_dir_name(metadata)
    paper_dir.mkdir(parents=True, exist_ok=True)
    code_dir = paper_dir / "paper_arxiv_code"
    code_dir.mkdir(parents=True, exist_ok=True)

    parsed_url = urllib.parse.urlparse(target.download_url or metadata.pdf_url)
    download_ext = Path(parsed_url.path).suffix or ".pdf"
    pdf_path = paper_dir / f"{slugify(metadata.title)}{download_ext}"
    source_archive_name: str | None = None

    if not args.source_only and should_download_pdf(pdf_path, args.refresh):
        download_with_resume(opener, target.download_url or metadata.pdf_url, pdf_path, args.retries)
        if not looks_like_valid_pdf(pdf_path):
            raise RuntimeError(
                f"Downloaded PDF is invalid for {target.download_url or target.arxiv_id}: {pdf_path}"
            )

    if target.download_url:
        source_archive_name = None
    elif not args.pdf_only and should_download_source(code_dir, args.refresh):
        source_archive_name = download_source_archive(opener, metadata, code_dir, args.retries)
    else:
        existing_archives = list(code_dir.glob("source_archive.*"))
        source_archive_name = existing_archives[0].name if existing_archives else None

    write_metadata_files(paper_dir, metadata, source_archive_name)
    return f"{target.arxiv_id} [{target.track}] -> {paper_dir}"


def main() -> int:
    args = parse_args()
    if args.pdf_only and args.source_only:
        raise SystemExit("Cannot use --pdf-only and --source-only together.")

    targets = read_ids(args)
    args.output_root.mkdir(parents=True, exist_ok=True)
    (args.output_root / "embodied_robotics").mkdir(parents=True, exist_ok=True)
    (args.output_root / "autonomous_driving").mkdir(parents=True, exist_ok=True)
    (args.output_root / "foundational_works").mkdir(parents=True, exist_ok=True)

    failures: list[tuple[str, str]] = []
    if args.workers <= 1:
        for target in targets:
            try:
                print(process_one(target, args))
            except Exception as exc:  # noqa: BLE001
                failures.append((target.arxiv_id, str(exc)))
                print(f"{target.arxiv_id} failed: {exc}", file=sys.stderr)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            future_map = {
                pool.submit(process_one, target, args): target for target in targets
            }
            for future in concurrent.futures.as_completed(future_map):
                target = future_map[future]
                try:
                    print(future.result())
                except Exception as exc:  # noqa: BLE001
                    failures.append((target.arxiv_id, str(exc)))
                    print(f"{target.arxiv_id} failed: {exc}", file=sys.stderr)

    if failures:
        print("\nFailures:", file=sys.stderr)
        for arxiv_id, message in failures:
            print(f"- {arxiv_id}: {message}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
