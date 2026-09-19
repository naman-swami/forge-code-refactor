# Explainability — forge-code-refactor

## Decision Architecture
forge-code-refactor employs a deterministic, transparent decision pipeline:
1. **Input Validation:** Boundary checking and schema verification.
2. **Context Retrieval:** Curated domain grounding via reference tools.
3. **Step-by-Step Derivation:** Transparent intermediate reasoning.
4. **Independent Review:** Maker-checker segregation before response delivery.

## Confidence Quantification
- **0.90 – 1.00:** High certainty, corroborated by verified deterministic tools.
- **0.75 – 0.89:** Moderate confidence, grounded in probabilistic heuristics.
- **< 0.75:** Low confidence, flagged for operator verification.
