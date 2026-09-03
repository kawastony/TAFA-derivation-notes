# MOND acceleration scale vs TAFA

Tony Kawas / 3 September 2026

## The product

    a_T = Lambda_*^2 * mu = 8.25e-11 m s^{-2}

MOND SPARC scale: a_0 ~ 1.2e-10 m s^{-2}.

    a_T / a_0 ~ 0.69
    a_0 ~ c H_0 / 2 pi
    a_T ~ 0.13 c H_0

BTFR is the same hat: v_inf^4 = G M a. TAFA 0.075 dex outer v_inf is this hat. Not a new constant; two TAFA numbers multiplied into one acceleration.

## Two hats, not one

MOND uses one a_0 for amplitude and for the radius where the law switches:

    r_M = sqrt(G M / a_0)  proportional to sqrt(M)

TAFA uses a_T for amplitude, and a universal pause r_p = 1/mu = 12.1 kpc for the fade. That is a second hat.

On SPARC, median r_M ~ 2.7 kpc (70% of galaxies have r_M < r_p/2). Dwarfs switch at ~0.3-1 kpc; TAFA still waits until 12 kpc. That is why the frozen-mu shape test failed on small disks.

Paper 1 already: putting H_0 into mu made SPARC worse. Same reason -- a universal length is the wrong switch.

## SPARC check (same Upsilon, same files as DM_shape_test)

Simple MOND interpolator g = g_N/2 + sqrt((g_N/2)^2 + g_N a).

All N=175 MAE mean dex:
- TAFA fade r_p=12.1: 0.232
- MOND a_0: 0.082
- MOND interpolator with a_T: 0.080

r_max >= 12.1 kpc:
- TAFA 0.180 / MOND 0.058 / a_T-MOND 0.058

Dwarfs M<3e9:
- TAFA 0.290 / MOND 0.109 / a_T-MOND 0.103

Giants M>3e10:
- TAFA 0.220 / MOND 0.051 / a_T-MOND 0.051

NGC 3198: TAFA 0.104, MOND 0.038. Using a_T instead of a_0 inside MOND interpolator does not matter; the mass-dependent r_M does.

## Floor

- a_T = Lambda^2 mu is recorded, not derived. Do not promote it to c H_0 or to the DE floor.
- The extra TAFA constant is not a better a_0. It is a fixed 12.1 kpc switch that MOND does not need and SPARC shape does not want.
- If the DM interpolator is upgraded, the honest one-constant version is MOND's: keep a_T or a_0, drop universal mu. That is a change to Floor_DM, not a derivation of mu.
