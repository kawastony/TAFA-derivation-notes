#!/usr/bin/env python3
"""DE-floor waist vs Hubble damper. Units Mpl=H0=1, rho_crit=3."""
import math
import numpy as np

Om, OL = 0.31, 0.69
rhoL = 3 * OL


def VA(phi, Lam4, f):
    u = np.clip(phi / (2 * f), -0.49 * np.pi, 0.49 * np.pi)
    return Lam4 * np.tan(u) ** 2


def dVA(phi, Lam4, f):
    u = np.clip(phi / (2 * f), -0.49 * np.pi, 0.49 * np.pi)
    return (Lam4 / f) * np.tan(u) * (1 / np.cos(u)) ** 2


def Nlapse(phi, f):
    """Listed candidate: same tan structure as V_A. Not fitted."""
    u = np.clip(phi / (2 * f), -0.49 * np.pi, 0.49 * np.pi)
    return np.cos(u) ** 2


def integrate_waist(f, alpha=1.0, nsteps=5000, a_min=0.40):
    phi0 = alpha * f
    Lam4 = rhoL / (np.tan(alpha / 2.0) ** 2)
    V0 = float(VA(phi0, Lam4, f))
    N0 = float(Nlapse(phi0, f))
    p0 = math.sqrt(max(0.02 * V0, 1e-18)) / max(N0, 1e-8)
    u = 0.0
    phi, p = phi0, p0
    hist = []
    du = math.log(a_min) / nsteps
    for i in range(nsteps + 1):
        a = math.exp(u)
        z = 1 / a - 1
        N = float(Nlapse(phi, f))
        V = float(VA(phi, Lam4, f))
        Vp = float(dVA(phi, Lam4, f))
        kin = 0.5 * (N * p) ** 2
        rho_phi = kin + V
        w = (kin - V) / max(rho_phi, 1e-30)
        rhom = 3 * Om * (a ** -3)
        H = math.sqrt(max((rhom + rho_phi) / 3, 1e-30))
        hist.append((z, w, N, phi / f))
        if i == nsteps:
            break
        phi += (N * p / H) * du
        p += (-N * Vp / H) * du
        u += du
        if abs(phi) >= 0.98 * math.pi * f:
            break
    return np.array(hist)


def integrate_hubble(f, alpha=1.0, nsteps=5000, a_min=0.40):
    phi0 = alpha * f
    Lam4 = rhoL / (np.tan(alpha / 2.0) ** 2)
    u = 0.0
    phi, psi = phi0, 0.0
    hist = []
    du = math.log(a_min) / nsteps
    for i in range(nsteps + 1):
        a = math.exp(u)
        z = 1 / a - 1
        V = float(VA(phi, Lam4, f))
        Vp = float(dVA(phi, Lam4, f))
        kin = 0.5 * psi ** 2
        rho_phi = kin + V
        w = (kin - V) / max(rho_phi, 1e-30)
        rhom = 3 * Om * (a ** -3)
        H = math.sqrt(max((rhom + rho_phi) / 3, 1e-30))
        hist.append((z, w, 1.0, phi / f))
        if i == nsteps:
            break
        phi += (psi / H) * du
        psi += ((-3 * H * psi - Vp) / H) * du
        u += du
        if abs(phi) >= 0.98 * math.pi * f:
            break
    return np.array(hist)


def w_at(hist, ztarget):
    i = int(np.argmin(np.abs(hist[:, 0] - ztarget)))
    return float(hist[i, 1])


if __name__ == "__main__":
    print("f/Mpl  model    w(0)    w(0.3)   w(1)")
    for f in (1.0, 10.0, 30.0):
        hw = integrate_waist(f)
        hh = integrate_hubble(f)
        print(f"{f:5.1f}  waist  {w_at(hw,0):7.3f} {w_at(hw,0.3):7.3f} {w_at(hw,1):7.3f}")
        print(f"{f:5.1f}  hubble {w_at(hh,0):7.3f} {w_at(hh,0.3):7.3f} {w_at(hh,1):7.3f}")
