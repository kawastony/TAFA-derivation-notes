# Golden bridge, 10D, and whether TAFA calculates QG

Tony Kawas / working note, 3 September 2026
Investigation only. Not a paper.

---

## The question

Were \(11/72\) and \(R=1.5156\) found while building a “Golden Gate / Golden bridge,” and was 10D / string language brought in so TAFA could calculate quantum gravity?

Short answers: **yes on the motive and the naming. No on the calculation.**

---

## What the stack actually says

Paper 44 (derive parent) and the Paper 43 continuation declare a 10D target:

- Type IIB warped flux compactification
- 4D physics = projection of 5D dynamics = shadow of 10D geometry
- a dictionary that *assigns*
  - cone angle \(35^\circ\) → “flux-stabilized deficit”
  - charge \(n\) → flux quanta
  - \(11/72\) → “quantized asymptotic slope”
  - \(R=1.5156\) → “warped-volume Jacobian”

The same text then says, in the simplification section, that one should **not** try to derive the exact number from 10D directly, and that \(11/72\) is “the only stable slope where everything balances,” compared to a guitar string.

That is a selection rule written in 10D vocabulary. It is not a Type IIB computation.

Paper 38 is the actual derived layer: 5D warped product, Einstein-frame reduction, \(M_{\mathrm{Pl}}^2=M_5^3\int e^{2A}\mathcal{W}\). No flux integers. No \(G_3\). No 10D action varied.

`PHYSICS_MODEL.md` still lists “Full quantum gravity derivation (currently semi-classical)” as open. The repo name and metadata describe a QG alternative to ΛCDM. The *intent* is QG. The *status* recorded in that file is semi-classical.

Paper 49 then aims an integrator at \(11/72\). The Golden Gate papers treat that number as already selected.

---

## What the consistent 5D theory does instead

From the action notes in this repo:

- \(A''=-\phi'^2/3\) is forced by Paper 38’s action.
- A regular tip requires \(V=0\). TAFA’s vacuum satisfies that. An exponential does not.
- Integrating TAFA in 5D gives a finite slab that ends on the field-space wall. \(A\) stays finite. \(A'\) diverges. No constant slope. No \(11/72\). No \(R=1.5156\).

So the bridge did two different jobs at once:

1. A real job: name a UV parent so that 4D Einstein + TAFA might someday sit inside a UV theory.
2. A bookkeeping job: park two fitted numbers in that parent’s dictionary so they looked derived.

Job 2 did not survive contact with the 5D action.

---

## Can TAFA calculate quantum gravity?

Not with what is written.

| Layer | What exists | QG? |
|---|---|---|
| 4D Einstein + \(T_{\mu\nu}[\phi_{\mathrm{TAFA}}]\) | Yes (pressure note) | No. Classical / semi-classical field on GR |
| 5D warped Einstein-scalar + TAFA potential | Yes (this week’s integration) | No. Still classical. Wall is singular in \(A'\) |
| Type IIB + \(G_3\) on a specified cone | Named, not computed | Would be a *string compactification*, still not a QG calculation of scattering or a wavefunction of the universe |
| Wheeler–DeWitt / one-loop / KK spectrum on the slab | Not done | This is the first well-posed QG-adjacent question the actual geometry allows |

String compactification is UV *completion of the classical action*. Quantum gravity is the quantum theory of that geometry. The papers use the first as a stand-in for the second.

---

## What is next

Do not reopen Paper 49 or the 10D dictionary until one of these is chosen.

**A. Stay honest and 4D.** Keep \(\Lambda,f\) as parameters. Use the stress-tensor note. Drop “calculates QG.” This is the smallest claim that the derived layer supports.

**B. First QG-adjacent calculation on the geometry you actually have.** Linearize gravity + \(\phi\) on the 5D TAFA slab. Compute the KK spectrum and whether \(M_{\mathrm{Pl}}\) from \(\int e^{2A}\) survives a cutoff at the wall. That is a real calculation. It will not produce \(11/72\) unless the spectrum says so.

**C. A specified 10D problem, not a dictionary.** Pick a manifold, integer flux, and the equation \(\nabla^2 h \propto |G_3|^2\). Integrate it. Compare the warp to TAFA. Expect a mismatch. Record the mismatch.

A is the scientific baseline. B is the next step if the goal is still “TAFA should calculate QG.” C is optional and expensive.

Do not treat the Golden Gate closure sentence as a theorem. Treat it as a programme heading that the 5D theory did not cash.
