# AST Code Refactoring Specification & Complexity Metrics

## 1. Abstract Syntax Tree (AST) Metrics Standard
Forge executes programmatic static analysis and transformation directly on Python Abstract Syntax Trees (using Python's `ast` module) in compliance with:
- **PEP 8 (Style Guide for Python Code)**
- **IEEE Std 1061 (Standard for Software Quality Metrics Methodology)**
- **ISO/IEC 25010 (Software Product Quality Model)**

---

## 2. McCabe Cyclomatic Complexity Formulation
Cyclomatic complexity ($M$) evaluates the number of linearly independent paths through a function's control flow graph:

$$M = E - N + 2P$$

In Python AST inspection, this is calculated directly from decision nodes:
$$M = 1 + \sum (\text{If} + \text{For} + \text{While} + \text{ExceptHandler} + \text{BoolOp} + \text{MatchCase})$$

### Refactoring Thresholds:
- $M \in [1, 5]$: Clean, modular, easily testable logic.
- $M \in [6, 10]$: Moderate complexity; acceptable for high-level business dispatchers.
- $M > 10$: **Refactoring Alert Trigger**; function must be decomposed into smaller sub-methods.
- $M > 20$: Critical refactoring priority; high defect probability and untestable edge cases.

---

## 3. Anti-Pattern Catalog & Automated Transformations

### Rule FORGE-001: Mutable Default Arguments
- **Defect**: Assigning mutable literals (`[]`, `{}`) as function argument defaults creates shared persistent state across invocations.
- **Transformation**: Replace default value with `None` and inject guard initialization at the top of the function body (`if arg is None: arg = []`).

### Rule FORGE-002: Bare Except Clauses
- **Defect**: Using `except:` catches critical system-exiting exceptions (`KeyboardInterrupt`, `SystemExit`) and masks programmer bugs.
- **Transformation**: Refactor bare clauses to specify targeted exception hierarchies (`except (ValueError, KeyError) as err:`) with structured error logging.

### Rule FORGE-003: Cognitive Nesting Depth
- **Defect**: Nested control structures exceeding 4 indent levels increase mental parsing overhead.
- **Transformation**: Apply early-return guard clauses to invert nested conditionals.

---

## 4. AST Transformation Safety Guarantees
All refactoring passes are idempotent and guaranteed safe:
1. Syntax validity is confirmed by compiling the transformed AST into bytecode via `compile(node, filename, 'exec')`.
2. Unit test suites must achieve identical pass rates before and after refactoring.
