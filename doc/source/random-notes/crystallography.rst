Crystallography
=================

.. note:: This is a work in progress.

    How do you simulate diffraciton patterns?


MSAE E3100/E4100 - Crystallography Prof. K. Barmak. I also used the book of Space Groups for SOlid State scientists by G. Burns M. Glazer.

Active operator vs. Passive operator

Active operator leaves the axies fixed, move the position vectors. Passive operator moves the axes of references.

.. math::

   \begin{bmatrix}
   x' \\
   y' \\
   z'
   \end{bmatrix}
   =
   \begin{bmatrix}
   a_{11} & a_{12} & a_{13} \\
   a_{21} & a_{22} & a_{23} \\
   a_{31} & a_{32} & a_{33}
   \end{bmatrix}
   \begin{bmatrix}
   x \\
   y \\
   z
   \end{bmatrix}


.. math::

    \boldsymbol{r}' = R \boldsymbol{r}


What is the crystal frame?

.. math::

    \{m[010]\}(x, y, z) = (x, -y, z)

Define lattice

An infinite array of points in space, in which each point has identical **surroundings**.

Define primitive cell
A unit cell that contains only one lattice point.

Define basis
The group of atoms and molecules is called the basis or the motif.


.. list-table::
   :header-rows: 1

   * - Crystal cystem
     - Conditions

   * - Triclinic
     - No conditions

   * - Monoclinic
     - :math:`\alpha = \beta = 90^\circ` (first setting),
       :math:`\alpha = \gamma = 90^\circ` (second setting)

   * - Orthorhombic
     - :math:`\alpha = \beta = \gamma = 90^\circ`

   * - Tetragonal
     - :math:`a = b; \alpha = \beta = \gamma = 90^\circ`

   * - Cubic
     - :math:`a = b = c; \alpha = \beta = \gamma = 90^\circ`

   * - Hexagonal
     - :math:`a = b; \alpha = \beta = 90^\circ; \gamma = 120^\circ`

   * - Trigonal
     - :math:`a = b; \alpha = \beta = 90^\circ; \gamma = 120^\circ`

   * - Rhombohedral
     - :math:`a = b = c; \alpha = \beta = \gamma`



Symmetry operations impose restrictions on the axes and angles used to define the lattice.

Symmetry --> Crystal system --> Bravais lattice --> Point group --> Space group --> Crystal structure

14 Bravais lattices
32 point groups
230 space groups

Here is an exmaple of applying the symmetry operations to the monoclinic system 

.. math::
    \boldsymbol{r}' = \{2[200]\}\boldsymbol{r} =
    \begin{bmatrix}
    -1 & 0 & 0 \\
    0 & -1 & 0 \\
    0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
    x \\
    y \\
    z
    \end{bmatrix}
    = 
    -xa = yb + zc    


Crystal lattice 
^^^^^^^^^^^^^^^

Square braekts denote a single direction, .i.g., [uvw]
Angled brakets denote a family of directions related by symmetry <uvw>

For a given crystal with basis vectors a, b, c the metric entric in the crystalogrpahic reference is given by 

The metric tensor is dot products of the lattice vectors. The product between two vectors :math:`u` and :math:`v` is given by

.. math::

    \boldsymbol{u} \cdot \boldsymbol{v} = u_x v_x + u_y v_y + u_z v_z = |\boldsymbol{u}| |\boldsymbol{v}| \cos \theta

What is the metric tensor?

.. math::

    \alpha &= \angle(\mathbf{b}, \mathbf{c}) \\
    \beta &= \angle(\mathbf{a}, \mathbf{c}) \\
    \gamma &= \angle(\mathbf{a}, \mathbf{b})

.. math::

    \mathbf{a} \cdot \mathbf{a} &= a^2 \\
    \mathbf{a} \cdot \mathbf{b} &= ab \cos \gamma \\
    \mathbf{a} \cdot \mathbf{c} &= ac \cos \beta \\
    \mathbf{b} \cdot \mathbf{b} &= b^2 \\
    \mathbf{b} \cdot \mathbf{c} &= bc \cos \alpha \\
    \mathbf{c} \cdot \mathbf{c} &= c^2 \\

.. math::

    g_{\text{triclinic}} =
    \begin{pmatrix}
    a^2 & ab \cos \gamma & ac \cos \beta \\
    ab \cos \gamma & b^2 & bc \cos \alpha \\
    ac \cos \beta & bc \cos \alpha & c^2
    \end{pmatrix}

    \quad
    g_{\text{monoclinic}} =
    \begin{pmatrix}
    a^2 & 0 & ac \cos \beta \\
    0 & b^2 & 0 \\
    ac \cos \beta & 0 & c^2
    \end{pmatrix}

    \quad
    g_{\text{orthorhombic}} =
    \begin{pmatrix}
    a^2 & 0 & 0 \\
    0 & b^2 & 0 \\
    0 & 0 & c^2
    \end{pmatrix}


Now I want to find the lenght of the vector in real-space from the origin. How do I do that?

I mean I understand that the metric tensors are used to calculate distances and angles.

