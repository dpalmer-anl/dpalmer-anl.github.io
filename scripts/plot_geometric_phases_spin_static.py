"""
Static diagram for the geometric-phases blog post: B in the xy plane (parallel
field lines), spin at origin, |chi_+> / |chi_-> along +/- n_hat, and a curved
arrow indicating CCW rotation of B. Style follows research/60sPlot_example.py.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.ticker import MultipleLocator

# --- style aligned with 60sPlot_example.py ---
label_fontsize = 10
tick_fontsize = 10
linewidth = 1
major_xtick_length = 8
minor_xtick_length = 4
major_ytick_length = 8
minor_ytick_length = 4

mpl.rcParams["font.weight"] = "normal"
mpl.rcParams["axes.linewidth"] = linewidth
mpl.rcParams["lines.linewidth"] = linewidth
mpl.rcParams["xtick.labelsize"] = tick_fontsize
mpl.rcParams["ytick.labelsize"] = tick_fontsize
mpl.rcParams["xtick.major.width"] = linewidth
mpl.rcParams["ytick.major.width"] = linewidth
mpl.rcParams["xtick.minor.width"] = linewidth
mpl.rcParams["ytick.minor.width"] = linewidth

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "geometric-phases-spin-static.png"

# snapshot: B along n in xy plane
phi = np.deg2rad(38)
n = np.array([np.cos(phi), np.sin(phi)])
perp = np.array([-n[1], n[0]])

fig, ax = plt.subplots(figsize=(5, 5))
math_fs = 11

# parallel B-field lines (uniform field, direction n)
half_len = 0.92
for k in range(-5, 6):
    off = k * 0.14
    base = off * perp
    p0 = base - half_len * n
    p1 = base + half_len * n
    ax.annotate(
        "",
        xy=p1,
        xytext=p0,
        arrowprops=dict(
            arrowstyle="->",
            color="k",
            lw=linewidth,
            shrinkA=0,
            shrinkB=0,
        ),
        zorder=1,
    )

# Label B field lines (one mathtext near a representative line, away from origin)
k_B_label = 4
off_B = k_B_label * 0.14
base_B = off_B * perp
mid_B = base_B + 0.35 * n
pos_B = mid_B + 0.12 * perp
ax.text(
    pos_B[0],
    pos_B[1],
    r"$\mathbf{B}$",
    fontsize=math_fs,
    color="k",
    ha="center",
    va="center",
    zorder=3,
)

# spin (particle at origin)
ball_r = 0.085
circ = Circle(
    (0, 0),
    ball_r,
    facecolor="0.9",
    edgecolor="k",
    linewidth=linewidth,
    zorder=5,
)
ax.add_patch(circ)

# eigenvectors |chi_+> (gold) and |chi_-> (orange) along +/- n
L_e = 0.48
ax.annotate(
    "",
    xy=L_e * n,
    xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color="#DAA520", lw=1.4 * linewidth, shrinkA=0, shrinkB=0),
    zorder=6,
)
ax.annotate(
    "",
    xy=-L_e * n,
    xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color="#CC6600", lw=1.4 * linewidth, shrinkA=0, shrinkB=0),
    zorder=6,
)

# Mathtext labels for eigenvectors (matplotlib mathtext)
pos_plus = L_e * n + 0.05 * perp + 0.02 * n
pos_minus = -L_e * n - 0.05 * perp - 0.02 * n
ax.text(
    pos_plus[0],
    pos_plus[1],
    r"$|\chi_{+}\rangle$",
    fontsize=math_fs,
    color="k",
    ha="center",
    va="bottom",
    zorder=7,
)
ax.text(
    pos_minus[0],
    pos_minus[1],
    r"$|\chi_{\text{-}}\rangle$",
    fontsize=math_fs,
    color="k",
    ha="center",
    va="top",
    zorder=7,
)

# curved arrow: sense of rotation of B in the xy plane (CCW when viewed from +z)
R_arc = 0.68
a0 = np.deg2rad(18)
a1 = np.deg2rad(118)
p0 = R_arc * np.array([np.cos(a0), np.sin(a0)])
p1 = R_arc * np.array([np.cos(a1), np.sin(a1)])
ax.annotate(
    "",
    xy=p1,
    xytext=p0,
    arrowprops=dict(
        arrowstyle="-|>",
        color="k",
        lw=linewidth,
        shrinkA=0,
        shrinkB=0,
        connectionstyle="arc3,rad=0.35",
    ),
    zorder=4,
)

ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-1.12, 1.12)
ax.set_ylim(-1.12, 1.12)
ax.set_xlabel("x", fontsize=label_fontsize, labelpad=8)
ax.set_ylabel("y", fontsize=label_fontsize, labelpad=8)

ax.tick_params("x", which="both", bottom=True, top=False, direction="in", labelsize=tick_fontsize)
ax.tick_params("y", which="both", left=True, right=False, direction="in", labelsize=tick_fontsize)
ax.tick_params("x", which="major", length=major_xtick_length)
ax.tick_params("x", which="minor", length=minor_xtick_length)
ax.tick_params("y", which="major", length=major_ytick_length)
ax.tick_params("y", which="minor", length=minor_ytick_length)
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))

fig.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=200, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Wrote {OUT}")
