# Baseline A — \(\alpha\) scan

Tony Kawas / working note, 3 September 2026
Next lineage step after `Baseline_A_first_cosmology.md`.
One parameter scanned: today’s field angle \(\alpha=\phi_0/M_{\mathrm{Pl}}\).
Nothing else added.

---

## Setup (unchanged)

\(f=M_{\mathrm{Pl}}=1\), \(H_0=1\), \(\rho_{\mathrm{crit}}=3\), \(\Omega_m=0.31\), \(\Omega_\Lambda=0.69\).

\[
\Lambda^4=\frac{\rho_\Lambda}{\tan^2(\alpha/2)},
\qquad
\dot\phi_0=0.
\]

Integrate backward from \(a=1\). 42 values of \(\alpha\in[0.05,\,3.05]\) (wall at \(\pi\)).

Cuts (order-of-magnitude, not a likelihood):

- loose: \(w(0)<-0.95\), \(w(0.3)<-0.8\), \(w(0.5)<-0.6\)
- tight: \(w(0)<-0.98\), \(w(0.3)<-0.95\), \(w(0.5)<-0.9\), \(w(1)<-0.8\)

---

## Result

**Loose passes: 0. Tight passes: 0.**

| \(\alpha\) | \(m/H_0\) at \(\phi=0\) | \(w(0.3)\) | \(w(0.5)\) | \(w(1)\) |
|---|---|---|---|---|
| 0.05 | 41 | \(-0.35\) | \(-0.88\) | \(+0.84\) |
| 0.15 | 14 | \(-0.85\) | \(+0.50\) | \(-0.27\) |
| 1.0 | 1.9 | \(+0.04\) | \(+0.75\) | \(+1.00\) |
| 2.5 | 0.34 | \(+0.32\) | \(+0.81\) | \(+0.99\) |
| 3.0 | 0.07 | \(+0.96\) | \(+0.99\) | \(+1.00\) |

Small \(\alpha\): curvature at the bottom is large, the backward history oscillates.
Large \(\alpha\): you sit on the steep face of the wall. The mass *at the origin* is small, the *local slope* is not. The field runs.

There is no \(\mathrm{O}(1)\) — and no scanned — angle that keeps \(w\approx-1\) from today back through \(z=0.3\) under these conventions.

---

## Tuning statement

To save late acceleration on this line you must break at least one Baseline A convention:

1. give up \(f=M_{\mathrm{Pl}}\) (re-introduce a decay-constant hierarchy), or
2. give up \(\Lambda^4=\rho_\Lambda/\tan^2(\alpha/2)\) (re-introduce a second scale), or
3. add another field / a bare \(\Lambda\) (leave the lineage).

None of those is a scan of \(\alpha\). \(\alpha\) alone cannot do it.

That is the cost of retiring \(Q\) and the Golden Gate numbers: the original “one field is DE” sentence is not viable as an \(\mathrm{O}(1)\), one-scale theory on this potential.

---

## What this does for all TOEs

Observer, TIFA, and TAFA all used “one well explains late acceleration.” After the reduction, that sentence needs a hierarchy \(f\ll M_{\mathrm{Pl}}\) or an extra scale. Say that in every later TOE. Do not fix it with \(Q\).
