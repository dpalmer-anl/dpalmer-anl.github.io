---
layout: page
title: Research
permalink: /research/
---

My research focuses on developing efficient and accurate computational methods for studying electronic and mechanical propeties of two-dimensional materials, with a particular emphasis on graphene-based systems. I aim to understand the connection between electronic properties and mechanical properties in 2D materials using various tools such as DFT, Tight Binding, Interatomic potentials, Machine Learning and Uncertainty Quantification.

---

## Total Energy Tight Binding for Bilayer Graphene

<div class="research-project">

### Overview

I have developed a semi-empirical Total Energy Tight Binding (TETB) parameterization for bilayer graphene that is transferable to arbitrary interlayer separation, local disregistry, and twist angle. The approach combines electronic structure information into the total energy calculation and allows us to recreate the potential energy surface fitted to Quantum Monte Carlo (QMC) and DFT total energy data. This enables large-scale calculations (tens of thousands of atoms) with QMC-accurate total energies and built-in electronic structure dependence.

### Key Results

- **Magic angle dependent on relaxation model**: The magic angle for twisted Bilayer Graphene changes depending on which model is used to relax the system. Biaxial strain does not change the magic angle for systems relaxed with TETB.
- **Realistic mechanics**: TETB Predicts negative out-of-plane Poisson ratio comparable to DFT, capturing strain effects on magic angles that classical potentials miss
- **Large-Scale Capability**: Enables relaxation of twisted bilayer graphene structures with as many as 16,876 atoms (θ = 0.88°), orders of magnitude faster than DFT


</div>

---

## Bilayer Graphene Model Uncertainty Quantification

<div class="research-project">

### Overview

I have used Markov Chain Monte Carlo to quantify and propagate uncertainties for total energy and tight binding models for bilayer graphene. This works aims to show how much uncertainty in our calculations we can expect. For example, how much uncertainty is there in the band width of twisted Bilayer Graphene given a specific model and dataset.

</div>


## Computational Methods & Tools

My research involves development and application of various computational methods:

- **Electronic Structure**: Tight-binding, DFT (Quantum ESPRESSO), and hybrid approaches
- **Molecular Dynamics**: LAMMPS and ASE integration for large-scale atomistic simulations
- **Machine Learning**: Gaussian Process and Neural Networks
- **High-Performance Computing**: Parallel algorithms and GPU acceleration
- **Scientific software skills**: NumPy, SciPy, PyTorch, JAX, ASE, c++

