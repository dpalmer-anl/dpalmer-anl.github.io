---
layout: page
title: Research
permalink: /research/
---

My research focuses on developing efficient and accurate computational methods for studying electronic and mechanical propeties of two-dimensional materials, with a particular emphasis on graphene-based systems. I aim to understand the connection between electronic properties and mechanical properties in 2D materials using various tools such as DFT, Tight Binding, Interatomic potentials, Machine Learning and Uncertainty Quantification.

---

## Electronic and structural properties of twisted Bilayer Graphene

I have developed a semi-empirical Total Energy Tight Binding (TETB) parameterization for bilayer graphene. This approach combines electronic structure information into the total energy calculation. These types of models allow us to understand how the band structure might alter the relaxed structure and tBLG's elastic properties and vice versa.

<div class="research-figure-row">
<figure>
  <img src="{{ '/assets/images/bilayer_graphene_poisson_ratio_pz.png' | relative_url }}" alt="Schematic bilayer graphene Poisson response and pz-related physics." loading="lazy" decoding="async" />
  <figcaption>Li, Xiaowen, et al., &ldquo;Tunable negative Poisson&rsquo;s ratio in van der Waals superlattice,&rdquo; <em>Research</em> (2021).</figcaption>
</figure>
<figure>
  <img src="{{ '/assets/images/poisson_ratio_nanoribbon.jpeg' | relative_url }}" alt="Negative Poisson's ratio in a single-layer graphene nanoribbon." loading="lazy" decoding="async" />
  <figcaption>Jiang, Jin-Wu, and Harold S. Park, &ldquo;Negative Poisson&rsquo;s ratio in single-layer graphene ribbons,&rdquo; <em>Nano Letters</em> 16.4 (2016): 2657&ndash;2662.</figcaption>
</figure>
<figure>
  <img src="{{ '/assets/images/tblg_corrugation.png' | relative_url }}" alt="Corrugation in twisted bilayer graphene." loading="lazy" decoding="async" />
</figure>
</div>

---

## Uncertainty Quantification for Bilayer Graphene Models

Calculated properties for bilayer graphene and tBLG are extremely sensitive to the models used and the underlying training data. I am quantifying uncertainties in these models and seeing how these uncertainties propagate to different quantities of interest. Particularly I am investigating the uncertainty in tBLG structures and their magic angle properties.

<div class="research-figure-row">
<figure>
  <img src="{{ '/assets/images/mcmc_sampling_cost_function.png' | relative_url }}" alt="Markov-chain Monte Carlo samples exploring a cost function landscape." loading="lazy" decoding="async" />
  <figcaption>Markov-chain Monte Carlo samples of a cost function, image courtesy of <a href="https://arogozhnikov.github.io/2016/12/19/markov_chain_monte_carlo.html">https://arogozhnikov.github.io/2016/12/19/markov_chain_monte_carlo.html</a>.</figcaption>
</figure>
<figure>
  <img src="{{ '/assets/images/band_structure_TETB_popov_mcmc_t_0.99.png' | relative_url }}" alt="Uncertainty in magic-angle twisted bilayer graphene band structure from MCMC." loading="lazy" decoding="async" />
  <figcaption>Uncertainty in magic angle band structure.</figcaption>
</figure>
</div>

## Computational Methods & Tools

My research involves development and application of various computational methods:

- **Electronic Structure**: Tight-binding models, DFT (Quantum ESPRESSO), and continuum models
- **Molecular Dynamics**: LAMMPS and ASE integration for large-scale atomistic simulations
- **Machine Learning**: Gaussian Processes and Neural Networks
- **Uncertainty Quantification**: Markov Chain Monte Carlo, Bootstrapping, Gaussian Processes
- **High-Performance Computing**: Parallel algorithms and GPU acceleration
- **Scientific software skills**: NumPy, SciPy, PyTorch, JAX, ASE, c++

