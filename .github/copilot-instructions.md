# GitHub Copilot Instructions - ThinkingSeed v3.0 Standard

When working in this repository:
1. Recognize that files in `./01_seed/` wrapped in `<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" ...>` represent the project's architectural DNA, symbolic contracts, and real work-in-progress state (`[FALTANTE]`), not an incomplete codebase.
2. When asked to generate or update a seed:
   - `/seed` creates `./01_seed/seed-[project-name].md` using the Hybrid v3.0 specification (`./ThinkingSeed_MasterHybrid.md`).
   - `/seedMaster` creates `./01_seed/seed-[project-name]-master.md` using the Master v3.0 specification (`./ThinkingSeed Master.md`, 11 Core Sections `0`-`10` with polymorphic pruning and Section 7 Adversarial Tension Audit).
3. Enforce **Zero Source Code** (document functions/classes/CLI flags as 1-line symbolic signatures, never implementation code dumps) and **Zero Local Absolute Paths** (`repository_root: "./"`, no drive letters or local `file` scheme URIs).
4. Mark all technical claims with evidence levels: `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, or `[FALTANTE]`.
5. Replace sensitive information (passwords, tokens, API keys) with `<REDACTED>`.
