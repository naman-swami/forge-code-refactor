import os
import pytest
from analyzers.ast_complexity import CodeQualityEngine

def test_legacy_code_anti_patterns():
    fixtures_dir = os.path.join(os.path.dirname(__file__), "..", "fixtures", "legacy_samples")
    path = os.path.join(fixtures_dir, "monolithic_calculator.py")
    res = CodeQualityEngine.analyze_file(path)
    
    assert res["cyclomatic_complexity"] >= 6
    assert res["anti_patterns_count"] >= 2
    types = [p["type"] for p in res["anti_patterns"]]
    assert "MUTABLE_DEFAULT_ARGUMENT" in types
    assert "BARE_EXCEPT" in types
    assert res["recommendation"] == "REFACTOR_RECOMMENDED"

def test_clean_code_standards():
    fixtures_dir = os.path.join(os.path.dirname(__file__), "..", "fixtures", "legacy_samples")
    path = os.path.join(fixtures_dir, "clean_calculator.py")
    res = CodeQualityEngine.analyze_file(path)
    
    assert res["cyclomatic_complexity"] <= 5
    assert res["anti_patterns_count"] == 0
    assert res["recommendation"] == "APPROVED"
