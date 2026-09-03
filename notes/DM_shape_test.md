# DM test 2 — radial shape, Λ* and μ frozen

Tony Kawas / 3 September 2026

Locked interpolator (Floor_DM, Paper 1):

    v_∞ = (Λ*^2 G M_bar μ)^{1/4}
    v(r) = v_∞ (1 − e^{-μ r})^{1/2}

    Λ* = 175.8 km s^{-1} kpc^{1/2}
    μ  = 0.0824 kpc^{-1}   (not fitted per galaxy)

Data: SPARC Rotmod_LTG, N=175 files. Υ_disk=0.5, Υ_bul=0.7.
M_bar = V_bar^2(r_max) r_max / G (enclosed at last point).
No quality cut (Paper 1 used Q≤2, N=125). Not 12.28×, not NFW.

## Results

| Sample | N | v(r) MAE (mean dex) | shape-only MAE (mean) | log10(v_∞/V_last) rms |
|---|---|---|---|---|
| All SPARC rotmod | 175 | 0.232 | 0.088 | 0.103 |
| r_max ≥ 12.1 kpc | 84 | 0.180 | 0.105 | 0.075 |

NGC 3198: r_max=44 kpc, v_∞=147 vs V_last=150, v(r) MAE=0.104 dex.

## Read this correctly

- **v_∞ vs last Vobs** on the outer sample (0.075 dex rms) matches Paper 1’s ~0.08 dex *amplitude* story. BTFR-like. Calibration is doing that job.
- **v(r) with frozen μ** is worse (~0.18 dex) because (1−e^{-μ r})^{1/2} is not Newton at small r. Worst objects are tiny (r_max ≪ r_p): NGC 6789, UGC 7232.
- Shape-only (scale to last V, μ still frozen) median ~0.07–0.08 dex — the *form* is not a disaster, but it is not the 0.08 dex Paper 1 number either (that number was v_∞, not the curve).

## Verdict for the floor

The two constants earn the outer speed. They do **not** yet earn the inner rise. Next DM work, if any: a Newton-matching interpolator that still has only Λ*, μ — or admit v(r) is a one-parameter fade, not a rotation-curve theory.

Do not repair this with λ^2, NFW templates, or 12.28×.
