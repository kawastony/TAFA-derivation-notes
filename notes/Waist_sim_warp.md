# Waist integrator — warp lapse

Tony Kawas / 6 September 2026. Result note. Not a paper.

Second listed \(N\) from [Waist.md](Waist.md). First run: [Waist_sim.md](Waist_sim.md).

---

## Setup

Same two parameters as the cos² run. Same pass bar.

From the 5D TAFA integration ([OpenB_TAFA_5D_integration.md](OpenB_TAFA_5D_integration.md)):

$$
A\to -\tfrac12
\quad(\Lambda=f=1\ \text{units}),
\qquad
A'\ \text{diverges at the wall}.
$$

Map, not fitted:

$$
A(\phi)=A_{\mathrm{wall}}\left(\frac{\phi}{\pi f}\right)^2,
\qquad
A_{\mathrm{wall}}=-\tfrac12,
\qquad
N=e^{A(\phi)}.
$$

Tip \(A=0\), \(N=1\). Wall \(N=e^{-1/2}\approx 0.61\). Today (\(\alpha=1\)) \(N\approx 0.95\). The warp factor barely moves on the cosmological trajectory.

---

## Numbers

| \(f/M_{\mathrm{Pl}}\) | \(w(0)\) | \(w(0.3)\) | \(w(1)\) |
|---|---|---|---|
| 1 warp | -0.980 | **-0.297** | +0.818 |
| 1 cos² (prev) | -0.980 | -0.534 | +0.666 |
| 1 3H | -1.000 | +0.041 | +1.000 |
| 10 warp | -0.980 | -0.954 | -0.905 |
| 30 warp | -0.980 | -0.973 | -0.961 |

---

## Verdict

**Fail** at \(f=M_{\mathrm{Pl}}\). Worse than the first listed lapse.

Reason: the 5D result that *is* derived is a finite \(A\), not a small \(N\). A clock factor that only drops to \(0.61\) at the wall cannot hide kinetic energy at \(z\sim 0.3\) when \(f\) is Planckian.

The hierarchy \(f\gtrsim 10\,M_{\mathrm{Pl}}\) is still required. Both listed \(N\)s have been used. Neither earns \(z\sim 0.3\) as a waist.

That tick stays the 5D \(\Delta y\) linear map only.

---

## Stop rule

No third \(N\). Fitting an exponent so that \(N\) is tiny today would be a new parameter. Both listed candidates are in this repo. The waist remains geometry; it is not a DE calculator at Convention 1.
