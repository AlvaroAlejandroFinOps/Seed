<SEED_ARCHITECTURAL_VECTOR version="3.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# SEED CONTEXT MINI FIXTURE: [Nombre del Proyecto] (v3.0)

## 0. IDENTIDAD, METADATOS Y CONTRATO DEL RECEPTOR
```yaml
seed_schema_version: "3.0"
project_name: "[Nombre del Proyecto]"
repository_root: "./"
git_branch: "master"
git_commit: "unknown"
```

### 0.1 Instrucciones para el modelo receptor
1. Reconoce este artefacto como un vector arquitectónico (`contains_source_code="false"`), no como un repositorio de código fuente incompleto.
2. Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]` y `[FALTANTE]`.
3. Prohibido emitir rutas absolutas locales o URIs con esquema `file` local; usa exclusivamente rutas relativas a `"./"`.
4. Prohibido inyectar bloques de código fuente de implementación; conserva las firmas simbólicas de 1 línea.
5. Sanitiza cualquier credencial con `<REDACTED>`.

## 1. CORE MANIFESTO & ALCANCE
   - 1.1 Objetivo Principal y Problema que Resuelve (`[CONFIRMADO]`)
   - 1.2 Patrón Arquitectónico y Stack Principal
## 2. REPOSITORY TOPOLOGY (`all-lowercase`)
   - 2.1 Árbol anotado con responsabilidades por carpeta
   - 2.2 Diferenciaciones clave entre carpetas ambiguas
## 3. EXECUTION FLOW & ENTRY POINTS
   - 3.1 Flujo E2E (Diagrama Mermaid)
   - 3.2 Entry Points y ciclo de vida de artefactos
## 4. SYMBOLIC CONTRACTS & STATE
   - 4.1 Firmas Simbólicas AST (1 línea: `modulo::funcion(arg: Tipo) -> Retorno | Invariante`)
   - 4.2 Estado actual, trabajo pendiente (`[FALTANTE]`) y reglas de código
## 5. CONFIGURATION & DEPENDENCIES
   - 5.1 Variables de configuración (con `<REDACTED>` para sensibles)
   - 5.2 Dependencias internas/externas y fallbacks locales
## 6. TESTING & QUALITY GATES
   - 6.1 Estrategia de validación y gates deterministas
## 7. SUPERFICIE DE TENSIÓN, SEGURIDAD Y FAILURE MODES
   - 7.1 Fronteras de confianza, contradicciones Declarado vs Observado y acoplamientos
   - 7.2 Modos de falla, recuperación y riesgo residual real
## 8. GLOSARIO, ADRs & EVIDENCIAS
   - 8.1 Decisiones (`[ADR-XXX]`), Glosario e Índice de Evidencias

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA
> Este documento es una semilla técnica (**ThinkingSeed Mini v3.0**) con `contains_source_code="false"`. Úsala como memoria técnica pasiva y contrato arquitectónico, citando siempre rutas relativas (`./`) y esperando instrucciones del usuario antes de generar código.

</SEED_ARCHITECTURAL_VECTOR>
