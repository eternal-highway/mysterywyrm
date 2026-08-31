# Version-Control and Re-entry Protocol

Established: 2026-08-24  
Status: mandatory after the 0.9.0 duplicate-pass incident

## Purpose

The corpus is cumulative. A correct re-entry capsule inside an older package can still direct work that has already been completed elsewhere. Source validity therefore does not establish version currency.

## Mandatory preflight

Before beginning any acquisition turn:

1. Identify the exact supplied seed filename and internal version.
2. Search the durable project folder for every corpus package with the same base name.
3. Sort candidate versions numerically and inspect the latest package's `README.md`, `CHANGELOG.md`, `05_method/reentry_capsule.md`, and `05_method/lineage_log.md`.
4. Compare the proposed target with the latest completed acquisition turn.
5. Record the canonical input filename and checksum in the working notes before editing.

An attached package is an input. It is not proof that no later package exists.

## Mandatory stop conditions

Stop before acquisition or publication when:

- the proposed version number already exists;
- the proposed chapter is already marked complete in a later package;
- a save operation produces a suffix such as `(1)`;
- two packages claim the same version but have different hashes;
- the latest package cannot be resolved unambiguously.

Resolve the lineage first. Do not continue and explain afterward.

## Release semantics

- Patch release (`0.9.0 → 0.9.1`): lineage repair, correction, or evidence-preserving refinement with no new chapter acquisition.
- Minor release (`0.9.x → 0.10.0`): the next completed chapter acquisition or comparably substantial corpus extension.
- Existing numbered packages remain immutable. Corrections receive a new version.
- A parallel draft never inherits the next version merely because work was performed.
- Do not publish a version for one wording change, stale count, or isolated note. Accumulate defects into one consolidation batch under `maintenance_policy.md` and validate once.
- Open research questions are not release blockers when the missing evidence and allowed next action are explicit in `01_inventory/open_questions.csv`.

## Duplicate reconciliation

When duplicate versions exist:

1. The earlier successfully published package remains canonical unless evidence establishes corruption or incompleteness.
2. Compare the packages file by file.
3. Preserve canonical wording, identifiers, and relations by default.
4. Carry forward only independently useful material that does not displace stronger canonical evidence.
5. Record both hashes, the cause, the selected contributions, and all rejected duplication.
6. Publish a patch release.
7. Move the redundant package out of the active version line while keeping the incident recoverable.

## Current canonical line

`0.8.0 → 0.9.0 (The Water Cycle) → 0.9.1 (lineage repair) → 0.10.0 (Prosperity) → 0.11.0 (You Have Nothing Else) → 0.12.0 (Light) → 0.13.0 (By Land and By Sea) → 0.13.1 (Claude-audit reconciliation) → 0.13.2 (Claude-review correction) → 0.14.0 (Axis Mundi) → 0.15.0 (They'll Cut You) → 0.16.0 (Moody Joy) → 0.17.0 (Everything is Temporary) → 0.18.0 (page-local cipher reconciliation) → 0.19.0 (Claude cipher integration) → 0.20.0 (series coverage) → 0.21.0 (structural consolidation) → 0.22.0 (Shh plate transcription) → 0.23.0 (For Anybody plate transcription) → 0.24.0 (five-plate batch) → 0.25.0 (three-plate batch) → 0.26.0 (Rune Code closure) → 0.26.1 (Rune Code QA correction)`
