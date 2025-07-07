# Time-Independent Schrödinger Wave Equation Solver

This project was developed as the Final Year Project (FYP) for a Bachelor's degree in Physics. It focuses on solving the **Time-Independent Schrödinger Wave Equation (TISE)** — a cornerstone of quantum mechanics — using both **analytical methods** and **numerical simulations** implemented in Python.

---

## 🧠 Overview

The Time-Independent Schrödinger Equation describes quantum behavior at the microscopic level. This project explores how wavefunctions and particle probabilities behave under different quantum mechanical potentials. Both **analytical** and **numerical** methods are used to solve TISE, and results are compared through visualizations of eigenfunctions and energy spectra.

---

## 🔬 Potentials Analyzed

The Schrödinger Equation was solved for the following 1D potentials:

- 📦 **Infinite Square Well**
- 🎯 **Quantum Harmonic Oscillator**
- 🌀 **Double-Well Potential**

Each potential includes:

- Analytical solution (if applicable)
- Numerical simulation using Finite Difference Method (FDM)
- Graphical comparison and interpretation

---

## 🧮 Methodology

### Analytical Approach
Standard quantum mechanics techniques were used to derive closed-form solutions for solvable potentials like the square well and harmonic oscillator.

### Numerical Approach
We applied the **Finite Difference Method (FDM)** to discretize the Schrödinger equation and solve it as a matrix eigenvalue problem:

- Constructed potential energy arrays
- Built Hamiltonian matrices
- Solved for eigenvalues and eigenfunctions using NumPy and SciPy
- Visualized results using Matplotlib

---

## 🛠️ Tools & Technologies

- **Python** — main programming language
- **NumPy** / **SciPy** — for matrix operations and eigenvalue problems
- **Matplotlib** — for plotting wavefunctions and energy levels
- **Jupyter Notebooks** — for interactive development

---

## 📁 Project Structure

TISE-Solver-FYP/
│
├── infinite_square_well/
│ ├── analytical_solution.py
│ ├── numerical_solution.py
│ └── results/
│
├── harmonic_oscillator/
│ ├── analytical_solution.py
│ ├── numerical_solution.py
│ └── results/
│
├── double_well_potential/
│ ├── numerical_solution.py
│ └── results/
│
├── utils/
│ └── fdm_solver.py
│
├── README.md
└── Report.pdf (optional: full research report)
