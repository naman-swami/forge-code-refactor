import argparse
import os
from analyzers.ast_complexity import CodeQualityEngine

def main():
    parser = argparse.ArgumentParser(description="Forge Code Refactoring & AST Analysis CLI")
    parser.add_argument("--demo", action="store_true", help="Analyze benchmark legacy sample")
    parser.add_argument("--file", type=str, help="Path to Python file to inspect")
    args = parser.parse_args()

    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures", "legacy_samples")

    if args.demo:
        print("=== FORGE CODE REFACTORING AST AUDIT ===\n")
        for sample in ["monolithic_calculator.py", "clean_calculator.py"]:
            path = os.path.join(fixtures_dir, sample)
            res = CodeQualityEngine.analyze_file(path)
            print(f"File: {sample}")
            print(f"  Cyclomatic Complexity: {res['cyclomatic_complexity']}")
            print(f"  Quality Grade: {res['quality_grade']} | Recommendation: {res['recommendation']}")
            print(f"  Anti-Patterns Detected: {res['anti_patterns_count']}")
            for p in res["anti_patterns"]:
                print(f"    [Line {p['line']}] {p['type']} ({p['severity']}): {p['description']}")
            print("-" * 50)
    elif args.file:
        res = CodeQualityEngine.analyze_file(args.file)
        print(res)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
