# Forge Code Refactor & AST Engine

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![DevTools](https://img.shields.io/badge/Domain-Static_Analysis_AST-blue.svg)](docs/refactoring_catalog.md)
[![Standard](https://img.shields.io/badge/Metric-McCabe_Complexity-yellow.svg)](docs/refactoring_catalog.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A developer productivity engine analyzing Abstract Syntax Trees (AST) to compute McCabe cyclomatic complexity, detect anti-patterns (bare excepts, mutable default arguments), and guide systematic code modernizations.

```
                    ┌─────────────────────────┐
                    │  Python Source File     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   ast.parse AST Tree    │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │ McCabe Cyclomatic   │         │ Anti-Pattern Walker │
      │ Complexity ($CC$)   │         │ (Mutable defaults)  │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Quality Grade & Action  │
                    │ (A / B / C / REFACTOR)  │
                    └─────────────────────────┘
```

## Features

- **McCabe Cyclomatic Metric**: Deterministically tracks decision branch bifurcations (`if`, `for`, `while`, `try`, `bool_ops`).
- **AST Pattern Traversal**: Flags anti-patterns that induce subtle runtime production bugs.
- **Fixture Verification**: Comes bundled with representative legacy and modernized implementations.

## Directory Structure

```
forge-code-refactor/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint software engineering provenance
├── analyzers/
│   └── ast_complexity.py            # AST visitor & complexity evaluator
├── fixtures/
│   └── legacy_samples/
│       ├── monolithic_calculator.py # Sample with high CC and anti-patterns
│       └── clean_calculator.py      # Refactored baseline
├── docs/
│   └── refactoring_catalog.md       # Refactoring pattern reference
├── tests/
│   └── test_agent.py                # AST analysis regression tests
├── main.py                          # CLI entry point
└── requirements.txt
```

## Quick Start

```bash
# Run refactoring analyzer test suite
pytest tests/ -v

# Analyze benchmark legacy script
python main.py --demo
```
