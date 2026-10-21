# CLAUDE.md: ThinkingSeed v3.0 Integration for Claude Code

This repository implements the **ThinkingSeed v3.0 Standard** (by Gravity HyperScale Thinking) to manage deterministic architectural vectors and project knowledge seeds.

---

## 🧬 Core Concept: `<SEED_ARCHITECTURAL_VECTOR>` (Zero Source Code)
- A **ThinkingSeed** is the **architectural DNA, symbolic contract map, and technical memory** of a software project (`contains_source_code="false"`). **It is NOT the full source code repository**.
- Every v3.0 seed is wrapped in `<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">` ... `</SEED_ARCHITECTURAL_VECTOR>`.
- When reading a ThinkingSeed, never interpret the absence of implementation code blocks as an incomplete or broken repository. Instead, use the 1-line AST symbolic signatures (Section 4) and the Adversarial Tension Surface (Section 7) to reason about system behavior, hunt for bugs, and plan safe modifications.
- Components marked as `[FALTANTE]` reflect real work-in-progress (WIP) or intentional architectural scaffolding.

---

## 🛠️ Slash Commands / Workflows (v3.0)

### 1. `/seed` (Hybrid ThinkingSeed v3.0 - Fast & Frequent)
When the user types `/seed` or asks for a project seed:
1. Perform incremental Delta-Seeding if a previous seed exists in `./01_seed/`, combined with `./.context/tree.json`.
2. Extract public functions, classes, and CLI flags as 1-line symbolic contracts (`module::symbol(arg: Type) -> Return | Invariant`). **Never dump implementation source code blocks.**
3. Enforce `repository_root: "./"` and **Zero Local Absolute Paths / Zero File-Scheme URIs**.
4. Apply epistemic tags (`[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[FALTANTE]`) and sanitize sensitive data with `<REDACTED>`.
5. Write `./01_seed/seed-[project-name].md` following `./ThinkingSeed_MasterHybrid.md` and wrap it in `<SEED_ARCHITECTURAL_VECTOR version="3.0" ...>` ... `</SEED_ARCHITECTURAL_VECTOR>`.

### 2. `/seedMaster` (Master ThinkingSeed v3.0 - Deep & Adversarial)
When the user types `/seedMaster` or asks for the exhaustive master seed:
1. Run Delta-Seeding (`git diff --name-status <old_commit>..HEAD`) and inspect `./.context/tree.json` + `.context.yaml` beacons.
2. Consolidate findings into the **11 Core Sections (`0` to `10`)** with polymorphic pruning (omit non-applicable conditional sub-modules) and strict **DRY Intra-Seed** referencing (`[ADR-XXX]`, `[INV-XX]`).
3. Extract all public symbols and CLI flags into the Section 4 Symbolic Contracts table (0 implementation code blocks allowed).
4. Conduct an **Adversarial Tension Audit** in Section 7: expose trust boundaries, shared mutable state, casing violations (`all-lowercase`), and external binaries assumed in `PATH`.
5. Write `./01_seed/seed-[project-name]-master.md` and validate with `python scripts/test_seed_coverage.py --target-repo . --no-anonymize`.

---

## 🔒 Security & Portability Invariants
- **ZERO LEAKS:** Never output actual credentials, API keys, or private certificates into any seed. Always replace with `<REDACTED>`.
- **ZERO LOCAL PATHS:** Never include host-specific paths (drive letters `C` or `D`, `/Users/`, `/home/`) or local `file` scheme URIs in any generated artifact.
