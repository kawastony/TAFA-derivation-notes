# DM floor — tests that do not touch DE

The galactic law is a two-constant fit. Tests are of that law, not of the DE rooms.

## Already used

- SPARC N=125, Q≤2, MAE ≈ 0.08 dex on v_∞
- Slope 0.25 on stellar-dominated subset (BTFR quarter-power)
- Gas-rich dwarfs systematically off — Paper 2 correction, still effective

## Honest next tests (no new constants)

1. Hold Λ_*, μ fixed. Predict v_∞ for galaxies *not* in the SPARC Q≤2 cut (new rotation curves). Pass/fail on MAE.
2. Radial shape: v(r)=v_∞ (1−e^{-μ r})^{1/2} vs SPARC V(R) where coverage reaches ≳ r_p. If the shape fails while v_∞ works, the profile is wrong even if BTFR holds.
3. Residuals vs R_eff, f_gas, quality flag — Paper 1 already saw gas trend; independent sample must reproduce it.
4. Do **not** test by mapping 12.1 kpc to a redshift, or by fitting μ per galaxy.

Until (1)–(2) are done on a held-out sample, the DM floor is a SPARC description, not a prediction engine.
