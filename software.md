---
layout: page
title: Software
permalink: /software/
---

Below are the main software packages I have developed and maintain.

---

## TETB_GRAPHENE

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

---

## BLG_model_builder

### Bilayer Graphene Model Uncertainty Quantification

![Language](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-ee4c2c.svg)

**Repository**: [https://github.com/dpalmer-anl/BLG_model_builder](https://github.com/dpalmer-anl/BLG_model_builder)

#### Description

A comprehensive toolkit for building and parameterizing bilayer graphene models. There are implementations for tight binding models, interatomic potentials, and total energy tight binding models. Both physics based and linear descriptor based models are available. This package provides tools for fitting model parameters to DFT/QMC data and includes uncertainty quantification capabilities.

## Key Features

- **Model Fitting**: functions to fit models to match ab initio reference data
- **Uncertainty Quantification**: Markov Chain Monte Carlo for uncertainty quantification

### Tight Binding models

- **Moon-Koshino (MK)**
- **Local Environment Tight Binding (LETB)**
- **linear descriptor based**

### Interatomic potentials

- **Tersoff**
- **Kolmgorov-Crespi (KC)**
- **Dihedral registry dependent potential (DRIP)**
- **Proper Orthogonal Descriptor potential (POD)**

### Total energy Tight Binding Model

- **linear descriptor based**

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

## AtomBridge

### Extracting crystallographic information for structure generation from STEM literature.

![Language](https://img.shields.io/badge/python-3.10+-blue.svg)

**Repository**: [https://github.com/dpalmer-anl/AtomBridge](https://github.com/dpalmer-anl/AtomBridge)

#### Description

This package was initially developed as part of the LLM-hackathon for Materials Science and Chemistry. This package uses an LLM agent to parse pdfs of STEM journal article, decides what are the relevant structures, and generates code for constructing a .cif file for the relevant structures to be used in simulations. The goal of this project is to make it easier for computational and experimental scientists to verify and compare their work.

Instructions on how to use and run this agent are given in README.md

