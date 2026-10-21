---
name: seed
description: >-
  Crea un snapshot técnico ágil y portable (ADN híbrido v3.0) de un proyecto en formato seed-[nombre-proyecto].md
  siguiendo el estándar ThinkingSeed_MasterHybrid.md (v3.0) y alojándolo en la carpeta 01_seed
  del directorio donde se ejecute. Usar cuando el usuario ponga /seed o solicite crear el seed ágil del proyecto.
---

# Workflow: Generación de ThinkingSeed Master Hybrid v3.0 (`/seed`)

Este workflow inspecciona el proyecto actual y genera un vector arquitectónico compacto, verificable y libre de código fuente denominado `./01_seed/seed-[nombre-proyecto].md` siguiendo `./ThinkingSeed_MasterHybrid.md` (v3.0).

---

## Pasos de Ejecución Obligatorios

### Paso 1: Determinación del Proyecto y Delta-Seeding Incremental
1. Identificar el nombre del proyecto actual y asegurar que existe el directorio `./01_seed/`.
2. **Delta-Seeding Incremental:**
   - Si ya existe `./01_seed/seed-[nombre-proyecto].md`, leer `git_commit` de la Sección `0` y ejecutar `git diff --name-status <old_commit>..HEAD` para focalizar el escaneo en los archivos modificados junto con `./.context/tree.json`.

### Paso 2: Inspección y Extracción Simbólica Sin Código
El agente actúa como **Lead Systems Architect**:
1. **Raíz, Manifiestos y Topología (`all-lowercase`):** Leer manifiestos de dependencias y construir el árbol estructural omitiendo directorios generados (`.git`, `node_modules`, `__pycache__`, `.venv`, etc.).
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

### Paso 4: Generación del Archivo Seed Híbrido v3.0
Crear o sobrescribir `./01_seed/seed-[nombre-proyecto].md` siguiendo la estructura de `./ThinkingSeed_MasterHybrid.md`:

```markdown
<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# MASTER HYBRID SEED: [Nombre del Proyecto] (v3.0)

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **¿Qué es este archivo?:** Este documento es un **Vector Arquitectónico Híbrido (ThinkingSeed v3.0)** con `contains_source_code="false"`. Representa el **ADN arquitectónico, contratos simbólicos y memoria técnica** del sistema. **NO es el repositorio completo de código fuente**.
> 2. **Estado de Avance (Work in Progress):** La ausencia de bloques de código de implementación es **deliberada por diseño (Zero Source Code)**. Los componentes marcados como `[FALTANTE]` reflejan áreas en desarrollo (WIP).
> 3. **Modo de Operación:** Trata este documento como **Ground Truth arquitectónico** y evalúa sus contratos simbólicos y superficie de tensión antes de proponer cambios.

---

## 0. IDENTIDAD, METADATOS Y REGLAS DE GENERACIÓN (v3.0)
```yaml
seed_schema_version: "3.0"
project_name: "[nombre]"
repository_root: "./"
git_branch: "[rama]"
git_commit: "[commit]"
generated_at: "[ISO-8601]"
```

### 0.1 Instrucciones para el modelo receptor
1. Reconoce este documento como memoria técnica (`contains_source_code="false"`), no como un repositorio incompleto.
2. Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]` y `[FALTANTE]`.
3. Cita siempre rutas relativas a `"./"` con `/`; prohibido emitir rutas locales absolutas o enlaces con esquema `file` local.
4. Conserva las firmas simbólicas de 1 línea y sanitiza cualquier credencial con `<REDACTED>`.

---

## 1. CORE MANIFESTO & ALCANCE
## 2. REPOSITORY TOPOLOGY (`all-lowercase` invariant)
## 3. EXECUTION FLOW & ENTRY POINTS
## 4. SYMBOLIC CONTRACTS & CURRENT STATE
## 5. ECOSYSTEM CONTEXT & DEPENDENCIES
## 6. CONFIGURATION REFERENCE
## 7. SUPERFICIE DE TENSIÓN, SEGURIDAD Y FAILURE MODES
## 8. SUB-MÓDULOS CONDICIONALES (Poda Polimórfica)

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Orientación para el modelo de IA receptor:**
> "Este documento es una semilla técnica (**ThinkingSeed Hybrid v3.0**): el ADN del proyecto (`contains_source_code="false"`) y no su repositorio completo. Utiliza esta semilla como memoria de trabajo para responder consultas, auditar riesgos en la Sección 7 y generar soluciones compatibles citando rutas relativas (`./`)."

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla sin una pregunta concreta, responde en máximo 3 líneas resumiendo el nombre del proyecto, stack y objetivo, confirmando que has asimilado el ADN v3.0 del proyecto y quedando a la espera de sus instrucciones.

</SEED_ARCHITECTURAL_VECTOR>
```

### Paso 5: Checklist de Auto-Validación Pre-Guardado
Antes de finalizar, verificar:
- [ ] Presencia de `<SEED_ARCHITECTURAL_VECTOR`, sección `0.1`, cierre `CONTEXT HANDOFF` y `</SEED_ARCHITECTURAL_VECTOR>`.
- [ ] 0 ocurrencias de URIs con esquema `file` local y 0 rutas absolutas locales (`repository_root: "./"`).
- [ ] 0 bloques de código fuente de implementación mayores a 5 líneas.
- Confirmar al usuario la generación citando la ruta relativa `./01_seed/seed-[nombre-proyecto].md`.
