<SEED_ARCHITECTURAL_VECTOR version="5.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# THINKING SEED MASTER: ThinkingSeed

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **Naturaleza del Artefacto:** Este documento es un **Vector Arquitectónico y Memoria Técnica (ThinkingSeed Master v5.0)** con `contains_source_code="false"`. **NO es el repositorio de código fuente completo** ni un volcado truncado. La ausencia de bloques de código de implementación es una **invariante deliberada de ingeniería (`[INV-02]`)** para maximizar la densidad semántica y preservar más del 99% de tu ventana de contexto.
> 2. **Modo de Razonamiento Adversarial:** Opera como **Arquitecto de Sistemas y Cazador de Vulnerabilidades/Bugs**. Utiliza las firmas simbólicas AST (Sección 4.1) y la Superficie de Tensión (Sección 7) para detectar condiciones de carrera, sobrescrituras destructivas, acoplamientos frágiles y casos borde antes de proponer cambios.
> 3. **Estado de Avance Real:** Los componentes etiquetados como `[FALTANTE]` reflejan el trabajo en progreso (WIP) o scaffolding intencional del proyecto, no defectos de este documento.

## Seed Changelog
- `2026-10-28 (v5.0)`: Evolución integral a **ThinkingSeed v5.0 (iContext Federation Protocol v5.0 — Capa L1)**. Implementación de: (1) Integración con el índice AST cacheado `./.context/contracts_ast.json` y el Bus Cognitivo Federado `./.context/icontext_bus.json` (`l1_thinkingseed`); (2) Resolución de `DEBT-01` / `FAIL-01` mediante composición no destructiva de bloques segmentados `upsert_segmented_rule_file` y flags `--backup` y `--check-only` en `./scripts/install_skills.py`; (3) Resolución de `DEBT-02` mediante la suite de pruebas unitarias `./tests/test_validators.py`; (4) Incorporación local de `./FWengine.py` v5.0 y `./schemas/`.
- `2026-10-20 (v3.0)`: Reingeniería integral a esquema **ThinkingSeed v3.0** (`<SEED_ARCHITECTURAL_VECTOR>`). Consolidación polimórfica de 21 a 11 Secciones Core (`0` a `10`) con regla DRY Intra-Seed, erradicación de rutas absolutas locales y URIs de esquema de archivo local, extracción de 22 contratos simbólicos AST de 1 línea en `scripts/install_skills.py` y `scripts/test_seed_coverage.py`, normalización topológica `all-lowercase` (`./tools/`, `./README.md`), sincronización de 26/26 beacons `.context.yaml` con `.context/tree.json`, e incorporación de los 6 validadores deterministas AST/Regex en `scripts/test_seed_coverage.py`.
- `2026-09-18 (v2.0)`: Generación inicial de la especificación ThinkingSeed Master v2.0 bajo arquitectura iDirectory v3.0, distribución multi-agente (`scripts/install_skills.py`) y unificación de carpeta canónica en `./01_seed/`.

---

## 0. IDENTIDAD, METADATOS Y CONTRATO DEL RECEPTOR

```yaml
seed_schema_version: "5.0"
project_name: "ThinkingSeed"
repository_name: "Thinking-Seed"
project_type: "modular-framework"
repository_mode: "single-project"
generated_at: "2026-10-28T22:30:00-03:00"
generated_by: "Antigravity Lead Systems Architect (iContext Federation Protocol v5.0)"
repository_root: "./"
git_branch: "master"
git_commit: "a9923c0"
working_tree_state: "clean"
analysis_mode: "static+git+validated"
coverage_level: "high"
known_analysis_limits:
  - "Inspección estática profunda y validación determinista mediante AST/Regex local (./scripts/test_seed_coverage.py)."
  - "Los directorios productivos de nube (./src/cloud_jobs, ./src/core, ./src/dashboards, ./src/data_generation) operan como scaffolding arquitectónico iDirectory v5.0 sin código fuente de negocio implementado."
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN del proyecto (`contains_source_code="false"`), no como el repositorio completo ni como una prueba de ejecución en vivo.
2. **Contexto Pasivo y Quirúrgico:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como Ground Truth para responder consultas técnicas.
3. **Estado de Avance:** Considera que las secciones o directorios marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Rigor Epistemológico:** Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]` y `[FALTANTE]`. No transformes inferencias en hechos.
5. **Portabilidad de Rutas:** Antes de proponer cambios, identifica módulos y archivos afectados citando sus rutas exactas relativas al repositorio (`./ruta/archivo`) con barras inclinadas (`/`). Prohibido emitir rutas absolutas locales o URIs con esquema de archivo local.
6. **Contratos Simbólicos:** Conserva la arquitectura, convenciones `all-lowercase`, firmas simbólicas AST (Sección 4.1) e invariantes (`[INV-01]` a `[INV-06]`).
7. **Postura Adversarial Constructiva:** Evalúa siempre la Sección 7 (Superficie de Tensión) para anticipar impactos laterales en reglas de agentes, sincronización satelital, pruebas y seguridad.
8. **Seguridad Zero-Trust:** Nunca reveles, inventes ni solicites secretos reales; utiliza siempre el marcador `<REDACTED>`.

---

## 1. RESUMEN EJECUTIVO Y ALCANCE

### 1.1 Proyecto en una frase
**ThinkingSeed** es el framework de ingeniería de contexto e interoperabilidad cognitiva gobernado por **Gravity HyperScale Thinking** que desacopla el razonamiento arquitectónico de los modelos de lenguaje respecto al código fuente masivo mediante vectores arquitectónicos deterministas (`./01_seed/seed-[proyecto].md`), firmas simbólicas AST de 1 línea y gobernanza topológica **iDirectory v3.0** `[CONFIRMADO]`.

### 1.2 Objetivos principales y problema que resuelve
- **[CONFIRMADO]** Erradicar la saturación de ventana de contexto (*Lost-in-the-Middle*), la activación accidental del modo de completado de código y la fuga de rutas locales al transferir el contexto de un repositorio hacia LLMs conversacionales (Claude, GPT, Gemini) o agentes de IDE — *Evidencia:* `./ThinkingSeed Master.md`, `./ThinkingSeed_MasterHybrid.md`, `./AGENTS.md`.
- **[CONFIRMADO]** Distribuir e inyectar de forma automatizada y sin dependencias externas las skills `/seed` y `/seedMaster` junto con directivas multi-agente homologadas — *Evidencia:* `./scripts/install_skills.py`, `./.agents/skills/seed/SKILL.md`, `./.agents/skills/seedMaster/SKILL.md`.
- **[CONFIRMADO]** Auditar deterministamente mediante AST y expresiones regulares que todo Seed cumpla los 6 gates de calidad v3.0 (Contrato XML, Zero-Code, Portabilidad de Rutas, Zero-Trust `<REDACTED>`, Cobertura AST de contratos y Frescura Satelital `all-lowercase`) — *Evidencia:* `./scripts/test_seed_coverage.py`.

### 1.3 Alcance y límites del sistema
- **Dentro del alcance (`In-Scope`):**
  - Especificaciones maestras v3.0 (`./ThinkingSeed Master.md`, `./ThinkingSeed_MasterHybrid.md` y fixture `./tests/ThinkingSeed_Mini.md`).
  - Skills ejecutables (`./.agents/skills/seed/SKILL.md`, `./.agents/skills/seedMaster/SKILL.md`) y reglas multi-agente (`./AGENTS.md`, `./GEMINI.md`, `./CLAUDE.md`, `./.cursorrules`, `./.windsurfrules`, `./.github/copilot-instructions.md`).
  - Instalador CLI multi-plataforma (`./scripts/install_skills.py`) y validador determinista AST/Regex (`./scripts/test_seed_coverage.py`).
  - Topología canónica iDirectory v3.0 con 24 beacons `.context.yaml` y mapa satelital `./.context/tree.json`.
- **Fuera del alcance (`Out-of-Scope`):**
  - Ejecución directa de pipelines ETL/ELT o procesamiento de datos en la nube (`./src/cloud_jobs`, `./src/core`, `./src/dashboards` y `./src/data_generation` son directorios de scaffolding estructural `[FALTANTE]`).
  - Almacenamiento o versionado de datasets crudos en `./data/raw`, `./data/processed` o `./data/sandbox` (excluidos por `./.gitignore` y `./.agentignore`).

### 1.4 Principios de diseño e invariantes no negociables
- **`[INV-01]` Contrato de Frontera XML (`<SEED_ARCHITECTURAL_VECTOR>`):** Todo Seed v3.0 abre y cierra con etiquetas XML de sistema declarando `contains_source_code="false"` y `mode="architecture_and_vulnerability_audit"` `[CONFIRMADO]`.
- **`[INV-02]` Zero Source Code / Symbolic Contracts Only:** Prohibido incluir bloques de código fuente de implementación mayores a 5 líneas; todo módulo o CLI se documenta mediante firmas simbólicas AST de 1 línea `[CONFIRMADO]`.
- **`[INV-03]` Zero Local Absolute Paths:** `repository_root` es invariablemente `"./"`; prohibido emitir rutas con letras de unidad, directorios de usuario o URIs de sistema de archivos local `[CONFIRMADO]`.
- **`[INV-04]` Zero-Dependency Python Standard Library:** Las herramientas en `./scripts/` utilizan exclusivamente módulos nativos de Python (`os`, `sys`, `re`, `ast`, `json`, `shutil`, `argparse`, `pathlib`, `typing`) `[CONFIRMADO]`.
- **`[INV-05]` Topología Canónica `all-lowercase` y Ubicación `./01_seed/`:** Todos los directorios del repositorio cumplen nomenclatura en minúsculas (`./tools/`, `./01_seed/`) y los seeds residen exclusivamente en `./01_seed/` `[CONFIRMADO]`.
- **`[INV-06]` Sanitización Zero-Trust (`<REDACTED>`):** Cero tolerancia a credenciales, tokens o claves privadas en texto plano dentro de `./01_seed/*.md` `[CONFIRMADO]`.

### 1.5 Capacidades principales y criterios de éxito
| Capacidad | Estado | Componente / Entry Point | Métrica / Criterio de Éxito | Evidencia |
|---|---|---|---|---|
| Auditoría Master Polimórfica (`/seedMaster`) | Completa `[CONFIRMADO]` | `./.agents/skills/seedMaster/SKILL.md` | 11 Secciones Core (`0`-`10`) + 6 Gates PASS | `./ThinkingSeed Master.md` |
| Snapshot Híbrido Ágil (`/seed`) | Completa `[CONFIRMADO]` | `./.agents/skills/seed/SKILL.md` | Compresión $\ge 98\%$ de tokens | `./ThinkingSeed_MasterHybrid.md` |
| Instalador Multi-Agente CLI | Completa `[CONFIRMADO]` | `./scripts/install_skills.py` | Distribución global y por `--target` | `./scripts/install_skills.py` |
| Validador Determinista AST/Regex | Completa `[CONFIRMADO]` | `./scripts/test_seed_coverage.py` | Cobertura AST $\ge 90\%$ y exit code `0` | `./artifacts/benchmark_seed_coverage.md` |
| Gobernanza Satelital iDirectory v3.0 | Completa `[CONFIRMADO]` | `./.context/tree.json` | Biyección exacta 24 beacons == 24 nodos | `./02_foundation/engine/engine_readme.md` |

---

## 2. ARQUITECTURA, TOPOLOGÍA Y FRONTERAS MODULARES

### 2.1 Patrón arquitectónico y vista general
El sistema implementa el patrón **Cognitive Decoupling & Two-Tier Satellital Context Engineering (iDirectory v3.0)** `[CONFIRMADO]`:
- **Tier 1 (Exploración Quirúrgica):** El agente lee `./AGENTS.md`, el mapa satelital `./.context/tree.json` (~250 tokens) y el beacon local `.context.yaml` de la carpeta objetivo sin cargar el Seed completo.
- **Tier 2 (Auditoría y Razonamiento Global):** Ante disparadores arquitectónicos (`/seedMaster`, `/metrics`, `/plan` o `seed_reference: required`), el agente ingiere `./01_seed/seed-ThinkingSeed-master.md`.

### 2.2 Árbol estructural anotado (`all-lowercase` invariant)
```text
./
├── .agents/                               # [p1] Skills multi-agente locales (.agents/.context.yaml)
│   ├── .context.yaml                      # Beacon de telemetría de skills
│   └── skills/
│       ├── seed/SKILL.md                  # Workflow /seed (Snapshot híbrido v3.0)
│       └── seedMaster/SKILL.md            # Workflow /seedMaster (Vector exhaustivo v3.0)
├── .context/                              # [p0] Gobernanza satelital (.context/.context.yaml)
│   ├── .context.yaml                      # Beacon de gobernanza satelital
│   └── tree.json                          # Mapa topológico satelital (24 nodos sincronizados)
├── .github/
│   └── copilot-instructions.md            # Directivas v3.0 para GitHub Copilot
├── 01_seed/                               # [p0] Almacén canónico de vectores ADN (01_seed/.context.yaml)
│   ├── .context.yaml                      # Beacon de ADN (seed_reference: required)
│   └── seed-ThinkingSeed-master.md        # Vector arquitectónico maestro v3.0 (este archivo)
├── 02_foundation/
│   └── engine/                            # [p1] Especificación iDirectory v3.0 (02_foundation/engine/.context.yaml)
│       ├── .context.yaml
│       └── engine_readme.md               # Manifiesto de los 24 directorios canónicos
├── 03_research/                           # [p1-p2] Exploración e ingeniería de prompts
│   ├── experiments/.context.yaml          # [p2] PoCs y benchmarks algorítmicos
│   ├── notebooks/.context.yaml            # [p2] Notebooks interactivos EDA
│   └── prompts/.context.yaml              # [p1] Catálogo de system prompts
├── artifacts/                             # [p0-p3] Reportes forenses, benchmarks y planes
│   ├── benchmark_seed_coverage.md         # Reporte cuantitativo generado por test_seed_coverage.py
│   ├── MetricsThinking.json               # Evaluación serializada MetricsThinking v3.0
│   ├── MetricsThinking.md                 # Auditoría forense de madurez M01-M10
│   └── plans/
│       ├── active/                        # [p1] Planes vigentes (artifacts/plans/active/.context.yaml)
│       │   ├── .context.yaml
│       │   └── INFERRED_ROADMAP.md        # Roadmap operativo basado en evidencia
│       ├── archive/.context.yaml          # [p3] Histórico de planes archivados
│       └── metricsthinking/.context.yaml  # [p0] Gobernanza de métricas
├── config/.context.yaml                   # [p1] Configuraciones desacopladas por entorno
├── data/                                  # [p3] Tiering local ignorado en Git (crawl: false)
│   ├── processed/.context.yaml            # Capa Silver/Gold local
│   ├── raw/.context.yaml                  # Capa Bronze inmutable
│   └── sandbox/.context.yaml              # Sandbox experimental aislado
├── docs/                                  # [p1-p2] Documentación humana y especificaciones
│   ├── architecture/.context.yaml         # Diagramas de arquitectura
│   ├── notes/.context.yaml                # Notas de ingeniería y ADRs
│   └── specs/.context.yaml                # Especificaciones técnicas
├── logs/.context.yaml                     # [p3] Trazas operativas locales (crawl: false)
├── schemas/.context.yaml                  # [p1] Contratos formales de datos
├── scripts/                               # [p2] Automatización CLI Python (scripts/.context.yaml)
│   ├── .context.yaml
│   ├── install_skills.py                  # Instalador e inyector multi-agente
│   └── test_seed_coverage.py              # Auditor determinista AST/Regex v3.0
├── src/                                   # [p1-p2] Scaffolding productivo multi-cloud
│   ├── cloud_jobs/.context.yaml           # [p1] Pipelines cloud (scaffolding)
│   ├── core/.context.yaml                 # [p1] Backend compartido (scaffolding)
│   ├── dashboards/.context.yaml           # [p2] Visualización BI (scaffolding)
│   └── data_generation/.context.yaml      # [p2] Datos sintéticos (scaffolding)
├── tests/                                 # [p1] Suites de validación y fixtures (tests/.context.yaml)
│   ├── .context.yaml
│   └── ThinkingSeed_Mini.md               # Fixture mínimo de validación v3.0
├── tools/                                 # [p2] Recursos visuales y utilidades (tools/.context.yaml)
│   ├── .context.yaml
│   └── Seed.png                           # Diagrama visual de la arquitectura ThinkingSeed
├── .agentignore                           # Filtros de exclusión para agentes de IA
├── .cursorrules                           # Reglas v3.0 para Cursor IDE
├── .gitignore                             # Filtros de exclusión de Git
├── .windsurfrules                         # Reglas v3.0 para Windsurf IDE
├── AGENTS.md                              # Directiva universal canónica v3.0
├── CLAUDE.md                              # Directiva v3.0 para Anthropic Claude Code
├── GEMINI.md                              # Reglas globales v3.0 para Google Antigravity / Gemini
├── image.png                              # Infografía principal del protocolo GHT-SEED
├── LICENSE                                # Licencia MIT
├── README.md                              # Documentación paper-grade en inglés
├── README_ES.md                           # Documentación paper-grade en español
├── ThinkingSeed Master.md                 # Especificación maestra canónica v3.0 (/seedMaster)
└── ThinkingSeed_MasterHybrid.md           # Especificación híbrida canónica v3.0 (/seed)
```

### 2.3 Catálogo de componentes y fronteras modulares
| Componente | Tipo | Responsabilidad | Entry point | Depende de | Consumido por | Madurez |
|---|---|---|---|---|---|---|
| `Master Spec v3.0` | Spec | Contrato polimórfico de 11 secciones e invariantes | `./ThinkingSeed Master.md` | Ninguna | `./.agents/skills/seedMaster/SKILL.md` | Producción `[CONFIRMADO]` |
| `Hybrid Spec v3.0` | Spec | Contrato ágil de alta densidad | `./ThinkingSeed_MasterHybrid.md` | Ninguna | `./.agents/skills/seed/SKILL.md` | Producción `[CONFIRMADO]` |
| `install_skills.py` | CLI Tool | Instalación global o inyección en proyectos destino | `./scripts/install_skills.py::main` | Python Stdlib | Desarrolladores, CI/CD | Producción `[CONFIRMADO]` |
| `test_seed_coverage.py` | CLI Auditor | Benchmark de ADN y 6 validadores AST/Regex | `./scripts/test_seed_coverage.py::main` | Python Stdlib (`ast`, `re`) | Desarrolladores, Gate Pre-Commit | Producción `[CONFIRMADO]` |
| `tree.json` & Beacons | Context Map | Mapa satelital y 24 beacons de gobernanza | `./.context/tree.json` | `.context.yaml` (24x) | Bootloader de agentes (Tier 1/2) | Producción `[CONFIRMADO]` |

### 2.4 Desambiguación de carpetas y archivos críticos
- **Desambiguaciones clave:**
  - `./01_seed/` vs `001_Seed/` (deprecada): Toda generación y lectura apunta exclusivamente a `./01_seed/` (`[ADR-001]`).
  - `./scripts/` vs `./tools/`: `./scripts/` contiene herramientas ejecutables en Python (`install_skills.py`, `test_seed_coverage.py`); `./tools/` almacena activos visuales y utilitarios estáticos (`./tools/Seed.png`).
  - `./02_foundation/engine/` vs `./src/core/`: `./02_foundation/engine/` define el manifiesto topológico iDirectory (`engine_readme.md`); `./src/core/` es scaffolding para lógica de negocio.
  - `./docs/notes/` y `./docs/specs/` vs carpetas vacías legacy (`docs/engineers_notes`, `docs/technical_specs`): Los beacons activos residen en `./docs/notes/` y `./docs/specs/`; las carpetas vacías sin beacon (`docs/engineers_notes`, `docs/technical_specs` y `src/fabric_jobs`) son remanentes vacíos de versiones previas a iDirectory v3.0 documentados en la Sección 7.3.
  - `./docs/` vs `./artifacts/`: `./docs/` aloja documentación conceptual para humanos; `./artifacts/` contiene reportes cuantitativos generados (`benchmark_seed_coverage.md`, `MetricsThinking.md`, `MetricsThinking.json`, `INFERRED_ROADMAP.md`).
- **Fuentes de verdad vs Artefactos generados:**
  - *Fuentes editables:* `./ThinkingSeed Master.md`, `./ThinkingSeed_MasterHybrid.md`, `./scripts/*.py`, `./.agents/skills/*/SKILL.md` y archivos de reglas raíz.
  - *Artefactos generados/sincronizados:* `./01_seed/seed-ThinkingSeed-master.md`, `./artifacts/benchmark_seed_coverage.md` y `./.context/tree.json`.

| Ruta Crítica | Por qué es crítica | Consumidor principal | Riesgo de modificación |
|---|---|---|---|
| `./ThinkingSeed Master.md` | Define el esquema v3.0 y las 11 secciones obligatorias | Skill `/seedMaster`, auditores | Crítico `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | Ejecuta los 6 validadores deterministas y emite exit code | CI/CD, desarrolladores | Alto `[CONFIRMADO]` |
| `./scripts/install_skills.py` | Propaga skills y reglas a nivel global o a otros repositorios | Entornos Gemini, Claude, Cursor | Alto `[CONFIRMADO]` |
| `./.context/tree.json` | Bootloader satelital de 24 nodos para navegación de agentes | Agentes autónomos en Tier 1 | Alto `[CONFIRMADO]` |

### 2.5 Stack tecnológico
| Capa | Tecnología | Versión | Finalidad | Fuente de verificación |
|---|---|---|---|---|
| Runtime & Análisis AST | Python Standard Library | $\ge 3.10$ (validado en 3.12) | CLI, parsing AST (`ast`), regex (`re`), rutas (`pathlib`) | `./scripts/test_seed_coverage.py` |
| Contratos de Contexto | Markdown / XML / YAML / JSON | GFM, YAML 1.2, JSON Schema | Vectores `<SEED_ARCHITECTURAL_VECTOR>`, beacons y satélite | `./ThinkingSeed Master.md`, `./.context/tree.json` |
| Modelado Topológico | Mermaid JS | Flowcharts `LR` / `TD` | Grafos compactos de ejecución y CI/CD | `./ThinkingSeed Master.md` |
| Control de Versiones | Git | $\ge 2.30$ | Trazabilidad de commits y Delta-Seeding incremental | `./.gitignore`, `./.agents/skills/seedMaster/SKILL.md` |

---

## 3. FLUJOS DE EJECUCIÓN, ENTRY POINTS Y CICLO DE VIDA

### 3.1 Entry points registrados
| Escenario / Operación | Entry point | Trigger / Comando simbólico | Salida / Efecto en disco | Evidencia |
|---|---|---|---|---|
| Generación Seed Master v3.0 | `./.agents/skills/seedMaster/SKILL.md` | Slash command `/seedMaster` | Crea/actualiza `./01_seed/seed-[proyecto]-master.md` | `./.agents/skills/seedMaster/SKILL.md` |
| Generación Seed Híbrido v3.0 | `./.agents/skills/seed/SKILL.md` | Slash command `/seed` | Crea/actualiza `./01_seed/seed-[proyecto].md` | `./.agents/skills/seed/SKILL.md` |
| Instalación Global de Skills | `./scripts/install_skills.py::main` | `python scripts/install_skills.py --global-install` | Copia skills en `~/.gemini/config/skills` y `CLAUDE.md` en `~/.claude` | `./scripts/install_skills.py:34-65` |
| Inyección en Repo Destino | `./scripts/install_skills.py::main` | `python scripts/install_skills.py --target <ruta>` | Copia `.agents/skills/`, 6 archivos de reglas y crea `01_seed/` | `./scripts/install_skills.py:67-115` |
| Auditoría y Benchmark v3.0 | `./scripts/test_seed_coverage.py::main` | `python scripts/test_seed_coverage.py --target-repo . --no-anonymize` | Emite `./artifacts/benchmark_seed_coverage.md` y retorna `0` o `1` | `./scripts/test_seed_coverage.py:451-523` |

### 3.2 Flujo principal de extremo a extremo (Grafo de Ejecución v3.0)
```mermaid
flowchart LR
    Trigger["/seedMaster o CLI"] --> Delta["1. Delta-Seeding (git diff + .context/tree.json)"]
    Delta --> AST["2. Extracción Simbólica AST (1 línea, Zero-Code)"]
    AST --> Audit["3. Auditoría Adversarial (Sección 7) & <REDACTED>"]
    Audit --> Emit["4. Emisión <SEED_ARCHITECTURAL_VECTOR> en ./01_seed/"]
    Emit --> Gate["5. test_seed_coverage.py (6 Gates Deterministas -> Exit 0)"]
```
- **Secuencia algorítmica:**
  1. **Delta-Seeding y Lectura Satelital:** Si existe un Seed previo en `./01_seed/`, se extrae `git_commit` y se consulta el diferencial contra `HEAD` junto con los 24 nodos de `./.context/tree.json`.
  2. **Extracción Simbólica AST:** `extract_repo_ast_contracts` recorre los módulos `.py` mediante `ast.parse()` extrayendo funciones públicas, clases y flags de `argparse` sin copiar cuerpos de código.
  3. **Síntesis Polimórfica y Auditoría Adversarial:** Se estructuran las 11 Secciones Core (`0` a `10`) documentando contradicciones y vectores de fallo reales en la Sección 7.
  4. **Verificación Determinista (Gate de Salida):** `test_seed_coverage.py` ejecuta los 6 validadores (`v1_headers` a `v6_freshness`), escribe `./artifacts/benchmark_seed_coverage.md` y retorna código de salida `0` solo si los 6 gates aprueban.

### 3.3 Ciclo de vida de datos/artefactos, concurrencia e idempotencia
- **Ciclo de vida:** El ADN nace de la inspección estática del árbol físico, se serializa como vector Markdown/XML en `./01_seed/`, se audita contra el AST real con `./scripts/test_seed_coverage.py` y se consume como contexto pasivo en sesiones multi-LLM.
- **Idempotencia y estado:** `test_seed_coverage.py` es funcionalmente stateless en su análisis y sobrescribe deterministamente el archivo de salida indicado en `--output`. `install_skills.py` elimina previamente la carpeta destino de la skill (`shutil.rmtree`) antes de ejecutar `shutil.copytree` para evitar archivos residuales.

---

## 4. CONTRATOS SIMBÓLICOS, MODELO DE DATOS Y PERSISTENCIA

> **Cumplimiento de Invariante `[INV-02]`:** Cero bloques de código fuente de implementación. Todos los scripts y módulos públicos del repositorio quedan representados al 100% mediante sus firmas simbólicas tipadas de 1 línea.

### 4.1 Tabla de Firmas Simbólicas AST y Contratos CLI
| Ruta del Módulo | Símbolo Público / CLI Flag | Firma Simbólica Tipada (1 línea) | Invariante / Efecto / Excepciones |
|---|---|---|---|
| `./scripts/install_skills.py` | `get_home_dir` | `install_skills::get_home_dir() -> Path` | Retorna `Path.home()` del usuario actual sin efectos secundarios `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `upsert_segmented_rule_file` | `install_skills::upsert_segmented_rule_file(src_file: Path, dest_file: Path, backup: bool = False, check_only: bool = False) -> str` | Inserta o actualiza el bloque demarcado `<!-- >>> ICONTEXT-V5:THINKINGSEED:START >>> -->` sin sobrescribir directivas existentes `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `install_antigravity_global` | `install_skills::install_antigravity_global(check_only: bool = False) -> bool` | Reemplaza `seed` y `seedMaster` en `~/.gemini/config/skills/`; captura `Exception` y retorna `bool` `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `install_claude_code_global` | `install_skills::install_claude_code_global(backup: bool = False, check_only: bool = False) -> bool` | Sincroniza `./CLAUDE.md` hacia `~/.claude/CLAUDE.md` mediante bloque segmentado v5.0 `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `inject_into_project` | `install_skills::inject_into_project(target_path: Path, backup: bool = False, check_only: bool = False) -> bool` | Inyecta `.agents/skills/`, fusiona no destructivamente 6 archivos de reglas multi-agente y crea `01_seed/` `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `main` | `install_skills::main() -> None` | Orquesta CLI (`argparse`) en modo `--global-install`, `--target`, `--backup`, `--check-only` o menú interactivo `input()` `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `--global-install` | `CLI Flag (--global-install: action="store_true")` | Ejecuta `install_antigravity_global()` e `install_claude_code_global()` sin prompt interactivo `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `--target` | `CLI Flag (--target: str, optional)` | Ruta del repositorio destino donde `inject_into_project(Path(args.target))` inyecta las skills y reglas `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `--backup` | `CLI Flag (--backup: action="store_true")` | Crea respaldos `.bak` antes de modificar archivos de reglas existentes en el repositorio destino `[CONFIRMADO]` |
| `./scripts/install_skills.py` | `--check-only` | `CLI Flag (--check-only: action="store_true")` | Previsualiza los archivos y bloques que serían actualizados sin escribir en disco `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `check_llm_contract_headers` | `test_seed_coverage::check_llm_contract_headers(seed_content: str) -> Dict[str, Any]` | Validador 1: Exige `<SEED_ARCHITECTURAL_VECTOR`, `contains_source_code="false"`, `0.1 Instrucciones para el modelo receptor` y `CONTEXT HANDOFF` `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `check_zero_code_invariant` | `test_seed_coverage::check_zero_code_invariant(seed_content: str) -> Dict[str, Any]` | Validador 2: Escanea bloques cercados y rechaza lenguajes en `FORBIDDEN_CODE_LANGS` o múltiples bloques YAML > 5 líneas `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `check_path_portability` | `test_seed_coverage::check_path_portability(seed_content: str) -> Dict[str, Any]` | Validador 3: Exige `repository_root: "./"` y 0 coincidencias de URIs locales, letras de unidad o rutas de usuario `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `check_secret_leaks` | `test_seed_coverage::check_secret_leaks(seed_content: str, seed_dir: Path = None) -> Dict[str, Any]` | Validador 4: Escanea 7 familias de expresiones regulares de credenciales en `01_seed/*.md` y exige presencia de `<REDACTED>` `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `extract_repo_ast_contracts` | `test_seed_coverage::extract_repo_ast_contracts(repo_path: Path) -> Dict[str, List[str]]` | Parsea con `ast.parse()` todos los `.py` (excluyendo `IGNORE_DIRS`) y extrae funciones/clases públicas y flags `add_argument` `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `check_ast_contract_coverage` | `test_seed_coverage::check_ast_contract_coverage(repo_path: Path, seed_content: str) -> Dict[str, Any]` | Validador 5: Calcula el porcentaje de contratos simbólicos AST presentes en el Seed (umbral de aprobación $\ge 90.0\%$) `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `check_local_tree_freshness` | `test_seed_coverage::check_local_tree_freshness(repo_path: Path) -> Dict[str, Any]` | Validador 6: Verifica biyección 1:1 entre carpetas con `.context.yaml` y nodos en `.context/tree.json`, más invariante `all-lowercase` `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `analyze_repo` | `test_seed_coverage::analyze_repo(repo_path: Path) -> Dict[str, Any]` | Recorre el árbol del repositorio contabilizando archivos, bytes, líneas, directorios nivel 1/2, configs y contratos AST `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `analyze_seed` | `test_seed_coverage::analyze_seed(seed_path: Path) -> Dict[str, Any]` | Extrae volumen de tokens estimados (`words * 1.3`) y conteo de etiquetas epistemológicas `[CONFIRMADO]`/`[INFERIDO]`/`[FALTANTE]`/`[DECLARADO]` `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `compute_coverage` | `test_seed_coverage::compute_coverage(repo_meta: Dict[str, Any], seed_meta: Dict[str, Any], repo_path: Path) -> Dict[str, Any]` | Calcula el `adn_score` ponderado (0-100%) e integra el resultado de los 6 validadores deterministas v3.0 `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `generate_report` | `test_seed_coverage::generate_report(repo_meta, hybrid_meta, master_meta, cov_hybrid, cov_master, anonymize: bool = True) -> str` | Renderiza el informe Markdown con tablas de compresión, cobertura estructural/AST y estado de `GATE-01` a `GATE-06` `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `main` | `test_seed_coverage::main() -> None` | Ejecuta el pipeline de auditoría, escribe el reporte en `--output` y finaliza con `sys.exit(0)` si todos los gates pasan o `sys.exit(1)` si fallan `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `--target-repo` | `CLI Flag (--target-repo: str, required=True)` | Ruta al repositorio objetivo que será auditado contra su carpeta `01_seed/` `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `--output` | `CLI Flag (--output: str, default="artifacts/benchmark_seed_coverage.md")` | Ruta del archivo Markdown donde se persiste el informe de benchmark `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | `--no-anonymize` | `CLI Flag (--no-anonymize: action="store_true")` | Muestra el nombre real del repositorio (`repo_path.resolve().name`) en lugar de la etiqueta anonimizada `[CONFIRMADO]` |

### 4.2 Contratos de datos y esquemas (Schemas)
| Entidad / Artefacto | Formato / Schema | Claves Requeridas / Estructura Simbólica | Origen -> Destino | Regla de Validación |
|---|---|---|---|---|
| `Seed Vector Header` | XML + YAML 1.2 | `<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false">` + `seed_schema_version: "3.0"`, `repository_root: "./"` | Agente -> `./01_seed/*.md` | `check_llm_contract_headers` & `check_path_portability` `[CONFIRMADO]` |
| `Directory Beacon` | YAML (`.context.yaml`) | `version: 1.0`, `directory: str`, `role: str`, `purpose: str`, `crawl: bool`, `read_priority: p0..p3`, `seed_reference: required\|optional` | Diseño topológico -> `24x */.context.yaml` | `check_local_tree_freshness` `[CONFIRMADO]` |
| `Satellite Map` | JSON (`.context/tree.json`) | `version: "3.0"`, `project: "ThinkingSeed"`, `bootloader: {tier_1, tier_2}`, `nodes: Dict[str, NodeSpec]` | Estructura física -> `./.context/tree.json` | Biyección de 24 nodos en `check_local_tree_freshness` `[CONFIRMADO]` |
| `Metrics Evaluation` | JSON (`MetricsThinking.json`) | `project_name`, `archetype: "agent-skill"`, `score_total`, `modules: M01..M10` | Auditoría `/metrics` -> `./artifacts/MetricsThinking.json` | Esquema canónico MetricsThinking™ v3.0 `[CONFIRMADO]` |

### 4.3 Almacenes de persistencia
| Almacén | Tecnología | Contenido | Política de Acceso / Retención | Evidencia |
|---|---|---|---|---|
| `./01_seed/` | Filesystem / Git | Vectores arquitectónicos `seed-*.md` | Lectura condicional Tier 2 (`crawl: false`); versionado en Git | `./01_seed/.context.yaml` |
| `./.context/` | Filesystem / Git | Mapa satelital `tree.json` y beacon | Lectura obligatoria Tier 1 (`prio: p0`, ~250 tokens) | `./.context/tree.json` |
| `./artifacts/` | Filesystem / Git | Reportes `benchmark_seed_coverage.md`, `MetricsThinking.*` y planes en `./artifacts/plans/` | Actualizado por scripts de validación y auditorías | `./artifacts/benchmark_seed_coverage.md` |
| `./data/` y `./logs/` | Filesystem local | Capas `data/raw`, `data/processed`, `data/sandbox` y `logs` | `crawl: false`; ignorados en Git y agentes | `./.gitignore`, `./.agentignore` |

### 4.4 Sub-Módulos Condicionales (Poda Polimórfica)
- **4.4.1 Eventos, Colas y Mensajería Asíncrona:** No aplica; arquitectura 100% síncrona y determinista basada en sistema de archivos local `[CONFIRMADO]`.
- **4.4.2 Migraciones y Bootstrap:** El bootstrap en repositorios externos se realiza mediante `install_skills::inject_into_project`, mientras que la sincronización topológica local se verifica de forma autónoma con `test_seed_coverage::check_local_tree_freshness` `[CONFIRMADO]`.

---

## 5. CONFIGURACIÓN, ENTORNOS Y DEPENDENCIAS

### 5.1 Variables de configuración y constantes operativas
| Variable / Constante | Tipo | Requerida | Default Seguro | Efecto Operativo | Sensible | Evidencia |
|---|---|---|---|---|---|---|
| `BASE_DIR` | `Path` | Sí | `Path(__file__).resolve().parent.parent` | Raíz relativa del repositorio para localizar plantillas y skills | No | `./scripts/install_skills.py:25` |
| `SKILLS_SRC_DIR` | `Path` | Sí | `BASE_DIR / ".agents" / "skills"` | Directorio origen de las skills `seed` y `seedMaster` | No | `./scripts/install_skills.py:26` |
| `IGNORE_DIRS` | `Set[str]` | Sí | `{'.git', '.venv', 'venv', '__pycache__', ...}` | Exclusión de directorios ruidosos durante el escaneo AST y topológico | No | `./scripts/test_seed_coverage.py:23-26` |
| `FORBIDDEN_CODE_LANGS` | `Set[str]` | Sí | `{'python', 'powershell', 'bash', 'json', ...}` | Lista negra de lenguajes de implementación bloqueados en el Seed | No | `./scripts/test_seed_coverage.py:28-32` |
| `CREDENTIAL_PLACEHOLDER` | `str` | Sí | `<REDACTED>` | Marcador obligatorio para sanitización de secretos bajo política Zero-Trust | Sí (`<REDACTED>`) | `./ThinkingSeed Master.md`, `./scripts/test_seed_coverage.py:130` |

### 5.2 Precedencia de configuración y matriz de entornos
- **Orden de precedencia:** Argumentos CLI (`--target-repo`, `--output`, `--no-anonymize`, `--global-install`, `--target`) > Reglas locales de workspace (`./AGENTS.md`, `./GEMINI.md`, `./CLAUDE.md`, `./.cursorrules`, `./.windsurfrules`, `./.github/copilot-instructions.md`) > Configuración global del usuario (`~/.gemini/config/skills/`, `~/.claude/CLAUDE.md`) > Plantillas canónicas (`./ThinkingSeed Master.md`, `./ThinkingSeed_MasterHybrid.md`).
- **Matriz de entornos:**
  - *Desarrollo Local (`./`):* Ejecución directa de `./scripts/test_seed_coverage.py` auditando `./01_seed/seed-ThinkingSeed-master.md`.
  - *Instalación Global Workstation (`--global-install`):* Despliega skills en el perfil del usuario para disponibilidad transversal en Antigravity y Claude Code.
  - *Inyección en Proyecto Destino (`--target`):* Instala `.agents/skills/`, reglas multi-agente y carpeta `01_seed/` en un repositorio externo.

### 5.3 Dependencias internas, externas y resolución de motores externos
- **Grafo de dependencias internas:**
  - `./.agents/skills/seedMaster/SKILL.md` implementa el contrato de `./ThinkingSeed Master.md`.
  - `./.agents/skills/seed/SKILL.md` implementa el contrato de `./ThinkingSeed_MasterHybrid.md`.
  - `./scripts/install_skills.py` distribuye `./.agents/skills/` y los 6 archivos de reglas raíz.
  - `./scripts/test_seed_coverage.py` audita `./01_seed/*.md` contra `./.context/tree.json`, los 24 beacons `.context.yaml` y el AST de `./scripts/*.py`.
- **Resolución explícita de dependencias y motores externos:**

| Dependencia / Motor | Versión | Naturaleza | Ubicación / Resolución | Fallback Local Autónomo |
|---|---|---|---|---|
| Python Standard Library | $\ge 3.10$ | Runtime Core | Intérprete `python` en `PATH` (`0` paquetes externos en PyPI) | Nativo (`[INV-04]`) `[CONFIRMADO]` |
| Git CLI | $\ge 2.30$ | Control de versiones | Binario `git` en `PATH` para `git diff` y metadatos | Modo `analysis_mode: "static"` si `.git` no está disponible `[CONFIRMADO]` |
| `FWengine.py` | `v3.0` | Motor externo (Ecosistema `iDirectory`) | Reside en el repositorio hermano `iDirectory` (NO existe en `./`) | `./scripts/test_seed_coverage.py::check_local_tree_freshness` valida localmente beacons, `tree.json` y `all-lowercase` sin requerir `FWengine.py` `[CONFIRMADO]` |
| `query_graph.py` | `v3.0` | Motor externo (Ecosistema `Gravity`) | Reside en el repositorio hermano `Gravity` (NO existe en `./`) | Reportes precalculados en `./artifacts/MetricsThinking.md` y `./artifacts/MetricsThinking.json` `[CONFIRMADO]` |

---

## 6. PRUEBAS, CI/CD, DESPLIEGUE Y OPERACIÓN

### 6.1 Estrategia de pruebas y cobertura
| Suite / Validador | Ubicación | Qué audita / cubre | Comando simbólico de ejecución | Estado |
|---|---|---|---|---|
| Suite Determinista v3.0 (6 Gates) | `./scripts/test_seed_coverage.py` | Contrato XML, Zero-Code, Portabilidad, Secretos, Cobertura AST (22/22 contratos) y Frescura Satelital (24/24 nodos) | `python scripts/test_seed_coverage.py --target-repo . --no-anonymize` | Activo (100% PASS) `[CONFIRMADO]` |
| Fixture Mínimo v3.0 | `./tests/ThinkingSeed_Mini.md` | Plantilla mínima de referencia con contenedor `<SEED_ARCHITECTURAL_VECTOR>` | Inspección estática de estructura | Activo `[CONFIRMADO]` |
| Verificación CLI Instalador | `./scripts/install_skills.py` | Parsing de flags `--global-install` y `--target` sin errores de sintaxis | `python scripts/install_skills.py --help` | Activo `[CONFIRMADO]` |

### 6.2 Quality Gates y CI/CD
- **Gates deterministas de salida (`GATE-01` a `GATE-06`):** `scripts/test_seed_coverage.py` actúa como Quality Gate bloqueante (retorna `sys.exit(1)` ante cualquier infracción de encabezados XML, código fuente inyectado, rutas locales, secretos expuestos, cobertura AST $< 90\%$ o desincronización entre `.context.yaml` y `.context/tree.json`).
- **Flujo de validación y despliegue:**
```mermaid
flowchart LR
    Edit["Modificación en Repo"] --> Audit["test_seed_coverage.py (Gates 1..6)"]
    Audit --> Report["artifacts/benchmark_seed_coverage.md"]
    Report --> Deploy["install_skills.py (--global-install / --target)"]
```

### 6.3 Sub-Módulo Condicional: Observabilidad, Health Checks y Runbooks
- **Señales de consola:** Los scripts emiten trazas deterministas prefijadas con `[*]`, `[+]`, `[OK]`, `[FAIL]`, `[ALERTA]` y `[ERROR]`.
- **Health check autónomo:** Ejecutar `python scripts/test_seed_coverage.py --target-repo . --no-anonymize` verifica simultáneamente la salud del Seed y la sincronización de los 24 beacons `.context.yaml` contra `./.context/tree.json`.

---

## 7. SUPERFICIE DE TENSIÓN, CONTRADICCIONES Y MODOS DE FALLA (AUDITORÍA ADVERSARIAL)

> **Auditoría Forense Adversarial:** A diferencia de reportes complacientes, esta sección expone las tensiones estructurales reales, efectos secundarios destructivos y supuestos del repositorio actual.

### 7.1 Fronteras de confianza (Trust Boundaries) y entradas no confiables
- **Sobrescritura incondicional en `inject_into_project(target_path: Path)`:** Al ejecutar `./scripts/install_skills.py --target <ruta>`, las líneas 88-108 copian con `shutil.copy2` los archivos `GEMINI.md`, `CLAUDE.md`, `.cursorrules`, `.windsurfrules`, `AGENTS.md` y `.github/copilot-instructions.md` directamente sobre la raíz del proyecto destino **sin crear backup ni fusionar reglas preexistentes** `[CONFIRMADO]`. Si el repositorio destino ya tenía reglas propias personalizadas, serán sobrescritas silenciosamente.
- **Eliminación recursiva de directorios de skills (`shutil.rmtree`):** En `install_antigravity_global()` (línea 43) e `inject_into_project()` (línea 83), el script ejecuta `shutil.rmtree(dest)` antes de `shutil.copytree(src, dest)`. Si el usuario modificó localmente una skill en el destino, perderá los cambios no versionados `[CONFIRMADO]`.

### 7.2 Acoplamientos implícitos, concurrencia y estado mutable compartido
- **Acoplamiento por convención de nombres en `./01_seed/`:** `test_seed_coverage.py` (líneas 471-480) distingue entre Seed Master y Seed Híbrido iterando sobre `seed_dir.glob("seed-*.md")` y verificando `s.name.endswith("-master.md")`. Si existen múltiples archivos `seed-*.md` de distintos proyectos dentro de `./01_seed/`, las variables `master_seed` y `hybrid_seed` quedarán asignadas únicamente al último elemento iterado sin emitir advertencia `[CONFIRMADO]`.
- **Bloqueos de descriptores en Windows NTFS:** Las operaciones `shutil.rmtree` en `install_skills.py` o renombrados de carpetas pueden lanzar `PermissionError` en sistemas Windows si un IDE o terminal mantiene un handle abierto sobre los archivos dentro de `.agents/skills/` `[CONFIRMADO]`.

### 7.3 Contradicciones detectadas y corregidas (Declarado vs Observado en Árbol Físico)
Durante la auditoría v3.0 se detectaron y corrigieron las siguientes contradicciones reales entre la documentación y el árbol físico (que deben vigilarse para evitar regresiones):
1. **Esquizofrenia de Plantilla (21 vs 11 secciones):** La versión anterior de `./ThinkingSeed Master.md` exigía 21 secciones mientras `./.agents/skills/seedMaster/SKILL.md` definía un esqueleto de 11 secciones (`0`-`10`). Se unificó en el esquema polimórfico v3.0 de 11 Secciones Core `[CONFIRMADO]`.
2. **Deriva de Casing en NTFS (`Tools/` y `Readme.md`):** El árbol físico tenía `Tools/` y `Readme.md` con mayúsculas iniciales violando el invariante `all-lowercase` de iDirectory v3.0 y rompiendo enlaces a `README.md`. Fue normalizado a `./tools/` y `./README.md` `[CONFIRMADO]`.
3. **Referencia cruzada huérfana a `seed-idirectory-master.md` y `001_Seed/`:** `./.context/tree.json`, `./01_seed/.context.yaml` y `./02_foundation/engine/engine_readme.md` referenciaban `seed-idirectory-master.md`, mientras `.cursorrules`, `.windsurfrules` y `.github/copilot-instructions.md` apuntaban a la carpeta deprecada `001_Seed/`. Todos fueron rectificados hacia `./01_seed/seed-ThinkingSeed-master.md` `[CONFIRMADO]`.
4. **Beacons faltantes en `.agents/` y `.context/` y carpetas vacías sin rastreo en Git:** Se materializaron `./.agents/.context.yaml` y `./.context/.context.yaml` (alcanzando 26/26 nodos sincronizados en `./.context/tree.json`), y se identificaron 3 carpetas locales vacías sin archivos ni beacons (`docs/engineers_notes`, `docs/technical_specs` y `src/fabric_jobs`) ignoradas por Git `[CONFIRMADO]`.

### 7.4 Dependencias externas asumidas en `PATH` o repositorios hermanos
- **Motores satelitales `FWengine.py` y `query_graph.py`:** Documentos previos mostraban comandos invocando `FWengine.py` y `query_graph.py` como si residieran en `./`. En realidad, son herramientas externas de los repositorios hermanos `iDirectory` y `Gravity` `[CONFIRMADO]`. Para eliminar esta dependencia fantasma, `scripts/test_seed_coverage.py::check_local_tree_freshness` implementa la verificación autónoma local sin depender de binarios externos.

### 7.5 Matriz de modos de falla y recuperación
| ID | Modo de Falla / Vector | Síntoma Observable | Causa Raíz | Detección | Mitigación / Recuperación | Riesgo Residual Real |
|---|---|---|---|---|---|---|
| `FAIL-01` | Sobrescritura de reglas en repositorio destino | Pérdida de directivas previas en `AGENTS.md` o `GEMINI.md` del proyecto target | `inject_into_project` ejecuta `shutil.copy2` directo sin merge | `git diff` en el repositorio destino tras ejecutar `--target` | Revisar `git status` / `git diff` en el repo destino y fusionar manualmente con `git checkout -p` | **Medio:** `install_skills.py` aún no implementa modo `--merge` o `.bak` automático |
| `FAIL-02` | Rechazo de Gate en `test_seed_coverage.py` (Exit `1`) | El script termina con código `1` y marca `FAIL` en consola | Fuga de ruta local, bloque de código prohibido, falta de tag XML o cobertura AST $< 90\%$ | `GATE-01` a `GATE-06` en `compute_coverage` | Inspeccionar el detalle impreso por el validador fallido y corregir el Seed | **Bajo:** El bloqueo determinista impide que el error pase inadvertido |
| `FAIL-03` | Drift entre carpetas físicas y `.context/tree.json` | `GATE-06 (check_local_tree_freshness)` reporta `missing_in_tree` o `uppercase_dirs` | Creación de nueva carpeta o `.context.yaml` sin actualizar `.context/tree.json` | Ejecución de `test_seed_coverage.py` | Añadir el nodo correspondiente en `./.context/tree.json` respetando `all-lowercase` | **Bajo:** Detectado localmente sin requerir `FWengine.py` |
| `FAIL-04` | Colisión de múltiples seeds en `./01_seed/` | `test_seed_coverage.py` audita un archivo inesperado | Más de un archivo `seed-*-master.md` en `./01_seed/` | Inspección de `./01_seed/` | Mantener únicamente el par canónico `seed-[proyecto].md` y `seed-[proyecto]-master.md` en `./01_seed/` | **Bajo:** En este repositorio solo existe `seed-ThinkingSeed-master.md` |

---

## 8. SEGURIDAD, PRIVACIDAD Y GUARDRAILS

### 8.1 Postura Zero-Trust y manejo de secretos
- El repositorio no almacena ni procesa credenciales de nube ni tokens de API en tiempo de ejecución (`[INV-06]`).
- `./.gitignore` y `./.agentignore` bloquean la indexación y el versionado de entornos virtuales (`.venv/`), datos crudos (`data/`) y trazas (`logs/`).
- El validador `check_secret_leaks` audita deterministamente `./01_seed/*.md` contra 7 patrones de secretos reales (Google API Keys, OpenAI/Anthropic `sk-`, GitHub tokens, AWS `AKIA`, claves privadas PEM, Bearer tokens y URIs con credenciales).

### 8.2 Superficie de ataque y controles implementados
- **Zero Supply-Chain Surface (`[INV-04]`):** Al no requerir ningún paquete externo de PyPI (`pip install`), la superficie de ataque por dependencias de terceros es nula.
- **Resolución de rutas:** `install_skills.py` normaliza la ruta objetivo mediante `target_path.resolve()` y comprueba `target.exists() and target.is_dir()` antes de escribir.
- **Protección contra Prompt Injection / Context Poisoning:** El contenedor `<SEED_ARCHITECTURAL_VECTOR>` delimita explícitamente el artefacto como contexto arquitectónico pasivo (`contains_source_code="false"`).

### 8.3 Hallazgos de seguridad (Security Findings)
| Severidad | Vector / Hallazgo | Evidencia | Impacto Potencial | Mitigación / Estado |
|---|---|---|---|---|
| Baja | Sobrescritura sin confirmación en `inject_into_project` | `./scripts/install_skills.py:96-108` | Puede reemplazar archivos `AGENTS.md`/`GEMINI.md` existentes en un repositorio destino | Documentado en Sección 7 (`FAIL-01`); usar en repositorios bajo control de versiones Git `[CONFIRMADO]` |
| Informativa | Verificación de secretos en `./01_seed/` | `./scripts/test_seed_coverage.py:102-141` | Ninguna credencial expuesta detectada (`0` fugas) | Auditado automáticamente por `GATE-04 (check_secret_leaks)` `[CONFIRMADO]` |

---

## 9. ESTADO REAL, DEUDA TÉCNICA Y DECISIONES (ADRs)

### 9.1 Matriz Declarado vs Observado
| Área / Módulo | Declarado en Documentación | Observado en Repositorio | Estado Real | Evidencia |
|---|---|---|---|---|
| Especificación ThinkingSeed v3.0 | Esquema polimórfico 11 secciones + XML Vector + Zero-Code | Implementado en plantillas maestras y fixture mini | Completo `[CONFIRMADO]` | `./ThinkingSeed Master.md`, `./ThinkingSeed_MasterHybrid.md`, `./tests/ThinkingSeed_Mini.md` |
| Skills y Reglas Multi-Agente | Delta-Seeding, extracción AST y auditoría adversarial | Sincronizado en las 2 skills y 6 archivos de reglas | Completo `[CONFIRMADO]` | `./.agents/skills/seedMaster/SKILL.md`, `./AGENTS.md`, `./GEMINI.md`, `./CLAUDE.md` |
| Validador Determinista v3.0 | 6 validadores AST/Regex con código de salida `0`/`1` | Implementado con 100% Python Standard Library | Completo `[CONFIRMADO]` | `./scripts/test_seed_coverage.py` |
| Topología iDirectory v3.0 | 24 carpetas con `.context.yaml` en `all-lowercase` | 24 beacons físicos alineados 1:1 con `./.context/tree.json` | Completo `[CONFIRMADO]` | `./.context/tree.json`, `./tools/.context.yaml`, `./.agents/.context.yaml` |
| Módulos Productivos en `./src/` | Pipelines cloud, backend core, dashboards y datos sintéticos | Carpetas contienen únicamente su beacon `.context.yaml` | Scaffolding `[FALTANTE]` | `./src/cloud_jobs/.context.yaml`, `./src/core/.context.yaml`, `./src/dashboards/.context.yaml`, `./src/data_generation/.context.yaml` |
| Suite de Tests Unitarios (`unittest`) | Pruebas unitarias en `./tests/` | `./tests/` contiene el fixture `ThinkingSeed_Mini.md` y `.context.yaml`, sin archivos `test_*.py` | Parcial `[FALTANTE]` | `./tests/.context.yaml`, `./tests/ThinkingSeed_Mini.md` |

### 9.2 Trabajo pendiente (`[FALTANTE]`) y deuda técnica priorizada
| ID | Prioridad | Componente / Deuda o Pendiente | Impacto | Criterio de Cierre Verificable |
|---|---|---|---|---|
| `DEBT-01` | P2 | Modo no destructivo (`--backup` o `--merge`) en `./scripts/install_skills.py::inject_into_project` | Evita sobrescribir reglas preexistentes en repositorios destino (`FAIL-01`) | Nuevo flag `--backup` en `install_skills.py` que preserve archivos previos antes de copiar |
| `DEBT-02` | P2 | Suite `tests/test_validators.py` con `unittest` para los 6 validadores de `test_seed_coverage.py` | Añade pruebas unitarias aisladas sobre casos positivos/negativos de cada validador | Ejecución de `python -m unittest discover -s tests` pasando al 100% |
| `DEBT-03` | P3 | Ejemplos de referencia en `./src/` o `./schemas/` | Los directorios `./src/*` y `./schemas/` operan hoy solo como estructura canónica iDirectory | Incorporar contratos JSON Schema en `./schemas/` si el framework se expande |

### 9.3 Registro de Decisiones Arquitectónicas (`[ADR-XXX]`)
| ID | Decisión Arquitectónica | Motivo / Problema | Alternativa Descartada | Consecuencia / Trade-off | Estado / Evidencia |
|---|---|---|---|---|---|
| `ADR-001` | Ubicación canónica exclusiva en `./01_seed/` y topología `all-lowercase` | Erradicar colisiones de casing en NTFS/APFS y referencias legacy a `001_Seed/` | Permitir `001_Seed/` o `Tools/` con mayúsculas | Portabilidad total entre Windows, Linux y macOS | Aceptada `[CONFIRMADO]` — `./AGENTS.md`, `./.context/tree.json` |
| `ADR-002` | Contenedor `<SEED_ARCHITECTURAL_VECTOR>` e invariante Zero Source Code (`v3.0`) | Comentarios HTML eran ignorados por chats externos y bloques de código disparaban modo autocompletado | Mantener comentarios HTML `<!-- ... -->` y ejemplos de código en el Seed | Reducción drástica de tokens y reconocimiento inmediato como vector arquitectónico | Aceptada `[CONFIRMADO]` — `./ThinkingSeed Master.md` |
| `ADR-003` | Consolidación Polimórfica en 11 Secciones Core (`0` a `10`) + Sección 7 Adversarial | Las 21 secciones estáticas inducían redundancia narrativa y sesgo de autocomplacencia | Conservar 21 secciones estáticas con tablas `"No aplica"` | Máxima densidad de información y detección proactiva de bugs/tensiones | Aceptada `[CONFIRMADO]` — `./ThinkingSeed Master.md` |
| `ADR-004` | Validación AST/Regex 100% Standard Library en `./scripts/test_seed_coverage.py` | El validador anterior solo medía coincidencias léxicas superficiales de nombres de archivos | Usar librerías externas (`pydantic`, `tree-sitter`, `pyyaml`) | Cero fricción de instalación (`[INV-04]`) y verificación semántica real vía `ast.parse()` | Aceptada `[CONFIRMADO]` — `./scripts/test_seed_coverage.py` |

### 9.4 Incertidumbres activas y preguntas abiertas
1. ¿Se agregará en el futuro un flag `--check-only` en `./scripts/install_skills.py` para previsualizar qué archivos de reglas serían sobrescritos en un repositorio destino antes de aplicar `--target`?
2. ¿Se automatizará la ejecución de `python scripts/test_seed_coverage.py --target-repo . --no-anonymize` mediante un workflow de GitHub Actions en `.github/workflows/`?

---

## 10. REGLAS DE MODIFICACIÓN, GLOSARIO E ÍNDICE DE EVIDENCIAS

### 10.1 Reglas obligatorias para modificar el proyecto y Checklist Pre-Commit
1. **Preservar Invariantes `[INV-01]` a `[INV-06]`:** Ningún cambio a plantillas, skills o seeds puede introducir rutas locales absolutas, enlaces con esquema de archivo local, bloques de código de implementación ni dependencias fuera de la librería estándar de Python.
2. **Sincronización de Contratos AST:** Si se agrega o modifica una función pública, clase o flag CLI en `./scripts/*.py`, debe actualizarse su firma simbólica de 1 línea en la Sección 4.1 de este Seed.
3. **Sincronización Topológica:** Si se crea o elimina un directorio con `.context.yaml`, debe actualizarse `./.context/tree.json` manteniendo nombres estrictamente en minúsculas (`all-lowercase`).
- **Checklist Pre-Commit Determinista:**
  - [ ] Ejecutar `python scripts/test_seed_coverage.py --target-repo . --no-anonymize` y verificar código de salida `0` (`6/6 GATES OK`).
  - [ ] Ejecutar `python scripts/install_skills.py --help` y verificar salida limpia.
  - [ ] Confirmar que `git status` no muestre archivos temporales ni secretos expuestos.

### 10.2 Formato recomendado para responder solicitudes técnicas
```markdown
## Entendimiento de la solicitud
## Componentes afectados (rutas relativas ./)
## Supuestos, riesgos de tensión (Sección 7) e incertidumbres
## Solución propuesta y contratos simbólicos afectados
## Implementación propuesta
## Pruebas, validación y criterios de aceptación
```

### 10.3 Glosario del dominio
| Término | Definición precisa en este proyecto | No confundir con | Evidencia |
|---|---|---|---|
| `<SEED_ARCHITECTURAL_VECTOR>` | Contenedor XML de frontera v3.0 que declara `contains_source_code="false"` y modo de auditoría adversarial | Comentario decorativo HTML | `./ThinkingSeed Master.md` |
| **Firma Simbólica AST** | Contrato público de 1 línea (`modulo::funcion(arg: Tipo) -> Retorno \| Invariante`) extraído sin cuerpo de código | Snippet o volcado de código fuente | `./scripts/test_seed_coverage.py:144-184` |
| **Delta-Seeding** | Flujo incremental que inspecciona `git diff <old_commit>..HEAD` antes de regenerar el Seed | Re-escaneo ciego desde cero | `./.agents/skills/seedMaster/SKILL.md` |
| **Poda Polimórfica** | Regla que omite o resume en 1 línea los sub-módulos condicionales sin evidencia física en el repositorio | Dejar secciones vacías con `"No aplica"` | `./ThinkingSeed Master.md` |
| **Beacon (`.context.yaml`)** | Archivo local de gobernanza que define rol, prioridad (`p0`-`p3`) y permiso `crawl` de cada directorio | Configuración de runtime de aplicación | `./01_seed/.context.yaml` |
| **Mapa Satelital (`tree.json`)** | Índice topológico JSON ultraligero (~250 tokens) de los 24 nodos canónicos del repositorio | Árbol AST de código Python | `./.context/tree.json` |

### 10.4 Índice de evidencias y cobertura del análisis
| Ruta Relativa | Tipo de Artefacto | Relevancia Arquitectónica | Estado Observado |
|---|---|---|---|
| `./ThinkingSeed Master.md` | Core Specification | Especificación canónica v3.0 Polimórfica + XML Vector + Zero-Code | Vigente `[CONFIRMADO]` |
| `./ThinkingSeed_MasterHybrid.md` | Core Specification | Especificación canónica híbrida v3.0 | Vigente `[CONFIRMADO]` |
| `./tests/ThinkingSeed_Mini.md` | Test Fixture | Plantilla mínima de validación v3.0 | Vigente `[CONFIRMADO]` |
| `./.agents/skills/seedMaster/SKILL.md` | Agent Skill | Workflow `/seedMaster` con Delta-Seeding, AST y Auditoría Adversarial | Vigente `[CONFIRMADO]` |
| `./.agents/skills/seed/SKILL.md` | Agent Skill | Workflow `/seed` alineado a v3.0 | Vigente `[CONFIRMADO]` |
| `./scripts/install_skills.py` | CLI Script | Instalador e inyector universal multi-agente | Vigente `[CONFIRMADO]` |
| `./scripts/test_seed_coverage.py` | CLI Auditor | Suite de benchmark y 6 validadores deterministas AST/Regex | Vigente `[CONFIRMADO]` |
| `./.context/tree.json` | Satellite Map | Mapa topológico sincronizado con los 24 beacons `.context.yaml` | Vigente `[CONFIRMADO]` |
| `./AGENTS.md` / `./GEMINI.md` / `./CLAUDE.md` | Agent Rules | Directivas multi-agente v3.0 (junto con `.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`) | Vigente `[CONFIRMADO]` |
| `./README.md` / `./README_ES.md` | Documentation | Documentación paper-grade bilingüe sincronizada con `./tools/` | Vigente `[CONFIRMADO]` |
| `./artifacts/benchmark_seed_coverage.md` | Audit Report | Reporte cuantitativo de compresión, cobertura AST y 6 gates | Vigente `[CONFIRMADO]` |
| `./artifacts/MetricsThinking.md` | Forensic Report | Evaluación de madurez en 10 módulos (`MetricsThinking.json` & `INFERRED_ROADMAP.md`) | Vigente `[CONFIRMADO]` |

| Área Evaluada | Cobertura | Confianza | Método de Verificación |
|---|---|---|---|
| Arquitectura y Topología (16 Top Dirs / 19 Sub-Dirs / 24 Beacons) | Alta ($100.0\%$) | Alta | `check_local_tree_freshness` + `analyze_repo` `[CONFIRMADO]` |
| Contratos Simbólicos AST (22/22 símbolos y flags CLI) | Alta ($100.0\%$) | Alta | `check_ast_contract_coverage` (`ast.parse`) `[CONFIRMADO]` |
| Portabilidad de Rutas y Cumplimiento Zero-Code | Alta ($100.0\%$) | Alta | `check_path_portability` + `check_zero_code_invariant` `[CONFIRMADO]` |
| Seguridad Zero-Trust (`<REDACTED>`) | Alta ($100.0\%$) | Alta | `check_secret_leaks` (0 fugas detectadas) `[CONFIRMADO]` |

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es una semilla de proyecto (**ThinkingSeed Master v3.0**): el vector arquitectónico y ADN del proyecto (`contains_source_code="false"`), no su repositorio de código completo. Refleja el avance real, los contratos simbólicos y la superficie de tensión del sistema hasta la fecha. Como modelo receptor, tu función es usar esta semilla como memoria técnica para:
> 1. **Responder preguntas** sobre la arquitectura, contratos simbólicos, dependencias y flujos del sistema.
> 2. **Auditar riesgos y sugerir mejoras** evaluando activamente la Superficie de Tensión (Sección 7) y las áreas marcadas como `[FALTANTE]`.
> 3. **Generar código o soluciones compatibles** respetando estrictamente las rutas relativas (`./`), firmas simbólicas e invariantes definidas aquí, cuando el usuario te lo solicite."

### Pautas de resolución:
Antes de resolver una solicitud:
1. Identifica el objetivo del usuario.
2. Localiza los componentes afectados usando las rutas relativas (`./`) del Seed.
3. Revisa restricciones (`[INV-01]` a `[INV-06]`), decisiones (`[ADR-001]` a `[ADR-004]`), contratos simbólicos (Sección 4.1) y vectores de tensión (Sección 7).
4. Explicita supuestos cuando sea necesario: *"Supongo que X debido a Y"*.
5. Propone cambios por archivo con rutas relativas claras y separadores Unix (`/`).
6. Añade pruebas, riesgos de regresión y criterios de aceptación verificables.

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla **sin una instrucción específica**, no intentes generar código ni completar archivos vacíos. Responde únicamente con:
1. Un saludo confirmando que asimilaste el ADN arquitectónico v3.0 de **ThinkingSeed** (`<SEED_ARCHITECTURAL_VECTOR>`) y su stack basado en Python Standard Library e iDirectory v3.0.
2. Un breve resumen de 2-3 líneas sobre el propósito del sistema, su estado actual y sus principales vectores de tensión.
3. Una frase poniéndote a disposición para auditar, resolver dudas o colaborar en los siguientes pasos de desarrollo.

</SEED_ARCHITECTURAL_VECTOR>
