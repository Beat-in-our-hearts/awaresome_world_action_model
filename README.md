# awaresome_world_action_model
A World Action Model extends VLA (Vision-Language-Action) by predicting how an agent's actions influence future environment states, enabling planning and decision-making through learned dynamics.

This repository is a lightweight paper vault for World Action Model research. It is organized around collectible paper folders, local PDFs, and source links so we can steadily build a reusable reading list for robot policy learning, action-conditioned video prediction, and dynamics-aware control.

## Research Tracks

This repository treats World Action Model research as two main tracks:

- Embodied Robotics: how an agent's actions change the surrounding physical world for manipulation, navigation, and closed-loop control
- Autonomous Driving: how ego actions interact with traffic participants and influence future scene evolution for prediction and planning

This split helps us organize papers more naturally, because the two tracks share the idea of action-conditioned world modeling, but differ a lot in data scale, action space, evaluation setup, and downstream decision-making.

## What is included

- A curated paper index in [paper_list.md](paper_list.md)
- A quick abstract digest in [paper_abstracts.md](paper_abstracts.md)
- Paper storage under [docs/papers](docs/papers)
- Download utilities under `scripts/`
- Per-paper metadata in each `paper_arxiv_code/README.md`, including title, authors, summary, and external links

## Storage rule

Paper assets follow the convention documented in [docs/docs.md](docs/docs.md):

- each paper lives under either `docs/papers/embodied_robotics/` or `docs/papers/autonomous_driving/`
- folder names use `YYYYMMDD_title_slug`
- each folder keeps a local PDF together with a `paper_arxiv_code/` directory for notes and source metadata

## Scripts

- `scripts/paper_ids.py`: maintain alias-to-arXiv-ID mappings by track
- `scripts/paper_download.py`: download papers, PDFs, and arXiv source packages into the repository layout, with automatic track detection for known aliases and IDs

Common examples:

```bash
python3 scripts/paper_ids.py
python3 scripts/paper_download.py dreamzero --proxy http://127.0.0.1:7890
python3 scripts/paper_download.py driveva --proxy http://127.0.0.1:7890
python3 scripts/paper_download.py --from-file ids.txt --proxy http://127.0.0.1:7890
python3 scripts/paper_download.py 2601.99999 --track embodied_robotics --proxy http://127.0.0.1:7890
```

## Current focus

The current seed collection is concentrated on the `Embodied Robotics` track, including:

- zero-shot policy construction from world-action models
- efficient action-centered world modeling for deployment
- multiview video generation for end-to-end policy learning
- dynamics-adaptive manipulation under changing object physics

The `Autonomous Driving` branch is now seeded with `DriveVA`, a representative paper on jointly modeling future driving videos and action trajectories. The next natural expansion is to continue adding papers on action-conditioned scene evolution, interactive traffic forecasting, and planning-oriented world models.
