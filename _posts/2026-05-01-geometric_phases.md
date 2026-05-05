---
title: "Geometric phases in quantum mechanics"
---

This blog post will explore geometric phases in physical systems. A geometric phase is the phase a system acquires along a closed loop. We'll look at two separate systems to try to understand what the geometric phase is, and the implications of a non-trivial phase.

## Spin 1/2 particle in a magnetic field

Let's start by examining the phase a spin 1/2 particle acquires as it rotates in a magnetic field. First, let's assume the $\mathbf{B}$ field rotates around $\hat{z}$ with frequency $\Omega$, with magnitude $B_{0}$. We can write the time dependent Hamiltonian of the system as,

$$H(t) = -\boldsymbol{\sigma}\mathbf{B}(t)$$

$$\mathbf{B}(t) = B_{0}[cos(\Omega t),sin(\Omega t),0]$$

$$\mathbf{n}(t) = \frac{\mathbf{B}(t)}{B_{0}}$$

Where we set the gyromagnetic ratio and Bohr magneton equal to 1. $\boldsymbol{\sigma}$ are the Pauli matrices. At each time $t$, the Hamiltonian is diagonal in the basis where $\mathbf{n}(t)$ defines the direction of the magnetic field. The instantaneous eigenstates are spin-up and spin-down along $\mathbf{B}(t)$.

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

These eigenstates rotate as the field rotates, adiabatically following the instantaneous ground state. 

Let's now try to understand what this geometrical phase is doing in this model Hamiltonian. In general, the eigenstates of a system will evolve with some phase, which we can rewrite into a dynamical and geometric phase. 

$$|\psi(t)\rangle = e^{i \phi t}|u(t)\rangle  = e^{i \phi_{dyn}(t)}e^{i \phi_{geom}(t)}|u(t)\rangle$$

The geometrical phase or Berry phase is then written as 

$$\gamma(t) = \int_{0}^{T} \mathbf{A}(t) dt $$

$$\mathbf{A}(t) = i \langle \chi_{+}(t)| \partial_{t}|\chi_{+}(t)\rangle$$

and after substituting for $\chi_{+}(t)$, we get

$$\mathbf{A}(t) = -\frac{\Omega}{2}$$

$$\gamma(t) = -\pi$$

So we see now that a spin 1/2 particle picks up an extra phase of $-\pi$ after rotating a full $360^{o}$ in the $\textbf{B}$ field.

## Aharonov–Bohm effect

It's hard to see why this extra phase of $-\pi$ even matters in the previous example. We know global phases cannot affect the probabilities of different states, but this geometric phase is different from a global one. The Aharonov-Bohm effect shows how the presence of this geometric phase actually affects the system. 
