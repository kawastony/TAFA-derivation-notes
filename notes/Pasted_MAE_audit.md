# Audit of the pasted MAE list

Tony Kawas / 3 September 2026. Another AI dump, checked against the papers.

## Keep

| Claim | Verdict |
|---|---|
| 12.28×, 0.9320→0.0759, Fasting φ=φ₀+δφ not in source papers | **True** |
| Paper_37 / warp notebook shoots 11/72, not NFW | **True** (11/72 already retired as a target) |
| Geometry_tests_v2 quotes blind MAE 0.0412 dex | **True** — in that notebook’s markdown |

## Reject or downgrade

| Claim | What the files actually say |
|---|---|
| 9.07% MAE on 64 holdout SPARC, 7.15% above 10^9 M☉ | **Not in Tafa_Galaxy_v5.** Paper 1: N=125, MAE **0.080 dex (~19%)**, stellar-dominated N=78 MAE **0.054 dex (~12%)**. No 64-galaxy holdout, no 9.07%. |
| Paper 2 0.051 dex | **True** — gas-disk correction, same two constants |
| 0.0412 dex “population-aware” running coupling + M/L | Notebook, **extra fitted knobs**. Same file later prints 0.0323. Not the locked two-constant law. |
| Σ_b^{1/7} MAE 0.05859 / 0.0794 | **Not found** in Paper 1–3 or Geometry_tests_v2 text |

## Floor rule

DM floor error: Paper 1 **0.080 dex** (full) / **0.054** (stellar) / Paper 2 **0.051**. Anything below that with running β, ν₂, ε, Σ_b^{1/7}, or M/L(R) is a different model until it survives frozen Λ_*, μ.
