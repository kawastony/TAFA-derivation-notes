# DM prediction — one frozen a_T

Tony Kawas / 4 September 2026

Floor change executed. Universal μ dropped. a_T frozen at the Paper 1 product. Not retuned on this run.

    a_T = 8.25e-11 m s^{-2}
    g   = g_N/2 + sqrt((g_N/2)^2 + g_N a_T)
    v   = sqrt(g r)

Data: SPARC Rotmod_LTG, N=175. Υ_disk=0.5, Υ_bul=0.7. No Q cut.
Old column is the retired fade v = v_∞ (1-e^{-μ r})^{1/2} with the same a_T.

## MAE (dex)

Sample | N | old fade | frozen a_T | frozen a_0 (1.2e-10)
---|---|---|---|---
All | 175 | 0.232 | 0.080 | 0.082
r_max ≥ 12.1 kpc | 84 | 0.180 | 0.058 | 0.058
Dwarfs M < 3e9 | 65 | 0.290 | 0.103 | 0.109
Giants M > 3e10 | 53 | 0.220 | 0.051 | 0.051

NGC 3198: old 0.104 dex → a_T 0.035 dex. r_M = 8.5 kpc (not 12.1).

a_T vs a_0: no meaningful gap. The gain is the mass-dependent switch, not a better number.

## Read it correctly

This is MOND’s interpolator wearing TAFA’s calibrated a_T. It is a better *description* of SPARC curves. It is not a derivation of a_T, and it does not touch the DE floor.

Worst remaining objects are tiny, poorly sampled disks (CamB, UGC7577, F574-2). That is expected; do not add a second constant to chase them.

## Next (if any)

Held-out rotation curves, not SPARC retuning. Or leave DM here and return to the DE fork (B1/B2). Do not glue floors.
