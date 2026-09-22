# Forge Code Refactor & AST Linter

> **Abstract Syntax Tree (AST) Static Refactoring & Complexity Auditing Engine**  
> Parsing Python AST to Measure McCabe Cyclomatic Complexity and Remediate Code Smells.

---

### Refactoring Rule Engine

```
Source .py File ──► ast.parse() ──► AST Visitor Pipeline ──► Unified Diff Output
                                          │
                   ┌──────────────────────┼──────────────────────┐
                   ▼                      ▼                      ▼
             [FORGE-001]            [FORGE-002]            [FORGE-003]
            Mutable Default         Bare Except           High Complexity
             Argument Trap         Clause Handler           (M > 10)
```

### Verified Code Remediation Example

```diff
--- a/fixtures/legacy_samples/monolithic_calculator.py
+++ b/fixtures/legacy_samples/clean_calculator.py
@@ -10,7 +10,7 @@
-def execute_transaction(records, log_buffer=[]):
+def execute_transaction(records, log_buffer=None):
+    if log_buffer is None:
+        log_buffer = []
     try:
         for r in records:
             process_record(r)
-    except:
+    except (ValueError, KeyError) as err:
-        pass
+        logger.error(f"Transaction processing error: {err}")
```

---

### Command Line Interface

```bash
# Analyze benchmark monolithic code samples
python refactor.py --demo

# Verify AST complexity unit tests
pytest tests/ -v
```

Configuration settings, maximum cyclomatic thresholds, and exclude filters are managed via standard [pyproject.toml](pyproject.toml).
