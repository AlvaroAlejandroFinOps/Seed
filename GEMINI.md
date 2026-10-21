# GLOBAL WORKSPACE RULES: ThinkingSeed Standard (v3.0)

> **Ámbito:** Este archivo aplica a todo el workspace y establece las reglas obligatorias para la generación, validación y consumo de vectores arquitectónicos (ThinkingSeeds), gobernanza topológica y análisis de código.

---

## 1. ESTÁNDAR THINKINGSEED v3.0 & CONTRATO `<SEED_ARCHITECTURAL_VECTOR>`
- Un **ThinkingSeed** es el **vector arquitectónico, mapa de contratos simbólicos y memoria técnica** de un proyecto (`contains_source_code="false"`), **NO su repositorio de código fuente completo**.
- Todo seed generado debe abrir y cerrar obligatoriamente con el contenedor XML `<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">` ... `</SEED_ARCHITECTURAL_VECTOR>`, incluir la sección `0.1 Instrucciones para el modelo receptor` al inicio y cerrar con el bloque `## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA`.
- Los archivos seed generados deben almacenarse siempre dentro de la subcarpeta `./01_seed/` del directorio del proyecto.

---

## 2. INVARIANTES DE GENERACIÓN v3.0 (CUMPLIMIENTO ESTRICTO)
1. **Zero Source Code (Symbolic Contracts Only):** Prohibido inyectar bloques de código fuente de implementación (`.py`, `.ps1`, `.sh`, `.rs`, `.go`, `.sql`, `.json`, `.yaml` mayores a 5 líneas) dentro del Seed. Todo script, clase, función pública o flag CLI se documenta exclusivamente mediante **Firmas Simbólicas AST de 1 línea**: `ruta/modulo.py::funcion(arg: Tipo) -> Retorno | Invariante / Efecto`.
2. **Zero Local Absolute Paths & Zero File-Scheme URIs:** Queda estrictamente prohibido incluir rutas absolutas del disco local (unidades `C` o `D`, `/Users/`, `/home/`) o enlaces con esquema `file` local en cualquier archivo generado o regla del proyecto. En los metadatos del Seed, `repository_root` debe ser siempre `"./"`.
3. **Estructura Polimórfica Consolidada (11 Secciones Core `0` a `10`):** El Seed Master se organiza en las 11 Secciones Core (`0` a `10`) con poda polimórfica de sub-módulos condicionales y regla **DRY Intra-Seed** (cero repetición narrativa de archivos o hechos).
4. **Auditoría Adversarial en Sección 7 (Superficie de Tensión):** Prohibido caer en sesgo de autocomplacencia (`"100% mitigado / riesgo nulo"`). El agente debe cruzar las reglas documentadas contra el árbol físico real para reportar fronteras de confianza, acoplamientos mutables, contradicciones, violaciones de casing (`all-lowercase`) y dependencias externas asumidas en `PATH`.

---

## 3. WORKFLOWS Y SKILLS DE GENERACIÓN
Existen dos niveles de profundidad para la generación de seeds:

1. **`/seed` (Estándar Híbrido v3.0 - Uso Frecuente):**
   - Basado en `./ThinkingSeed_MasterHybrid.md` y `./.agents/skills/seed/SKILL.md`.
   - Genera: `./01_seed/seed-[nombre-proyecto].md`.
   - Ágil, condensado y enfocado en transferir el ADN arquitectónico y firmas simbólicas de forma eficiente a chats de IA comercial.

2. **`/seedMaster` (Estándar Exhaustivo v3.0 - Uso Ocasional):**
   - Basado en `./ThinkingSeed Master.md` y `./.agents/skills/seedMaster/SKILL.md`.
   - Genera: `./01_seed/seed-[nombre-proyecto]-master.md`.
   - Incluye Delta-Seeding incremental (`git diff`), extracción AST de contratos simbólicos, auditoría adversarial de superficie de tensión y validación determinista con `./scripts/test_seed_coverage.py`.

---

## 4. RIGOR EPISTEMOLÓGICO Y EVIDENCIA
Toda afirmación técnica dentro de los seeds o reportes generados debe etiquetarse explícitamente:
- `[CONFIRMADO]`: Datos, dependencias, configuraciones o contratos observados directamente en la inspección del proyecto.
- `[INFERIDO]`: Deducciones lógicas razonables basadas en la arquitectura, pero no declaradas de forma explícita.
- `[DECLARADO]`: Afirmaciones presentes en documentación pero no contrastadas o divergentes de la implementación física.
- `[FALTANTE]`: Componentes, configuraciones o implementaciones esperables pero ausentes en el proyecto (refleja el avance real en curso).

---

## 5. POLÍTICA RIGUROSA DE SEGURIDAD (ZERO-TRUST)
- **PROHIBICIÓN ABSOLUTA:** Queda estrictamente prohibido incluir o reproducir llaves de API, credenciales, contraseñas, tokens JWT, certificados privados o cadenas de conexión con credenciales explícitas en cualquier archivo generado.
- **Redacción de Datos Sensibles:** Todo valor sensible debe ser reemplazado invariablemente por la etiqueta `<REDACTED>`. Si se detectan secretos commiteados en código o configuraciones, registrar el hallazgo como alerta en la Sección 8 sin exponer el valor.
