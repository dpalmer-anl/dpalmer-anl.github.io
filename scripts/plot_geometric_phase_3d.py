"""
3D plot: geometric phase vs time around one period for the spin-1/2, equatorial
B-rotation case (constant Berry connection A = -Omega/2).

- xy circle parameterizes t mod T (angle alpha = 2*pi*t/T).
- z is phi_geom(t) = -(Omega/2)*t, so over one turn phi_geom = -pi.
- Vertical segments from the xy circle (z=0) to the spiral show the phase height.
- Closing the loop in xy returns to the same field configuration at t=T and t=0,
  but the geometric phase differs by pi (single-valued branch cut); the dashed
  vertical line marks that mismatch; a red bracket joins the t=0 point (R,0,0)
  to the t=T end point (R,0,-pi) to highlight the Berry phase jump.

Style matches 60sPlot_example.py / plot_geometric_phases_spin_static.py.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# --- style aligned with 60sPlot_example.py ---
label_fontsize = 10
tick_fontsize = 10
linewidth = 1

mpl.rcParams["font.weight"] = "normal"
mpl.rcParams["axes.linewidth"] = linewidth
mpl.rcParams["lines.linewidth"] = linewidth
mpl.rcParams["xtick.labelsize"] = tick_fontsize
mpl.rcParams["ytick.labelsize"] = tick_fontsize
mpl.rcParams["xtick.major.width"] = linewidth
mpl.rcParams["ytick.major.width"] = linewidth

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "geometric-phase-3d.png"

# Period T, Omega = 2*pi/T; equatorial case: phi_geom(t) = -(Omega/2)*t
Omega = 1.0
T = 2 * np.pi / Omega
R = 1.0


def phi_geom_from_alpha(alpha):
    """alpha = 2*pi*t/T in [0, 2*pi). Same as -(Omega/2)*t with t = alpha*T/(2*pi)."""
    t = alpha * T / (2 * np.pi)
    return -(Omega / 2) * t


def main():
    fig = plt.figure(figsize=(6.0, 5.2))
    ax = fig.add_subplot(111, projection="3d")

    # --- dense 3D curve: (R cos a, R sin a, phi(a)) for a in [0, 2*pi) ---
    n_curve = 500
    alpha_curve = np.linspace(0, 2 * np.pi, n_curve, endpoint=False)
    x_c = R * np.cos(alpha_curve)
    y_c = R * np.sin(alpha_curve)
    z_c = np.array([phi_geom_from_alpha(a) for a in alpha_curve])
    ax.plot(x_c, y_c, z_c, color="k", lw=linewidth, label=r"$\phi_{\mathrm{geom}}(t)$")

    # --- reference circle in xy plane (z=0): time parameter ---
    alpha_ring = np.linspace(0, 2 * np.pi, 200, endpoint=True)
    ax.plot(R * np.cos(alpha_ring), R * np.sin(alpha_ring), np.zeros_like(alpha_ring), color="0.45", lw=linewidth * 0.8, ls="--")

    # --- 20 vertical connectors: circle (z=0) -> phase point ---
    n_vec = 20
    alphas_v = 2 * np.pi * np.arange(n_vec) / n_vec
    for a in alphas_v:
        x0, y0 = R * np.cos(a), R * np.sin(a)
        z1 = phi_geom_from_alpha(a)
        ax.plot([x0, x0], [y0, y0], [0.0, z1], color="k", lw=linewidth * 0.75, alpha=0.85)

    # --- mismatch at closure: same (R,0) in xy but z jumps from -pi to 0 ---
    z_end = phi_geom_from_alpha(2 * np.pi - 1e-6)  # ~ -pi
    ax.plot([R, R], [0.0, 0.0], [z_end, 0.0], color="k", lw=linewidth * 1.2, ls="--")

    # --- red bracket: t=0 point (R,0,0) to t=T / alpha=2pi point (R,0,-pi) ---
    # "[" in the y=0 plane, opening to +x, embracing the mismatch segment at x=R
    delta = 0.14 * R
    bx = [
        R,
        R - delta,
        R - delta,
        R,
    ]
    by = [0.0, 0.0, 0.0, 0.0]
    bz = [0.0, 0.0, -np.pi, -np.pi]
    ax.plot(bx, by, bz, color="C3", lw=1.8 * linewidth, zorder=10)

    ax.set_xlabel(r"$(t/T)$", fontsize=label_fontsize, labelpad=8)
    #ax.set_ylabel(r"$y$ (proportional to $\sin(2\pi t/T)$)", fontsize=label_fontsize, labelpad=8)
    ax.set_zlabel(r"$\phi_{\mathrm{geom}}$", fontsize=20)

    # No tick marks or numeric tick labels on x, y, or z
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.tick_params(axis="x", length=0, width=0, labelsize=0)
    ax.tick_params(axis="y", length=0, width=0, labelsize=0)
    ax.tick_params(axis="z", length=0, width=0, labelsize=0)
    ax.grid(False)

    # Reasonable 3D box aspect
    ax.set_xlim(-1.15 * R, 1.15 * R)
    ax.set_ylim(-1.15 * R, 1.15 * R)
    ax.set_zlim(-np.pi * 1.15, 0.35)

    ax.view_init(elev=22, azim=-55)

    # Leave room so z-axis label is not clipped when saving (tight_layout often crops 3D z labels)
    fig.subplots_adjust(left=0.02, right=0.92, top=0.94, bottom=0.02)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUT,
        dpi=200,
        #bbox_inches="tight",
        pad_inches=0.45,
        facecolor="white",
    )
    plt.close(fig)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
