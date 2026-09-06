# Waist integrator — first run

Tony Kawas / 6 September 2026. Result note. Not a paper.

Code: [`scripts/waist_integrator.py`](../scripts/waist_integrator.py).  
Parent: [`Waist.md`](Waist.md).

---

## Setup

Units \(M_{\mathrm{Pl}}=H_0=1\), \(\rho_{\mathrm{crit}}=3\), \(\Omega_m=0.31\), \(\Omega_\Lambda=0.69\).

- \(\alpha=\phi_0/f=1\) (Convention-2 angle).
- \(\Lambda^4=\rho_\Lambda/\tan^2(\alpha/2)\).
- Listed lapse, not fitted: \(N=\cos^2(\phi/2f)\).
- Cosmic kinetic \(\tfrac12(Np)^2\). Today set so \(w(0)\approx-0.98\) (\(p\) stored, not zero).
- No \(3H\dot\phi\) on the waist branch.
- Control: Baseline A Hubble damper, \(\dot\phi(0)=0\).
- Integrate **backward** from \(a=1\) to \(a=0.4\).

No third parameter. No retune of \(\Lambda,f\).

---

## Numbers

| \(f/M_{\mathrm{Pl}}\) | model | \(w(0)\) | \(w(0.3)\) | \(w(1)\) |
|---|---|---|---|---|
| 1 | waist | -0.980 | **-0.534** | +0.666 |
| 1 | 3H | -1.000 | +0.041 | +1.000 |
| 10 | waist | -0.980 | -0.964 | -0.935 |
| 10 | 3H | -1.000 | -0.984 | -0.607 |
| 30 | waist | -0.980 | -0.975 | -0.968 |
| 30 | 3H | -1.000 | -0.998 | -0.948 |

---

## Verdict

**Fail** at Convention 1 (\(f=M_{\mathrm{Pl}}\)).

The lapse is *better* than Hubble bleed at \(z=0.3\) (\(-0.53\) vs \(+0.04\)). It is not dark energy. Pass was \(w\approx-1\) through that window without a new letter.

At \(f=10\,M_{\mathrm{Pl}}\) the waist holds \(w\) through \(z=1\) better than \(3H\). That is the same super-Planckian hierarchy Storey B already required. The neck did not remove it.

\(z\sim 0.3\) stays derived only as the 5D \(\Delta y\) linear map on the DE floor. It is **not** derived from this lapse.

---

## What this does not license

- Fitting \(N(z)\) or a new exponent on \(\cos\).
- Declaring the waist a success because it beat \(3H\) at \(f=1\).
- Moving \(a_T\) or 12.1 kpc.
- Putting \(Q\) back.

Next, if any: the other listed \(N\) (warp \(e^{A(y(\phi))}\)) with the *same* two parameters. Same pass bar. Or stop.
