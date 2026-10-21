<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# MASTER HYBRID SEED: [Nombre del Proyecto] (v3.0)

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **¿Qué es este archivo?:** Este documento es un **Vector Arquitectónico Híbrido (ThinkingSeed v3.0)** con `contains_source_code="false"`. Representa el **ADN arquitectónico, contratos simbólicos y memoria técnica** del sistema. **NO es el repositorio completo de código fuente**, sino su mapa genético de alta densidad extraído del entorno de desarrollo.
> 2. **Estado de Avance (Work in Progress):** Refleja el estado real del desarrollo. La ausencia de bloques de código fuente es una **invariante deliberada de diseño (Zero Source Code)** para optimizar la ventana de contexto. Los componentes etiquetados como `[FALTANTE]` reflejan áreas en desarrollo (WIP).
> 3. **Modo de Operación:** Trata este documento como **Ground Truth arquitectónico** y analiza críticamente sus contratos y vectores de tensión antes de proponer cambios.

---

## 0. IDENTIDAD, METADATOS Y REGLAS DE GENERACIÓN (v3.0)

```yaml
seed_schema_version: "3.0"
project_name: "<nombre>"
repository_root: "./"
git_branch: "<rama o unknown>"
git_commit: "<hash corto o unknown>"
generated_at: "<ISO-8601>"
```

### 0.1 Instrucciones para el modelo receptor y reglas de evidencia
1. **ADN vs Repositorio:** Reconoce este documento como memoria técnica (`contains_source_code="false"`), no como un repositorio truncado.
2. **Etiquetas Epistemológicas:** Respeta `[CONFIRMADO]` (observado en código/config), `[INFERIDO]` (deducción lógica), `[DECLARADO]` (en docs) y `[FALTANTE]` (esperado pero ausente).
3. **Invariante Zero Source Code:** Prohibido volcar bloques de código de implementación (>5 líneas); documenta módulos mediante firmas simbólicas de 1 línea (`ruta::simbolo(args) -> Retorno | Invariante`).
4. **Invariante Zero Local Paths:** Prohibido incluir rutas absolutas locales (unidades `C` o `D`, `/Users/`, `/home/`) o enlaces con esquema `file` local. Usa siempre rutas relativas a `"./"`.
5. **Seguridad Zero-Trust:** **PROHIBIDO** reproducir secretos, passwords, tokens o connection strings. Sustituye siempre por `<REDACTED>`.

---

## 1. CORE MANIFESTO & ALCANCE
- **1.1 Objetivo Principal y Problema que Resuelve** (`[CONFIRMADO]`)
- **1.2 Patrón Arquitectónico y Límites del Sistema (In-Scope / Out-of-Scope)**
- **1.3 Stack Principal** (Versiones y fuente de verificación)

## 2. REPOSITORY TOPOLOGY (`all-lowercase` invariant)
- **2.1 Árbol anotado completo** (bloque `text` omitiendo ruido: `.git`, `node_modules`, `__pycache__`, `.venv`)
- **2.2 Diferenciaciones clave entre carpetas ambiguas y archivos críticos**

## 3. EXECUTION FLOW & ENTRY POINTS
- **3.1 Flujo E2E** (Diagrama `mermaid` compacto)
- **3.2 Entry Points** (Qué comandos o triggers inician qué procesos usando rutas relativas `./`)
- **3.3 Ciclo de vida de datos y persistencia**

## 4. SYMBOLIC CONTRACTS & CURRENT STATE
- **4.1 Contratos Simbólicos AST (1 línea por función/clase/flag CLI):**
  `Ruta | Símbolo Público / CLI Flag | Firma Tipada (1 línea) | Invariante / Efecto`
- **4.2 Estado de madurez y trabajo pendiente (`[FALTANTE]`)**
- **4.3 Reglas de código y convenciones de directorios**

## 5. ECOSYSTEM CONTEXT & DEPENDENCIES
- Proyectos hermanos, dependencias internas/externas y resolución explícita de motores externos (con su fallback local).

## 6. CONFIGURATION REFERENCE
- Tabla: `Variable | Tipo | Requerida | Default Seguro | Efecto | Sensible (Sí/No)`

## 7. SUPERFICIE DE TENSIÓN, SEGURIDAD Y FAILURE MODES (AUDITORÍA ADVERSARIAL)
- **7.1 Superficie de Tensión y Contradicciones:** Fronteras de confianza, estado mutable compartido, contradicciones Declarado vs Observado y dependencias asumidas en `PATH`.
- **7.2 Security Findings:** Análisis estático de vulnerabilidades y sanitización `<REDACTED>`.
- **7.3 Failure Modes:** Tabla de fallas, detección, recuperación y riesgo residual real.

## 8. SUB-MÓDULOS CONDICIONALES (Poda Polimórfica: Incluir solo si aplica)
- Data Contracts / Schemas, ADRs (`[ADR-XXX]`), Testing & Quality Gates.

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Orientación para el modelo de IA receptor:**
> "Este documento es una semilla técnica (**ThinkingSeed Hybrid v3.0**): el ADN del proyecto (`contains_source_code="false"`) y no su repositorio completo. Refleja la arquitectura, contratos simbólicos y el avance real hasta la fecha. Como modelo receptor, utiliza esta semilla como memoria de trabajo para:
> 1. **Responder preguntas** sobre la arquitectura, funcionamiento, dependencias y flujos del sistema.
> 2. **Auditar riesgos y sugerir mejoras** basadas en la superficie de tensión (Sección 7) y áreas pendientes (`[FALTANTE]`).
> 3. **Generar código o soluciones compatibles** respetando las rutas relativas (`./`), contratos simbólicos y patrones definidos aquí, cuando el usuario te lo solicite."

### Directrices de interacción para la IA receptora:
1. **Entender:** Identificar el objetivo y los componentes afectados antes de proponer código.
2. **Validar:** Si falta información crítica, preguntar puntualmente en vez de alucinar.
3. **Citar Rutas Relativas:** Usar siempre las rutas relativas (`./...`) declaradas en la topología al sugerir modificaciones.
4. **Respetar:** Mantener el stack, firmas simbólicas y restricciones de seguridad (`<REDACTED>`).
5. **Acuse de Recibo Inicial:** Si el usuario adjuntó esta semilla sin una pregunta concreta, responde en máximo 3 líneas resumiendo el nombre del proyecto, stack y objetivo, confirmando que has asimilado el ADN v3.0 del proyecto y quedando a la espera de sus consultas o tareas.

</SEED_ARCHITECTURAL_VECTOR>
