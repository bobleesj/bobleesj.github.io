---
layout: post
title: Python matrix operations and linear algebra cheatsheet (Ft. NumPy)
categories: tutorial
---

## Motivation

A matrix represents a set of values. Matrices are used in solving a system of
equations, representing graphs, etc. The more concisely and clearly we represent
matrices in scripts, the less time is required for debugging.

Here I document `NumPy` matrix functions. In coursework, I used them for
training neural networks and approximating a solution to the Schrödinger
equation.

The document serves as a concise reference for my research. Examples are based
on my own work or borrowed from the links referenced.

### Group operations

Assume `X` and `Y` represent matrices and `vec` is an 1-D array.

```python
np.add(X,Y)       # Add
np.substract(X,Y) # Substract
np.divide(X,Y)    # Divide

# Multiply, all same
X @ Y             # recommended
np.multiply(X,Y)
np.matmul(X, Y)
np.dot(X, Y)
X.dot(Y)
```

### Individual operations

```python
X.flatten()        # Flatten
np.sqrt(X)         # Square root all elements
np.sum(X)          # Sum all elements
np.sum(X,axis=0)   # Row-wise sum
np.sum(X,axis=1)   # Column-wise sum
np.amax(X)         # Single max value
np.amax(X, axis=0) # Get max in each column
np.amax(X, axis=1) # Get max in each row
np.mean(X)         # Mean
np.std(X)          # Standard deviation
np.var(X)          # Variance
np.trace(X)        # Sum of the elements on the diagonal
np.linalg.matrix_rank(X)  # Rank of the matrix
np.linalg.det(X)   # Determinant of the matrix
```

### Individual manipulation

```python
X[0, 1]  # Get value from 1st row, 2nd col
X[0, 1] = 1 # Update
```

### 1D slicing

```python
vec = list(range(10)) # [1, ..., 9]
vec[4:8]       # [4, 5, 6, 7]
vec[-5:-2]     # 5th last to 2nd last => [5, 6, 7]

# Get every Nth index value
vec[::2]      # [0, 2, 4, 6, 8]
vec[::5]      # [0, 5]

# Inverse
vec[::-1]     # Temp inverse [9, 8, ... 1, 0]
vec.reverse() # Permanent inverse
```

### 2D slicing

```python
X =  vec.reshape((3, 3))
X[1, :]       # get second row
X[:, -1]      # get last col
X[0:2, :]     # get first two rows
X[[0, 2], :]  # get first and thrid rows
X[:, 0:2]     # get first two columns
X[:, [0, 2]]  # get first and thrid columns
X[0:2, 0:2]   # get submatrix of first two rows/columnes
X[X > 5]      # get elements greater than 5

# Advanced
X[:, ::-1]    # reverse cols for each row
=> [[3 2 1]
    [6 5 4]
    [9 8 7]]
X[1:, ::-1]   # same as above but skip first row
=> [[6 5 4]
    [9 8 7]]
```

### Booleon Indexing

```python
cols = X[0, :] > 1  # select col(s) where first row > 1
=> [False  True  True]
X[:, cols]
=> [[2 3]
    [5 6]
    [8 9]]
```

### Matrix creation

```python
np.matrix(np.arange(12).reshape((3,4)))
np.zeros((5,), dtype=int)
np.zeros((2, 1))

# Copy
X = np.arange(6)
X = X.reshape((2, 3))
np.copy(X)              # Copy X
np.ones_like(X)         # Return 1's with (2,3) shape
np.zeros_like(X)        # Return 0's with (2,3) shape

# Full
np.full((2, 2), 10)     # Generate (2,2), all 10
np.full((2, 2), np.inf) # Generate (2,2), all inf
np.full((2, 2), [1, 2]) # Generate (2,2), each row of [1,2]
```

### Others

```python
np.set_printoptions(
    precision=3,   # Set decimal places
    suppress=True, # Avoid scientific notations
    threshold=100, # Max number of elements to be printed
    linewidth=80,
    edgeitems=2    # Show two values per edge when truncated
)
```

### References

- https://numpy.org/doc/stable/reference/generated/numpy.matrix.all.html
- https://note.nkmk.me/en/python-numpy-matrix/
- https://note.nkmk.me/en/python-numpy-ndarray-slice/
