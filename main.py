import json
import argparse
from src.refactor_engine import CodeRefactorAuditor

def main():
    parser = argparse.ArgumentParser(description="Forge Code Refactor Auditor CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated AST complexity refactoring audit")
    args = parser.parse_args()

    auditor = CodeRefactorAuditor()
    sample_code = """
def process_transactions(records):
    results = []
    for r in records:
        if r.get("status") == "ACTIVE":
            if r.get("amount") > 1000:
                if r.get("flagged"):
                    results.append("REJECT")
                else:
                    results.append("APPROVE_HIGH")
            else:
                results.append("APPROVE_STANDARD")
        else:
            results.append("IGNORE")
    return results
"""

    report = auditor.analyze_source(sample_code)
    print("="*60)
    print(" FORGE AST CODE QUALITY & MAINTAINABILITY AUDIT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
