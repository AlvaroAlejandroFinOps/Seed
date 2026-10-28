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
import sys
import shutil
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_SRC_DIR = BASE_DIR / ".agents" / "skills"

TEMPLATE_HYBRID = BASE_DIR / "ThinkingSeed_MasterHybrid.md"
TEMPLATE_MASTER = BASE_DIR / "ThinkingSeed Master.md"

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

def inject_into_project(target_path: Path) -> bool:
    target = target_path.resolve()
    if not target.exists() or not target.is_dir():
        print(f"  [ERROR] La ruta destino no existe o no es un directorio: {target}")
        return False

    print(f"\nInyectando soporte ThinkingSeed en proyecto: {target}")

    # 1. Copiar .agents/skills/
    target_agents_skills = target / ".agents" / "skills"
    target_agents_skills.mkdir(parents=True, exist_ok=True)
    for skill_name in ["seed", "seedMaster"]:
        src = SKILLS_SRC_DIR / skill_name
        dest = target_agents_skills / skill_name
        if src.exists():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            print(f"  [OK] Skill instalada: {dest}")

    # 2. Copiar archivos de reglas multi-agente
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
            shutil.copy2(src, target / fname)
            print(f"  [OK] Regla copiada: {target / fname}")

    # 3. Copiar copilot instructions si existe .github
    copilot_src = BASE_DIR / ".github" / "copilot-instructions.md"
    if copilot_src.exists():
        target_github = target / ".github"
        target_github.mkdir(parents=True, exist_ok=True)
        shutil.copy2(copilot_src, target_github / "copilot-instructions.md")
        print(f"  [OK] GitHub Copilot configurado: {target_github / 'copilot-instructions.md'}")

    # 4. Asegurar carpeta 01_seed
    (target / "01_seed").mkdir(parents=True, exist_ok=True)
    print(f"  [OK] Directorio 01_seed/ preparado.")

    print(f"\n¡Exito! El proyecto {target.name} ahora soporta /seed y /seedMaster en cualquier agente.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Instalador Universal de ThinkingSeed Skills")
    parser.add_argument("--global-install", action="store_true", help="Instala las skills globalmente en el sistema")
    parser.add_argument("--target", type=str, help="Ruta de un proyecto destino donde inyectar las skills y reglas")

    args = parser.parse_args()

    print("=" * 70)
    print("  Gravity HyperScale Thinking - ThinkingSeed Multi-Agent Installer")
    print("=" * 70)

    if args.global_install:
        print("\nInstalando skills en el entorno global del usuario...")
        install_antigravity_global()
        install_claude_code_global()
        install_codex_global()
        print("\n[OK] Instalacion global completada con exito.")
        return

    if args.target:
        inject_into_project(Path(args.target))
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
