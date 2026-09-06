# Waist — the pause as geometry

Tony Kawas / 6 September 2026. Constitution. Not a paper.

One field. Two floors. The pause is a **shape critical point**, not an observer and not Hubble drag.

---

## What this note is for

Write the pause so it can be integrated. If the numbers do not land, the waist stays a picture and we do not invent a letter.

---

## Field vs floor (locked)

- **Field:** one scalar \(\phi\) in Einstein plus \(V_A=\Lambda^4\tan^2(\phi/2f)\), \(|\phi|<\pi f\).
- **Floor:** the same field used in one arena (DE cosmology, DM disk, later a lab patch). Not a second kinetic term.

\(\phi=\phi_0+\delta\phi\) is one field on two floors. It is not two fields.

---

## What the pause is not

| Old name | Why it is out |
|---|---|
| Observer / \(Q\) / intent | Extra source in \(T_{\mu\nu}\) |
| \(3H\dot\phi\) freeze | Bleeds momentum. Memory dies. |
| Universal \(r_p=12.1\,\mathrm{kpc}\) | Fitted length on the DM floor |
| \(z=12\) as a date | Winding is not a cosmic clock |
| Calm voice as a person | The waist is a neck, not advice |

The **observer** in the cone story is the volume constraint. It is not in \(T_{\mu\nu}\).

---

## Working equations

Proper-time roll on the well, outside clocks from a lapse:

$$
\frac{\mathrm{d}\phi}{\mathrm{d}\tau}=p,\qquad
\frac{\mathrm{d}p}{\mathrm{d}\tau}=-V_A'(\phi),\qquad
\frac{\mathrm{d}\tau}{\mathrm{d}t}=N.
$$

Coordinate speed is \(\mathrm{d}\phi/\mathrm{d}t=N p\). At the waist, \(N\to 0\) (or is minimal). \(p\) is **stored**. Outside time looks slow. Inner time is \(\tau\).

Homogeneous stress (DE floor) is still

$$
\rho=\tfrac12 p^2+V_A,\qquad
w=\frac{\tfrac12 p^2-V_A}{\tfrac12 p^2+V_A}
$$

written with proper momentum. Do not replace this by a friction term.

Volume constraint (the advisor):

$$
\mathrm{Vol}=\text{const}.
$$

For a revolution profile \(r(z)\) that is the cone family,
\(\int r^2\,\mathrm{d}z\) is held fixed while aspect ratio breathes. The **waist** is the neck: along-wall slope flat, \(\partial_s a_\parallel=0\).

---

## Status of \(N\)

\(N\) is **not yet derived**. Two candidates, both still a choice of embedding:

1. **Warp lapse.** Identify a monotone map \(y=y(\phi)\) and set \(N=e^{A(y(\phi))}\) from the 5D integration already in OpenB notes. No new constant if \(A\) is the solved warp. The map \(y(\phi)\) is the remaining choice.
2. **Hyperboloid family.** \(r^2=A+B z^2\) with \(A+B/3\) fixed by Vol. Neck radius \(\sqrt{A}\). Take \(N \propto \sqrt{A}/\sqrt{A_{\max}}\). The family is chosen; Vol is not a new scale.

Until one of those maps is forced by \(V_A\) plus Vol=const, \(N(\phi)\) is a cube on the rim, not a law.

Forbidden: fitting a new function \(N(z)\) to supernovae.

---

## Tests (no extra letters)

**DE floor.** Use existing B2 (or B1+well as spectator) parameters from Floor_DE.md. Integrate the system above with one candidate \(N\). Ask only:

- Does \(w(z)\) sit near \(-1\) through the late window \(z\sim 0.3\) *because* \(N\) is small while \(p\) is not?
- After the neck, does stored \(p\) thaw without a new mass?

Baseline A with \(3H\dot\phi\) already failed to hold that window without super-Planckian \(f\). This test is whether the lapse does the job the damper could not.

Pass → \(z\sim 0.3\) is no longer only the 5D linear map; it is also a waist.  
Fail → keep \(\Delta y\to z\sim 0.3\) as the derived tick, keep the waist as geometry, do not retune \(\Lambda,f\).

**DM floor.** Same neck idea on a disk is already written as

$$
r_M=\sqrt{G M_{\mathrm{bar}}/a_T}.
$$

Do not put the cosmological \(N\) onto SPARC. Do not move \(a_T\). The disk waist is mass-dependent. 12.1 kpc remains a typical giant, not a law.

**Lab floor (later).** Quadratic jet \(m^2=\Lambda^4/(2f^2)\) only. No tourmaline, no \(Q\), no intent torque in this note.

---

## Derived vs chosen

| Object | Kind |
|---|---|
| One field, two floors | Locked |
| Pause = neck at fixed volume | Picture, now an equation template |
| \(p\) stored, not bled | Locked (rejects Hubble pause) |
| \(V_A\), walls at \(\pm\pi f\) | Derived (Möbius) |
| Form of \(N(\phi)\) | **Chosen** until a map is forced |
| \(z\sim 0.3\) from \(\Delta y\) | Derived on the DE floor (5D + linear map) |
| \(z\sim 0.3\) from this lapse | **Not shown** |
| \(a_T\) | Calibrated on the DM floor |
| \(Q\), F7-as-force, piezo as proof | Out |

---

## Next integrator

A short 4D script, two parameters from Floor_DE, one listed \(N\) candidate, output \(w(z)\) from \(z=1\) to \(z=0\). Compare to Baseline_A_4D.md. No third parameter. No git commit of a “pass” unless the plot is in this repo.
