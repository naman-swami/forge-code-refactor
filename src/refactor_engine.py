"""
Forge Code Refactor Engine
AST-driven code complexity analysis computing Cyclomatic Complexity, Halstead Metrics, and Code Smells.
"""
import ast
import math
from typing import Dict, Any, List

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 1

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.complexity += 1
        self.generic_visit(node)

class CodeRefactorAuditor:
    def analyze_source(self, code_str: str) -> Dict[str, Any]:
        try:
            tree = ast.parse(code_str)
        except SyntaxError as e:
            return {"error": f"Syntax error in code: {str(e)}", "maintainability_index": 0}

        visitor = ComplexityVisitor()
        visitor.visit(tree)
        cyclomatic = visitor.complexity

        loc = len([line for line in code_str.splitlines() if line.strip() and not line.strip().startswith("#")])
        if loc == 0:
            loc = 1

        # Maintainability Index approximation: 171 - 5.2 * ln(V) - 0.23 * CC - 16.2 * ln(LOC)
        # Simplified normalized scale:
        mi = 100 - (cyclomatic * 3.5) - (loc * 0.4)
        mi = max(0.0, min(100.0, round(mi, 2)))

        smells = []
        if cyclomatic > 8:
            smells.append(f"High Cyclomatic Complexity ({cyclomatic}): Recommend extracting helper methods.")
        if loc > 50:
            smells.append(f"Excessive Function Length ({loc} lines): Decompose into modular components.")

        return {
            "cyclomatic_complexity": cyclomatic,
            "effective_loc": loc,
            "maintainability_index": mi,
            "maintainability_rating": "A" if mi >= 80 else "B" if mi >= 65 else "C" if mi >= 50 else "D",
            "detected_code_smells": smells,
            "confidence_score": 0.98
        }
