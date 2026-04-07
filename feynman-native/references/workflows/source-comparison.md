# Source Comparison

Use this workflow to compare tools, papers, models, frameworks, products, claims, or approaches.

## Trigger phrases
- compare X vs Y
- source comparison
- comparison matrix
- pros and cons with evidence

## Deliverable
- Final artifact: `outputs/<slug>.md`
- Provenance sidecar: `outputs/<slug>.provenance.md`

## Execution contract

### 1. Define dimensions before searching
Write comparison dimensions into the plan before gathering. Common dimensions:
- capability
- cost
- evidence quality
- reproducibility
- performance
- maturity
- operational complexity
- risks / caveats

### 2. Gather primary sources by item
Use one research pass per major item or source family when the comparison is wide.
Keep evidence clearly attributable to each compared item.

### 3. Produce a grounded matrix
Required structure:
```md
# Title

## Executive Summary

## Comparison Dimensions

## Matrix

## Agreements Across Sources

## Disagreements / Caveats

## Recommendation or Decision Framing
```

### 4. Rules
- Do not pick a winner if the evidence is too mixed.
- Distinguish vendor self-claims from independent evidence.
- Flag missing evidence as missing evidence, not as a negative or positive.

### 5. Verification loop
Run the verifier/reviewer loop before delivery for substantial comparisons.

## Minimum acceptance bar
- dimensions declared up front
- matrix grounded in direct URLs
- caveats section present
- no winner-picking without support
