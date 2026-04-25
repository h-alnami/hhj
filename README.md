# NARIS Production Documents

This repository is the GitHub documentation index for **NARIS / Call of Naris** by **NARIS Studios — Alnami Company**.

## Current purpose

The repository collects the project documents, version notes, system summaries, QA checklists, and production handoff files for the NARIS game prototype pipeline.

## Uploaded document set

- `docs/00_PACKAGE_INDEX.md` — package registry and version map.
- `docs/01_MASTER_OVERVIEW.md` — full project overview.
- `docs/02_VERSION_HISTORY.md` — v1.2 to v1.8 version summary.
- `docs/03_SYSTEMS_INDEX.md` — gameplay, world, quest, inventory, companion, boss, build, and release systems.
- `docs/04_NEXT_ROADMAP.md` — v1.9 to v2.4 roadmap.
- `docs/05_TEAM_HANDOFF.md` — handoff plan for programmer, artist, animator, sound designer, QA, and producer.
- `docs/06_QA_BUILD_EXPORT.md` — QA and export checklist.
- `docs/07_MARKETING_TRAILER.md` — trailer/storyboard and marketing notes.

## Version order

1. v1.2 — Godot vertical slice seed.
2. v1.3 — visual branding, English-only naming, NARIS Studios + Alnami Company.
3. v1.4 — combat, energy, abilities, HUD, poise, VFX spawner.
4. v1.5 — world interaction, quests, inventory, dialogue, lore, save/load.
5. v1.6 — companion, crafting, map, AI director, factions, world events.
6. v1.7 — bosses, cinematics, localization, settings, accessibility, build, QA.
7. v1.8 — GameRoot, demo loop, save slots, achievements, release candidate tools.

## Next target

The next production step is:

```txt
NARIS v1.9 — Unified Integration Build
```

That step should merge the separated version packages into one playable Godot project with one `project.godot`, unified `assets/`, unified `data/`, unified `scripts/`, unified `scenes/`, and a single demo loop.
