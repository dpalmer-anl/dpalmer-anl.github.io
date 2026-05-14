---
title: "Geometric phases in quantum mechanics"
---

This blog post will explore geometric phases in physical systems. A geometric phase is the phase a system acquires along a closed loop. We'll look at two separate systems to try to understand what the geometric phase is, and the implications of a non-trivial phase.

# What is a geometric phase ? (Deriving the Berry phase)

To first answer the question of what a geometric phase is, let's first think about how a quantum system evolves with time.

If a system evolves adiabatically, the system will remain in its initial eigenstate. If we have a two state system, we have two eigenstates $\lvert \chi_{+} \rangle$ and $\lvert \chi_{\text{-}} \rangle$. Assume at t=0, the system is in $\lvert \chi_{+} \rangle$. When a quantum state evolves under a time-dependent Hamiltonian, it acquires phase. We can decompose this total phase into two parts:

$$\lvert\psi(t)\rangle = e^{i\phi_{dyn}(t)} e^{i\phi_{geom}(t)} \lvert\chi_{+}(t)\rangle$$

The **dynamical phase** $\phi_{dyn}(t)$ is the familiar phase from time evolution:

$$\phi_{dyn}(t) = -\frac{1}{\hbar}\int_0^t E(\chi_+(t')) dt'$$

where $E(\chi_+)$ is the instantaneous energy eigenvalue. This is the phase you'd get from solving the time-dependent Schrödinger equation.

The **geometric phase** $\phi_{geom}(t)$ is something different — it's an *extra* phase that comes from how we are changing the Hamiltonian. Even if we subtract off the dynamical phase, the state still picks up phase as we move along the path of eigenstates. This phase depends on the *shape* of the path through eigenspace, not on how fast we traverse it.

To isolate the geometric phase, imagine a state $\lvert\chi_{+}(t)\rangle$ evolves as:

$$\lvert\psi(t)\rangle = e^{i\phi(t)} \lvert\chi_{+}(t)\rangle$$

For an infinitesimal time step, the state must remain normalized and remain in the instantaneous eigenspace. Let's plug this equation into the time dependent Schrodinger equation.

$$i \hbar \frac{d\lvert \psi \rangle}{dt} = H(t)\lvert \psi \rangle = E(t) \lvert \psi \rangle$$

$$ i \hbar \frac{d\lvert \psi \rangle}{dt} = i \frac{d\lvert \phi \rangle}{dt}e^{i \phi}\lvert \chi_{+} \rangle + e^{i \phi}\frac{\lvert \chi_{+} \rangle}{dt} = E(t)\lvert \chi_{+} \rangle $$

Taking the inner product with $\langle \chi_{+} \lvert$ then gives

$$ -\hbar \frac{d\phi}{dt} + i \hbar \langle \chi_{+} \lvert \frac{d\lvert \chi_{+} \rangle}{dt} = E(t) $$

now if we split $\phi = \phi_{geom} + \phi_{dyn}$, we can write,

$$  -\hbar \left( \frac{d\phi_{geom}}{dt} + \frac{d\phi_{dyn}}{dt} \right)+ i \hbar \langle \chi_{+} \lvert \frac{d\lvert \chi_{+} \rangle}{dt} = E(t) $$

Simplifying this expression using the above equation for $\phi_{dyn}$ as the integral of E w.r.t. to t gives,

$$ -\hbar \frac{d\phi}{dt} + i \hbar \langle \chi_{+} \lvert \frac{d\lvert \chi_{+} \rangle}{dt} = 0 $$ 

Writing the full equation for $d\phi_{geom}$ gives us the definition of the Berry connection.

$$\mathbf{A}(t) = d \phi_{geom} = i\langle\chi_+(t)\lvert\partial_t\lvert\chi_+(t)\rangle$$

The geometrc phase acquired over the period t, is then the integral of the Berry connection. This is called the Berry phase.

$$\phi_{geom} = \int_0^t \mathbf{A}(t') dt'$$

## Spin 1/2 particle in a magnetic field

Let's use a concrete example to understand the Berry phase. Consider a spin 1/2 particle in a rotating magnetic field. First, let's assume the $\mathbf{B}$ field rotates around $\hat{z}$ with frequency $\Omega$, magnitude $B_{0}$, and azimuthal angle $\theta$. We can write the time dependent Hamiltonian of the system as,

$$H(t) = -\boldsymbol{\sigma}\mathbf{B}(t)$$

$$\mathbf{B}(t) = B_{0}[sin(\theta)cos(\Omega t),sin(\theta)sin(\Omega t),cos(\theta)]$$

$$\mathbf{n}(t) = \frac{\mathbf{B}(t)}{B_{0}}$$

Where we set the gyromagnetic ratio and Bohr magneton equal to 1. $\boldsymbol{\sigma}$ are the Pauli matrices. At each time $t$, the Hamiltonian is diagonal in the basis where $\mathbf{n}(t)$ defines the direction of the magnetic field. The instantaneous eigenstates are spin-up and spin-down along $\mathbf{B}(t)$.

<figure class="post-animation-embed">
  <img src="{{ '/assets/images/geometric-phases-spin-static.png' | relative_url }}" alt="xy-plane diagram: parallel B-field lines, spin at the origin, arrows along plus and minus B for the instantaneous eigenstates, curved arrow for rotation of B." loading="lazy" decoding="async" />
</figure>

To find them, we need to solve:

$$
(\mathbf{n}(t) \cdot \boldsymbol{\sigma})  = \lvert \chi_{+}(t) \rangle
$$

We can rotate the spin-up $S_z$ eigenstates to the $x$-axis to find $\lvert \chi_{+}(t) \rangle$. Starting with the spin-up state along $z$:

$$
\lvert {\uparrow}_z \rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

We rotate it to align with $\mathbf{n}(t)$. The rotation takes us from the $z$-axis to the direction $\mathbf{n}(t)$. Using spherical coordinates where $\mathbf{n}(t)$ has azimuthal angle $\phi(t) = \Omega t$ and polar angle $= \pi/2$:

$$
\lvert \chi_{+}(t) \rangle = \begin{pmatrix} \cos(\theta/2) \\ e^{i\Omega t}\sin(\theta/2) \end{pmatrix}
$$

You can verify this satisfies $\mathbf{n}(t) \cdot \boldsymbol{\sigma} \lvert \chi_{+}(t) \rangle = \lvert \chi_{+}(t) \rangle$.

Similarly, the spin-down eigenstate is:

$$
\lvert \chi_{-}(t) \rangle = \begin{pmatrix} -\sin(\theta/2) \\ e^{i\Omega t}\cos(\theta/2) \end{pmatrix}
$$

These eigenstates rotate as the field rotates, adiabatically following the instantaneous ground state. This adiabatic condition requires $\Omega \ll B_0$ — so the field rotates much slower than the frequency of the dynamical phase of the spin.

Spin-$1/2$ particle **at the origin** in a rotating $\mathbf{B}$ field. The **yellow** and **orange** arrows are the instantaneous eigenvectors. $\lvert\chi_{+}(t)\rangle$ and $\lvert\chi_{-}(t)\rangle$.

### Computing the Berry Phase for the spin 1/2 system

Now let's calculate $\mathbf{A}(t)$ using our explicit eigenstate:

$$\lvert\chi_+(t)\rangle = \begin{pmatrix} \cos(\theta/2) \\ e^{i\Omega t}\sin(\theta/2) \end{pmatrix}$$

Taking the time derivative:

$$\partial_t\lvert\chi_+(t)\rangle = \begin{pmatrix} 0 \\ i\Omega e^{i\Omega t}\sin(\theta/2) \end{pmatrix}$$

Computing the inner product:

$$\langle\chi_+(t)\lvert\partial_t\lvert\chi_+(t)\rangle = \begin{pmatrix} \cos(\theta/2) & e^{-i\Omega t}\sin(\theta/2) \end{pmatrix} \begin{pmatrix} 0 \\ i\Omega e^{i\Omega t}\sin(\theta/2) \end{pmatrix}$$

$$= e^{-i\Omega t}\sin(\theta/2) \cdot i\Omega e^{i\Omega t}\sin(\theta/2) = i\Omega\sin^2(\theta/2)$$

Therefore:

$$\mathbf{A}(t) = i \cdot i\Omega\sin^2(\theta/2) = -\Omega\sin^2(\theta/2)$$

Using the identity $\sin^2(\theta/2) = \frac{1-\cos\theta}{2}$:

$$\mathbf{A}(t) = -\frac{\Omega}{2}(1 - \cos\theta)$$

For one complete rotation (from $t=0$ to $t=2\pi/\Omega$), the geometric phase is:

$$\phi_{geom} = \int_0^{2\pi/\Omega} \mathbf{A}(t) dt = -\frac{\Omega}{2}(1-\cos\theta) \cdot \frac{2\pi}{\Omega} = -\pi(1-\cos\theta)$$

So we see that a spin 1/2 particle picks up an extra phase of $-\pi(1-\cos\theta)$. For the special case of rotation around $\hat{z}$ in the xy  plane, ($\theta = \pi/2$), $\phi_{geom} = -\pi$ This phase is purely geometric: it depends only on the solid angle enclosed by the path, not on how fast the field rotates.

<figure class="post-animation-embed">
  <img src="{{ '/assets/images/geometric-phase-3d.png' | relative_url }}" alt="3D diagram: geometric phase versus time mod T on a circle in the xy plane, phase plotted vertically; vertical connectors and a red bracket marking the Berry phase mismatch when the loop closes." loading="lazy" decoding="async" />
</figure>
