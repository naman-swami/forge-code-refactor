# Code Refactoring Patterns Catalog

## Martin Fowler Refactoring Catalog Reference

### 1. Extract Function
- **Symptom**: Long method with high cyclomatic complexity ($CC > 10$).
- **Remedy**: Group cohesive lines into separate named functions with clear parameter signatures.

### 2. Replace Nested Conditionals with Guard Clauses
- **Symptom**: Deeply nested `if / else` blocks reducing cognitive readability.
- **Remedy**: Use early returns (`if not valid: return`) to flatten the execution path.

### 3. Eliminate Mutable Default Arguments
- **Symptom**: `def foo(items=[])` creates state retention across successive function calls.
- **Remedy**: Use `items=None` with `items = items if items is not None else []`.
