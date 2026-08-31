# Sustainable Maintenance Policy

Established: 2026-08-29

## Defect versus open research

A **defect** is an internal inconsistency, stale current-state statement, broken local reference, missing registered content page, malformed record, failed verifier, or live archive member absent from the register. Defects are repaired in a single consolidation batch.

An **open research question** requires new external evidence, a new transcription, source adjudication, or access not currently available. It belongs in `01_inventory/open_questions.csv`; it is not repeatedly described as a pending fix.

## Bounded work rule

1. Begin from the latest canonical package and run one inventory pass.
2. Collect all tractable defects before editing.
3. Apply them together and validate once.
4. Make one bounded attempt at any evidence route named in the task.
5. If the route is non-decisive, record `unresolvable_by_current_means` and stop reopening it without changed evidence.

## Release rule

Do not publish a new corpus version for a single wording change, one stale count, or an isolated note. A release requires at least one of:

- a completed acquisition or consolidation batch;
- a schema or evidence-model change;
- a materially new decipherment with reproduction evidence;
- a user-requested durable checkpoint or handoff.

Minor repairs accumulated between those boundaries remain working changes. Historical release reports remain historical; only current-state files are updated.

## Completion rule

The corpus is complete for structural acquisition when all registered content pages are captured, principal series/category paths are mapped, and register/capture reconciliation contains only intentional archive/index surfaces. Unsolved ciphers and unadjudicated historical claims do not prevent that milestone when their uncertainty and required evidence are explicitly registered.
