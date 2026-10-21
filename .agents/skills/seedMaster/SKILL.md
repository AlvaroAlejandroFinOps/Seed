---
name: seedMaster
description: >-
  Crea un vector arquitectónico exhaustivo y profundo (ADN completo v3.0) de un proyecto en formato seed-[nombre-proyecto]-master.md
  siguiendo el estándar ThinkingSeed Master.md (v3.0) y alojándolo en la carpeta 01_seed del directorio actual.
  Usar cuando el usuario ponga /seedMaster o solicite crear el seed exhaustivo/profundo del proyecto.
---

# Workflow: Generación de ThinkingSeed Master Exhaustivo v3.0 (`/seedMaster`)

Este workflow inspecciona a profundidad el proyecto actual y genera un vector arquitectónico determinista, libre de código fuente y libre de rutas locales absolutas denominado `./01_seed/seed-[nombre-proyecto]-master.md` bajo la especificación `./ThinkingSeed Master.md` (v3.0).

> **Nota de Frecuencia:** Esta skill se utiliza para auditorías exhaustivas, migraciones o transferencias completas de arquitectura y superficie de tensión. Para snapshots ágiles cotidianos, utilizar `/seed`.

---

## Pasos de Ejecución Obligatorios

### Paso 1: Determinación del Proyecto y Delta-Seeding Incremental
1. Identificar el nombre del proyecto actual y asegurar que existe la carpeta `./01_seed/`.
2. **Flujo de Delta-Seeding Incremental:**
   - Antes de escanear el repositorio completo, verificar si ya existe `./01_seed/seed-[proyecto]-master.md`.
   - Si existe, leer el campo `git_commit` de la Sección `0` y ejecutar `git diff --name-status <old_commit>..HEAD` para identificar exactamente qué archivos mutaron, fueron añadidos o eliminados.
   - Combinar este diferencial con la lectura del mapa satelital `./.context/tree.json` y los beacons `.context.yaml` para dirigir la inspección hacia los nodos prioritarios (`p0`-`p2`) y los módulos modificados.

### Paso 2: Extracción Simbólica AST Sin Código (Invariante Zero Source Code)
El agente actúa como **Lead Systems Architect y Principal Context Engineer**:
1. **Prohibición de Código Fuente:** Queda estrictamente prohibido copiar cuerpos de funciones, scripts shell (`.ps1`, `.sh`, `.bash`), archivos `.py`, `.rs`, `.go`, `.sql` o volcados `.json`/`.yaml` mayores a 5 líneas.
2. **Extracción Simbólica AST de 1 Línea:**
   - Inspeccionar los módulos de código y extraer todas las funciones públicas, clases, dataclasses y parámetros CLI (`argparse`, `typer`, `click`) como firmas simbólicas tipadas de 1 sola línea para la Sección 4.1:
     `ruta/modulo.py::funcion(arg: Tipo) -> Retorno | Invariante / Efecto / Excepciones`.
3. **Invariante Zero Local Paths & Zero File-Scheme URIs:**
   - Configurar siempre `repository_root: "./"` en el bloque YAML de la Sección `0`.
   - Prohibido incluir rutas locales absolutas (letras de unidad, `/Users/`, `/home/`) o enlaces con esquema `file` local en cualquier parte del documento. Utilizar exclusivamente rutas relativas limpias (`./ruta/archivo`).

### Paso 3: Auditoría Adversarial Pre-Emisión (Sección 7) y Reglas Epistemológicas
1. **Cruce Adversarial de Reglas vs Árbol Físico:**
   - Contrastar lo declarado en `./AGENTS.md`, `./GEMINI.md`, `./CLAUDE.md` y `./README.md` contra el árbol físico real buscando violaciones: directorios con mayúsculas en entornos `all-lowercase`, scripts huérfanos, comandos que invocan binarios externos inexistentes en el repositorio (ej. `FWengine.py`, `query_graph.py`), riesgos de sobrescritura de archivos o condiciones de carrera.
   - Documentar obligatoriamente estos vectores reales en la **Sección 7 (Superficie de Tensión, Contradicciones y Modos de Falla)**, evitando el sesgo de autocomplacencia (`"100% mitigado / riesgo nulo"`).
2. **Etiquetas de Evidencia y Sanitización Zero-Trust:**
   - Clasificar cada afirmación técnica con `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]` o `[FALTANTE]`.
   - Reemplazar cualquier secreto, token, API key o credencial por `<REDACTED>`.

### Paso 4: Renderizado Polimórfico en las 11 Secciones Core (`0` a `10`)
Generar `./01_seed/seed-[nombre-proyecto]-master.md` aplicando la regla **DRY Intra-Seed** (definir cada archivo/invariante una sola vez y referenciar por `[ADR-XXX]` o `[INV-XX]`) y **Poda Polimórfica** (omitir sub-módulos condicionales sin evidencia física en vez de llenar tablas con `"No aplica"`):

```markdown
<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# THINKING SEED MASTER: [Nombre del Proyecto]

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **Naturaleza del Artefacto:** Este documento es un **Vector Arquitectónico y Memoria Técnica (ThinkingSeed Master v3.0)** con `contains_source_code="false"`. **NO es el repositorio de código fuente completo** ni un volcado truncado. La ausencia de bloques de código de implementación es una **invariante deliberada de ingeniería** para maximizar la densidad semántica y preservar más del 99% de tu ventana de contexto.
> 2. **Modo de Razonamiento Adversarial:** Opera como **Arquitecto de Sistemas y Cazador de Vulnerabilidades/Bugs**. Utiliza las firmas simbólicas (Sección 4) y la superficie de tensión (Sección 7) para detectar condiciones de carrera, acoplamientos frágiles y casos borde antes de proponer cambios.
> 3. **Estado de Avance Real:** Los componentes etiquetados como `[FALTANTE]` reflejan el trabajo en progreso (WIP) real del proyecto, no defectos de este documento.

## Seed Changelog
- `[YYYY-MM-DD]`: `[Resumen de cambios verificados respecto al commit anterior]`

---

## 0. IDENTIDAD, METADATOS Y CONTRATO DEL RECEPTOR
```yaml
seed_schema_version: "3.0"
project_name: "[nombre]"
repository_name: "[nombre]"
project_type: "[tipo]"
repository_mode: "[modo]"
generated_at: "[ISO-8601]"
generated_by: "[agente/modelo]"
repository_root: "./"
git_branch: "[rama]"
git_commit: "[commit]"
working_tree_state: "[clean|dirty]"
analysis_mode: "static+git+validated"
coverage_level: "high"
known_analysis_limits:
  - "[límite verificado]"
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN del proyecto (`contains_source_code="false"`), no como el repositorio completo ni como una prueba de ejecución.
2. **Contexto Pasivo y Quirúrgico:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como Ground Truth para responder preguntas sobre el sistema.
3. **Estado de Avance:** Considera que los componentes marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Rigor Epistemológico:** Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]` y `[FALTANTE]`.
5. **Portabilidad de Rutas:** Cita siempre rutas relativas a la raíz del repositorio (`./ruta/archivo`) con `/`. Prohibido emitir rutas locales absolutas o enlaces con esquema `file` local.
6. **Contratos Simbólicos:** Conserva arquitectura, firmas simbólicas (Sección 4) e invariantes (`[INV-XX]`).
7. **Postura Adversarial Constructiva:** Revisa siempre la Sección 7 (Superficie de Tensión) antes de proponer cambios.
8. **Seguridad Zero-Trust:** No reveles ni solicites secretos. Usa placeholders (`<REDACTED>`).

---

## 1. RESUMEN EJECUTIVO Y ALCANCE
## 2. ARQUITECTURA, TOPOLOGÍA Y FRONTERAS MODULARES
## 3. FLUJOS DE EJECUCIÓN, ENTRY POINTS Y CICLO DE VIDA
## 4. CONTRATOS SIMBÓLICOS, MODELO DE DATOS Y PERSISTENCIA
## 5. CONFIGURACIÓN, ENTORNOS Y DEPENDENCIAS
## 6. PRUEBAS, CI/CD, DESPLIEGUE Y OPERACIÓN
## 7. SUPERFICIE DE TENSIÓN, CONTRADICCIONES Y MODOS DE FALLA
## 8. SEGURIDAD, PRIVACIDAD Y GUARDRAILS
## 9. ESTADO REAL, DEUDA TÉCNICA Y DECISIONES (ADRs)
## 10. REGLAS DE MODIFICACIÓN, GLOSARIO E ÍNDICE DE EVIDENCIAS

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es una semilla de proyecto (**ThinkingSeed Master v3.0**): el vector arquitectónico y ADN del proyecto (`contains_source_code="false"`), no su repositorio completo. Refleja el avance real, los contratos simbólicos y la superficie de tensión del sistema hasta la fecha. Como modelo receptor, tu función es usar esta semilla como memoria técnica para:
> 1. **Responder preguntas** sobre la arquitectura, contratos simbólicos, dependencias y flujos del sistema.
> 2. **Auditar riesgos y sugerir mejoras** evaluando activamente la Superficie de Tensión (Sección 7) y las áreas marcadas como `[FALTANTE]`.
> 3. **Generar código o soluciones compatibles** respetando las rutas relativas (`./`), firmas simbólicas e invariantes definidas aquí, cuando el usuario te lo solicite."

### Pautas de resolución:
Antes de resolver una solicitud:
1. Identifica el objetivo del usuario.
2. Localiza los componentes afectados usando las rutas relativas (`./`) del Seed.
3. Revisa restricciones (`[INV-XX]`), contratos simbólicos (Sección 4) y vectores de tensión (Sección 7).
4. Explicita supuestos cuando sea necesario: "Supongo que X debido a Y".
5. Propone cambios por archivo con rutas relativas claras y separadores Unix (`/`).
6. Añade pruebas, riesgos y criterios de aceptación.

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla **sin una instrucción específica**, no intentes generar código ni completar archivos vacíos. Responde únicamente con:
1. Un saludo confirmando que asimilaste el ADN arquitectónico v3.0 de **[Nombre del Proyecto]** (`<SEED_ARCHITECTURAL_VECTOR>`) y su stack principal.
2. Un breve resumen de 2-3 líneas sobre el objetivo, su estado actual y sus principales vectores de tensión.
3. Una frase poniéndote a disposición para resolver dudas sobre su funcionamiento o colaborar en los siguientes pasos de desarrollo.

</SEED_ARCHITECTURAL_VECTOR>
```

### Paso 5: Checklist de Auto-Validación Final (Gate de Salida)
Antes de dar por finalizada la generación en `./01_seed/seed-[nombre-proyecto]-master.md`, verificar obligatoriamente:
1. **Contrato XML y Handoff:** Presencia de `<SEED_ARCHITECTURAL_VECTOR`, sección `0.1 Instrucciones para el modelo receptor`, bloque `CONTEXT HANDOFF` y cierre `</SEED_ARCHITECTURAL_VECTOR>`.
2. **Portabilidad Estricta:** 0 coincidencias de URIs con esquema `file` local y 0 rutas absolutas locales en el archivo generado; `repository_root` es `"./"`.
3. **Invariante Zero-Code:** 0 bloques de código fuente de implementación (`.py`, `.ps1`, `.sh`, `.json`, `.yaml` literales > 5 líneas); todos los módulos públicos están documentados con firmas simbólicas AST de 1 línea en la Sección 4.
4. **Ejecución de Validador (si existe en el repo):** Ejecutar `python scripts/test_seed_coverage.py --target-repo . --no-anonymize` y verificar que retorne código de salida `0`.
5. Confirmar al usuario la generación exitosa citando la ruta `./01_seed/seed-[nombre-proyecto]-master.md`.
