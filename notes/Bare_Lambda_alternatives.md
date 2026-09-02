# Bare \(\Lambda\) and the other ways out

Tony Kawas / working note, 3 September 2026
Follows `Baseline_A_alpha_scan.md`. Investigation, not a paper.

The \(\alpha\) scan showed: Einstein + TAFA with \(f=M_{\mathrm{Pl}}\) and \(\Lambda^4=\rho_\Lambda/\tan^2(\alpha/2)\) cannot keep \(w\approx-1\) through \(z=0.3\). Something in Baseline A must break. This note compares the breaks.

---

## 0. Why \(V_A\) cannot be the late vacuum

\[
V_A(0)=0.
\]

A frozen field at the TAFA (or TIFA) minimum contributes **zero** vacuum energy. Late acceleration on this line was never “the well’s floor.” It was a *displaced* field. The scan says an \(\mathrm{O}(1)\) displacement with \(f=M_{\mathrm{Pl}}\) runs too fast.

So every alternative is a way to put energy in the vacuum *without* relying on that displacement.

---

## 1. The three breaks

| Break | What you add or drop | One-field DE? | New hierarchy? | Lineage cost |
|---|---|---|---|---|
| **B1. Bare \(\Lambda\)** | \(S\supset -\int\sqrt{-g}\,M_{\mathrm{Pl}}^2\Lambda_0\) | No. DE is a constant. TAFA is something else | No new matter scale if \(\phi=0\) | Abandons TIFA’s “one well is early *and* late” |
| **B2. \(f\) hierarchy** | Decay constant not equal to Planck | Yes, if \(m\ll H_0\) and the local slope is small | Yes. \(f/M_{\mathrm{Pl}}\) is a new number | Keeps one field; EFT/control problem if \(f\gg M_{\mathrm{Pl}}\) |
| **B3. Two TAFA scales** | \(\Lambda\) and \(f\) both free | Maybe | Yes, two numbers | Parameter reduction dies; Golden Gate temptation returns |

B1 is bare \(\Lambda\). B2 and B3 are the alternatives *to* it.

---

## 2. B1 — bare \(\Lambda\), worked out

Action:

\[
S=\int\mathrm{d}^4x\,\sqrt{-g}\left[
\frac{M_{\mathrm{Pl}}^2}{2}(R-2\Lambda_0)
+\frac12(\partial\phi)^2
-V_A(\phi)
\right],
\qquad
V_A=\Lambda^4\tan^2\!\Bigl(\frac{\phi}{2f}\Bigr).
\]

Set \(\phi=0=\dot\phi\) after any early epoch. Then \(V_A=0\) and

\[
H^2=\frac{\rho_m+\rho_r}{3M_{\mathrm{Pl}}^2}+\frac{\Lambda_0}{3}.
\]

That is \(\Lambda\)CDM. \(w=-1\) at all late \(z\) by construction. The \(\alpha\) scan becomes irrelevant.

**What TAFA is then for**

| Role | Status under B1 |
|---|---|
| Late DE | **Retired.** \(\Lambda_0\) does it |
| Early inflation | Possible if \(\phi\) starts near the wall and \(V_A\sim\Lambda^4\) is a high scale. That \(\Lambda\) is *not* \(\rho_\Lambda^{1/4}\) |
| Ultralight DM / cores | Possible if \(m=\Lambda^2/\sqrt{2}f\) is chosen for that job. That \(m\) is *not* \(H_0\) |
| Walls / observer replacement | Geometry of field space. Interpretive. Not a 4D observable by itself |

B1 splits the original TIFA sentence into two objects: a constant for late time, a TAFA field for something else. That is how standard cosmology already works. TAFA is no longer a TOE of the dark sector. It is a scalar with walls, living *in* \(\Lambda\)CDM.

Law 4 remains: gravity sees a stress tensor. The late tensor is \(\Lambda_0 g_{\mu\nu}\). Fear/\(Q\) still do not come back.

\(\Lambda_0\) is fixed by \(\rho_\Lambda\). TAFA still has \((\Lambda,f)\) for its *other* job. You did not remove parameters. You stopped asking TAFA to be DE.

---

## 3. B2 — keep one field, change \(f\)

Near the bottom \(V\approx\tfrac12 m^2\phi^2\), \(m^2=\Lambda^4/(2f^2)\).
For \(V\sim\rho_\Lambda\) and \(\phi\sim f\),

\[
m\sim H_0\,\frac{M_{\mathrm{Pl}}}{f}.
\]

Dark energy needs \(m\ll H_0\), hence **\(f\gg M_{\mathrm{Pl}}\)** — a super-Planckian decay constant, the usual EFT problem.

Fuzzy cores need \(m\sim 10^{-22}\,\mathrm{eV}\gg H_0\), the opposite hierarchy.

One \(f\) cannot be both DE and fuzzy DM.

---

## 4. B3 — two free TAFA scales

Ordinary quintessence with a \(\tan^2\) shape. Can fit \(w(z)\). Does not progress the TOE line. Golden Gate numbers will try to return as “derived” \(\Lambda,f\). They are fits.

---

## 5. TIFA vs TAFA

TIFA also has \(V_T(0)=0\). A bare \(\Lambda_0\) on TIFA is the same split. The Möbius map does not create a floor. Walls do not create a floor.

---

## 6. Least damage to the original ideas

1. Laws, not an audience.
2. One field for early *and* late acceleration.
3. Gravity sees a stress tensor.

B1 keeps (1) and (3), breaks (2).
B2 keeps all three, with an EFT warning on (2).
B3 keeps them as a fit.

- Non-negotiable (2) → B2, write \(f\gg M_{\mathrm{Pl}}\) in the open.
- Non-negotiable honest late \(w(z)\) and no super-Planckian \(f\) → B1. The well never had a late floor.
- B3 is phenomenology, not a TOE step.

\(Q\) is not on this list.

---

## 7. Recommendation

- Record B1 as the default late universe if you will not defend \(f\gg M_{\mathrm{Pl}}\).
- Keep B2 as the only remaining one-field-DE branch, with that hierarchy explicit, and a ban on also using the field as \(10^{-22}\,\mathrm{eV}\) DM.
- Do not open B3 inside the derivation repo.

Next: pick B1 or B2. If B1, write what TAFA is for once DE is \(\Lambda_0\). If B2, compute the \(f/M_{\mathrm{Pl}}\) required for a stated \(w(z)\) bound, and stop.
