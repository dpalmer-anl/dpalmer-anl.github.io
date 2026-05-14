GlowScript 3.2 VPython
# B(t) uniform in xy plane, rotating about z; particle at origin.
# Yellow arrow = |chi_+> eigenvector along +n_hat (with B); orange = |chi_-> along -n_hat.

scene = canvas(width=900, height=600, autoscale=False, title="Rotating B + spin eigenvectors at origin")
scene.center = vec(0, 0, 0)
scene.background = vec(0.02, 0.02, 0.06)
scene.camera.pos = vec(1, 1, 1)
scene.camera.axis = vec(-1, -1, -1)
scene.up = vec(0, 0, 1)
scene.range = 1.65

period_B = 10
Omega = 2 * pi / period_B

ball_r = 0.09
L_evec = 0.52

L_line = 1.05
n_lines = 11
spacing = 0.18
shaft_field = 0.014
shaft_spin = 0.02

field_arrows = []
for k in range(-(n_lines // 2), n_lines // 2 + 1):
    field_arrows.append(
        arrow(shaftwidth=shaft_field, color=vec(0.35, 0.75, 1), round=True, opacity=0.9)
    )

particle = sphere(pos=vec(0, 0, 0), radius=ball_r, color=color.red, shininess=0.35)
arrow_chi_plus = arrow(pos=vec(0, 0, 0), axis=vec(L_evec, 0, 0), shaftwidth=shaft_spin, color=color.yellow, round=True)
arrow_chi_minus = arrow(pos=vec(0, 0, 0), axis=vec(-L_evec, 0, 0), shaftwidth=shaft_spin, color=color.orange, round=True)

t = 0
dt = 0.016

def B_hat(tt):
    return -1 * vec(cos(Omega * tt), sin(Omega * tt), 0)

while True:
    rate(60)
    n = B_hat(t)
    perp = vec(-n.y, n.x, 0)
    mp = mag(perp)
    if mp > 1e-6:
        perp = perp / mp
    else:
        perp = vec(0, 1, 0)

    idx = 0
    for k in range(-(n_lines // 2), n_lines // 2 + 1):
        base = perp * (k * spacing)
        a = field_arrows[idx]
        a.pos = base - L_line * n
        a.axis = 2 * L_line * n
        idx += 1

    particle.pos = vec(0, 0, 0)
    arrow_chi_plus.pos = vec(0, 0, 0)
    arrow_chi_plus.axis = L_evec * n
    arrow_chi_minus.pos = vec(0, 0, 0)
    arrow_chi_minus.axis = -L_evec * n

    t = t + dt
