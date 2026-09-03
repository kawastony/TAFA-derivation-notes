# The claimed 12× accuracy

Tony Kawas / 3 September 2026. Searched papers and code.

No notebook or paper writes “12× from extra dimensions.” Closest hits in `Quantum_Gravity/Geometry_tests_v2.ipynb`:

## What is actually in the code

| Number | What it is | Extra spacetime D? |
|---|---|---|
| Paper 1 MAE 0.080 → Paper 2 0.051 dex | gas-disk layer, factor **1.57** | No |
| Blind MAE **0.0323** dex vs MOND 0.046 | later SPARC refinements, **1.4×** | No |
| T2 `DELTA_PSI / 1.47` ≈ **15.5×** | cone-angle gap vs Paper 7 cap, pass if >10 | Geometry test, not SPARC |
| TAFA v3 blind MAE **1.187** then v3-fixed **0.063** | unit/formula bugfix, ~19× | No — broken code |
| 5-parameter recalibration | extra knobs (β, ν₂, ε…) | No |

If the memory is “baryons-only vs TAFA ~12×”: that would be Newton vs the DM-floor law, not 4D vs 5D. I did not find a baryon-only MAE printed as 0.38 dex next to 0.032. Do not invent it.

## Can it be used on the floors?

No, not as an extra-dimension theorem. A 12× that is not in a closed equation is not a storey.

Paper 2’s 0.051 dex stays on the DM floor. The 0.0323 dex runs used extra fitted functions (running coupling, 5 parameters). That is a better SPARC description only if it survives a frozen-Λ_*, frozen-μ held-out test. It does not license n=5, n=10, or glue to DE.
