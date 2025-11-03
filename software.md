---
layout: page
title: Software
permalink: /software/
---

# Software & Open Source Projects

I am committed to open science and reproducible research. Below are the main software packages I have developed and maintain.

---

## TETB_GRAPHENE

<div class="software-card">

### Total Energy Tight Binding for Graphene Systems

![Language](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Repository**: [https://github.com/Johnson-Research-Group/TETB_GRAPHENE](https://github.com/Johnson-Research-Group/TETB_GRAPHENE)

#### Description

A Python package for calculating forces, energies, and band structures for multi-layer graphene systems using the Total Energy Tight Binding method. This package enables accurate quantum mechanical simulations at scales that were previously only accessible to classical force fields.

#### Key Features

- **Force & Energy Calculations**: Compute atomic forces and total energies for arbitrary graphene configurations
- **Band Structure**: Calculate electronic band structures including the effects of twist angles and strain
- **Geometry Optimization**: Relax atomic positions to find minimum energy structures
- **LAMMPS Integration**: Hybrid potential combining tight-binding with interatomic potentials
- **GPU Acceleration**: CUDA/CuPy implementation for systems with 10,000+ atoms
- **ASE Interface**: Compatible with the Atomic Simulation Environment

#### Installation

```bash
# Clone the repository
git clone https://github.com/Johnson-Research-Group/TETB_GRAPHENE.git
cd TETB_GRAPHENE

# Install pylammps (requires virtual environment)
python lammps_installer.py

# Install TETB_GRAPHENE
pip install .
```

#### Quick Start Example

```python
from TETB_GRAPHENE import TETB_GRAPHENE_calc
from ase.build import graphene

# Create a graphene structure
atoms = graphene(size=(10, 10, 1))

# Initialize the TETB model
model_dict = dict({"tight binding parameters":{"interlayer":"popov","intralayer":"porezag"},
                        "basis":"pz",
                        "kmesh":(11,11,1),
                        "parallel":"serial", #other options for parallel include "dask" (good for multinode cases) and "serial"
                        "intralayer potential":"Pz rebo",
                        "interlayer potential":"Pz KC inspired",
                        'output':"grapheneCalc"})
calc = TETB_GRAPHENE_calc.TETB_GRAPHENE_Calc(model_dict)

# Calculate energy and forces
atoms.calc = calc
energy = atoms.get_total_energy(atoms)
forces = atoms.get_forces(atoms)

# Calculate band structure
Gamma = [0,   0,   0]
K = [2/3,1/3,0]
Kprime = [1/3,2/3,0]
M = [1/2,0,0]
sym_pts=[K,Gamma,M,Kprime]
nk=40
kdat = calc_obj.k_path(sym_pts,nk)
kpoints = kdat[0]
bands = calc.get_band_structure(atoms, kpath)
```

#### Documentation

See the [README](https://github.com/Johnson-Research-Group/TETB_GRAPHENE/blob/main/README.md) and `tests/example_usage.py` for more examples.

</div>

---

## BLG_model_builder

<div class="software-card">

### Bilayer Graphene Model Uncertainty Quantification

![Language](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-ee4c2c.svg)

**Repository**: [https://github.com/dpalmer-anl/BLG_model_builder](https://github.com/dpalmer-anl/BLG_model_builder)

#### Description

A comprehensive toolkit for building and parameterizing bilayer graphene models using total energy tight binding approaches. This package provides tools for fitting model parameters to DFT/QMC data and includes uncertainty quantification capabilities.

#### Key Features

- **Parameter Optimization**: Advanced fitting algorithms to match ab initio reference data
- **optional PyTorch Backend**: automatic differentiation, gpu acceleration
- **Uncertainty Quantification**: Markov Chain Monte Carlo for rigorous uncertainty estimates

#### Installation

```bash
# Clone the repository
git clone https://github.com/dpalmer-anl/BLG_model_builder.git
cd BLG_model_builder

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

</div>

---

## Contributing

I welcome contributions to any of these projects! Please see the individual repositories for contribution guidelines. Feel free to:
- Report bugs and request features via GitHub issues
- Submit pull requests with improvements
- Contact me for collaboration opportunities

---

## Dependencies & Acknowledgments

These packages build upon excellent open-source software including:
- [ASE](https://wiki.fysik.dtu.dk/ase/) - Atomic Simulation Environment
- [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/) - Scientific computing
- [PyTorch](https://pytorch.org/) - Machine learning and optimization
- [LAMMPS](https://lammps.sandia.gov/) - Molecular dynamics
- [EMCEE](https://emcee.readthedocs.io/en/stable/) - Markov Chain Monte Carlo

---

## Support

For questions or support, please:
1. Check the documentation in each repository
2. Open an issue on GitHub
3. Contact me directly at [dpalmer3@illinois.edu](dpalmer3@illinois.edu)

