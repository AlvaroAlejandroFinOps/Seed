# AGENTS.md: ThinkingSeed v5.0 Universal Agent Directives (iContext Federation Protocol)

> Standard protocol for autonomous coding agents and conversational LLMs operating within this repository.

## 1. Project DNA & `<SEED_ARCHITECTURAL_VECTOR>` Contract (v5.0)
- A **ThinkingSeed** is the architectural DNA, symbolic contract map, and technical memory of a project, **NOT its full source code repository**.
- Every v5.0 seed opens and closes with `<SEED_ARCHITECTURAL_VECTOR version="5.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">` ... `</SEED_ARCHITECTURAL_VECTOR>`.
- When consuming a file wrapped in `<SEED_ARCHITECTURAL_VECTOR>`, treat `contains_source_code="false"` as an intentional engineering invariant (Zero Source Code) and adopt an adversarial bug, tension, and vulnerability hunting posture.
- All seeds reside exclusively in `./01_seed/` (`./01_seed/seed-[project-name].md` and `./01_seed/seed-[project-name]-master.md`).

## 2. Generation Invariants (ThinkingSeed v5.0)
- **Zero Source Code (Symbolic Contracts Only):** Never embed implementation source code blocks (`.py`, `.ps1`, `.sh`, `.rs`, `.go`, `.sql`, `.json`, `.yaml` > 5 lines) inside a seed. Document public functions, classes, and CLI flags strictly as 1-line AST symbolic signatures: `path/module.py::symbol(arg: Type) -> Return | Invariant / Effect`.
- **Zero Local Absolute Paths & Zero File-Scheme URIs:** Never emit host-specific absolute paths (local drive letters `C` or `D`, `/Users/`, `/home/`) or local `file` scheme links. Always set `repository_root: "./"` and use clean relative paths (`./path/to/file`).
- **Polymorphic Pruning (11 Core Sections `0`-`10`):** Consolidate deep audits into the 11 Core Sections (`0` to `10`). Omit conditional sub-modules that have no physical evidence in the repository instead of filling tables with `"N/A"`.
- **Adversarial Tension Audit (Section 7):** Actively cross-check documentation (`AGENTS.md`, `GEMINI.md`, `README.md`) against the physical file tree (`./.context/tree.json`) to expose trust boundaries, shared mutable state, casing violations (`all-lowercase`), and external binaries assumed in `PATH`.

## 3. Workflows
- **`/seed`**: Fast, hybrid architectural vector (`./ThinkingSeed_MasterHybrid.md`). Generates `./01_seed/seed-[project-name].md`.
- **`/seedMaster`**: Deep, exhaustive architectural & adversarial vector (`./ThinkingSeed Master.md`). Generates `./01_seed/seed-[project-name]-master.md`.

## 4. Epistemic Rigor & Zero-Trust Security
- `[CONFIRMADO]`: Directly verified in repository code/manifests.
- `[INFERIDO]`: Reasonable architectural deduction.
- `[DECLARADO]`: Stated in documentation, pending or diverging from code verification.
- `[FALTANTE]`: Expected component currently absent (reflects real WIP progress).
- Redact all credentials, tokens, and secrets with `<REDACTED>`.
