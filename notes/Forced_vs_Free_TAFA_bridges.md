# Forced vs Free: a closure note on the TAFA bridges

Tony Kawas / working note, 3 September 2026
Status: research note, not a claim of UV completion.

This note does the job that was still open: separate what the geometry *forces* from what was still *chosen*. It uses only the objects already in the TAFA / TIFA / 5D-cone papers. No new substances. No observer quality \(Q\). No probability postulate.

A derivation here means: axioms \(\Rightarrow\) unique next object, or a named obstruction.

---

## 0. Dictionary

| Name | Potential | Domain |
|---|---|---|
| TIFA | \(V_T(\phi)=\Lambda^4\bigl(1-\cos(\phi/f)\bigr)\) | \(\phi\in\mathbb{R}\), periodic |
| TAFA | \(V_A(\phi)=\Lambda^4\tan^2(\phi/2f)\) | \(\lvert\phi\rvert<\pi f\), walls at \(\pm\pi f\) |

Warped cone metric (Paper 38):

\[
\mathrm{d}s_5^2 = e^{2A(y)}\,g_{\mu\nu}(x)\,\mathrm{d}x^\mu\mathrm{d}x^\nu + \mathrm{d}y^2.
\]

---

## 1. Axioms (minimal set)

These are the only inputs used below. Everything else must be earned.

**A1 (Evenness).** The effective potential is even: \(V(-\phi)=V(\phi)\).  
**A2 (Vacuum).** There is a local minimum at \(\phi=0\) with \(V(0)=0\) and \(V''(0)>0\).  
**A3 (Parent periodicity).** There exists a smooth, even, \(2\pi f\)-periodic parent potential \(U(\phi)\) whose only harmonic is the first: \(U(\phi)=c_0-c_1\cos(\phi/f)\), \(c_1>0\).  
**A4 (Wall).** The physical field domain is the open interval on which the parent can be inverted to a complete Riemannian metric on field space. The parent maximum is sent to an inextendible boundary.  
**A5 (Canonical kinetics).** The 4D scalar is canonical: \(\mathcal{L}=\frac12(\partial\phi)^2-V(\phi)\).  
**A6 (Warped product).** Gravity is the 4D Einstein-frame reduction of the 5D warped product in Paper 38, at control parameter \(\varepsilon_{\mathrm{cone}}\to 0\).

A3 is the strongest axiom. It is the TIFA parent. If A3 is dropped, uniqueness of \(\tan^2\) fails.

---

## 2. Lemma: TIFA \(\leftrightarrow\) TAFA is a Möbius map, not a new field

**Lemma 1.** On \(\lvert\phi\rvert<\pi f\),

\[
\tan^2\!\Bigl(\frac{\phi}{2f}\Bigr)
=\frac{1-\cos(\phi/f)}{1+\cos(\phi/f)}.
\]

Proof. Set \(\theta=\phi/f\). The half-angle identity \(\tan^2(\theta/2)=(1-\cos\theta)/(1+\cos\theta)\) is elementary.

**Corollary 1.1.** If \(V_T=\Lambda^4(1-\cos(\phi/f))\), then

\[
\frac{V_A}{\Lambda^4}=\frac{V_T}{2\Lambda^4-V_T},
\qquad
V_A=\Lambda^4\,\frac{V_T}{2\Lambda^4-V_T}.
\]

This is the unique fractional-linear map \(M(u)=u/(2\Lambda^4-u)\) that sends

- the TIFA vacuum \(V_T=0\) to the TAFA vacuum \(V_A=0\),
- the TIFA hilltop \(V_T=2\Lambda^4\) to a wall \(V_A=\infty\).

**What this forces.** TAFA is not an unrelated potential. It is TIFA with the hilltop compactified to a boundary. That is the geometric replacement of “the field can sit on a plateau with small probability of rolling” by “the field cannot cross the wall.”

**What this does not force.** It does not yet force A3. Cosine is *assumed* as the unique 1-harmonic parent.

---

## 3. Theorem: uniqueness of \(\tan^2\) given A1–A4

**Theorem 2 (wall uniqueness).** Assume A1–A4. Then, up to the overall scale \(\Lambda^4\) and the period \(f\),

\[
V(\phi)=\Lambda^4\tan^2\!\Bigl(\frac{\phi}{2f}\Bigr)
\]

is the unique potential on the physical domain.

Proof sketch.

1. A3 fixes the parent: \(U(\phi)=\Lambda^4\bigl(1-\cos(\phi/f)\bigr)\) after using A2 to set the constant so that \(U(0)=0\) and \(U_{\max}=2\Lambda^4\).
2. A4 requires a strictly increasing map \(M:[0,U_{\max})\to[0,\infty)\) with \(M(0)=0\) and \(M(u)\to\infty\) as \(u\to U_{\max}\).
3. A5 plus the requirement that the field-space metric remain canonical forbids a nontrivial field redefinition \(\phi\to\psi(\phi)\) other than a constant rescaling already absorbed into \(f\).
4. The unique Möbius map \(\mathbb{RP}^1\to\mathbb{RP}^1\) sending \(\{0,U_{\max}\}\) to \(\{0,\infty\}\) and preserving the vacuum quadratic jet up to scale is \(M(u)=u/(U_{\max}-u)\). Substituting \(U_{\max}=2\Lambda^4\) yields Corollary 1.1, hence \(V=V_A\).

**Status.** This is a derivation *conditional on A3*. The cosine parent is the remaining choice. A serious next paper must replace A3 by a statement such as: “the only closed 1-form on the circle that is even and has a single pair of critical points is \(\mathrm{d}U\propto\sin(\phi/f)\,\mathrm{d}\phi\).” That is true on \(S^1\) for Morse functions with exactly two critical points, up to diffeomorphism; the harmonic representative is cosine. That upgrade is short and should be written as a standalone lemma.

---

## 4. Lemma: quadratic mass matching (inflation \(\leftrightarrow\) late time is *not* two fields)

Near \(\phi=0\),

\[
V_T=\Lambda^4\cdot\frac{\phi^2}{2f^2}+\mathrm{O}(\phi^4),
\qquad
V_A=\Lambda^4\cdot\frac{\phi^2}{4f^2}+\mathrm{O}(\phi^4).
\]

Same operator, different convention for \(f\). Absorbing \(f_A=f_T/\sqrt{2}\) makes the masses identical. Late-time dark energy and the bottom of the inflationary well are one quadratic jet.

**What this forces.** You do not need two fields to talk about two epochs. You need two *locations* on one jet, or two values of the modulus that sets \(f\).

**What this does not force.** The jump \(f=7M_{\mathrm{Pl}}\to f_{\mathrm{eff}}=0.5M_{\mathrm{Pl}}\) in the TIFA publication notebook. That jump is a modulus vev, not a theorem. Name it:

**Open Theorem A (modulus map).** Derive \(f_{\mathrm{IR}}/f_{\mathrm{UV}}\) from the warp integral

\[
\frac{f_{\mathrm{IR}}}{f_{\mathrm{UV}}}=\exp\!\bigl(A(y_{\mathrm{IR}})-A(y_{\mathrm{UV}})\bigr)
\]

with \(A(y)\) solved, not chosen. Until that ODE is solved, the two-scale story is a matching condition.

---

## 5. Lemma: Einstein limit from the cone (this bridge *is* a derivation)

From A6, the 5D Einstein–Hilbert term reduces as in Paper 38:

\[
M_{\mathrm{Pl}}^2=M_5^3\int\mathrm{d}y\,e^{2A(y)}\,\mathcal{W}_{\mathrm{cone}}(y).
\]

If \(\varepsilon_{\mathrm{cone}}\to 0\),

\[
G_{\mu\nu}=\frac{1}{M_{\mathrm{Pl}}^2}T_{\mu\nu}^{\mathrm{eff}}.
\]

This is the standard warped-product reduction. It is a derivation of 4D GR as an *infrared limit*, not a derivation of the warp function \(A(y)\).

**Forced:** GR is what a 4D observer sees when cone corrections are small.  
**Free:** \(A(y)\). Paper 38 writes both a log-soft law \(A=A_0+\alpha\ln(1+y/Y_c)\) and a constant slope \(A'=11/72\). Those cannot both be fundamental. Pick one and derive the other as an approximation.

**Open Theorem B (warp slope).** Show that the radial Poisson problem \(\nabla^2 h \propto \lvert G_3\rvert^2\) with the TAFA cone boundary condition has a unique normalisable mode, and that this mode gives one number for \(A'\). Do not insert \(11/72\). Compute it. If the number is not \(11/72\), keep the computed number and drop the slogan.

The same applies to \(R=1.5156\). That is a normalisation integral. Evaluate the integral from the solved \(A(y)\) and \(\mathcal{W}_{\mathrm{cone}}\). If the integral is not \(1.5156\), the prediction package that uses \(R=1.5156\) is a calibration, not a derivation.

---

## 6. What “replace probability and the observer” actually means, derived

Once Theorem 2 is granted, the field domain is the open interval \((-\pi f,\pi f)\). The metric on field space,

\[
\mathrm{d}s_\phi^2=\mathrm{d}\phi^2,
\]

is incomplete: geodesics reach the wall in finite field distance.

**Lemma 3 (no residual Born rule).** There is no extra collapse map in the dynamics. The Cauchy problem for \(\phi\) on the open interval either

- remains inside the interval for all finite time, or
- hits the wall in finite time and the classical description ends.

That is a geometric cutoff, not a probability. It *removes* the observer factor \(Q\) from \(\Psi_{\mathrm{TOE}}\). It does *not* derive the Born rule from the cone. Anyone who still wants quantum measurement statistics must add a new axiom. TAFA’s claim should be narrowed to:

> Measurement is not a fifth force in the action. Incomplete field-space geometry already bounds the classical domain.

That sentence is derivable. “Geometry produces the Born rule” is not, from A1–A6.

---

## 7. Dark matter / dark energy: what is derived

From A5 and Theorem 2, the late-time fluid is the TAFA scalar plus baryons. Then

\[
w=\frac{\tfrac12\dot\phi^2-V}{\tfrac12\dot\phi^2+V}.
\]

Near the vacuum, \(w\to-1\) if the field is frozen by Hubble friction; \(w\) departs from \(-1\) when the field rolls. That is derived.

It does **not** derive \(\Omega_{\mathrm{DE}}\) or \(H_0\). Those still enter as boundary data unless Open Theorem A plus the warp integral fix \(\Lambda^4\) in Planck units.

Galaxy-scale formula of the type \(V_{\mathrm{flat}}^4=G\,R\,m_1^2 M_b\) is a *derived shape* (Tully–Fisher slope \(1/4\)) only after \(R\) and \(m_1\) are fixed by Open Theorem B. Until then it is MOND with a TAFA name.

Narrow the claim:

- **Derived:** one scalar, one wall, \(w(z)\) from the action, GR as IR limit.
- **Not derived:** numerical values \(35^\circ\), \(11/72\), \(1.5156\), \(m_1\sim10^{-22}\,\mathrm{eV}\), \(f_{\mathrm{UV}}/f_{\mathrm{IR}}\).

---

## 8. The \(35^\circ\) cone

Let the wall \(\phi=\pm\pi f\) be mapped to a spatial generators of a cone in the extra-dimensional plane \((r,\theta)\). An opening half-angle \(\alpha\) is a boundary condition, not an output, until it is a critical point of the cone action \(\mathcal{L}_{\mathrm{cone}}\).

**Open Theorem C (angle).** Show

\[
\frac{\delta S_{\mathrm{cone}}}{\delta\alpha}=0 \quad\Longrightarrow\quad \alpha=\alpha_\star
\]

with \(\alpha_\star\) computed. If \(\alpha_\star\neq 35^\circ\), keep \(\alpha_\star\). \(35^\circ\) may be a convenient observational proxy (near \(\pi/5=36^\circ\)); it is not currently an eigenvalue in the papers.

---

## 9. Scoreboard

| Bridge | Status after this note |
|---|---|
| TIFA cosine \(\to\) TAFA tangent | **Derived** as the unique wall compactification of the 1-harmonic parent (Thm 2) |
| One field for inflation and late DE | **Derived** at the level of the quadratic jet; scale jump not derived (Open A) |
| 5D cone \(\to\) 4D Einstein | **Derived** as IR limit (Lemma of §5); warp function not derived (Open B) |
| Geometry replaces \(Q\) / collapse postulate | **Derived** as domain incompleteness (Lemma 3); Born rule not derived |
| Geometry replaces DM/DE substances | **Partially derived** as a scalar + warp correction; numbers still calibrated |
| \(35^\circ\), \(11/72\), \(R=1.5156\) | **Not derived.** Named open theorems B and C |

---

## 10. What a serious next week of work is

Do not write Paper 50. Prove three statements, in this order.

1. Upgrade A3 to a Morse lemma on \(S^1\) so Theorem 2 does not assume cosine by hand.
2. Solve Open Theorem B: one ODE for \(A(y)\), one number for \(A'\) and for \(R\). Throw away whichever of \(11/72\) or \(1.5156\) fails the integral.
3. Solve Open Theorem A: \(f_{\mathrm{IR}}/f_{\mathrm{UV}}\) from that same \(A(y)\). Then \(\Lambda^4\) is no longer a fit to \(\Omega_{\mathrm{DE}}\); it is a prediction, and the model can die.

Until (2) and (3) exist, the bridges are constructed. After (2) and (3), they are derivations.

---

## 11. One-sentence verdict

TAFA is the unique wall-compactification of TIFA, and 4D Einstein gravity is its infrared limit; the numerical engine (\(35^\circ\), \(11/72\), \(R\), \(f\)-jump) is still calibration, and that is the work that remains.
