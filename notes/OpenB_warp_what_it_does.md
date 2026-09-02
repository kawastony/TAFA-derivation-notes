# Open B — what solving the warp does

Tony Kawas / working note, 3 September 2026
Companion to `Forced_vs_Free_TAFA_bridges.md` and `TAFA_stress_tensor_and_pressure.md`.
Not a paper.

---

## Plain language

Think of the extra dimension as a funnel.

The wide end is the part of the geometry we live in. The narrow end is the deep throat. The function \(A(y)\) is how tightly the funnel is squeezed as you walk along it. Steep squeeze means a short walk turns a huge microscopic energy into a tiny energy that 4D physics can see. Shallow squeeze means the two ends are almost the same scale.

Right now TAFA *names* the steepness:

- slope \(A' = 11/72\)
- volume factor \(R \approx 1.5156\)

Those names were put in by hand, then Paper 49 was written to *hit* \(11/72\) with a shooting method. Hitting a target you already chose is not solving the funnel. Solving the funnel means: write the equation for how the walls and the flux hold the funnel, integrate it, and *read off* the slope. If the number is \(11/72\), keep it. If it is not, throw \(11/72\) away.

What that number then does:

1. It converts throat scales into 4D scales. That is how \(f\) at the bottom can differ from \(f\) at the top (Open A), without a slide that just writes \(7M_{\mathrm{Pl}}\to 0.5M_{\mathrm{Pl}}\).
2. It converts \(\Lambda\) and \(f\) into a mass \(m^2=\Lambda^4/(2f^2)\) that is no longer a free symbol in the pressure note.
3. It turns the leftover 5D stress into a computed correction to 4D pressure, instead of a slot labelled “quantum geometry.”
4. It tells you whether the funnel is stable. If every regular start runs to the same slope, that slope is an output of the geometry. If it only appears when you aim at it, it is a slogan.

Until that integral exists, DE pressure, DM-core pressure, and “warp pressure” cannot be compared as numbers. They can only be named.

---

## What Paper 49 actually did

The reduced system used there is

\[
A''(y)=-\frac13\bigl(\phi'(y)\bigr)^2,
\qquad
\phi''(y)+4A'(y)\phi'(y)=\lambda V_0\,e^{\lambda\phi}.
\]

Boundary data at the origin: \(A'(0)=\phi'(0)=0\). The integrator then *minimises* \(\lvert A'(y_{\max})-11/72\rvert\). The published result \(A'(120)=0.15277778\) is the target being recovered, not an eigenvalue being found.

That is useful as a consistency check: a regular solution that *can* approach \(11/72\) exists if you tune \(\phi(0)\). It is not Open B.

Open B forbids the target in the loss function.

---

## The well-posed problem

**Given** the 5D warp-scalar equations (or the better 10D Poisson problem \(\nabla^2 h\propto\lvert G_3\rvert^2\) when that reduction is written), regularity at the origin, and finite warped volume

\[
M_{\mathrm{Pl}}^2=M_5^3\int\mathrm{d}y\,e^{2A(y)}\,\mathcal{W}_{\mathrm{cone}}(y)<\infty,
\]

**find**

\[
a_\infty=\lim_{y\to y_{\mathrm{IR}}}A'(y)
\qquad\text{and}\qquad
R=\frac{\int\mathrm{d}y\,e^{2A}\mathcal{W}_{\mathrm{cone}}}{\text{a stated reference integral}}.
\]

No term \(\lvert A'-11/72\rvert\) is allowed. No term \(\lvert R-1.5156\rvert\) is allowed.

If the limit does not exist, say so. If it exists and is not \(11/72\), the prediction package that used \(11/72\) and \(R=1.5156\) is recalibrated or dropped.

---

## What success looks like

A short table:

| Output | Used for |
|---|---|
| \(a_\infty\) | IR/UV scale ratio; Open A |
| warped-volume \(R\) | 4D Planck mass; galaxy normalisation if you still want one |
| \(\varepsilon_{\mathrm{cone}}\) from the solved profile | warp residual pressure in the stress-tensor note |
| \(m^2=\Lambda^4/(2f^2)\) after \(f\) is read from the same profile | core scale in \(p_Q\) |

Failure is also success: if no regular finite-volume profile exists, the 5D reduction in Papers 42–43 is not a container for TAFA.

---

## Next computation (not done in this note)

Integrate the reduced system with a loss that is only regularity plus finite volume. Report \(a_\infty\) and \(R\) as measured numbers with error bars from step size and \(y_{\max}\). Do not print \(11/72\) unless it appears by itself.

Paper 49’s ODE can be the first integrator, provided the target is removed. The 10D Poisson problem is the second, harder integrator. Do the first one first.
