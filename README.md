# NARIS Production Documents

**Project:** NARIS / Call of Naris  
**Studio:** NARIS Studios  
**Company:** Alnami Company  
**Repository:** hashimalnami1556-sketch/hhj

This repository is the GitHub documentation index for the NARIS game prototype pipeline.

---

## 1. Package Registry

| Version | Package | Purpose |
|---|---|---|
| Engine Bridge v1.1 | `Naris_Engine_Bridge_v1_1_JSON_Godot_VFX.zip` | JSON bridge, Godot scripts, hit frames, pivot data, destructible tiles, VFX descriptors. |
| Master v1.3 | `Naris_Master_Delivery_v1_3.zip` | Master wrapper for early art, bridge, visual branding, preview, manifest. |
| v1.2 | `Naris_Vertical_Slice_Godot_v1_2.zip` | First Godot vertical slice seed. |
| v1.3 | `Naris_Vertical_Slice_Godot_v1_3_Visual_Branding.zip` | Visual branding, English-only naming, NARIS Studios + Alnami Company. |
| v1.4 | `Naris_Vertical_Slice_Godot_v1_4_Combat_Energy.zip` | Combat, energy, abilities, HUD, poise, VFX spawner. |
| v1.5 | `Naris_Vertical_Slice_Godot_v1_5_World_Quest_Inventory.zip` | World interaction, quests, inventory, dialogue, lore, gates. |
| v1.6 | `Naris_Vertical_Slice_Godot_v1_6_Companion_Crafting_Map_AI.zip` | Spirit Wolf, crafting, upgrades, map, AI director, factions. |

Large ZIP packages should be uploaded later through GitHub Releases or Git LFS.

---

## 2. Master Overview

NARIS is a saturated dark-fantasy game project. The visual language is:

- **Naris Fire:** orange / ember / amber.
- **Aether Violet:** saturated violet.
- **Mist Cyan:** cyan fog, rim light, spectral accents.
- **Ancient Gold:** UI separators, premium borders, brand accents.
- **Ash Black:** base material and atmosphere, not the whole image.

Mandatory brand lockup:

```txt
NARIS: Call of Naris
NARIS Studios
Alnami Company
```

Production rule:

```txt
Dark fantasy does not mean colorless.
Each key frame should include orange ember + violet aether + cyan mist rim + ancient gold accent.
```

---

## 3. Version History

### v1.2 — Godot Vertical Slice Seed
- Godot project seed.
- English naming.
- Placeholder visuals.
- Basic Godot scripts.

### v1.3 — Visual Branding
- Stronger visual direction.
- NARIS Studios + Alnami Company branding.
- English-only files and prompts.
- Color Bible: Aether Violet + Naris Fire + Mist Cyan + Ancient Gold.

### v1.4 — Combat + Energy
- EnergyManager.
- AbilitySystem.
- CombatResolver.
- ResonanceMeter.
- EnemyController.
- HUDController.
- VFXSpawner.
- SaveSystem.

### v1.5 — World + Quest + Inventory
- InventoryManager.
- QuestManager.
- DialogueManager.
- Interactable system.
- Item pickups.
- Locked gates.
- LoreManager.
- World save/load.

### v1.6 — Companion + Crafting + Map + AI
- Spirit Wolf companion.
- Bond and Echo Link.
- Crafting recipes.
- Weapon upgrade tree.
- World map and fast travel hooks.
- AI Director.
- Factions.
- World events.

### v1.7 — Boss + Cinematic + Localization + Build
- Boss phase controller.
- Cinematic director.
- EN/AR localization.
- Settings and accessibility.
- Input rebinding.
- Build profiles.
- QA cases.

### v1.8 — GameRoot + Demo Loop + Release Candidate
- GameRoot.
- Scene Flow Manager.
- Demo Hub.
- Save Slots.
- Achievements.
- Telemetry.
- Release checklist tools.

---

## 4. Systems Index

### Core
- GameRoot
- SceneFlowManager
- SaveSlotManager
- ProgressionManager
- AchievementManager

### Combat
- CombatResolver
- ResonanceMeter
- WeaponHitboxDriver
- EnemyController
- BossPhaseController

### Energy
- EnergyManager
- AbilitySystem
- Naris Flame
- Ash Essence
- Aether
- Void
- Radiant

### World
- QuestManager
- InventoryManager
- DialogueManager
- LoreManager
- Checkpoint
- LockedGate

### Companion
- Spirit Wolf
- CompanionBondManager
- CompanionController
- Echo Link

### Production
- LocalizationManager
- SettingsManager
- AccessibilityManager
- InputRebindManager
- BuildProfileReader
- QATestRunner
- ReleaseChecklistRunner

---

## 5. Demo Target

The playable demo should prove a 10–15 minute loop:

1. Main Menu.
2. Intro cinematic.
3. Wake Area.
4. Movement and attack tutorial.
5. Collect Memory Crystal.
6. Naris First Whisper dialogue.
7. Bone Beast encounter.
8. Open Ash Gate.
9. Spirit Wolf reveal.
10. Ash Giant or Mist Guardian encounter.
11. End of demo screen.

---

## 6. Next Roadmap

| Target | Description |
|---|---|
| v1.9 | Unified Integration Build — merge separated packages into one Godot project. |
| v2.0 | Playable Demo — build the 10–15 minute loop. |
| v2.1 | Final Art Pass — replace placeholder visuals. |
| v2.2 | Audio + Trailer Pack — music, SFX, voiceover guide, trailer scripts. |
| v2.3 | Export Builds — Windows, Web, Android. |
| v2.4 | Store + Marketing Kit — store copy, screenshots, capsules, privacy policy, terms, press kit. |

---

## 7. Team Handoff

### Programmer
Merge managers into GameRoot, wire demo flow, connect JSON data, validate save/load, add export presets.

### Technical Artist
Replace VFX, validate sprite sheets, confirm transparency and atlas setup.

### Concept Artist
Final hero, Spirit Wolf, Bone Beast, Ash Giant, Mist Guardian, Ashen Forest.

### UI Artist
Final HUD, quest log, inventory, dialogue box, map panel, companion wheel, settings.

### Sound Designer
Main theme, combat theme, boss theme, ambience, UI clicks, sword swings, footsteps, wolf howl, boss roars.

### QA
Movement, combat, collision, dialogue, quest progress, inventory, save/load, localization, export.

---

## 8. QA + Build Export Checklist

- GameRoot starts.
- Scene registry parses.
- Player moves.
- Attack triggers hit frames.
- Enemy receives damage.
- Ability energy spending works.
- Quest starts from dialogue.
- Item pickup updates objective.
- Locked gate checks required item.
- Spirit Wolf commands work.
- Crafting consumes materials.
- Weapon upgrade changes tier.
- Boss phase transition works.
- Save/load restores state.
- EN/AR localization works.

Export targets:

```txt
Windows Desktop
Web
Android preview
```

Required build files:

```txt
export_presets.cfg
README_BUILD.md
QA_CHECKLIST.md
KNOWN_ISSUES.md
RELEASE_CANDIDATE_CHECKLIST.md
```

---

## 9. Marketing + Trailer Notes

Trailer structure:

1. Dark ash forest.
2. Hero wakes with no memory.
3. Whisper: Naris.
4. First flame appears.
5. Bone Beast emerges.
6. Spirit Wolf reveal.
7. Sword of Poem ignition.
8. Ash Gate opens.
9. Boss silhouette.
10. Logo lockup.

Visual rule:

```txt
Do not publish gray-only images.
Use Aether Violet + Naris Fire + Mist Cyan + Ancient Gold.
```

Store copy draft:

**NARIS: Call of Naris** is a dark fantasy action adventure where memory, fire, and trust shape the fate of a broken world. Wake in the Ashen Forest, follow the whisper of Naris, bond with the Spirit Wolf, master five energies, and uncover the truth behind the Ash Gate.
