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


EMBODIED_ROBOTICS_IDS: dict[str, str] = {
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
    "action_images": "2604.06168",
    "dywa": "2503.16806",
}

AUTONOMOUS_DRIVING_IDS: dict[str, str] = {
    "driveva": "2604.04198",
}

LEGACY_ALIAS_IDS: dict[str, str] = {
    "gr_1": "2312.13139",
    "gr_2": "2410.06158",
    "fast_wam": "2603.16666",
    "prediction_with_action": "2411.18179",
    "unified_video_action_model": "2503.00200",
    "unified_world_models": "2504.02792",
    "lingbot_va": "2601.21998",
    "mimic_video_model": "2512.15692",
    "cosmospolicy": "2601.16163",
}

PAPER_IDS: dict[str, str] = {
    **EMBODIED_ROBOTICS_IDS,
    **AUTONOMOUS_DRIVING_IDS,
    **LEGACY_ALIAS_IDS,
}

PAPER_TRACKS: dict[str, str] = {
    **{key: "embodied_robotics" for key in EMBODIED_ROBOTICS_IDS},
    **{key: "autonomous_driving" for key in AUTONOMOUS_DRIVING_IDS},
    **{key: "embodied_robotics" for key in LEGACY_ALIAS_IDS},
}

ARXIV_ID_TO_TRACK: dict[str, str] = {
    **{value: "embodied_robotics" for value in EMBODIED_ROBOTICS_IDS.values()},
    **{value: "autonomous_driving" for value in AUTONOMOUS_DRIVING_IDS.values()},
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
    print("[embodied_robotics]")
    for key, value in sorted(EMBODIED_ROBOTICS_IDS.items()):
        print(f"{key}: {value}")
    print()
    print("[autonomous_driving]")
    for key, value in sorted(AUTONOMOUS_DRIVING_IDS.items()):
        print(f"{key}: {value}")
