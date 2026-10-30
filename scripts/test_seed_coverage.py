#!/usr/bin/env python3
"""
test_seed_coverage.py - Benchmark y Auditoría Determinista para ThinkingSeed v3.0
Evalúa cuantitativamente el % de cobertura del ADN de un proyecto y audita los
6 invariantes deterministas del estándar ThinkingSeed v3.0 usando exclusivamente
la librería estándar de Python:
1. check_llm_contract_headers: Contrato XML <SEED_ARCHITECTURAL_VECTOR>, 0.1 y CONTEXT HANDOFF
2. check_zero_code_invariant: Prohibición de código fuente de implementación inyectado
3. check_path_portability: Cero rutas absolutas locales y cero URIs file:///
4. check_secret_leaks: Escaneo determinista Zero-Trust (<REDACTED>)
5. check_ast_contract_coverage: Cobertura semántica de contratos públicos y CLI flags vía AST
6. check_local_tree_freshness: Sincronización nativa entre beacons .context.yaml, tree.json y all-lowercase
"""

import os
import sys
import re
import ast
import json
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any

IGNORE_DIRS: Set[str] = {
    '.git', '.venv', 'venv', '__pycache__', '.pytest_cache',
    'node_modules', '.mypy_cache', '.ruff_cache', 'dist', 'build'
}

FORBIDDEN_CODE_LANGS: Set[str] = {
    'python', 'py', 'powershell', 'ps1', 'bash', 'sh', 'shell', 'zsh',
    'json', 'rust', 'rs', 'go', 'golang', 'sql', 'javascript', 'js',
    'typescript', 'ts', 'c', 'cpp', 'csharp', 'java', 'ruby', 'php'
}

ALLOWED_STRUCTURAL_LANGS: Set[str] = {
    '', 'text', 'plaintext', 'ascii', 'yaml', 'yml', 'mermaid', 'markdown', 'md'
}


def check_llm_contract_headers(seed_content: str) -> Dict[str, Any]:
    """Validador 1: Verifica la presencia del contenedor XML v3.0, sección 0.1 y CONTEXT HANDOFF."""
    has_xml_open = '<SEED_ARCHITECTURAL_VECTOR' in seed_content and 'contains_source_code="false"' in seed_content
    has_xml_close = '</SEED_ARCHITECTURAL_VECTOR>' in seed_content
    has_section_0_1 = '0.1 Instrucciones para el modelo receptor' in seed_content
    has_context_handoff = 'CONTEXT HANDOFF' in seed_content

    missing = []
    if not has_xml_open:
        missing.append('<SEED_ARCHITECTURAL_VECTOR ... contains_source_code="false">')
    if not has_xml_close:
        missing.append('</SEED_ARCHITECTURAL_VECTOR>')
    if not has_section_0_1:
        missing.append('0.1 Instrucciones para el modelo receptor')
    if not has_context_handoff:
        missing.append('CONTEXT HANDOFF')

    return {
        'passed': len(missing) == 0,
        'has_xml_open': has_xml_open,
        'has_xml_close': has_xml_close,
        'has_section_0_1': has_section_0_1,
        'has_context_handoff': has_context_handoff,
        'missing': missing
    }


def check_zero_code_invariant(seed_content: str) -> Dict[str, Any]:
    """Validador 2: Escanea bloques cercados con triple backtick y bloquea código de implementación."""
    fence_pattern = re.compile(r'```([a-zA-Z0-9_-]*)\n(.*?)```', re.DOTALL)
    matches = fence_pattern.findall(seed_content)

    violations: List[str] = []
    yaml_blocks_seen = 0

    for idx, (lang, body) in enumerate(matches, start=1):
        lang_clean = lang.strip().lower()
        body_lines = [line for line in body.strip().splitlines() if line.strip()]
        num_lines = len(body_lines)

        if lang_clean in FORBIDDEN_CODE_LANGS:
            violations.append(f"Bloque #{idx} con lenguaje de implementación prohibido '{lang_clean}' ({num_lines} líneas)")
            continue

        if lang_clean not in ALLOWED_STRUCTURAL_LANGS:
            violations.append(f"Bloque #{idx} con etiqueta no autorizada '{lang_clean}' ({num_lines} líneas)")
            continue

        if lang_clean in ('yaml', 'yml'):
            yaml_blocks_seen += 1
            # Solo se permite el bloque YAML de metadatos en Sección 0 (o bloques <= 5 líneas)
            if yaml_blocks_seen > 1 and num_lines > 5:
                violations.append(f"Bloque YAML #{idx} adicional mayor a 5 líneas ({num_lines} líneas)")

    return {
        'passed': len(violations) == 0,
        'total_blocks': len(matches),
        'allowed_blocks': len(matches) - len(violations),
        'violations': violations
    }


def check_path_portability(seed_content: str) -> Dict[str, Any]:
    """Validador 3: Verifica 0 rutas absolutas locales y 0 URIs file:///."""
    portability_regex = re.compile(r'(file:///|[a-zA-Z]:[/\\]|/Users/[a-zA-Z0-9._-]+|/home/[a-zA-Z0-9._-]+)')
    found_matches = portability_regex.findall(seed_content)
    has_relative_root = bool(re.search(r'repository_root:\s*["\']\./["\']', seed_content))

    return {
        'passed': len(found_matches) == 0 and has_relative_root,
        'has_relative_root': has_relative_root,
        'matches': found_matches
    }


def check_secret_leaks(seed_content: str, seed_dir: Path = None) -> Dict[str, Any]:
    """Validador 4: Escaneo determinista Zero-Trust contra fugas de secretos en 01_seed/*.md."""
    secret_patterns = [
        ('Google API Key', re.compile(r'AIza[0-9A-Za-z\-_]{35}')),
        ('OpenAI/Anthropic Key', re.compile(r'\bsk-[A-Za-z0-9\-_]{20,}\b')),
        ('GitHub Token', re.compile(r'\bgh[pousr]_[A-Za-z0-9_]{20,}\b')),
        ('AWS Access Key', re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
        ('PEM Private Key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
        ('Bearer Token Real', re.compile(r'Bearer\s+(?!<REDACTED>)[A-Za-z0-9\-\._~\+\/]{20,}')),
        ('Credential URI', re.compile(r'[a-zA-Z0-9+.-]+://[^/\s:@<]+:(?!<REDACTED>)[^/\s@<]+@[^\s"\'`]+'))
    ]

    leaks: List[str] = []
    targets: List[Tuple[str, str]] = [('current_seed', seed_content)]

    if seed_dir and seed_dir.exists():
        for md_file in sorted(seed_dir.glob('*.md')):
            try:
                targets.append((md_file.name, md_file.read_text(encoding='utf-8', errors='ignore')))
            except Exception:
                pass

    seen_leaks: Set[str] = set()
    for label, text in targets:
        for pat_name, pat_regex in secret_patterns:
            for m in pat_regex.findall(text):
                finding = f"{label}: {pat_name}"
                if finding not in seen_leaks:
                    seen_leaks.add(finding)
                    leaks.append(finding)

    has_redacted_tag = '<REDACTED>' in seed_content
    return {
        'passed': len(leaks) == 0 and has_redacted_tag,
        'leaks': leaks,
        'has_redacted_tag': has_redacted_tag
    }


def extract_repo_ast_contracts(repo_path: Path) -> Dict[str, List[str]]:
    """Extrae funciones públicas, clases y flags CLI de todos los scripts Python del repositorio (v5.0)."""
    public_symbols: List[str] = []
    cli_flags: List[str] = []
    is_idirectory_repo = repo_path.resolve().name.lower() == 'idirectory'

    # 1. Consultar .context/tree.json y .context/contracts_ast.json (Protocolo iContext v5.0)
    pruned_prefixes: List[str] = []
    tree_hash = ""
    tree_file = repo_path / '.context' / 'tree.json'
    if tree_file.exists():
        try:
            tree_data = json.loads(tree_file.read_text(encoding='utf-8', errors='ignore'))
            tree_hash = str(tree_data.get('topology_hash', ''))
            for node_path, node_meta in (tree_data.get('nodes') or {}).items():
                if isinstance(node_meta, dict) and node_meta.get('crawl') is False:
                    pruned_prefixes.append(node_path.strip('/'))
        except Exception:
            pass

    contracts_cache = repo_path / '.context' / 'contracts_ast.json'
    if contracts_cache.exists() and tree_hash:
        try:
            cache_data = json.loads(contracts_cache.read_text(encoding='utf-8', errors='ignore'))
            modules_data = cache_data.get('modules') or cache_data.get('files')
            if cache_data.get('topology_hash') == tree_hash and isinstance(modules_data, dict):
                for rel_file, fmeta in sorted(modules_data.items()):
                    rel_clean = rel_file.lstrip('./')
                    if rel_clean == 'tests' or rel_clean.startswith('tests/'):
                        continue
                    if rel_clean == 'FWengine.py' and not is_idirectory_repo:
                        continue
                    if any(rel_clean == pr or rel_clean.startswith(pr + '/') for pr in pruned_prefixes):
                        continue
                    syms = fmeta.get('symbols') or fmeta.get('public_symbols') or []
                    for sym in syms:
                        sym_name = sym.get('name') if isinstance(sym, dict) else str(sym)
                        if sym_name and sym_name not in public_symbols:
                            public_symbols.append(sym_name)
                    for flg in fmeta.get('cli_flags', []):
                        if flg not in cli_flags:
                            cli_flags.append(flg)
                return {
                    'public_symbols': public_symbols,
                    'cli_flags': cli_flags,
                    'all_contracts': public_symbols + cli_flags
                }
        except Exception:
            pass

    for root, dirs, files in os.walk(repo_path):
        rel_root = os.path.relpath(root, repo_path).replace('\\', '/')
        if rel_root == '.':
            rel_root = ''
        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
            and not d.startswith('.')
            and f"{rel_root}/{d}".strip('/') != 'tests'
            and not any(
                f"{rel_root}/{d}".strip('/') == pr or f"{rel_root}/{d}".strip('/').startswith(pr + '/')
                for pr in pruned_prefixes
            )
        ]
        if rel_root == 'tests' or rel_root.startswith('tests/'):
            continue
        if any(rel_root == pr or rel_root.startswith(pr + '/') for pr in pruned_prefixes):
            continue

        for f in sorted(files):
            if not f.endswith('.py'):
                continue
            if rel_root == '' and f == 'FWengine.py' and not is_idirectory_repo:
                continue
            p = Path(root) / f
            try:
                source = p.read_text(encoding='utf-8', errors='ignore')
                tree = ast.parse(source, filename=str(p))
            except Exception:
                continue

            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    if not node.name.startswith('_'):
                        if node.name not in public_symbols:
                            public_symbols.append(node.name)

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if node.func.attr == 'add_argument':
                        for arg in node.args:
                            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                                if arg.value.startswith('-'):
                                    if arg.value not in cli_flags:
                                        cli_flags.append(arg.value)

    return {
        'public_symbols': public_symbols,
        'cli_flags': cli_flags,
        'all_contracts': public_symbols + cli_flags
    }


def check_ast_contract_coverage(repo_path: Path, seed_content: str) -> Dict[str, Any]:
    """Validador 5: Mide el porcentaje de contratos simbólicos AST y CLI flags documentados en el Seed."""
    contracts = extract_repo_ast_contracts(repo_path)
    all_items = contracts['all_contracts']

    if not all_items:
        return {
            'passed': True,
            'matched': 0,
            'total': 0,
            'pct': 100.0,
            'symbols_matched': [],
            'missing': []
        }

    matched: List[str] = []
    missing: List[str] = []
    for item in all_items:
        if item in seed_content:
            matched.append(item)
        else:
            missing.append(item)

    pct = (len(matched) / len(all_items)) * 100.0
    return {
        'passed': pct >= 90.0,
        'matched': len(matched),
        'total': len(all_items),
        'pct': round(pct, 2),
        'symbols_matched': matched,
        'missing': missing
    }


def check_local_tree_freshness(repo_path: Path) -> Dict[str, Any]:
    """Validador 6: Verifica de forma autónoma que las carpetas con .context.yaml coincidan con .context/tree.json y cumplan all-lowercase."""
    beacon_dirs: Set[str] = set()
    uppercase_dirs: List[str] = []

    tree_file = repo_path / '.context' / 'tree.json'
    tree_nodes: Set[str] = set()
    expected_disk_nodes: Set[str] = set()
    nodes_dict: Dict[str, Any] = {}
    pruned_prefixes: List[str] = []
    if tree_file.exists():
        try:
            data = json.loads(tree_file.read_text(encoding='utf-8', errors='ignore'))
            nodes = data.get('nodes', {})
            if isinstance(nodes, dict):
                nodes_dict = nodes
                tree_nodes = set(nodes.keys())
                for k, v in nodes.items():
                    if isinstance(v, dict):
                        if v.get('exists', True) is not False:
                            expected_disk_nodes.add(k)
                        if v.get('crawl') is False:
                            pruned_prefixes.append(k.strip('/'))
        except Exception:
            pass

    for root, dirs, files in os.walk(repo_path):
        rel_root = os.path.relpath(root, repo_path).replace('\\', '/')
        if rel_root == '.':
            rel_root = ''
        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
            and (d == '.context' or not d.startswith('.'))
            and not any(
                f"{rel_root}/{d}".strip('/').startswith(pr + '/')
                for pr in pruned_prefixes
            )
        ]
        if rel_root:
            if not rel_root.startswith('.agents/skills/') and not rel_root.startswith('.'):
                for part in rel_root.split('/'):
                    if any(c.isupper() for c in part) and rel_root not in uppercase_dirs:
                        uppercase_dirs.append(rel_root)
            if '.context.yaml' in files:
                beacon_dirs.add(rel_root)

    # .context es un nodo de metadatos especial en tree.json donde .context.yaml es opcional
    if '.context' in expected_disk_nodes and (repo_path / '.context').is_dir():
        beacon_dirs.add('.context')

    # En iDirectory v5.0, los directorios ancestros intermedios tienen .context.yaml para herencia (resolve_beacon)
    intermediate_ancestors = {
        b for b in beacon_dirs
        if any(tn.startswith(b + '/') for tn in tree_nodes)
    }
    dynamic_children = {
        b for b in beacon_dirs
        if b not in expected_disk_nodes and (
            any(
                b.startswith(tn + '/') and isinstance(nodes_dict.get(tn), dict) and nodes_dict[tn].get('has_dynamic_children')
                for tn in tree_nodes
            )
            or b.split('/')[0] in ('artifacts', 'src', 'docs', '03_research', 'data', '02_foundation')
        )
    }
    comparable_beacons = beacon_dirs - intermediate_ancestors - dynamic_children

    missing_in_tree = sorted(list(comparable_beacons - expected_disk_nodes))
    missing_on_disk = sorted(list(expected_disk_nodes - beacon_dirs))

    passed = (
        tree_file.exists()
        and len(missing_in_tree) == 0
        and len(missing_on_disk) == 0
        and len(uppercase_dirs) == 0
    )

    return {
        'passed': passed,
        'beacons_count': len(comparable_beacons),
        'tree_nodes_count': len(expected_disk_nodes),
        'missing_in_tree': missing_in_tree,
        'missing_on_disk': missing_on_disk,
        'uppercase_dirs': sorted(uppercase_dirs)
    }


def analyze_repo(repo_path: Path) -> Dict[str, Any]:
    total_files = 0
    total_bytes = 0
    total_lines = 0
    ext_distribution: Dict[str, Dict[str, int]] = {}
    top_dirs: Set[str] = set()
    second_level_dirs: Set[str] = set()
    python_modules: List[str] = []
    scripts: List[str] = []
    config_files: List[str] = []
    data_files: List[str] = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        rel_root = os.path.relpath(root, repo_path).replace('\\', '/')

        if rel_root != '.':
            parts = rel_root.split('/')
            top_dirs.add(parts[0])
            if len(parts) >= 2:
                second_level_dirs.add(f"{parts[0]}/{parts[1]}")

        for f in files:
            p = Path(root) / f
            rel_f = os.path.normpath(os.path.join(rel_root, f)).replace('\\', '/')
            if rel_f.startswith('./'):
                rel_f = rel_f[2:]

            try:
                sz = p.stat().st_size
            except Exception:
                sz = 0

            total_files += 1
            total_bytes += sz
            ext = p.suffix.lower() or '[no_ext]'

            if ext not in ext_distribution:
                ext_distribution[ext] = {'files': 0, 'bytes': 0}
            ext_distribution[ext]['files'] += 1
            ext_distribution[ext]['bytes'] += sz

            if ext == '.py':
                python_modules.append(rel_f)
            if rel_f.startswith(('scripts/', 'tools/')):
                scripts.append(rel_f)
            if f.startswith('.') or ext in ('.toml', '.yaml', '.yml', '.ini', '.cfg', '.env'):
                config_files.append(rel_f)
            if ext in ('.tmdl', '.pbip', '.pbir', '.pbism', '.csv', '.parquet', '.avro', '.sql'):
                data_files.append(rel_f)

            if ext in ('.py', '.md', '.txt', '.json', '.yaml', '.yml', '.toml', '.tmdl', '.sql'):
                try:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                        total_lines += sum(1 for _ in fp)
                except Exception:
                    pass

    dependencies: Set[str] = set()
    pyproject = repo_path / 'pyproject.toml'
    if pyproject.exists():
        try:
            content = pyproject.read_text(encoding='utf-8', errors='ignore')
            matches = re.findall(r'["\']([a-zA-Z0-9_\-]+)(?:[>=<~^].*)?["\']', content)
            skip_words = {'name', 'version', 'description', 'authors', 'readme', 'python'}
            for m in matches:
                if len(m) > 2 and m.lower() not in skip_words:
                    dependencies.add(m.lower())
        except Exception:
            pass

    req_file = repo_path / 'requirements.txt'
    if req_file.exists():
        try:
            for line in req_file.read_text(encoding='utf-8', errors='ignore').splitlines():
                line = line.strip().split('#')[0].split(';')[0]
                dep = re.split(r'[=><~]', line)[0].strip()
                if dep:
                    dependencies.add(dep.lower())
        except Exception:
            pass

    ast_contracts = extract_repo_ast_contracts(repo_path)

    return {
        'repo_name': repo_path.resolve().name,
        'total_files': total_files,
        'total_bytes': total_bytes,
        'total_lines': total_lines,
        'ext_distribution': ext_distribution,
        'top_dirs': sorted(list(top_dirs)),
        'second_level_dirs': sorted(list(second_level_dirs)),
        'python_modules': sorted(python_modules),
        'scripts': sorted(scripts),
        'config_files': sorted(config_files),
        'data_files': sorted(data_files),
        'dependencies': sorted(list(dependencies)),
        'ast_contracts': ast_contracts['all_contracts']
    }


def analyze_seed(seed_path: Path) -> Dict[str, Any]:
    if not seed_path or not seed_path.exists():
        return {'exists': False}

    content = seed_path.read_text(encoding='utf-8', errors='ignore')
    lines = content.splitlines()
    words = len(content.split())
    chars = len(content)
    est_tokens = int(words * 1.3)

    conf = len(re.findall(r'\[CONFIRMADO\]', content))
    infer = len(re.findall(r'\[INFERIDO\]', content))
    falt = len(re.findall(r'\[FALTANTE\]', content))
    decl = len(re.findall(r'\[DECLARADO\]', content))

    headings = [l.strip() for l in lines if l.startswith('#')]
    has_handoff = 'CONTEXT HANDOFF' in content or 'PROTOCOLO DE ASISTENCIA' in content
    has_evidence_rules = 'REGLAS DE GENERACI' in content or 'Etiquetas de Evidencia' in content or 'Rigor Epistemológico' in content
    has_security_redact = '<REDACTED>' in content

    return {
        'exists': True,
        'size_bytes': len(content.encode('utf-8')),
        'lines': len(lines),
        'words': words,
        'chars': chars,
        'est_tokens': est_tokens,
        'epistemic': {
            'CONFIRMADO': conf,
            'INFERIDO': infer,
            'FALTANTE': falt,
            'DECLARADO': decl,
            'TOTAL_TAGS': conf + infer + falt + decl
        },
        'headings_count': len(headings),
        'has_handoff': has_handoff,
        'has_evidence_rules': has_evidence_rules,
        'has_security_redact': has_security_redact,
        'content_lower': content.lower(),
        'raw_content': content
    }


def compute_coverage(repo_meta: Dict[str, Any], seed_meta: Dict[str, Any], repo_path: Path) -> Dict[str, Any]:
    if not seed_meta.get('exists'):
        return {'covered': False}

    content = seed_meta['raw_content']
    content_lower = seed_meta['content_lower']

    def match_items(items: List[str], case_sensitive: bool = False) -> Tuple[int, int, float, List[str]]:
        if not items:
            return 0, 0, 100.0, []
        matched = []
        for it in items:
            needle = it if case_sensitive else it.lower()
            haystack = content if case_sensitive else content_lower
            base = os.path.basename(it)
            base_needle = base if case_sensitive else base.lower()
            if needle in haystack or base_needle in haystack:
                matched.append(it)
        score = (len(matched) / len(items)) * 100.0
        return len(matched), len(items), score, matched

    top_dir_m, top_dir_t, top_dir_pct, _ = match_items(repo_meta['top_dirs'])
    sec_dir_m, sec_dir_t, sec_dir_pct, _ = match_items(repo_meta['second_level_dirs'])
    scr_m, scr_t, scr_pct, _ = match_items(repo_meta['scripts'])
    py_m, py_t, py_pct, _ = match_items(repo_meta['python_modules'])
    dep_m, dep_t, dep_pct, _ = match_items(repo_meta['dependencies'])
    cfg_m, cfg_t, cfg_pct, _ = match_items(repo_meta['config_files'])

    # Ejecutar los 6 Validadores Deterministas v3.0
    v1_headers = check_llm_contract_headers(content)
    v2_zero_code = check_zero_code_invariant(content)
    v3_portability = check_path_portability(content)
    v4_secrets = check_secret_leaks(content, repo_path / '01_seed')
    v5_ast = check_ast_contract_coverage(repo_path, content)
    v6_freshness = check_local_tree_freshness(repo_path)

    # Ponderación de ADN Arquitectónico v3.0 (incluyendo cobertura semántica AST)
    adn_score = (
        (top_dir_pct * 0.20) +
        (sec_dir_pct * 0.15) +
        (dep_pct * 0.15) +
        (scr_pct * 0.15) +
        (min(py_pct * 2.5, 100.0) * 0.10) +
        (cfg_pct * 0.10) +
        (v5_ast['pct'] * 0.15)
    )

    # Penalización si fallan los contratos de identidad o portabilidad
    if not v1_headers['passed']:
        adn_score = max(0.0, adn_score - 15.0)
    if not v2_zero_code['passed']:
        adn_score = max(0.0, adn_score - 15.0)
    if not v3_portability['passed']:
        adn_score = max(0.0, adn_score - 15.0)

    all_gates_passed = (
        v1_headers['passed']
        and v2_zero_code['passed']
        and v3_portability['passed']
        and v4_secrets['passed']
        and v5_ast['passed']
        and v6_freshness['passed']
    )

    return {
        'covered': True,
        'top_dirs': {'matched': top_dir_m, 'total': top_dir_t, 'pct': top_dir_pct},
        'second_level_dirs': {'matched': sec_dir_m, 'total': sec_dir_t, 'pct': sec_dir_pct},
        'scripts': {'matched': scr_m, 'total': scr_t, 'pct': scr_pct},
        'python_modules': {'matched': py_m, 'total': py_t, 'pct': py_pct},
        'dependencies': {'matched': dep_m, 'total': dep_t, 'pct': dep_pct},
        'config_files': {'matched': cfg_m, 'total': cfg_t, 'pct': cfg_pct},
        'ast_contracts': {'matched': v5_ast['matched'], 'total': v5_ast['total'], 'pct': v5_ast['pct']},
        'validators': {
            'v1_headers': v1_headers,
            'v2_zero_code': v2_zero_code,
            'v3_portability': v3_portability,
            'v4_secrets': v4_secrets,
            'v5_ast': v5_ast,
            'v6_freshness': v6_freshness,
            'all_passed': all_gates_passed
        },
        'adn_score': round(adn_score, 2)
    }


def generate_report(
    repo_meta: Dict[str, Any],
    hybrid_meta: Dict[str, Any],
    master_meta: Dict[str, Any],
    cov_hybrid: Dict[str, Any],
    cov_master: Dict[str, Any],
    anonymize: bool = True
) -> str:
    project_label = "[PROJECT-ALPHA: ThinkingSeed Framework]" if anonymize else repo_meta.get('repo_name', 'ThinkingSeed')
    security_mode = "ANONYMIZED_EVALUATION" if anonymize else "DETERMINISTIC_V3_AUDIT"
    repo_tokens_est = int(repo_meta['total_bytes'] / 4)

    h_tokens = hybrid_meta.get('est_tokens', 0)
    m_tokens = master_meta.get('est_tokens', 0)

    h_savings = ((repo_tokens_est - h_tokens) / repo_tokens_est) * 100 if repo_tokens_est > 0 and hybrid_meta.get('exists') else 0.0
    m_savings = ((repo_tokens_est - m_tokens) / repo_tokens_est) * 100 if repo_tokens_est > 0 and master_meta.get('exists') else 0.0

    lines: List[str] = []
    lines.append("# INFORME BENCHMARK: COBERTURA Y AUDITORÍA DETERMINISTA THINKINGSEED v3.0")
    lines.append("")
    lines.append(f"> **Sujeto de Evaluación:** `{project_label}`  ")
    lines.append(f"> **Modo de Seguridad:** `{security_mode}` (Zero Local Paths & Zero-Trust `<REDACTED>`)  ")
    lines.append("> **Estándar Auditado:** `ThinkingSeed v3.0 (<SEED_ARCHITECTURAL_VECTOR>)`  ")
    lines.append("> **Herramienta:** `./scripts/test_seed_coverage.py` (Gravity HyperScale Thinking)  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. RESUMEN EJECUTIVO: ADN vs REPOSITORIO COMPLETO")
    lines.append("")
    h_lines = f"{hybrid_meta['lines']} líneas" if hybrid_meta.get('exists') else "0 líneas"
    m_lines = f"{master_meta['lines']} líneas" if master_meta.get('exists') else "0 líneas"
    h_size = f"{hybrid_meta['size_bytes'] / 1024:.1f} KB" if hybrid_meta.get('exists') else "0.0 KB"
    m_size = f"{master_meta['size_bytes'] / 1024:.1f} KB" if master_meta.get('exists') else "0.0 KB"
    h_comp = f"{repo_tokens_est / max(1, h_tokens):.0f}x más ligero" if hybrid_meta.get('exists') else "N/A"
    m_comp = f"{repo_tokens_est / max(1, m_tokens):.0f}x más ligero" if master_meta.get('exists') else "N/A"
    h_files = "1 archivo Markdown" if hybrid_meta.get('exists') else "0 archivo Markdown"
    m_files = "1 archivo Markdown" if master_meta.get('exists') else "0 archivo Markdown"

    lines.append("| Dimensión de Métrica | Repositorio Completo | Seed Híbrido (`/seed`) | Seed Master (`/seedMaster`) |")
    lines.append("|---|:---:|:---:|:---:|")
    lines.append(f"| **Volumen de Archivos** | **{repo_meta['total_files']} archivos** | {h_files} | {m_files} |")
    lines.append(f"| **Líneas de Código / Texto** | **{repo_meta['total_lines']:,} líneas** | {h_lines} | {m_lines} |")
    lines.append(f"| **Peso Físico** | **{repo_meta['total_bytes'] / (1024*1024):.2f} MB** | {h_size} | {m_size} |")
    lines.append(f"| **Tokens Estimados** | **~{repo_tokens_est:,} tokens** | **~{h_tokens:,} tokens** | **~{m_tokens:,} tokens** |")
    lines.append(f"| **Ahorro de Contexto (Tokens)** | 0% (Base) | **{h_savings:.2f}% de ahorro** | **{m_savings:.2f}% de ahorro** |")
    lines.append(f"| **Factor de Compresión** | 1x | **{h_comp}** | **{m_comp}** |")
    lines.append(f"| **ÍNDICE DE COBERTURA DE ADN** | 100% (Código crudo) | **{cov_hybrid.get('adn_score', 0.0):.1f}% (ADN Esencial)** | **{cov_master.get('adn_score', 0.0):.1f}% (ADN Exhaustivo)** |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. DESGLOSE DE COBERTURA ESTRUCTURAL Y SEMÁNTICA AST (%)")
    lines.append("")
    lines.append("| Componente Estructural / Semántico | Total en Repo | Detectado en `/seed` | % Cobertura `/seed` | Detectado en `/seedMaster` | % Cobertura `/seedMaster` |")
    lines.append("|---|:---:|:---:|:---:|:---:|:---:|")

    components = [
        ('Directorios Raíz (Top Dirs)', 'top_dirs', len(repo_meta['top_dirs'])),
        ('Módulos Nivel 2 (Sub-capas)', 'second_level_dirs', len(repo_meta['second_level_dirs'])),
        ('Dependencias & Librerías', 'dependencies', len(repo_meta['dependencies'])),
        ('Scripts & Herramientas CLI', 'scripts', len(repo_meta['scripts'])),
        ('Archivos de Configuración', 'config_files', len(repo_meta['config_files'])),
        ('Módulos Python Críticos', 'python_modules', len(repo_meta['python_modules'])),
        ('Contratos Simbólicos AST & Flags CLI', 'ast_contracts', len(repo_meta['ast_contracts']))
    ]

    for label, key, repo_total in components:
        h_data = cov_hybrid.get(key, {'matched': 0, 'total': repo_total, 'pct': 0.0})
        m_data = cov_master.get(key, {'matched': 0, 'total': repo_total, 'pct': 0.0})
        lines.append(f"| **{label}** | {repo_total} | {h_data['matched']} | **{h_data['pct']:.1f}%** | {m_data['matched']} | **{m_data['pct']:.1f}%** |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. AUDITORÍA DE INVARIANTES THINKINGSEED v3.0 (GATES DETERMINISTAS)")
    lines.append("")
    v = cov_master.get('validators', {})
    v1 = v.get('v1_headers', {'passed': False, 'missing': []})
    v2 = v.get('v2_zero_code', {'passed': False, 'total_blocks': 0, 'violations': []})
    v3 = v.get('v3_portability', {'passed': False, 'has_relative_root': False, 'matches': []})
    v4 = v.get('v4_secrets', {'passed': False, 'leaks': []})
    v5 = v.get('v5_ast', {'passed': False, 'matched': 0, 'total': 0, 'pct': 0.0})
    v6 = v.get('v6_freshness', {'passed': False, 'beacons_count': 0, 'tree_nodes_count': 0, 'uppercase_dirs': []})

    lines.append("| Gate ID | Validador Determinista | Estado | Evidencia / Métrica Verificada |")
    lines.append("|---|---|:---:|---|")
    lines.append(f"| **GATE-01** | `check_llm_contract_headers` (Contrato XML Multi-LLM) | {'PASS' if v1['passed'] else 'FAIL'} | `<SEED_ARCHITECTURAL_VECTOR>`, `0.1` y `CONTEXT HANDOFF` verificados |")
    lines.append(f"| **GATE-02** | `check_zero_code_invariant` (Zero Source Code) | {'PASS' if v2['passed'] else 'FAIL'} | {len(v2.get('violations', []))} violaciones en {v2.get('total_blocks', 0)} bloques cercados |")
    lines.append(f"| **GATE-03** | `check_path_portability` (Zero Local Paths & URIs) | {'PASS' if v3['passed'] else 'FAIL'} | `repository_root: \"./\"`={v3.get('has_relative_root')}, {len(v3.get('matches', []))} rutas locales/URIs |")
    lines.append(f"| **GATE-04** | `check_secret_leaks` (Zero-Trust `<REDACTED>`) | {'PASS' if v4['passed'] else 'FAIL'} | {len(v4.get('leaks', []))} fugas detectadas; política `<REDACTED>` activa |")
    lines.append(f"| **GATE-05** | `check_ast_contract_coverage` (Firmas Simbólicas AST) | {'PASS' if v5['passed'] else 'FAIL'} | {v5.get('matched', 0)}/{v5.get('total', 0)} contratos públicos y CLI flags ({v5.get('pct', 0.0):.1f}%) |")
    lines.append(f"| **GATE-06** | `check_local_tree_freshness` (Satélite & `all-lowercase`) | {'PASS' if v6['passed'] else 'FAIL'} | {v6.get('beacons_count', 0)} beacons == {v6.get('tree_nodes_count', 0)} nodos en `tree.json`, {len(v6.get('uppercase_dirs', []))} dirs con mayúsculas |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. RIGOR EPISTEMOLÓGICO Y CONTROL DE ALUCINACIONES")
    lines.append("")
    h_ep = hybrid_meta.get('epistemic', {'CONFIRMADO': 0, 'INFERIDO': 0, 'FALTANTE': 0, 'DECLARADO': 0, 'TOTAL_TAGS': 0})
    m_ep = master_meta.get('epistemic', {'CONFIRMADO': 0, 'INFERIDO': 0, 'FALTANTE': 0, 'DECLARADO': 0, 'TOTAL_TAGS': 0})

    lines.append("| Etiqueta Epistémica | Significado Metodológico | Frecuencia en `/seed` | Frecuencia en `/seedMaster` |")
    lines.append("|---|---|:---:|:---:|")
    lines.append(f"| `[CONFIRMADO]` | Verificado en código fuente y manifiestos | {h_ep['CONFIRMADO']} | **{m_ep['CONFIRMADO']}** |")
    lines.append(f"| `[INFERIDO]` | Deducción arquitectónica razonable | {h_ep['INFERIDO']} | {m_ep['INFERIDO']} |")
    lines.append(f"| `[FALTANTE]` | Brecha identificada / WIP del proyecto | {h_ep['FALTANTE']} | {m_ep['FALTANTE']} |")
    lines.append(f"| `[DECLARADO]` | Mencionado en docs pero pendiente o divergente | {h_ep['DECLARADO']} | {m_ep['DECLARADO']} |")
    lines.append(f"| **TOTAL AFIRMACIONES AUDITADAS** | Evidencia rastreable | **{h_ep['TOTAL_TAGS']}** | **{m_ep['TOTAL_TAGS']}** |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 5. CONCLUSIÓN Y VEREDICTO DE AUDITORÍA")
    lines.append(f"1. **Eficacia Demostrada:** El repositorio `{project_label}` con **{repo_meta['total_files']} archivos ({repo_meta['total_bytes'] / (1024*1024):.2f} MB)** queda representado en su vector arquitectónico v3.0 en **{m_size}** ({m_savings:.2f}% de ahorro de tokens).")
    lines.append(f"2. **Cobertura Semántica AST:** Se verificaron mediante `ast.parse()` **{v5.get('matched', 0)}/{v5.get('total', 0)} ({v5.get('pct', 0.0):.1f}%)** contratos públicos y flags CLI documentados como firmas simbólicas de 1 línea.")
    lines.append(f"3. **Cumplimiento de Gates v3.0:** Estado global de los 6 validadores deterministas: **{'PASS (6/6 GATES OK)' if v.get('all_passed') else 'FAIL (REVISAR VIOLACIONES)'}**.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Auditoría Determinista y Cobertura de ThinkingSeed v3.0")
    parser.add_argument("--target-repo", required=True, help="Ruta al repositorio completo a auditar")
    parser.add_argument("--output", default=".context/cache/benchmark_seed_coverage.md", help="Ruta de salida del reporte")
    parser.add_argument("--no-anonymize", action="store_true", help="Desactivar anonimización de datos")
    args = parser.parse_args()

    repo_path = Path(args.target_repo)
    if not repo_path.exists():
        print(f"[ERROR] La ruta {repo_path} no existe.", file=sys.stderr)
        sys.exit(1)

    seed_dir = repo_path / "01_seed"
    hybrid_seeds = list(seed_dir.glob("seed-*.md")) if seed_dir.exists() else []
    hybrid_seed = None
    master_seed = None

    for s in hybrid_seeds:
        if s.name.endswith("-master.md"):
            master_seed = s
        else:
            hybrid_seed = s

    print(f"[*] Analizando repositorio: {repo_path.resolve().name}...")
    repo_meta = analyze_repo(repo_path)
    print(f"    - Archivos: {repo_meta['total_files']}, Bytes: {repo_meta['total_bytes']:,}, Contratos AST: {len(repo_meta['ast_contracts'])}")

    print("[*] Analizando Seeds en ./01_seed/...")
    hybrid_meta = analyze_seed(hybrid_seed) if hybrid_seed else {'exists': False}
    master_meta = analyze_seed(master_seed) if master_seed else {'exists': False}

    print("[*] Calculando coberturas y ejecutando los 6 validadores deterministas v3.0...")
    cov_hybrid = compute_coverage(repo_meta, hybrid_meta, repo_path)
    cov_master = compute_coverage(repo_meta, master_meta, repo_path)

    print(f"    - Score ADN Hybrid: {cov_hybrid.get('adn_score', 0.0):.1f}%")
    print(f"    - Score ADN Master: {cov_master.get('adn_score', 0.0):.1f}%")

    validators = cov_master.get('validators', {})
    if validators:
        for gate_key, gate_label in [
            ('v1_headers', 'Validador 1 (Contrato XML Multi-LLM)'),
            ('v2_zero_code', 'Validador 2 (Invariante Zero-Code)'),
            ('v3_portability', 'Validador 3 (Portabilidad Zero Local Paths)'),
            ('v4_secrets', 'Validador 4 (Zero-Trust Secret Scanner)'),
            ('v5_ast', 'Validador 5 (Cobertura Semántica AST)'),
            ('v6_freshness', 'Validador 6 (Frescura Satelital & all-lowercase)')
        ]:
            g = validators.get(gate_key, {})
            status = "OK" if g.get('passed') else "FAIL"
            print(f"    [{status}] {gate_label}")
            if not g.get('passed'):
                print(f"         Detalle: {g}")

    report_content = generate_report(
        repo_meta, hybrid_meta, master_meta,
        cov_hybrid, cov_master,
        anonymize=(not args.no_anonymize)
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report_content, encoding='utf-8')
    print(f"[+] Reporte generado exitosamente en: {out_path}")

    # Actualizar Bus Cognitivo Federado v5.0 (.context/icontext_bus.json -> layers.l1_thinkingseed)
    bus_path = repo_path / '.context' / 'icontext_bus.json'
    if bus_path.exists():
        try:
            import hashlib, time, uuid, threading, random
            from datetime import datetime, timezone
            
            # Safe read with backoff for transient Windows contention
            bus_data = None
            delay = 0.015
            for _ in range(6):
                try:
                    bus_data = json.loads(bus_path.read_text(encoding='utf-8', errors='replace'))
                    break
                except (OSError, json.JSONDecodeError):
                    time.sleep(delay + random.uniform(0.005, 0.015))
                    delay *= 1.5

            if isinstance(bus_data, dict):
                v5_ast = validators.get('v5_ast', {})
                all_ok = bool(validators.get('all_passed', False))
                rel_seed = f"./01_seed/{master_seed.name}" if master_seed else ""
                bus_data['updated_at'] = datetime.now(timezone.utc).isoformat()
                
                # Limpiar clave huérfana en raíz si existía previamente
                bus_data.pop('l1_thinkingseed', None)

                layers = bus_data.setdefault('layers', {})
                l1_prev = layers.get('l1_thinkingseed', {}) if isinstance(layers.get('l1_thinkingseed'), dict) else {}

                seed_hash_val = l1_prev.get('seed_hash', '')
                if not seed_hash_val and master_seed and master_seed.exists():
                    seed_hash_val = hashlib.sha256(master_seed.read_bytes()).hexdigest()

                tree_hash_val = ""
                tree_file = repo_path / '.context' / 'tree.json'
                if tree_file.exists():
                    try:
                        tree_hash_val = str(json.loads(tree_file.read_text(encoding='utf-8')).get('topology_hash', ''))
                    except Exception:
                        pass

                layers['l1_thinkingseed'] = {
                    'present': True,
                    'version': '5.0.0',
                    'seed_path': rel_seed,
                    'seed_version': '5.0',
                    'ast_coverage_pct': float(v5_ast.get('pct', 0.0)),
                    'gates_passed': "6/6" if all_ok else "failed",
                    'seed_hash': seed_hash_val,
                    'synced_with_topology_hash': tree_hash_val or l1_prev.get('synced_with_topology_hash', ''),
                    'untracked_public_symbols': list(v5_ast.get('missing', [])),
                    'freshness_status': 'SYNCED' if all_ok else 'STALE_SEED',
                    'last_validated_at': datetime.now(timezone.utc).isoformat(),
                }

                # Escritura atómica segura y única con cleanup garantizado
                unique_suffix = f"{os.getpid()}_{threading.get_ident()}_{uuid.uuid4().hex[:8]}"
                tmp_bus = bus_path.parent / f".tmp_{unique_suffix}_{bus_path.name}"
                payload = json.dumps(bus_data, indent=2, ensure_ascii=False) + "\n"
                delay = 0.02
                try:
                    tmp_bus.write_text(payload, encoding='utf-8')
                    for attempt in range(10):
                        try:
                            os.replace(tmp_bus, bus_path)
                            break
                        except OSError:
                            if attempt == 9:
                                raise
                            time.sleep(delay + random.uniform(0.01, 0.03))
                            delay *= 1.4
                finally:
                    if tmp_bus.exists():
                        try:
                            tmp_bus.unlink()
                        except OSError:
                            pass
        except Exception:
            pass

    if not master_meta.get('exists') or not validators.get('all_passed', False):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
