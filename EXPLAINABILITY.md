# Explainability — forge-code-refactor

## Decision Reasoning
Forge determines refactoring paths by parsing source code into AST trees, calculating cyclomatic complexity and Halstead metrics, and applying proven structural design patterns (Strategy, Dependency Injection) while preserving behavioral equivalence.

## Data Sources and Inputs Used
Language abstract syntax trees (Python AST, TypeScript compiler API, Tree-sitter), static analysis security rules (OWASP Top 10, CWE patterns), algorithmic complexity benchmarks, and user code snippets.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, forge-code-refactor assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, forge-code-refactor will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, forge-code-refactor explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
forge-code-refactor actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Dynamic Runtime Reflection: Cannot statically predict runtime monkey-patching or dynamic `eval()` behaviors with 100% certainty.
- Integration Environment: Does not execute or deploy binaries to production environments without external CI/CD pipelines.
- Third-Party Library Bugs: Cannot resolve upstream bugs embedded inside closed-source proprietary dependencies.
- Domain Business Logic: Cannot infer unspoken business domain constraints not captured in unit test specifications.

## Uncertainty Quantification Approach
When refactoring code without comprehensive automated test coverage, Forge flags regression risks, generates accompanying unit test scaffolding, and mandates human developer review before merging PRs.
