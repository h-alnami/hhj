# NARIS Source Structure

This folder is the first source-code scaffold for **NARIS v1.9 — Unified Integration Build**.

## Purpose

The goal of `src/` is to begin converting the separated prototype packages into one Godot project structure.

## Current scaffold

```txt
src/
├── project.godot
├── scenes/
│   └── root/
│       └── game_root.tscn
├── scripts/
│   ├── core/
│   │   └── GameRoot.gd
│   ├── flow/
│   │   └── SceneFlowManager.gd
│   └── save/
│       └── SaveSlotManager.gd
└── data/
    ├── game_flow/
    │   └── game_flow.json
    └── scenes/
        └── scene_registry.json
```

## Next implementation target

Wire these systems into one playable demo loop:

1. Main Menu.
2. Intro Cinematic.
3. Wake Area.
4. Movement and attack tutorial.
5. Memory Crystal pickup.
6. Naris First Whisper dialogue.
7. Bone Beast encounter.
8. Ash Gate opening.
9. Spirit Wolf reveal.
10. Boss encounter.
11. End Demo screen.

## Branding rule

Required lockup:

```txt
NARIS: Call of Naris
NARIS Studios
Alnami Company
```
