#!/usr/bin/env python3
"""
ThinkingSeed Universal Skill Installer
=======================================
Instala las skills `/seed` y `/seedMaster` en cualquier entorno de agentes:
- Antigravity / Gemini CLI (Global o Local)
- Claude Code (Global o Local con CLAUDE.md)
- Cursor IDE (.cursorrules)
- Windsurf IDE (.windsurfrules)
- GitHub Copilot (.github/copilot-instructions.md)
- Estándar Agnóstico AGENTS.md

Uso:
    python scripts/install_skills.py                   # Modo interactivo
    python scripts/install_skills.py --global-install  # Instala globalmente para Antigravity y Claude
    python scripts/install_skills.py --target ./ruta   # Inyecta en un proyecto destino
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_SRC_DIR = BASE_DIR / ".agents" / "skills"

TEMPLATE_HYBRID = BASE_DIR / "ThinkingSeed_MasterHybrid.md"
TEMPLATE_MASTER = BASE_DIR / "ThinkingSeed Master.md"


def upsert_segmented_rule_file(src_path: Path, dest_path: Path, tool_key: str = "THINKINGSEED", backup: bool = False) -> bool:
    """
    Inserta o actualiza de forma no destructiva el bloque de reglas de ThinkingSeed v5.0
    en el archivo destino sin sobrescribir reglas preexistentes de iDirectory, MetricsThinking o iReadme.
    """
    content = src_path.read_text(encoding="utf-8", errors="replace").strip()
    start_marker = f"<!-- >>> ICONTEXT-V5:{tool_key}:START >>> -->"
    end_marker = f"<!-- <<< ICONTEXT-V5:{tool_key}:END >>> -->"
    wrapped = f"{start_marker}\n{content}\n{end_marker}"

    if not dest_path.exists():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(wrapped + "\n", encoding="utf-8")
        return True

    if backup:
        bak_path = dest_path.with_suffix(dest_path.suffix + ".bak")
        shutil.copy2(dest_path, bak_path)

    existing = dest_path.read_text(encoding="utf-8", errors="replace")
    if start_marker in existing and end_marker in existing:
        pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
        updated = pattern.sub(lambda _m: wrapped, existing)
    elif existing.strip() and existing.strip() != content:
        updated = existing.rstrip() + "\n\n" + wrapped + "\n"
    else:
        updated = wrapped + "\n"

    dest_path.write_text(updated, encoding="utf-8")
    return True

def get_home_dir() -> Path:
    return Path.home()

def install_antigravity_global() -> bool:
    gemini_skills_dir = get_home_dir() / ".gemini" / "config" / "skills"
    try:
        gemini_skills_dir.mkdir(parents=True, exist_ok=True)
        for skill_name in ["seed", "seedMaster"]:
            src = SKILLS_SRC_DIR / skill_name
            dest = gemini_skills_dir / skill_name
            if src.exists():
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(src, dest)
                print(f"  [OK] Antigravity/Gemini Global: Instalado '{skill_name}' en {dest}")
            else:
                print(f"  [ALERTA] No se encontro la carpeta origen de skill: {src}")
        return True
    except Exception as e:
        print(f"  [ERROR] Al instalar en Antigravity Global: {e}")
        return False

def install_claude_code_global() -> bool:
    claude_dir = get_home_dir() / ".claude"
    try:
        claude_dir.mkdir(parents=True, exist_ok=True)
        # Copiar CLAUDE.md global o en el home de claude
        claude_md_src = BASE_DIR / "CLAUDE.md"
        if claude_md_src.exists():
            shutil.copy2(claude_md_src, claude_dir / "CLAUDE.md")
            print(f"  [OK] Claude Code Global: Copiado CLAUDE.md en {claude_dir / 'CLAUDE.md'}")
        return True
    except Exception as e:
        print(f"  [ERROR] Al configurar Claude Code Global: {e}")
        return False

def install_codex_global() -> bool:
    codex_dir = get_home_dir() / ".codex"
    try:
        codex_dir.mkdir(parents=True, exist_ok=True)
        codex_md_src = BASE_DIR / "CODEX.md"
        if codex_md_src.exists():
            shutil.copy2(codex_md_src, codex_dir / "CODEX.md")
            print(f"  [OK] Codex Global: Copiado CODEX.md en {codex_dir / 'CODEX.md'}")
        codex_rules_src = BASE_DIR / ".codexrules"
        if codex_rules_src.exists():
            shutil.copy2(codex_rules_src, codex_dir / ".codexrules")
            print(f"  [OK] Codex Global: Copiado .codexrules en {codex_dir / '.codexrules'}")
        return True
    except Exception as e:
        print(f"  [ERROR] Al configurar Codex Global: {e}")
        return False

def inject_into_project(target_path: Path, backup: bool = False, check_only: bool = False) -> bool:
    target = target_path.resolve()
    if not target.exists() or not target.is_dir():
        print(f"  [ERROR] La ruta destino no existe o no es un directorio: {target}")
        return False

    print(f"\n{'[CHECK-ONLY] Previsualizando' if check_only else 'Inyectando'} soporte ThinkingSeed v5.0 en proyecto: {target}")

    # 1. Copiar .agents/skills/
    target_agents_skills = target / ".agents" / "skills"
    if not check_only:
        target_agents_skills.mkdir(parents=True, exist_ok=True)
    for skill_name in ["seed", "seedMaster"]:
        src = SKILLS_SRC_DIR / skill_name
        dest = target_agents_skills / skill_name
        if src.exists():
            if check_only:
                print(f"  [PREVIEW] Skill a sincronizar: {dest}")
            else:
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(src, dest)
                print(f"  [OK] Skill instalada: {dest}")

    # 2. Componer de forma no destructiva archivos de reglas multi-agente (v5.0)
    agent_rule_files = [
        "GEMINI.md",
        "CLAUDE.md",
        "CODEX.md",
        ".codexrules",
        ".cursorrules",
        ".windsurfrules",
        "AGENTS.md"
    ]

    for fname in agent_rule_files:
        src = BASE_DIR / fname
        if src.exists():
            dest_f = target / fname
            if check_only:
                state = "EXISTE (se fusionará por bloque v5.0)" if dest_f.exists() else "NUEVO"
                print(f"  [PREVIEW] Regla {dest_f}: {state}")
            else:
                upsert_segmented_rule_file(src, dest_f, tool_key="THINKINGSEED", backup=backup)
                print(f"  [OK] Regla sincronizada (no destructiva v5.0): {dest_f}")

    # 3. Copiar copilot instructions si existe .github
    copilot_src = BASE_DIR / ".github" / "copilot-instructions.md"
    if copilot_src.exists():
        target_github = target / ".github"
        dest_cop = target_github / "copilot-instructions.md"
        if check_only:
            print(f"  [PREVIEW] GitHub Copilot: {dest_cop}")
        else:
            target_github.mkdir(parents=True, exist_ok=True)
            upsert_segmented_rule_file(copilot_src, dest_cop, tool_key="THINKINGSEED", backup=backup)
            print(f"  [OK] GitHub Copilot configurado: {dest_cop}")

    # 4. Asegurar carpeta 01_seed
    if not check_only:
        (target / "01_seed").mkdir(parents=True, exist_ok=True)
        print(f"  [OK] Directorio 01_seed/ preparado.")

    print(f"\n¡Exito! El proyecto {target.name} ahora soporta /seed y /seedMaster v5.0 en cualquier agente.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Instalador Universal de ThinkingSeed Skills v5.0")
    parser.add_argument("--global-install", action="store_true", help="Instala las skills globalmente en el sistema")
    parser.add_argument("--target", type=str, help="Ruta de un proyecto destino donde inyectar las skills y reglas")
    parser.add_argument("--backup", action="store_true", help="Crea copia de respaldo (.bak) antes de actualizar archivos de reglas")
    parser.add_argument("--check-only", action="store_true", help="Previsualiza los cambios en el repositorio destino sin escribir en disco")

    args = parser.parse_args()

    print("=" * 70)
    print("  Gravity HyperScale Thinking - ThinkingSeed v5.0 Multi-Agent Installer")
    print("=" * 70)

    if args.global_install:
        print("\nInstalando skills en el entorno global del usuario...")
        install_antigravity_global()
        install_claude_code_global()
        install_codex_global()
        print("\n[OK] Instalacion global completada con exito.")
        return

    if args.target:
        inject_into_project(Path(args.target), backup=args.backup, check_only=args.check_only)
        return

    # Modo interactivo
    print("\nSelecciona una opcion:")
    print("1) Instalacion Global (Antigravity / Gemini CLI + Claude Code + Codex)")
    print("2) Inyectar en un proyecto especifico (Claude, Cursor, Windsurf, Copilot, Gemini, Codex)")
    print("3) Salir")

    try:
        choice = input("\nOpcion [1/2/3]: ").strip()
    except EOFError:
        choice = "1"

    if choice == "1":
        install_antigravity_global()
        install_claude_code_global()
        install_codex_global()
        print("\n[OK] Instalacion global completada con exito.")
    elif choice == "2":
        path_input = input("Introduce la ruta absoluta o relativa del proyecto: ").strip()
        if path_input:
            inject_into_project(Path(path_input))
        else:
            print("Ruta invalida.")
    else:
        print("Operacion cancelada.")

if __name__ == "__main__":
    main()
