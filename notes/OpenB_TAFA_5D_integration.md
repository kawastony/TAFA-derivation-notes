# Open B — 5D integration with the TAFA potential

Tony Kawas / working note, 3 September 2026
Not a paper. Consistent problem from `OpenB_Aprime_from_5D_action.md`.
No \(11/72\) target. No exponential potential.

---

## 0. Problem that is actually posed by the action

Bulk equations from Paper 38’s action:

\[
A''=-\frac13(\phi')^2,
\qquad
\phi''+4A'\phi'=V_A'(\phi),
\qquad
6(A')^2=\tfrac12(\phi')^2-V_A,
\]

\[
V_A=\Lambda^4\tan^2\!\Bigl(\frac{\phi}{2f}\Bigr),
\qquad
\lvert\phi\rvert<\pi f.
\]

Exact tip \(\phi=A'= \phi'=0\) is an equilibrium: \(V_A(0)=0\), everything stays there. That solution has no warp. Nontrivial solutions start a small, constraint-legal distance away from the tip.

**Family 1 (used below).** \(A'(0)=0\), \(\phi(0)=\varepsilon\), \(\phi'(0)=+\sqrt{2V_A(\varepsilon)}\). Constraint holds at \(y=0\).

Independent variable is \(\phi\), so the constraint is built in:

\[
\frac{\mathrm{d}A}{\mathrm{d}\phi}=\frac{A'}{\phi'},
\qquad
\frac{\mathrm{d}A'}{\mathrm{d}\phi}=-\frac{\phi'}{3},
\qquad
\phi'=\sqrt{12(A')^2+2V_A}.
\]

Default units \(\Lambda=f=1\) unless stated. Wall cutoff \(\phi=\pi-\delta\).

---

## 1. What happens

The field runs from the near-vacuum start to the wall in **finite** extra-dimension distance \(y\). Every Family-1 run hits the wall. There is no infinite throat and no constant-slope attractor.

Two numbers behave differently as the cutoff \(\delta\to 0\):

| Quantity | As \(\delta\to 0\), \(\varepsilon\to 0\), \(\Lambda=f=1\) |
|---|---|
| \(A\) at the wall | **converges**, \(A\to -1/2\) |
| \(A'\) at the wall | **diverges**, \(\Delta A'\approx -2.171\) per decade of \(\delta\) |
| extra-dimension length \(y_{\mathrm{wall}}\) | finite, grows as \(\varepsilon\) shrinks |
| warped volume \(\int e^{2A}\,\mathrm{d}y\) | finite |

Cutoff check at \(\varepsilon=10^{-3}\), \(\Lambda=f=1\):

| \(\delta\) | \(A_{\mathrm{end}}\) | \(A'_{\mathrm{end}}\) |
|---|---|---|
| \(10^{-2}\) | \(-0.50255\) | \(-6.21\) |
| \(10^{-3}\) | \(-0.50267\) | \(-8.38\) |
| \(10^{-4}\) | \(-0.50267\) | \(-10.55\) |
| \(10^{-5}\) | \(-0.50267\) | \(-12.72\) |
| \(10^{-6}\) | \(-0.50267\) | \(-14.90\) |
| \(10^{-7}\) | \(-0.50267\) | \(-17.07\) |

\(A'\) is not an eigenvalue. It is a wall singularity. \(A\) itself, and therefore the metric factor \(e^{2A}\), stay finite. For \(\Lambda=f=1\) that factor at the wall is \(e^{2A}\to e^{-1}\).

---

## 2. What does *not* appear

\(A'=11/72\approx +0.153\) does not appear. Family 1 has \(A'\le 0\) everywhere. The wall value of \(A'\) is large and negative and cutoff-dependent.

\(R=1.5156\) does not appear. The volume integral is finite and depends on how close to the tip you start.

Changing \(\Lambda\) at fixed \(f=1\) leaves \(A_{\mathrm{end}}\) unchanged and rescales \(A'\). Changing \(f\) changes \(A_{\mathrm{end}}\). So even the clean \(-1/2\) is a statement in the unit chart \(\Lambda=f=1\), not a universal 4D prediction until the scaling is written out.

---

## 3. What this means

The consistent 5D TAFA problem is a **finite slab that ends on the field-space wall**, not a Klebanov–Strassler-style throat with a constant warp slope.

- Tip: TAFA vacuum, legal because \(V_A=0\).
- Interior: field runs, warp factor falls to a finite value.
- IR end: geometric singularity in \(A'\), finite \(A\), finite volume.

That is enough to have a finite 4D Planck integral. It is not enough to mint \(11/72\) or a unique \(m\) in eV. The remaining free data are \(\Lambda\), \(f\), and how close to the exact tip the slice begins (the \(\varepsilon\) that sets the length of the slab).

Warp residual pressure in the 4D stress-tensor note is therefore a property of a singular wall, not of a mild \(\varepsilon_{\mathrm{cone}}\) expansion around a smooth eigenvalue.

---

## 4. Status after this integration

| Claim | Status |
|---|---|
| 5D TAFA tip is constraint-legal | Derived |
| Nontrivial profiles exist and reach the wall in finite \(y\) | Computed |
| \(A\) remains finite; \(A'\) diverges at the wall | Computed |
| Unique finite \(A'\) attractor | **Absent** |
| \(11/72\), \(R=1.5156\) | **Not produced** |
| \(m\) in eV from the warp | **Not produced** |

---

## 5. Next step after this (not done here)

Either stop treating 5D as the source of a slope eigenvalue, and keep \(\Lambda,f\) as 4D parameters in the pressure note, or change the 5D question:

- compactify with a second, mild boundary instead of running into the TAFA wall, or
- resolve the \(A'\) singularity and see whether a finite slope survives.

Do not restore the exponential potential. Do not put \(11/72\) back into a loss function.
