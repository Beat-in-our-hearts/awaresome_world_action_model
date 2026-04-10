#!/usr/bin/env python3
"""Maintain paper aliases for repository downloads.

This file groups paper aliases by track and exposes a merged `PAPER_IDS` mapping
for `scripts/paper_download.py`.

Known aliases and known arXiv IDs can both be mapped back to their track, which
lets the downloader auto-route papers into the correct repository folder.

Usage:
    python3 scripts/paper_ids.py
"""

from __future__ import annotations


EMBODIED_ROBOTICS_SOURCES: dict[str, str] = {
    "gr1": "2312.13139",
    "gr2": "2410.06158",
    "fastwam": "2603.16666",
    "adaworld": "2503.18938",
    "pad": "2411.18179",
    "uva": "2503.00200",
    "uwm": "2504.02792",
    "vidman": "2411.09153",
    "vpp": "2412.14803",
    "motus": "2512.13030",
    "lingbotva": "2601.21998",
    "mimic_video": "2512.15692",
    "cosmos_policy": "2601.16163",
    "dreamzero": "2602.15922",
    "gigaworld_policy": "2603.17240",
    "world2act": "2603.10422",
    "svam": "2603.16195",
    "action_images": "2604.06168",
    "dywa": "2503.16806",
}

AUTONOMOUS_DRIVING_SOURCES: dict[str, str] = {
    "epona": "2506.24113",
    "world4drive": "2507.00603",
    "drivelaw": "2512.23421",
    "driveva": "2604.04198",
}

FOUNDATIONAL_WORKS_SOURCES: dict[str, str] = {
    "serl": "2401.16013",
    "lapa": "2410.11758",
    "hil_serl": "2410.21845",
    "pi0": "2410.24164",
    "pi0_5": "https://www.physicalintelligence.company/download/pi05.pdf",
    "pi0_6": "2511.14759",
    "rl_token": "https://www.pi.website/download/rlt.pdf",
}

TRACK_SOURCE_GROUPS: dict[str, dict[str, str]] = {
    "embodied_robotics": EMBODIED_ROBOTICS_SOURCES,
    "autonomous_driving": AUTONOMOUS_DRIVING_SOURCES,
    "foundational_works": FOUNDATIONAL_WORKS_SOURCES,
}

TRACK_ID_GROUPS: dict[str, dict[str, str]] = {
    track: {
        key: value
        for key, value in sources.items()
        if not value.startswith(("http://", "https://"))
    }
    for track, sources in TRACK_SOURCE_GROUPS.items()
}

PAPER_IDS: dict[str, str] = {
    **TRACK_SOURCE_GROUPS["embodied_robotics"],
    **TRACK_SOURCE_GROUPS["autonomous_driving"],
    **TRACK_SOURCE_GROUPS["foundational_works"],
}

PAPER_TRACKS: dict[str, str] = {
    **{
        key: track
        for track, sources in TRACK_SOURCE_GROUPS.items()
        for key in sources
    },
}

ARXIV_ID_TO_TRACK: dict[str, str] = {
    **{
        value: track
        for track, ids in TRACK_ID_GROUPS.items()
        for value in ids.values()
    },
}


def normalize_alias_key(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def resolve_paper_id(name_or_id: str) -> str:
    """Return the arXiv ID for a paper alias or the input itself if not mapped."""
    key = normalize_alias_key(name_or_id)
    return PAPER_IDS.get(key, name_or_id.strip())


def resolve_paper_track(name_or_id: str) -> str | None:
    """Return the repository track for a known alias or known arXiv ID."""
    key = normalize_alias_key(name_or_id)
    if key in PAPER_TRACKS:
        return PAPER_TRACKS[key]
    resolved_id = resolve_paper_id(name_or_id)
    return ARXIV_ID_TO_TRACK.get(resolved_id)


if __name__ == "__main__":
    for track, ids in TRACK_SOURCE_GROUPS.items():
        print(f"[{track}]")
        for key, value in sorted(ids.items()):
            print(f"{key}: {value}")
        print()
