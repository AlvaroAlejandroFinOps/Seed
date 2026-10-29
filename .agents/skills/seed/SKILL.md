---
name: seed
description: >-
  Crea un snapshot técnico ágil y portable (ADN híbrido v5.0) de un proyecto en formato seed-[nombre-proyecto].md
  siguiendo el estándar ThinkingSeed_MasterHybrid.md (v5.0 / iContext Federation Protocol v5.0) y alojándolo en la carpeta 01_seed
  del directorio donde se ejecute. Usar cuando el usuario ponga /seed o solicite crear el seed ágil del proyecto.
---

# Workflow: Generación de ThinkingSeed Master Hybrid v5.0 (`/seed`)

Este workflow inspecciona el proyecto actual y genera un vector arquitectónico compacto, verificable y libre de código fuente denominado `./01_seed/seed-[nombre-proyecto].md` siguiendo `./ThinkingSeed_MasterHybrid.md` (v5.0).

---

## Pasos de Ejecución Obligatorios

### Paso 1: Determinación del Proyecto, Federación L0 y Delta-Seeding Incremental
1. Identificar el nombre del proyecto actual y asegurar que existe el directorio `./01_seed/`.
2. **Delta-Seeding Incremental & Federación v5.0:**
   - Si existe `./.context/contracts_ast.json` con `topology_hash` vigente, consumir las firmas AST pre-extraídas por `iDirectory v5.0`.
   - Si ya existe `./01_seed/seed-[nombre-proyecto].md`, leer `git_commit` de la Sección `0` y ejecutar `git diff --name-status <old_commit>..HEAD` para focalizar el escaneo en los archivos modificados junto con `./.context/tree.json`.

### Paso 2: Inspección y Extracción Simbólica Sin Código
El agente actúa como **Lead Systems Architect**:
1. **Raíz, Manifiestos y Topología (`all-lowercase`):** Leer manifiestos de dependencias y construir el árbol estructural omitiendo directorios generados y nodos con `crawl: false`.
2. **Invariante Zero Source Code (Contratos Simbólicos de 1 Línea):**
   - Prohibido volcar bloques de código fuente de implementación (`.py`, `.ps1`, `.sh`, `.json`, `.yaml` > 5 líneas).
   - Extraer funciones públicas, clases y flags CLI como firmas simbólicas de 1 línea (`ruta::simbolo(arg: Tipo) -> Retorno | Invariante`).
3. **Invariante Zero Local Paths & Zero File-Scheme URIs:**
   - Establecer `repository_root: "./"`.
   - Prohibido incluir rutas absolutas del disco local o enlaces con esquema `file` local. Usar exclusivamente rutas relativas con `/`.

### Paso 3: Reglas Epistemológicas, Auditoría Adversarial y Seguridad
1. **Etiquetado de Evidencia:** Clasificar afirmaciones con `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]` o `[FALTANTE]`.
2. **Superficie de Tensión (Sección 7):** Cruzar las reglas de `./AGENTS.md` y `./GEMINI.md` contra el árbol físico real y documentar contradicciones, acoplamientos y riesgos reales.
3. **Sanitización Zero-Trust:** Reemplazar cualquier password, token, API key o credencial por `<REDACTED>`.

### Paso 4: Generación del Archivo Seed Híbrido v5.0
Crear o sobrescribir `./01_seed/seed-[nombre-proyecto].md` con `<SEED_ARCHITECTURAL_VECTOR version="5.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">` y `seed_schema_version: "5.0"`.

### Paso 5: Checklist de Auto-Validación Pre-Guardado
Antes de finalizar, verificar:
- [ ] Presencia de `<SEED_ARCHITECTURAL_VECTOR`, sección `0.1`, cierre `CONTEXT HANDOFF` y `</SEED_ARCHITECTURAL_VECTOR>`.
- [ ] 0 ocurrencias de URIs con esquema `file` local y 0 rutas absolutas locales (`repository_root: "./"`).
- [ ] 0 bloques de código fuente de implementación mayores a 5 líneas.
- Confirmar al usuario la generación citando la ruta relativa `./01_seed/seed-[nombre-proyecto].md`.
