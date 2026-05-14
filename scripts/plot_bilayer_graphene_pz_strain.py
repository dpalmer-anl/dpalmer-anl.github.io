"""
Schematic **2D** $xz$ projection for negative out-of-plane (auxetic) response in bilayer graphene:
in-plane tensile strain along $x$ and layer separation (vertical axis: physical $z$, schematic $y$).

**Geometry:** schematic bilayer in the $xz$ plane ($y=0$): five equally spaced sites per layer along
$x$, top layer shifted for an AB-staggered look; strained panel uses a larger in-plane neighbor spacing.

**$p_z$ lobes:** elliptical envelopes in the $xz$ plane matching ``PZ_ISO_R_XY_MAX_*`` and
``PZ_ISO_Z_HALF_EXTENT_*`` (Å).

**Viewport:** fixed $\\pm 8\\,$Å in $x$ and $z$; axes drawn without ticks, spines, or axis labels.

Output: assets/images/bilayer-graphene-pz-negative-poisson.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# --- publication-style defaults ---
mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica", "sans-serif"],
        "font.size": 10,
        "axes.linewidth": 0.9,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "savefig.dpi": 300,
    }
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images" / "bilayer-graphene-pz-negative-poisson.png"

# Fixed $xz$ window (Å): same horizontal and vertical extent in both panels
PLOT_AXIS_HALF = 8.0


def build_schematic_equal_spacing_bilayer(
    n_atoms_per_layer: int,
    neighbor_spacing_A: float,
    layer_sep_A: float,
    *,
    ab_shift_fraction: float = 0.5,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Two layers in the $xz$ plane ($y=0$): ``n_atoms_per_layer`` sites on a line along $x$ with uniform
    spacing ``neighbor_spacing_A``. The top layer is shifted along $x$ by ``ab_shift_fraction`` times
    that spacing (default half step, staggered bilayer).

    Returns ``(positions Nx3, cell 3x3)`` in Å, centered at the centroid. ``cell[0]`` is a nominal
    in-plane vector length used only for strain-arrow scaling in the figure.
    """
    n = n_atoms_per_layer
    d = float(neighbor_spacing_A)
    half = 0.5 * float(n - 1)
    xs_bot = (np.arange(n, dtype=float) - half) * d
    shift = ab_shift_fraction * d
    xs_top = xs_bot + shift

    z0 = -0.5 * layer_sep_A
    z1 = 0.5 * layer_sep_A
    pos_bot = np.stack([xs_bot, np.zeros(n), np.full(n, z0)], axis=1)
    pos_top = np.stack([xs_top, np.zeros(n), np.full(n, z1)], axis=1)
    pos = np.vstack([pos_bot, pos_top])
    pos -= pos.mean(axis=0)

    span_x = float(np.max(pos[:, 0]) - np.min(pos[:, 0]))
    cell = np.zeros((3, 3))
    cell[0] = np.array([max(span_x + d, (n - 1) * d + abs(shift)), 0.0, 0.0])
    cell[1] = np.array([0.0, 1.0, 0.0])
    cell[2] = np.array([0.0, 0.0, max(layer_sep_A + 10.0, 12.0)])
    return pos, cell


def schematic_chain_bilayer_bond_pairs(n_atoms_per_layer: int) -> list[tuple[int, int]]:
    """Nearest-neighbor bonds along each layer chain (same index pairs for strained coordinates)."""
    pairs: list[tuple[int, int]] = []
    for layer in range(2):
        base = layer * n_atoms_per_layer
        for k in range(n_atoms_per_layer - 1):
            pairs.append((base + k, base + k + 1))
    return pairs


def plot_bonds_xz(ax, pos: np.ndarray, pairs: list[tuple[int, int]]) -> None:
    for i, j in pairs:
        p, q = pos[i], pos[j]
        ax.plot([p[0], q[0]], [p[2], q[2]], color="#1a1a1a", lw=1.35, solid_capstyle="round", zorder=4)


def draw_atoms_xz(ax, pos: np.ndarray, *, s: float = 38.0) -> None:
    ax.scatter(
        pos[:, 0],
        pos[:, 2],
        s=s,
        c="#2d2d2d",
        edgecolors="none",
        linewidths=0,
        alpha=0.96,
        zorder=5,
    )


def draw_pz_lobes_xz(
    ax,
    positions: np.ndarray,
    r_xy_max_A: float,
    z_half_extent_A: float,
    color: str = "#3d7a9e",
    alpha: float = 0.38,
) -> None:
    """Two elliptical $p_z$-like lobes per site in the $xz$ plane (envelope targets in Å)."""
    for p in positions:
        cx, cz = float(p[0]), float(p[2])
        w = 2.0 * r_xy_max_A
        h = z_half_extent_A
        for sign in (1.0, -1.0):
            cy = cz + sign * z_half_extent_A * 0.5
            ell = mpatches.Ellipse(
                (cx, cy),
                width=w,
                height=h,
                facecolor=color,
                edgecolor=color,
                lw=0.4,
                alpha=alpha,
                zorder=1,
            )
            ax.add_patch(ell)


def inplane_strain_arrow_z(
    interlayer_A: float, a1_len_A: float, ref_cc_A: float
) -> float:
    z_bot_layer = -0.5 * interlayer_A
    return (
        z_bot_layer
        - 1.12 * a1_len_A
        - 0.52 * ref_cc_A
        - 0.30 * interlayer_A
    )


def draw_strain_annotations_xz(
    ax,
    a1_len_A: float,
    interlayer_A: float,
    ref_cc_A: float,
    x_half_span: float,
) -> None:
    """In-plane strain: double arrow along $x$. Layer separation: double arrow along $z$."""
    c_in = "#a61c1c"
    c_sep = "#1b5e20"
    z_red = inplane_strain_arrow_z(interlayer_A, a1_len_A, ref_cc_A)
    # Original z is below the bilayer; with fixed $\pm$PLOT_AXIS_HALF limits it can clip out of view.
    z_red = max(z_red, -PLOT_AXIS_HALF + 0.55)
    Lx = 0.72 * x_half_span
    ax.annotate(
        "",
        xy=(Lx, z_red),
        xytext=(-Lx, z_red),
        arrowprops=dict(arrowstyle="<->", color=c_in, lw=2.2, shrinkA=0, shrinkB=0),
        zorder=6,
    )
    ax.text(
        0.0,
        z_red - 0.18 * ref_cc_A,
        "(inplane strain)",
        color=c_in,
        fontsize=8.5,
        ha="center",
        va="top",
        zorder=8,
    )

    xg = -0.86 * x_half_span
    hz = 0.52 * interlayer_A + 0.38 * a1_len_A
    z0g, z1g = -hz, hz
    ax.annotate(
        "",
        xy=(xg, z1g),
        xytext=(xg, z0g),
        arrowprops=dict(arrowstyle="<->", color=c_sep, lw=2.2, shrinkA=0, shrinkB=0),
        zorder=7,
    )
    ax.text(
        xg - 0.12 * x_half_span,
        0.5 * (z0g + z1g),
        "(layer separation)",
        color=c_sep,
        fontsize=8.5,
        ha="right",
        va="center",
        zorder=8,
    )


def panel_xz(
    ax,
    title: str,
    pos: np.ndarray,
    cell: np.ndarray,
    interlayer_A: float,
    r_xy_max_A: float,
    z_half_extent_A: float,
    ref_cc_A: float,
    bond_pair_indices: list[tuple[int, int]],
    show_strain_arrows: bool = False,
) -> None:
    draw_pz_lobes_xz(ax, pos, r_xy_max_A, z_half_extent_A)
    plot_bonds_xz(ax, pos, bond_pair_indices)
    draw_atoms_xz(ax, pos, s=38.0)

    a1_len = float(np.linalg.norm(cell[0]))
    if show_strain_arrows:
        draw_strain_annotations_xz(
            ax, a1_len, interlayer_A, ref_cc_A, PLOT_AXIS_HALF
        )

    ax.set_title(title, fontsize=11, fontweight="semibold", pad=10)
    lim = PLOT_AXIS_HALF
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal", adjustable="box")
    ax.tick_params(
        top=False,
        right=False,
        left=False,
        bottom=False,
        labelleft=False,
        labelbottom=False,
        labeltop=False,
        labelright=False,
    )
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)


def main() -> None:
    # --- Schematic chain along $x$ ($y=0$): five sites per layer, AB stagger; ref for text offsets (Å) ---
    ATOMS_PER_LAYER = 5
    INPLANE_NEIGHBOR_UNSTRAINED = 1.42  # nearest-neighbor spacing along the chain, unstrained (Å)
    INPLANE_STRAIN_FRAC = 0.32  # tensile strain along the chain; strained spacing = (1+ε) times unstrained
    INPLANE_NEIGHBOR_STRAINED = INPLANE_NEIGHBOR_UNSTRAINED * (1.0 + INPLANE_STRAIN_FRAC)

    LAYER_SEP_A_UNSTRAINED = 2.35
    STRAIN_CELL0_UNSTRAINED = 0.0

    LAYER_SEP_A_STRAINED = 4.15
    STRAIN_CELL0_STRAINED = INPLANE_STRAIN_FRAC

    # p_z envelope (Å): max radius in xy from each C, half-length of each lobe along z
    PZ_ISO_R_XY_MAX_UNSTRAINED = 0.4
    PZ_ISO_Z_HALF_EXTENT_UNSTRAINED = 1.5
    PZ_ISO_R_XY_MAX_STRAINED = 0.35
    PZ_ISO_Z_HALF_EXTENT_STRAINED = 2.5

    pos_u, cell_u = build_schematic_equal_spacing_bilayer(
        ATOMS_PER_LAYER,
        INPLANE_NEIGHBOR_UNSTRAINED,
        LAYER_SEP_A_UNSTRAINED,
    )
    pos_s, cell_s = build_schematic_equal_spacing_bilayer(
        ATOMS_PER_LAYER,
        INPLANE_NEIGHBOR_STRAINED,
        LAYER_SEP_A_STRAINED,
    )

    # Same $(i,j)$ connectivity in both panels; strained bonds use ``pos_s``.
    bond_pair_indices = schematic_chain_bilayer_bond_pairs(ATOMS_PER_LAYER)

    fig = plt.figure(figsize=(10.2, 4.8), constrained_layout=True)

    ax0 = fig.add_subplot(1, 2, 1)
    title_a = "(a) Unstrained bilayer"
    if STRAIN_CELL0_UNSTRAINED != 0.0:
        title_a = rf"(a) Bilayer ($\varepsilon_{{a_1}} \approx {STRAIN_CELL0_UNSTRAINED*100:.1f}\%$)"
    panel_xz(
        ax0,
        title_a,
        pos_u,
        cell_u,
        LAYER_SEP_A_UNSTRAINED,
        r_xy_max_A=PZ_ISO_R_XY_MAX_UNSTRAINED,
        z_half_extent_A=PZ_ISO_Z_HALF_EXTENT_UNSTRAINED,
        ref_cc_A=INPLANE_NEIGHBOR_UNSTRAINED,
        bond_pair_indices=bond_pair_indices,
        show_strain_arrows=False,
    )

    ax1 = fig.add_subplot(1, 2, 2)
    panel_xz(
        ax1,
        rf"(b) Strain along $\mathbf{{a}}_1$ ($\varepsilon_{{a_1}} \approx {STRAIN_CELL0_STRAINED*100:.1f}\%$)",
        pos_s,
        cell_s,
        LAYER_SEP_A_STRAINED,
        r_xy_max_A=PZ_ISO_R_XY_MAX_STRAINED,
        z_half_extent_A=PZ_ISO_Z_HALF_EXTENT_STRAINED,
        ref_cc_A=INPLANE_NEIGHBOR_UNSTRAINED,
        bond_pair_indices=bond_pair_indices,
        show_strain_arrows=True,
    )

    fig.suptitle(
        r"Bilayer graphene: $p_z$-like lobes in the $xz$ plane (schematic envelopes, Å)"
        "\n(schematic negative $\\nu_{zz}$)",
        fontsize=12,
        fontweight="normal",
        y=1.02,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
