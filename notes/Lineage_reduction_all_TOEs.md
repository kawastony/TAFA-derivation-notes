# Lineage reduction — what every TOE must keep

Tony Kawas / working note, 3 September 2026
Not a paper. Spine for Observer → TIFA → TAFA, and for any later TOE.

Priority: derivations that move the whole line, not only TAFA.

---

## 0. Why this note exists

Newer TOEs got heavier by *adding* symbols (\(Q\), fear density, \(11/72\), \(R\), flux integers). The original ideas were smaller:

- the world has laws, not an audience
- vacuum energy and early acceleration can be one field
- gravity sees a stress tensor, not a story

A later TOE is progress only if it keeps those three and *drops* symbols that were standing in for them. This note writes that filter as math.

---

## 1. The line, stripped

| Stage | What it was trying to say | What it actually wrote | What survives |
|---|---|---|---|
| Observer / Grand TOE | Collapse and “fear” pick outcomes | \(\Psi=Q\times(\mathrm{laws})\times(\mathrm{forces})+D(\mathrm{Fear},Q)\) | Four-law *shape*. Not \(Q\). Not Fear as a field |
| TIFA | Inflation and dark energy are one periodic potential | \(V_T=\Lambda^4(1-\cos\phi/f)\) | One canonical scalar, one well |
| TAFA | The well has walls; geometry replaces the observer | \(V_A=\Lambda^4\tan^2(\phi/2f)\), \(\lvert\phi\rvert<\pi f\) | Same scalar, incomplete field space |
| Baseline A | Stop claiming QG and 10D numbers | Einstein + \(V_A\), \(f=M_{\mathrm{Pl}}\), \(\Lambda\) from \(\rho_\Lambda\) | The working theory |

The only *forced* potential-level map on this line is TIFA → TAFA:

\[
\tan^2\theta=\frac{1-\cos 2\theta}{1+\cos 2\theta},
\qquad
\theta=\frac{\phi}{2f}
\quad\Rightarrow\quad
V_A=\Lambda^4\frac{V_T}{2\Lambda^4-V_T},
\]

walls at \(\phi=\pm\pi f\). That identity is the lineage. Everything else is interpretation.

---

## 2. Four laws, written once

State them so they do not mention \(Q\), and so each TOE is a reading of the same list.

1. **Motion.** There is a metric and there are geodesics.
2. **Source.** Motion changes when there is a source. \(G_{\mu\nu}=8\pi G\,T_{\mu\nu}\).
3. **Reaction.** The source is conserved. \(\nabla^\mu T_{\mu\nu}=0\).
4. **The source is the field.** \(T_{\mu\nu}\) is the TAFA (or TIFA) scalar, optionally with a Madelung piece if a condensate is assumed.

Observer Law 4 (“condensate / superconductor”) is a *picture* of \(T_{\mu\nu}^{\mathrm{Q}}\). It is not a fifth law and it does not insert \(Q\).

Any new TOE that wants to sit on this line must show its extra symbol is a coordinate, a component of this \(T_{\mu\nu}\), or an initial datum. Otherwise it is off the line.

---

## 3. What \(Q\) and Fear were

They were names for **selection and initial data**.

- Observer collapse → choose \(\phi_0=\alpha M_{\mathrm{Pl}}\) and whether \(\dot\phi_0=0\).
- Fear density → the only extra source allowed is \(T_{\mu\nu}^{\mathrm{Q}}\) of the *same* field, and only if a coherent mode is assumed.

\[
D(\mathrm{Fear},Q)\ \longrightarrow\ \text{initial angle }\alpha
\text{ plus, optionally, a condensate reading of }T_{\mu\nu}.
\]

New TOEs that put \(Q\) back on the right-hand side of Einstein’s equation are reversions.

---

## 4. Filter for later TOEs

1. Forced by Einstein + TAFA, or by the TIFA→TAFA identity?
2. If not: convention (\(f=M_{\mathrm{Pl}}\)) or observational anchor (\(\rho_\Lambda\))?
3. If not: initial datum (\(\alpha\))?
4. If not: it does not enter the lineage.

Applications inherit interpretation of the same four laws, not new constants.

---

## 5. The calculation that feeds every TOE

Integrate homogeneous Baseline A. See `Baseline_A_first_cosmology.md`.
Result in brief: an \(\mathrm{O}(1)\) angle does not keep \(w\approx-1\) through redshift 0.3. The original “one field for late acceleration” idea still needs tuning after \(Q\) is retired.
