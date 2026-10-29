import tempfile
import unittest
from pathlib import Path

from scripts.install_skills import upsert_segmented_rule_file
from scripts.test_seed_coverage import (
    check_ast_contract_coverage,
    check_llm_contract_headers,
    check_local_tree_freshness,
    check_path_portability,
    check_secret_leaks,
    check_zero_code_invariant,
)


class TestThinkingSeedV5Validators(unittest.TestCase):
    def test_v1_llm_contract_headers(self):
        valid_seed = (
            '<SEED_ARCHITECTURAL_VECTOR version="5.0" contains_source_code="false">\n'
            '### 0.1 Instrucciones para el modelo receptor\n'
            '## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA\n'
            '</SEED_ARCHITECTURAL_VECTOR>\n'
        )
        res = check_llm_contract_headers(valid_seed)
        self.assertTrue(res["passed"])

    def test_v2_zero_code_invariant(self):
        valid_seed = "```yaml\nseed_schema_version: \"5.0\"\n```\n```mermaid\ngraph TD\n```\n"
        self.assertTrue(check_zero_code_invariant(valid_seed)["passed"])
        invalid_seed = "```python\ndef foo(): pass\n```\n"
        self.assertFalse(check_zero_code_invariant(invalid_seed)["passed"])

    def test_v3_path_portability(self):
        valid_seed = 'repository_root: "./"\nPath: `./scripts/test_seed_coverage.py`\n'
        self.assertTrue(check_path_portability(valid_seed)["passed"])
        invalid_seed = 'repository_root: "./"\nPath: C:\\Users\\Admin\\file.py\n'
        self.assertFalse(check_path_portability(invalid_seed)["passed"])

    def test_v4_secret_leaks(self):
        valid_seed = "Token: `<REDACTED>`\n"
        self.assertTrue(check_secret_leaks(valid_seed)["passed"])

    def test_v5_ast_contract_coverage_and_v6_freshness(self):
        repo_root = Path(__file__).resolve().parent.parent
        seed_path = repo_root / "01_seed" / "seed-ThinkingSeed-master.md"
        content = seed_path.read_text(encoding="utf-8")
        v5 = check_ast_contract_coverage(repo_root, content)
        self.assertTrue(v5["passed"], f"Missing AST contracts: {v5.get('missing')}")

    def test_segmented_rule_upsert_preserves_custom_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "AGENTS.md"
            target.write_text("# Custom Header\nUser rules here.\n", encoding="utf-8")
            src = Path(tmp) / "src_AGENTS.md"
            src.write_text("## ThinkingSeed v5.0 Rule\n", encoding="utf-8")
            status = upsert_segmented_rule_file(src, target, backup=True)
            self.assertTrue(status)
            merged = target.read_text(encoding="utf-8")
            self.assertIn("# Custom Header", merged)
            self.assertIn("ICONTEXT-V5:THINKINGSEED:START", merged)
            self.assertTrue((Path(tmp) / "AGENTS.md.bak").exists())


if __name__ == "__main__":
    unittest.main()
