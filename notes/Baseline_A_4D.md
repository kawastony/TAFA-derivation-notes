# Baseline A — 4D TAFA

Tony Kawas / working note, 3 September 2026
Decision note. Not a paper.

Chosen path: stay 4D. Do not claim that TAFA calculates quantum gravity.

---

## Theory

Einstein gravity plus one canonical scalar:

\[
S=\int\mathrm{d}^4x\,\sqrt{-g}\left[
\frac{M_{\mathrm{Pl}}^2}{2}R
+\frac12(\partial\phi)^2
-V_A(\phi)
\right],
\qquad
V_A=\Lambda^4\tan^2\!\Bigl(\frac{\phi}{2f}\Bigr),
\quad
\lvert\phi\rvert<\pi f.
\]

Stress tensor and pressure: `notes/TAFA_stress_tensor_and_pressure.md`.

\[
T_{\mu\nu}
=\partial_\mu\phi\,\partial_\nu\phi
-g_{\mu\nu}\Bigl(\tfrac12(\partial\phi)^2+V_A\Bigr)
+(T_{\mu\nu}^{\mathrm{Q}}\ \text{only if a condensate is assumed}).
\]

Homogeneous:

\[
\rho=\tfrac12\dot\phi^2+V_A,
\qquad
p=\tfrac12\dot\phi^2-V_A.
\]

Near \(\phi=0\):

\[
m^2=\frac{\Lambda^4}{2f^2}.
\]

\(m\) is a derived combination of the two free parameters. It is not an independent input, and it is not a number in eV until \(\Lambda\) and \(f\) are fixed by data.

---

## Free data

| Symbol | Role |
|---|---|
| \(\Lambda\) | height of the TAFA well |
| \(f\) | field-space distance to the wall |
| \(\phi,\dot\phi\) at some \(t_i\) | cosmological initial data |
| optional coherent density \(n\) | only if galactic \(p_Q\) is used |

That is the parameter list. Nothing else is loaded from the Golden Gate dictionary.

---

## Kept (derived)

- TIFA cosine \(\to\) TAFA \(\tan^2\) by the Möbius identity (wall at \(\pm\pi f\))
- 4D Einstein as the infrared limit of Paper 38’s 5D reduction, without using \(11/72\)
- Law 4 as \(T_{\mu\nu}\), not as Newton-plus-slogan
- Observer factor \(Q\) retired

---

## Dropped as claims

- TAFA calculates quantum gravity
- Type IIB / 10D as a completed parent
- \(A'=11/72\) as an eigenvalue
- \(R=1.5156\) as a warped-volume Jacobian
- \(35^\circ\) as a derived cone angle
- fitted \(\Lambda_{\mathrm{eff}}(a)\) or \(f_{\mathrm{quantum}}(a)\) as geometry
- fear density / collapse bias

Those items may stay in the paper stack as history. They are not part of Baseline A.

---

## What 5D work is now for

The consistent 5D integration showed a finite slab and a wall singularity, not a slope eigenvalue. Under A, that result is a *negative theorem*: 5D does not mint 4D constants. It is not a licence to put 10D language back into the 4D theory.

---

## What “success” looks like from here

1. Cosmology: integrate the homogeneous TAFA scalar with \(\Lambda,f\) chosen once, compare \(w(z)\) and \(H(z)\) to data. No extra fluid.
2. If cores are still claimed: write \(p_Q\) with \(m^2=\Lambda^4/(2f^2)\) using the *same* \(\Lambda,f\) as cosmology. If that fails, drop the galactic reading rather than add a second mass.
3. Rewrite any “11 puzzles” answers that used \(Q\) so they either follow from this action or are withdrawn.

No Paper 50. No new Golden Gate. Next work that still belongs in this repo is a 4D homogeneous integrator with two parameters, or silence.
