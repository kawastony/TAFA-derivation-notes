# Held-out galaxies — frozen a_T

Tony Kawas / 4 September 2026

a_T = 8.25e-11 m s^{-2} not retuned. Same interpolator as Floor_DM.

Two samples that are not the SPARC Q=1 working set.

## 1. SPARC quality flag 3 (full v(r))

Lelli+2016 Q: 1 high, 2 medium, 3 low (asymmetries / noncircular motion).
Paper 1 used Q≤2. Q=3 was never the calibration cut. Still SPARC photometry, so not a new telescope — it is a quality hold-out.

Q | N | MAE mean dex | median
---|---|---|---
1 | 99 | 0.065 | 0.053
2 | 64 | 0.081 | 0.064
3 | 12 | 0.190 | 0.203

Q=3 is worse, as it should be. The law does not rescue messy kinematics. Best Q=3: UGCA281 0.020, UGC6973 0.065, NGC2366 0.078. Worst: F574-2 0.347, UGC2455 0.311 (same names that failed even on the training-like set).

## 2. LITTLE THINGS not in SPARC (amplitude only)

Oh+2015, 26 dwarfs. 3 overlap SPARC (DDO154, DDO168, NGC2366). 23 unique.
No public V_bar(r) in the CDS tables (rotdmbar is scaled V_tot). So this is v_inf = (G M_bar a_T)^{1/4} vs V(Rmax), with M_bar = Mgas + MstarK from their Table 2.

N=23: mean log10(v_inf/Vmax) = −0.064, rms 0.19 dex, MAE 0.14 dex.

Close: DDO210, DDO126, Haro29, CVnIdwA, IC10 (|Δ| < 0.03 dex).
Far: NGC3738 (−0.49), UGC8508 (−0.36), DDO101 (−0.31) — compact, Rmax ~ 2 kpc, Vmax is not an outer flat speed.

## Verdict

- Clean high-quality disks: a_T holds.
- Low-quality SPARC and compact dwarfs: it does not auto-win. Do not add μ back to chase them.
- A true shape test off SPARC needs a survey with Vgas+Vstar profiles (THINGS mass models not already in SPARC). WALLABY DR2 is Vrot-only / Tier 2 — skip for now.

DE floor still untouched.
