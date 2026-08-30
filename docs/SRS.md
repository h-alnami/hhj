# Software Requirements Specification — NARIS: Call of Naris

**Project:** NARIS / Call of Naris  
**Studio:** NARIS Studios  
**Company:** Alnami Company  
**Document Type:** Software Requirements Specification (SRS)  
**Version:** 1.0  
**Target Engine:** Godot 4.x  
**Primary Build Targets:** Windows Desktop, Web, Android Preview

---

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification defines the functional, technical, content, quality, and delivery requirements for **NARIS: Call of Naris**, a dark fantasy action-adventure prototype progressing toward a playable vertical slice and later a production-ready demo.

The document is intended for:

- Programmers.
- Game designers.
- Technical artists.
- UI/UX artists.
- Sound designers.
- QA testers.
- Producers.
- Marketing and publishing team members.

### 1.2 Scope

NARIS is a dark fantasy action-adventure game centered on memory loss, fire, trust, and supernatural energies. The player awakens in the Ashen Forest, follows the whisper of Naris, bonds with the Spirit Wolf, masters five energies, confronts enemies, collects memory fragments, opens the Ash Gate, and reaches the end of a 10–15 minute playable demo loop.

### 1.3 Product Vision

The game must present a premium dark fantasy identity that is visually rich, saturated, and readable. The core art direction is:

- Naris Fire: orange / ember / amber.
- Aether Violet: saturated violet.
- Mist Cyan: cyan fog, spectral rim light, atmosphere.
- Ancient Gold: premium UI borders and brand accents.
- Ash Black: base darkness and material contrast, not a full gray-only palette.

### 1.4 Branding Requirement

The following brand lockup is mandatory across splash screens, pitch documents, trailers, store pages, and public-facing materials:

```txt
NARIS: Call of Naris
NARIS Studios
Alnami Company
```

---

## 2. Overall Description

### 2.1 Product Perspective

NARIS is built as a modular Godot project composed of:

- Assets.
- Data-driven JSON systems.
- Scripts.
- Scenes.
- UI.
- VFX.
- Save/load systems.
- QA and build tooling.

The project has evolved through vertical-slice packages from v1.2 through v1.8 and is moving toward v1.9 Unified Integration Build and v2.0 Playable Demo.

### 2.2 User Classes

| User Class | Description |
|---|---|
| Player | Plays the demo, controls the hero, fights enemies, collects items, and progresses quests. |
| Developer | Integrates systems, debugs runtime logic, exports builds. |
| Designer | Tunes quests, combat, encounters, item economy, and demo flow. |
| Artist | Replaces placeholder visuals with final production art. |
| QA Tester | Tests movement, combat, quests, UI, save/load, builds, and localization. |
| Producer | Tracks milestones, deliverables, risk, and handoff state. |

### 2.3 Operating Environment

The project shall target:

- Godot 4.x.
- Windows desktop builds.
- Web export builds.
- Android preview builds.

### 2.4 Constraints

- File names should remain English-only for engine compatibility.
- JSON data must remain structured and readable.
- Placeholder assets must be replaceable without breaking paths.
- Large ZIP packages should be distributed through GitHub Releases or Git LFS rather than normal repository commits.
- The visual identity must avoid gray-only, low-saturation art.

---

## 3. Functional Requirements

## 3.1 Main Menu

### FR-001 — Main Menu
The system shall provide a main menu with the following options:

- New Game.
- Continue.
- Settings.
- Credits.
- Quit.

### FR-002 — Start Demo
The system shall start the playable demo from the main menu and load the Wake Area.

---

## 3.2 Player Controller

### FR-010 — Movement
The player shall move the hero using keyboard input.

### FR-011 — Running
The player shall be able to run using a run input modifier.

### FR-012 — Attack
The player shall be able to perform melee attacks using the equipped weapon.

### FR-013 — Hit Frames
Weapon damage shall only apply during configured animation hit frames.

### FR-014 — Interact
The player shall interact with items, NPC triggers, checkpoints, and gates through an interaction input.

---

## 3.3 Combat System

### FR-020 — Damage Resolution
The system shall calculate damage using attacker values, defender resistance, and damage type.

### FR-021 — Poise System
Enemies shall have poise values that can be reduced by attacks and reset after break state.

### FR-022 — Resonance Meter
The system shall track resonance gained from accurate hits, parries, and successful combat actions.

### FR-023 — Enemy Damage
Enemies shall receive health and poise damage from player attacks.

### FR-024 — Enemy Death
Enemies shall enter a death state when health reaches zero and may trigger VFX and quest events.

---

## 3.4 Energy and Abilities

### FR-030 — Energy Types
The system shall support five energy types:

- Naris Flame.
- Ash Essence.
- Aether.
- Void.
- Radiant.

### FR-031 — Energy Regeneration
Each energy type shall regenerate based on data-defined rates.

### FR-032 — Ability Casting
The player shall cast abilities if enough energy is available and cooldown has expired.

### FR-033 — Ability Set
The first playable ability set shall include:

- Naris Flame Dash.
- Ash Ward.
- Aether Slow Field.
- Void Step.
- Radiant Pulse.

---

## 3.5 Quest System

### FR-040 — Quest Start
Quests shall start from dialogue, triggers, or scripted events.

### FR-041 — Objective Tracking
Quests shall track objectives by event type and target.

### FR-042 — Prologue Quest
The demo shall include the main quest **Ashen Awakening** with objectives:

1. Wake in the Ashen Forest.
2. Reach the first Naris flame.
3. Collect a Memory Crystal.
4. Defeat the Bone Beast.
5. Open the sealed Ash Gate.

### FR-043 — Quest Completion
The system shall mark a quest complete after all objectives are complete.

---

## 3.6 Inventory and Items

### FR-050 — Inventory Capacity
The inventory shall support capacity limits.

### FR-051 — Item Definitions
Items shall be defined through JSON data.

### FR-052 — Stackable Items
The inventory shall support stackable and non-stackable items.

### FR-053 — Required Items
Locked gates and quest actions shall check for required items.

### FR-054 — Initial Items
The player may start with predefined items such as Memory Crystal or Silent Flask.

---

## 3.7 Dialogue System

### FR-060 — Branching Dialogue
Dialogue shall support nodes and choices.

### FR-061 — Dialogue Events
Dialogue nodes shall trigger events such as starting a quest.

### FR-062 — Naris First Whisper
The demo shall include a branching dialogue with Naris that can begin the prologue quest.

---

## 3.8 Lore System

### FR-070 — Lore Entries
The system shall store lore entries by ID.

### FR-071 — Lore Unlocks
Lore entries shall be unlockable through quests, pickups, triggers, or boss events.

---

## 3.9 Companion System

### FR-080 — Spirit Wolf Companion
The player shall gain or encounter a Spirit Wolf companion during the demo flow.

### FR-081 — Companion Commands
The Spirit Wolf shall support:

- Follow.
- Attack.
- Guard.
- Track.
- Echo Link.

### FR-082 — Bond System
The companion shall track bond value and allow certain commands only when bond requirements are met.

### FR-083 — Echo Link
Echo Link shall require sufficient bond and trigger a companion-energy fusion effect.

---

## 3.10 Crafting and Upgrades

### FR-090 — Crafting Recipes
The system shall load crafting recipes from JSON.

### FR-091 — Ingredient Consumption
Crafting shall consume ingredients and add the result item.

### FR-092 — Weapon Upgrade Tree
The Sword of Poem shall support upgrade tiers:

- Dormant Blade.
- Ember Cut.
- Aether Verse.
- Naris Resonance.

---

## 3.11 Map and Fast Travel

### FR-100 — World Map
The system shall provide a map for Ashen Forest regions.

### FR-101 — Region Unlocks
Regions shall unlock through exploration, checkpoints, or quests.

### FR-102 — Fast Travel
Fast travel shall only be allowed to unlocked regions flagged as fast-travel enabled.

---

## 3.12 AI Director

### FR-110 — Encounter Tables
The AI Director shall select encounters from low-tension or high-tension tables.

### FR-111 — Tension System
The AI Director shall track tension and use it to choose encounter intensity.

### FR-112 — Encounter Cooldown
The AI Director shall enforce a minimum gap between encounters.

---

## 3.13 Factions and Reputation

### FR-120 — Faction Data
Factions shall be defined through JSON.

### FR-121 — Reputation Value
Each faction shall track reputation between hostile and ally thresholds.

### FR-122 — Reputation Status
The system shall classify reputation as hostile, neutral, or ally.

---

## 3.14 World Events

### FR-130 — World Event Start
The system shall start world events by ID.

### FR-131 — World Event Duration
World events shall run for a configured duration then expire.

### FR-132 — Event Types
Initial event types shall include:

- Ash Rain.
- Naris Storm.
- Silent Mist.

---

## 3.15 Boss and Cinematic Systems

### FR-140 — Boss Phases
Bosses shall support multiple phases and phase transition events.

### FR-141 — Cinematic Director
The game shall support scripted cinematics for intro, boss reveal, gate reveal, and demo ending.

---

## 3.16 Save and Load

### FR-150 — Save Slots
The system shall support multiple save slots.

### FR-151 — Save Data
Save data shall include inventory, quest state, lore, companion bond, map unlocks, faction reputation, and progression flags.

### FR-152 — Load Data
The system shall restore saved state reliably.

---

## 3.17 Localization

### FR-160 — Supported Languages
The system shall support English and Arabic.

### FR-161 — RTL Support
Arabic UI shall support RTL layout where required.

### FR-162 — Language Files
Localization shall be stored in data files and referenced by keys.

---

## 3.18 Settings and Accessibility

### FR-170 — Settings
The system shall support:

- Master volume.
- Music volume.
- SFX volume.
- Screen mode.
- Language.
- Input mapping.

### FR-171 — Accessibility
The system shall support:

- Subtitles.
- High contrast mode.
- Screen shake reduction.
- Larger UI scale.

---

## 4. Non-Functional Requirements

### NFR-001 — Performance
The demo shall target stable performance appropriate for Windows desktop and Web preview.

### NFR-002 — Maintainability
Systems shall be modular and data-driven where possible.

### NFR-003 — Asset Replaceability
Placeholder assets shall be replaceable without changing core scripts.

### NFR-004 — Naming
Files and engine paths should use English-only names.

### NFR-005 — Visual Quality
Art should remain saturated and readable. Gray-only key art is not acceptable.

### NFR-006 — Build Stability
The project shall export without missing file references or broken scenes.

### NFR-007 — Documentation
All systems shall include brief handoff documentation.

---

## 5. Data Requirements

The game shall use JSON files for:

- Abilities.
- Energy types.
- Quests.
- Dialogue.
- Items.
- Inventory defaults.
- Lore entries.
- Companion definitions.
- Crafting recipes.
- Weapon upgrades.
- Map data.
- Encounters.
- Factions.
- World events.
- Scene registry.
- Localization.
- Settings defaults.

---

## 6. Build and Export Requirements

### BR-001 — Export Targets
The project shall prepare export presets for:

- Windows Desktop.
- Web.
- Android preview.

### BR-002 — Build Documentation
The repository shall include:

- `README_BUILD.md`.
- `QA_CHECKLIST.md`.
- `KNOWN_ISSUES.md`.
- `RELEASE_CANDIDATE_CHECKLIST.md`.
- `export_presets.cfg`.

---

## 7. QA Requirements

The QA process shall test:

- Main menu.
- Scene loading.
- Movement.
- Combat.
- Hit frames.
- Enemy damage.
- Poise break.
- Ability spending.
- Quest start and completion.
- Dialogue branching.
- Item pickup.
- Inventory.
- Locked gates.
- Spirit Wolf commands.
- Crafting.
- Weapon upgrades.
- Map unlocks.
- Boss phases.
- Save/load.
- Localization.
- Settings.
- Exported builds.

---

## 8. Release Readiness Requirements

A release candidate shall not be accepted unless:

- The demo loop is playable from start to end.
- Save/load works.
- No critical blocker remains.
- Required brand lockup appears.
- UI is readable.
- Placeholder assets are clearly documented.
- Export builds are generated.
- QA checklist is completed.

---

## 9. Current Next Step

The immediate next milestone is:

```txt
NARIS v1.9 — Unified Integration Build
```

This milestone shall merge all separate packages into one Godot project with:

```txt
project.godot
assets/
data/
scripts/
scenes/
docs/
export_presets.cfg
README_START_HERE.md
```

---

## 10. Approval

This SRS is the baseline software requirements document for the next integration phase.
