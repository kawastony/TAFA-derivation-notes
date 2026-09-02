# Baseline A — removing parameters, as far as the action allows

Tony Kawas / working note, 3 September 2026
Addendum to `Baseline_A_4D.md`. Not a paper.

---

## What cannot be done

The 4D action contains two dimensionful matter constants, \(\Lambda\) and \(f\). Nothing inside that integral fixes their values. The 5D slab does not either. So “zero free parameters from the action alone” is not available.

Initial data \(\phi_i,\dot\phi_i\) are a separate layer. They are not constants in the Lagrangian.

---

## What can be done

Two conventions that do not smuggle Golden Gate numbers.

**Convention 1 — only one new scale besides \(M_{\mathrm{Pl}}\).**
Set the decay constant to the only gravitational scale already present:

\[
f=M_{\mathrm{Pl}}.
\]

Then

\[
m^2=\frac{\Lambda^4}{2M_{\mathrm{Pl}}^2},
\qquad
V_A=\Lambda^4\tan^2\!\Bigl(\frac{\phi}{2M_{\mathrm{Pl}}}\Bigr).
\]

The theory has one matter scale, \(\Lambda\).

**Convention 2 — that scale is the observed late-time density.**
At the TAFA vacuum \(V_A(0)=0\). Late acceleration is not a cosmological constant. It is a frozen or slowly rolling displacement. Demand that today’s potential energy is the observed dark-energy density:

\[
V_A(\phi_0)=\Lambda^4\tan^2\!\Bigl(\frac{\phi_0}{2M_{\mathrm{Pl}}}\Bigr)
=\rho_{\Lambda}
=3H_0^2M_{\mathrm{Pl}}^2\,\Omega_{\Lambda}.
\]

If the displacement is order one in field units, \(\phi_0=\alpha M_{\mathrm{Pl}}\) with \(\alpha=\mathrm{O}(1)\) not tuned,

\[
\Lambda^4
=\frac{\rho_{\Lambda}}{\tan^2(\alpha/2)}.
\]

The choice \(\alpha=1\) (field sits one Planck unit off the vacuum) gives

\[
\Lambda^4
=\frac{\rho_{\Lambda}}{\tan^2(1/2)}
\approx 3.35\,\rho_{\Lambda},
\qquad
m
=\frac{\Lambda^2}{\sqrt{2}\,M_{\mathrm{Pl}}}
\sim H_0.
\]

That last line is the point: \(f=M_{\mathrm{Pl}}\) plus \(\rho_{\Lambda}\) plus an \(\mathrm{O}(1)\) angle automatically puts \(m\) at the Hubble scale, which is what a frozen scalar needs in order to look like dark energy today.

\(\alpha\) is still a choice. It is not a third Lagrangian parameter. It is today’s field value. The Lagrangian after Convention 1 has one number, \(\Lambda\). Convention 2 fixes that number from \(\rho_{\Lambda}\) once \(\alpha\) is stated.

---

## Parameter count after the reduction

| Object | Count |
|---|---|
| Lagrangian scales besides \(M_{\mathrm{Pl}}\) | **1** (\(\Lambda\)), or **0** if Convention 2 is adopted |
| Today’s field angle \(\alpha=\phi_0/M_{\mathrm{Pl}}\) | 1 initial datum, \(\mathrm{O}(1)\) |
| \(\dot\phi_0\) | 0 if Hubble-frozen (\(m\sim H_0\)) |
| \(11/72\), \(R\), \(Q\), \(35^\circ\) | 0 |

This is not a derivation of \(\rho_{\Lambda}\). It is the statement that TAFA does not need a second scale besides Planck and the density you are trying to account for, provided you accept \(f=M_{\mathrm{Pl}}\) and an \(\mathrm{O}(1)\) displacement.

---

## What this forbids

- A second, independent galactic mass. If cores are kept, they use this same \(m\sim H_0\). That is an ultralight field. It may or may not make cores. If it does not, drop cores. Do not add \(m\sim 10^{-22}\,\mathrm{eV}\) by hand.
- Using \(\Lambda\) as a high inflation scale and a tiny DE scale at once, unless the field actually rolls from near the wall to \(\alpha\sim\mathrm{O}(1)\) and you compute that trajectory. Two epochs, one \(\Lambda\): that trajectory is a calculation, not a new constant.

---

## Status

| Move | Kind |
|---|---|
| \(f=M_{\mathrm{Pl}}\) | Convention, not a theorem |
| \(\Lambda^4=\rho_{\Lambda}/\tan^2(\alpha/2)\) | Observational anchor, not a theorem |
| \(\alpha=\mathrm{O}(1)\) | Naturalness choice |
| Zero parameters from the action with no convention and no data | **Impossible** |

Baseline A with Conventions 1–2 is the tightest honest theory: Einstein + TAFA, one optional \(\mathrm{O}(1)\) angle, dark-energy density read from the sky rather than from \(11/72\).
