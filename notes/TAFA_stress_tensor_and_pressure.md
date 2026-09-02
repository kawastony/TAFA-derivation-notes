# TAFA stress tensor and pressure

Tony Kawas / working note, 3 September 2026
Status: research note. Companion to `Forced_vs_Free_TAFA_bridges.md`.
Not a paper. No observer factor \(Q\). No fitted \(\Lambda_{\mathrm{eff}}(a)\).

This note writes Law 4 as a stress tensor. Pressure is a component of that tensor, read in four regimes. The mass \(m\) is left as a symbol.

---

## 0. Action (only input)

Canonical TAFA scalar in 4D Einstein frame:

\[
S=\int\mathrm{d}^4x\,\sqrt{-g}\left[
\frac{M_{\mathrm{Pl}}^2}{2}R
+\frac12 g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi
-V_A(\phi)
\right],
\qquad
V_A(\phi)=\Lambda^4\tan^2\!\Bigl(\frac{\phi}{2f}\Bigr),
\quad
\lvert\phi\rvert<\pi f.
\]

No second fluid. No fear density. Gravity is the Einstein-frame reduction of Paper 38.

---

## 1. Classical stress tensor

Varying the matter part with respect to \(g^{\mu\nu}\) gives

\[
T_{\mu\nu}
=\partial_\mu\phi\,\partial_\nu\phi
-g_{\mu\nu}\Bigl(\tfrac12(\partial\phi)^2+V_A(\phi)\Bigr).
\]

Einstein’s equation is then

\[
G_{\mu\nu}=8\pi G\,T_{\mu\nu}.
\]

That is Law 4 as geometry-plus-source. Newton 1–3 are already inside geodesics and \(\nabla^\mu T_{\mu\nu}=0\).

If the field is a single coherent infrared mode, an extra piece \(T_{\mu\nu}^{\mathrm{Q}}\) is present. It is derived in §3. If the field is a homogeneous classical fluid, \(T_{\mu\nu}^{\mathrm{Q}}=0\).

---

## 2. Homogeneous cosmology (no spatial gradients)

Take \(\phi=\phi(t)\) on FLRW. Then

\[
\rho=\tfrac12\dot\phi^2+V_A,
\qquad
p=\tfrac12\dot\phi^2-V_A,
\qquad
w=\frac{p}{\rho}=\frac{\tfrac12\dot\phi^2-V_A}{\tfrac12\dot\phi^2+V_A}.
\]

**What this pressure manifests as**

| Regime | Kinematics | \(w\) | Observed name |
|---|---|---|---|
| Hubble-frozen near \(\phi=0\) | \(\dot\phi\approx0\), \(V_A\approx(\Lambda^4/4f^2)\phi^2\) small | \(\to-1\) | late-time acceleration |
| Slow roll | \(\tfrac12\dot\phi^2\ll V_A\) | close to \(-1\) | inflationary / thawing DE |
| Kinetic domination | \(\tfrac12\dot\phi^2\gg V_A\) | \(\to+1\) | stiff fluid (only if the field actually runs) |

This is ordinary scalar pressure. TIFA used the same formulae with a cosine. TAFA changes the domain, not the definition of \(p\).

Near the vacuum the mass jet is

\[
V_A=\frac{\Lambda^4}{4f^2}\phi^2+\mathrm{O}(\phi^4)
=\tfrac12 m^2\phi^2+\mathrm{O}(\phi^4),
\qquad
m^2=\frac{\Lambda^4}{2f^2}.
\]

The symbol \(m\) is defined by that jet. It is not inserted from outside in this note.

---

## 3. Condensate / galactic regime (gradients, one occupied mode)

Write a complex order parameter for the occupied mode,

\[
\psi=\sqrt{n}\,e^{iS/\hbar},
\]

with \(n\) the number density of that mode and \(S\) the phase. The Madelung map from a non-relativistic limit of the same scalar produces an extra stress, the quantum pressure

\[
p_Q=\frac{\hbar^2}{2m^2}\,n\,\frac{\nabla^2\sqrt{n}}{\sqrt{n}}.
\]

In the weak-field, slow limit the Einstein constraint becomes

\[
\nabla^2\Phi=4\pi G\,\rho_b
+\frac{\hbar^2}{2m^2}\nabla^2\Bigl(\frac{\nabla^2\sqrt{n}}{\sqrt{n}}\Bigr).
\]

The first term is baryons. The second term is \(T_{\mu\nu}^{\mathrm{Q}}\), not a second substance.

**What this pressure manifests as**

- a healing / Jeans length \(\xi=\hbar/\sqrt{2m\,g\,n}\) once a self-coupling \(g\) is fixed by the \(\phi^4\) jet of \(V_A\)
- constant-density cores instead of cusps
- a floor under collapse at the scale set by \(\xi\)

This is the only regime in which TAFA pressure looks like “dark matter.” It is the same field that, when homogeneous and frozen, looked like dark energy.

The self-coupling from the small-field expansion of \(V_A\) is

\[
V_A=\tfrac12 m^2\phi^2+\frac{\lambda}{4}\phi^4+\mathrm{O}(\phi^6),
\qquad
\lambda=\frac{\Lambda^4}{6f^4}=\frac{m^2}{3f^2}.
\]

Then \(g\) in Gross–Pitaevskii is fixed by \(\lambda\) and the non-relativistic reduction, once that reduction is written carefully. This note records the identification. It does not complete the non-relativistic limit as a theorem.

**Not claimed.** Magnetic / Meissner pressure. That requires a dynamical gauge field, which is not in the action above.

---

## 4. Wall (not a fluid)

The domain is \(\lvert\phi\rvert<\pi f\). As \(\phi\to\pm\pi f\),

\[
V_A\to+\infty.
\]

A naive homogeneous reading would say \(w\to-1\) with unbounded \(\rho\). That reading is discarded.

The wall is an inextendible boundary of field space. A geodesic in \(\phi\) reaches it in finite field distance. The classical Cauchy problem for \(\phi\) either stays inside the interval or ends. There is no derived matching rule that turns the wall into a bounce, a reflecting barrier, or an infinite dark-energy pulse.

Pressure language stops at the wall. Geometry language takes over: the domain is incomplete.

---

## 5. Warp residual (5D \(\to\) 4D)

Paper 38 reduces the warped cone to 4D Einstein plus corrections of order \(\varepsilon_{\mathrm{cone}}\). Those corrections are an anisotropic 5D stress, seen in 4D as a small extra source. They may be written as an effective pressure in Friedmann form after \(A(y)\) is solved.

This note does not compute that pressure. That is Open B in the companion note. Until \(A(y)\) is solved, warp pressure is a slot, not a number.

It is not the same object as \(p\) in §2 or \(p_Q\) in §3.

---

## 6. Dictionary

| Context | Object in \(T_{\mu\nu}\) | Manifests as | Status |
|---|---|---|---|
| Homogeneous cosmos | \(p=\tfrac12\dot\phi^2-V_A\) | acceleration if frozen | derived from the action |
| Galaxy / core | \(p_Q\) from Madelung | cores, healing length | derived in form; \(m,g,n\) not numerically fixed |
| Wall | none (boundary) | end of classical description | derived as incompleteness |
| Extra dimension | \(\mathcal{O}(\varepsilon_{\mathrm{cone}})\) stress | small geometric Friedmann correction | slot until Open B |
| Observer / fear density | — | — | not in the theory |
| Fitted \(\Lambda_{\mathrm{eff}}(a)\) | — | — | not \(T_{\mu\nu}\) |

---

## 7. What is still not derived

- \(m\) as a number in eV. Here \(m^2=\Lambda^4/(2f^2)\). \(\Lambda\) and \(f\) remain free until Open B and Open A.
- The non-relativistic reduction as a fully controlled limit (occupation number, frame, Hubble vs healing scale).
- Warp pressure as a computed \(\varepsilon_{\mathrm{cone}}\).
- Opening angle \(35^\circ\). Irrelevant to this note.

---

## 8. One-sentence verdict

TAFA handles pressure by reading one stress tensor at four resolutions: potential pressure when the field is smooth, quantum pressure when it is a coherent mode, no pressure at the wall, and a residual geometric stress from the warp once that warp is solved.
