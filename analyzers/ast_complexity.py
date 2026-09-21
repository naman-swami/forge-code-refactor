"""
Python AST Cyclomatic & Cognitive Complexity Analyzer
Traverses Abstract Syntax Tree to calculate McCabe cyclomatic complexity and flag anti-patterns.
"""
import ast
from typing import Dict, Any, List

class ASTComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.cyclomatic_complexity = 1 # Base complexity
        self.anti_patterns = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Check for mutable default arguments
        for default in node.args.defaults:
            if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                self.anti_patterns.append({
                    "line": node.lineno,
                    "type": "MUTABLE_DEFAULT_ARGUMENT",
                    "severity": "HIGH",
                    "description": f"Function '{node.name}' defines a mutable default argument."
                })
        self.generic_visit(node)

    def visit_If(self, node: ast.If):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_While(self, node: ast.While):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler):
        self.cyclomatic_complexity += 1
        if node.type is None:
            self.anti_patterns.append({
                "line": node.lineno,
                "type": "BARE_EXCEPT",
                "severity": "MEDIUM",
                "description": "Bare 'except:' catches BaseException, hiding KeyboardInterrupt and system exits."
            })
        self.generic_visit(node)

    def visit_BoolOp(self, node: ast.BoolOp):
        # 'and' / 'or' add conditional branches
        self.cyclomatic_complexity += len(node.values) - 1
        self.generic_visit(node)

class CodeQualityEngine:
    @staticmethod
    def analyze_source(code_string: str) -> Dict[str, Any]:
        tree = ast.parse(code_string)
        visitor = ASTComplexityAnalyzer()
        visitor.visit(tree)

        cc = visitor.cyclomatic_complexity
        grade = "A (EXCELLENT)" if cc <= 5 else "B (ACCEPTABLE)" if cc <= 10 else "C (HIGH_COMPLEXITY)" if cc <= 15 else "F (REFACTOR_IMMEDIATELY)"

        return {
            "cyclomatic_complexity": cc,
            "quality_grade": grade,
            "anti_patterns_count": len(visitor.anti_patterns),
            "anti_patterns": visitor.anti_patterns,
            "recommendation": "APPROVED" if cc <= 10 and not visitor.anti_patterns else "REFACTOR_RECOMMENDED"
        }

    @classmethod
    def analyze_file(cls, filepath: str) -> Dict[str, Any]:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()
        res = cls.analyze_source(code)
        res["filepath"] = filepath
        return res
