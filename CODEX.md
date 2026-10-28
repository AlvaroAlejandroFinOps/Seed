# ThinkingSeed v3.0 Codex Instructions / CODEX.md

> Standard instructions for OpenAI Codex, Codex CLI, and Codex-powered agent environments.

## 🧬 Core Architecture: `<SEED_ARCHITECTURAL_VECTOR>` Contract (v3.0)
- A **ThinkingSeed** is the **architectural DNA, symbolic contract map, and technical memory** of a project (`contains_source_code="false"`). **It is NOT the full source code repository**.
- Every seed generated must open and close with `<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">` ... `</SEED_ARCHITECTURAL_VECTOR>`.
- The absence of implementation code blocks is an intentional architectural invariant (**Zero Source Code**). Never attempt to regenerate or report missing implementation source code inside a seed.
- Components tagged as `[FALTANTE]` indicate intentional scaffolding or work-in-progress (WIP).
- All generated seeds must reside exclusively in `./01_seed/` (`./01_seed/seed-[project-name].md` or `./01_seed/seed-[project-name]-master.md`).

---

## 🛠️ Workflows & Commands

### 1. `/seed` or "Generar Seed Híbrido" (Fast Architectural Vector)
When invoked with `/seed` or requested to create/update the project seed:
1. Identify the project root and ensure `./01_seed/` exists.
2. Read `./ThinkingSeed_MasterHybrid.md` and `.agents/skills/seed/SKILL.md` as reference templates.
3. Perform incremental Delta-Seeding if a previous seed exists, inspecting `./.context/tree.json`.
4. Extract public functions, classes, and CLI flags as **1-line AST symbolic signatures**:
   `module/path.py::function_name(param: Type) -> ReturnType | Invariant`
   **Never dump full implementation code blocks (>5 lines).**
5. Enforce **Zero Local Absolute Paths**: use relative paths (`./`) and set `repository_root: "./"`. Prohibit drive letters (`C:`, `D:`) or `file://` schemes.
6. Apply epistemic tags: `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[FALTANTE]`. Redact secrets with `<REDACTED>`.
7. Output to `./01_seed/seed-[project-name].md`.

### 2. `/seedMaster` or "Generar Seed Master" (Exhaustive & Adversarial Vector)
When invoked with `/seedMaster` or requested for a deep audit seed:
1. Read `./ThinkingSeed Master.md` and `.agents/skills/seedMaster/SKILL.md`.
2. Inspect `./.context/tree.json`, `.context.yaml` beacons, and `git diff`.
3. Structure the audit into the **11 Core Sections (`0` to `10`)** with polymorphic pruning (omit non-applicable conditional blocks; do not populate empty tables).
4. Extract 100% of public APIs and CLI flags into Section 4 AST Symbolic Contracts.
5. Conduct an **Adversarial Tension Audit** in Section 7: cross-check documentation against actual code, expose trust boundaries, shared mutable state, casing issues, and external CLI dependencies.
6. Output to `./01_seed/seed-[project-name]-master.md`.

---

## 🔒 Security & Invariants
- **ZERO SECRETS:** Always redact tokens, passwords, and private keys with `<REDACTED>`.
- **ZERO LOCAL ABSOLUTE PATHS:** Always use `./` relative paths.
