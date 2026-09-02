# Open B — first integration without a 11/72 target

Tony Kawas / working note, 3 September 2026
Not a paper. First measurement of Paper 49’s reduced system.

---

## What was run

Paper 49’s equations, origin regularity \(A'(0)=\phi'(0)=0\), \(A(0)=0\):

\[
A''(y)=s\cdot\frac13\bigl(\phi'(y)\bigr)^2,
\qquad
\phi''(y)+4A'(y)\phi'(y)=\lambda V_0 e^{\lambda\phi}.
\]

Two signs for the warp equation:

- `paper_sign`: \(s=-1\), as written in Paper 49
- `flipped_A`: \(s=+1\), the sign that can even produce a *positive* slope

Grid, no loss term involving \(11/72\):

- \(\lambda\in\{-2,-1,-0.5,0.5,1,2\}\)
- \(V_0\in\{10^{-5},10^{-4},10^{-3},10^{-2},10^{-1}\}\)
- \(\phi(0)\in\{-1,-0.3142,0,0.3142,1\}\)
- \(y\in[0,40]\), 801 samples, `odeint`

300 runs. Notable non-frozen rows: `openb_warp/warp_scan_notable.csv`.

Target for comparison only, never in the integrator:

\[
\frac{11}{72}\approx 0.152778.
\]

---

## Result 1 — the printed Paper 49 system cannot reach \(+11/72\)

With \(s=-1\) and \(A'(0)=0\),

\[
A''(y)=-\frac13(\phi')^2\le 0
\]

so \(A'(y)\) is non-increasing. Every regular start has

\[
A'(y)\le 0.
\]

On the 80 non-frozen paper-sign runs:

- every final slope is \(\le 0\)
- closest approach to \(+11/72\) is \(0.152778\) away (the slope stayed near \(0\))
- closest approach to \(-11/72\) is still \(0.119\) away

A shooting method that minimises \(\lvert A'(y_{\max})-11/72\rvert\) on this sign is minimising the distance to a point *outside the reachable set*. Paper 49’s published \(A'(120)=0.15277778\) cannot be a solution of the ODE as written plus regular origin data.

That is the first Open B measurement.

---

## Result 2 — flipping the warp sign still does not select \(11/72\)

If the writeup had the wrong sign, set \(s=+1\). Then \(A'\ge 0\), so \(+11/72\) is at least allowed.

On 99 non-frozen flipped runs the closest tail slope to \(11/72\) was

\[
\langle A'\rangle_{\mathrm{tail}}\approx 0.099
\quad(\lambda=\pm 0.5,\; V_0=10^{-2},\; \lvert\phi(0)\rvert=1),
\]

about \(0.054\) below the slogan. Mild sources (\(V_0\le 10^{-3}\)) give a median tail slope \(\sim 4\times 10^{-5}\), i.e. almost no warp.

There is no isolated pile-up at \(11/72\). Slope tracks \((\lambda,V_0,\phi(0))\). That is a family of solutions, not an eigenvalue.

---

## What this does *not* kill

- The *idea* of a warp eigenvalue. A different 5D or 10D system might have one.
- Finite-volume 4D Einstein reduction in Paper 38, which does not need \(11/72\).
- The stress-tensor / pressure note, which left warp pressure as a slot.

## What it does kill, for this reduced system

The sentence “the reduced 5D dynamics uniquely select \(a=11/72\) under regularity.”
Under regularity they select \(A'\le 0\) if the equation is as printed, and a \(V_0\)-dependent positive slope if the sign is flipped. Neither is unique at \(11/72\).

---

## What a second integration should change

Do not retune \(\phi(0)\) to chase \(11/72\). Change the equation.

1. Re-derive \(A''\) from the 5D Einstein-scalar action used in Papers 42–43. Fix the sign from the action, not from the slogan.
2. State \(V_0\) and \(\lambda\) from the same action (flux integers, not a scan).
3. Impose finite warped volume as a filter, not a target value \(R=1.5156\).
4. Only then quote \(a_\infty\) and \(R\).

Until that action-level reduction is written, Open B on Paper 49 is finished: the printed target is not an output of the printed ODE.
