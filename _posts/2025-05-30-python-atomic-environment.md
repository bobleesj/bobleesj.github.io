---
layout: post
title: Python calcuclate atomic environment with .cif (Ft. ASE)
categories: tutorial
---

### Installation

```bash
pip install ase
```

### Example 1. Find all pair distances

```python
from ase.io import read, write
from ase.build import make_supercell
from ase.neighborlist import neighbor_list

# Load and create supercell as previously done
structure = read("cif/URhIn.cif")
scale = 1
scaling_matrix = [[scale, 0, 0], [0, scale, 0], [0, 0, scale]]
supercell = make_supercell(structure, scaling_matrix)

# write("supercell_POSCAR", supercell, format="vasp")
write("supercell.cif", supercell, format="cif")

# Set a cutoff distance
cutoff = 3.9

# Find neighbors within the cutoff distance
i, j, d = neighbor_list("ijd", supercell, cutoff)

# Distance information
for idx in range(len(i)):

    print(
        f"Atom {i[idx]} ({supercell[i[idx]].symbol})"
        f" Atom {j[idx]} ({supercell[j[idx]].symbol}) Dist: {d[idx]:.2f} Å"
    )

print(f"Number of atoms in supercell: {len(supercell)}")
```

Output

```text
Atom 0 (In) Atom 8 (Rh) Dist: 2.70 Å
Atom 0 (In) Atom 4 (U) Dist: 3.29 Å
Atom 0 (In) Atom 3 (U) Dist: 3.21 Å
Atom 0 (In) Atom 0 (In) Dist: 3.88 Å
Atom 0 (In) Atom 0 (In) Dist: 3.88 Å
Atom 0 (In) Atom 6 (Rh) Dist: 2.85 Å
Atom 0 (In) Atom 5 (U) Dist: 3.29 Å
Atom 0 (In) Atom 1 (In) Dist: 3.24 Å
Atom 0 (In) Atom 5 (U) Dist: 3.29 Å
Atom 0 (In) Atom 4 (U) Dist: 3.29 Å
Atom 0 (In) Atom 3 (U) Dist: 3.21 Å
Atom 0 (In) Atom 2 (In) Dist: 3.24 Å
```

### Source code
