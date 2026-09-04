# Did the runs use mass, volume, composition as the papers require?

Tony Kawas / 4 September 2026

Paper 1 (Tafa_Galaxy_v5) is explicit.

## What the papers said

Mass:
    M_bar = Υ* L_[3.6] + 1.33 M_HI
    Υ* = 0.5. The 1.33 is helium. Not optional for the amplitude test.

Composition:
    Stellar-dominated (f_gas < 0.5, N=78) recover the quarter-power.
    Gas-dominated dwarfs sit systematically off.
    Cause: pause/reception node follows how the mass is *spread*, not only how much there is.
    Paper 2 was the gas-disk node shift: μ_eff(f_gas, Σ_eff). Not derived here; still an allowed patch.

Volume / coverage:
    Residuals vs R_eff were consistent with zero (p=0.496) for the *stellar size*.
    What mattered was completion r = v_last / v_∞ (anti-correlation −0.98): if the curve does not reach the outskirts, v_∞ is not being tested.

## What the recent runs actually did

SPARC v(r) (one-constant a_T):
    Used Vgas, Υ_d Vdisk, Υ_b Vbul at each radius. That *is* composition and the radial spread, inside g_N(r).
    Did *not* rebuild M_bar from L_[3.6] + 1.33 M_HI. Last-point enclosed baryons from the rotmod file instead.
    Did *not* apply the Paper 2 gas-node shift.
    Did *not* split the reported MAE on f_gas < 0.5 vs gas-rich.

LITTLE THINGS unique (amplitude):
    Used Oh+2015 Mgas + MstarK. Helium 1.33 was *not* added on top (Oh gas mass may or may not already include it).
    V(Rmax) was treated as if it were v_∞. Paper 1 says that is wrong when coverage is short. The worst LT objects (NGC 3738, UGC 8508, DDO 101) have Rmax ~ 2 kpc — exactly the completion-ratio failure mode.
    No V_bar(r), so volume/composition of the disk could not enter the interpolator.

## Verdict

Partly checked on SPARC curves (gas vs stars vs bulge in g_N).
Not checked as Paper 1 specified for amplitude (helium catalog mass) or as Paper 2 specified for gas disks (node shift).
The held-out dwarf misses are therefore mixed: some are the coverage effect the papers already named; some may be the gas-geometry effect Paper 2 was written for.

Do not treat those misses as a failed a_T until the completion cut and the helium/f_gas bookkeeping are applied.
