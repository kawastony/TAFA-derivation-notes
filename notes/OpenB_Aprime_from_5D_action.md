# Open B — \(A''\) from the 5D action

Tony Kawas / working note, 3 September 2026
Not a paper. Derivation only. Companion to `OpenB_first_integration.md`.

---

## 0. Action and metric (Paper 38)

Take the Einstein-frame 5D action used in Paper 38, one scalar, units \(M_5^3=1\):

\[
S_5=\int\mathrm{d}^5x\,\sqrt{-G}\left[
\frac12 R_5
-\frac12 G^{MN}\partial_M\phi\,\partial_N\phi
-V(\phi)
\right].
\]

Warped-product ansatz (same paper):

\[
\mathrm{d}s_5^2
=e^{2A(y)}\,\eta_{\mu\nu}\,\mathrm{d}x^\mu\mathrm{d}x^\nu
+\mathrm{d}y^2.
\]

\(\phi=\phi(y)\) only. Four-dimensional slices are Minkowski so that the reduction is the vacuum Einstein limit. A cosmological 4D metric adds Hubble terms; it does not change the sign of \(A''\) derived below.

Einstein equation from this action:

\[
G_{MN}=T_{MN},
\qquad
T_{MN}
=\partial_M\phi\,\partial_N\phi
-G_{MN}\Bigl(\tfrac12(\partial\phi)^2+V\Bigr).
\]

Scalar equation:

\[
\Box_5\phi=V'(\phi).
\]

---

## 1. Curvature of the warped product

Christoffel symbols that are not zero:

\[
\Gamma^\mu{}_{\nu y}=A'\,\delta^\mu_\nu,
\qquad
\Gamma^y{}_{\mu\nu}=-A'\,e^{2A}\,\eta_{\mu\nu}.
\]

Ricci:

\[
R_{\mu\nu}=-e^{2A}\bigl(A''+4(A')^2\bigr)\,\eta_{\mu\nu},
\qquad
R_{yy}=-4\bigl(A''+(A')^2\bigr).
\]

Ricci scalar:

\[
R=-8A''-20(A')^2.
\]

Einstein tensor:

\[
G_{\mu\nu}=e^{2A}\bigl(3A''+6(A')^2\bigr)\,\eta_{\mu\nu},
\qquad
G_{yy}=6(A')^2.
\]

---

## 2. Stress tensor of \(\phi(y)\)

\[
(\partial\phi)^2=(\phi')^2,
\qquad
T_{\mu\nu}=-e^{2A}\bigl(\tfrac12(\phi')^2+V\bigr)\,\eta_{\mu\nu},
\qquad
T_{yy}=\tfrac12(\phi')^2-V.
\]

---

## 3. Einstein equations

**\(yy\) constraint (Hamiltonian constraint):**

\[
6(A')^2=\tfrac12(\phi')^2-V
\qquad\text{i.e.}\qquad
V=\tfrac12(\phi')^2-6(A')^2.
\tag{C}
\]

**\(\mu\nu\) equation:**

\[
3A''+6(A')^2=-\tfrac12(\phi')^2-V.
\tag{μ}
\]

Eliminate \(V\) with (C):

\[
3A''+6(A')^2
=-\tfrac12(\phi')^2-\bigl(\tfrac12(\phi')^2-6(A')^2\bigr)
=-(\phi')^2+6(A')^2.
\]

\[
3A''=-(\phi')^2
\qquad\Rightarrow\qquad
\boxed{A''=-\frac13(\phi')^2}.
\tag{A}
\]

The potential has cancelled. Equation (A) is geometric: warp curvature is sourced only by the scalar kinetic term, and the sign is fixed by Einstein's equation with the Paper 38 action.

This is Paper 49's first equation, with \(s=-1\). The sign in the writeup was not a typo.

---

## 4. Scalar equation

\[
\sqrt{-G}=e^{4A},
\qquad
\Box_5\phi=e^{-4A}\partial_y\bigl(e^{4A}\phi'\bigr)
=\phi''+4A'\phi'.
\]

\[
\boxed{\phi''+4A'\phi'=V'(\phi)}.
\tag{φ}
\]

If \(V=V_0 e^{\lambda\phi}\), then \(V'=\lambda V_0 e^{\lambda\phi}\), which is Paper 49's second equation.

---

## 5. Consistency: (A) follows from (C) and (φ)

Differentiate (C) and use (φ). You recover (A). So a correct integrator uses

- the constraint (C) as an initial-value condition and a monitor, and
- either (A) or (φ) as the evolution,

not two unconstrained second-order equations with independent initial data.

---

## 6. What this does to Paper 49's origin data

Paper 49 sets

\[
A'(0)=0,\qquad \phi'(0)=0
\]

and calls \(y=0\) a regular point. Put that into (C):

\[
V\bigl(\phi(0)\bigr)=0.
\]

An exponential \(V=V_0 e^{\lambda\phi}\) with \(V_0\neq 0\) is never zero. The printed boundary data and the printed potential are mutually inconsistent.

That is why the first integration never reached \(+11/72\):

- (A) forces \(A'\le 0\) once \(A'(0)=0\), so \(+11/72\) is unreachable;
- (C) forbids the origin data themselves unless \(V(\phi_0)=0\).

A shooting method that still reports \(A'(120)=11/72\) is not solving this action.

---

## 7. What a consistent 5D problem looks like

Pick one of the following. Do not mix them.

**Tip with vanishing potential.** Keep \(A'(0)=\phi'(0)=0\). Then \(V(\phi_0)=0\). An exponential cannot do that. The TAFA vacuum can: \(V_A(0)=0\).

**No tip.** Extra dimension is an interval or a half-line with \(A'(y_0)\) already nonzero. Then (C) fixes \(A'(y_0)\) from \(\phi'(y_0)\) and \(V(\phi_0)\). The slope at the UV end is data, not an output, unless a second boundary (IR regularity, finite volume) quantises it.

**Brane jump.** Israel conditions allow \(A'\) to jump. Then \(A''\) has a delta. The bulk equation remains (A). The slogan \(11/72\) would have to come from the jump or from the IR boundary, not from a smooth origin.

Finite warped volume,

\[
\int\mathrm{d}y\,e^{2A(y)}\,\mathcal{W}(y)<\infty,
\]

is a filter on solutions of (A)+(C)+(φ). It is not a licence to insert \(R=1.5156\).

---

## 8. What is now derived vs still open

| Statement | Status |
|---|---|
| \(A''=-\phi'^2/3\) from Paper 38's action | **Derived** |
| \(\phi''+4A'\phi'=V'\) | **Derived** |
| Constraint \(6A'^2=\phi'^2/2-V\) | **Derived** |
| Regular origin \(\Rightarrow V(\phi_0)=0\) | **Derived** |
| Exponential potential + regular origin | **Inconsistent** |
| \(A'\to 11/72\) from this action | **Not derived.** Unreachable from the printed origin data |
| \(R=1.5156\) | **Not derived** |

---

## 9. Next computation, if any

Do not integrate Paper 49 again. Either

1. put the TAFA potential in 5D, with a tip at \(\phi=0\) where \(V_A=0\), so (C) is satisfied, or
2. drop the tip and treat \(A'(y_{\mathrm{UV}})\) as fixed by (C), then impose finite volume at the IR.

Option 1 stays inside TAFA: the same field whose 4D stress tensor we already wrote. That is the correct 5D problem for Open B after this derivation.
