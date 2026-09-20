import pytest
from src.refactor_engine import CodeRefactorAuditor

def test_simple_clean_code():
    auditor = CodeRefactorAuditor()
    code = """
def add(a, b):
    return a + b
"""
    report = auditor.analyze_source(code)
    assert report["cyclomatic_complexity"] == 1
    assert report["maintainability_rating"] == "A"
    assert len(report["detected_code_smells"]) == 0

def test_complex_nested_code():
    auditor = CodeRefactorAuditor()
    code = """
def check(val):
    if val > 0:
        if val > 10:
            if val > 100:
                return 3
            return 2
        return 1
    elif val < 0:
        if val < -10:
            return -2
        return -1
    return 0
"""
    report = auditor.analyze_source(code)
    assert report["cyclomatic_complexity"] >= 6
    assert report["maintainability_index"] < 90
