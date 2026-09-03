# Source of 0.9320 / 0.0759 / 12.28x

Tony Kawas / 3 September 2026

Repo: Quadratic-Mechanism-Lens
Notebook: Unification_attempt_DSector.ipynb
Downstream: DM_work.ipynb hardcodes the same two numbers as plot targets.

## Metric (not SPARC MAE)

nfw_score: synthetic NFW rs=20 kpc, densities normalized at 10 kpc, RMS of log10 residual on 5-80 kpc.
Rotation curves separately scaled to 220 km/s at 30-80 kpc.
Not a SPARC residual. Not Paper 1 dex MAE.

## 0.9320 frozen plateau

Cells ~25-28: kappa/lambda sweeps of the nonlinear galactic KG solver.
Stability guard: if phi explodes, freeze derivatives. Profile does not change. Score stuck at 0.9320 across the whole table. Failed scan, not a physical NFW floor.

## 0.0759 lambda^2 tuned Yukawa

Cell 29: fasting split phi=phi0+dphi, source S=Phi_grav * phi0 / lambda^2 (the slide).
Cell 33: scan lambda^2 in [1e-2, 1e8] with m_eff^2 fixed.
Best lambda^2 = 6.4281e-02, score 0.0759, M(<200 kpc)=2.23e8 Msun.
MW halo is ~1e12 Msun. Shape match after normalizing rho at 10 kpc; mass ~4000x too small.
Same cell notes Compton 0.70 kpc vs needed 10-100 kpc unless lambda^2 is scanned (free coupling).

## 12.28x

0.9320/0.0759 = frozen failed solver over a lambda-tuned log-density score vs analytic NFW.

Do not put 12.28x on either floor.
