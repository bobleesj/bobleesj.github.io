---
layout: post
title: Python static type checking and automation (Ft. Mypy)
categories: python
---

## Motivation

Software tools are built using functions—reusable blocks that enhance our
productivity. Libraries like `numpy` provide functions that boost productivity.
However, the foundation of using functions effectively lies in writing excellent
ones that are clear, descriptive, and concise, in that order.

Type checking in Python is a powerful feature that helps achieve these goals by
adding type annotations to functions, though its application extends to
variables, classes, methods, and more.

## Toy examples

Consider a basic function example for beginners:

```python
def print_hello_world(name):
    print(f"Hello, {name}!")
```

In the above code, the parameter required is `name`. However, we can make it
clear that `name` should be a `str`:

```python
def print_hello_world(name: str):
    print(f"Hello, {name}!")
```

If there is a return value, you can specify its type using `-> str`:

```python
def return_hello_world(name: str) -> str:
    return f"Hello, {name}!"
```

## Practical examples

Now, let's look at a more practical example from research code. The following
returns a list of random numbers, either as `float` or `int`.

```python
def generate_random_numbers(
    count: int, low: int | float, high: int | float, is_float=True
) -> int | float:
    """
    Generate a list of random numbers (floating-point or integer).
    """
    if is_float:
        return [random.uniform(low, high) for _ in range(count)]
    else:
        return [random.randint(int(low), int(high)) for _ in range(count)]
```

The type information `int | float` provided in the function specifies explicitly
whether it returns a `float` or an `int`.

```python
min_dists = generate_random_numbers(100, 2.0, 4.0)  # float
atom_counts = generate_random_numbers(100, 1000, 3000, is_float=False)  # int
```

## Dyanmic vs static type checking

I have written extensive tutorials on `Swift`, a language that requires knowing
the type of each variable in advance. In contrast, Python allows dynamic typing,
where types can be assigned later:

```python
my_name = None
my_name = "Bob" # Dynamically typed as 'Str'
```

In Python, this is called dynamic typing, where the type of `my_name` is not
assigned initially but determined later as `str`.

In `Swift`, the type must be known and cannot change after complied,
illustrating static type checking:

```python
let my_name = "Bob"  # Static type inference
```

## Benefits of static type checking

Static type checking enhances the development experience by providing
autocomplete and function signatures in IDEs, as demonstrated in the
`generate_random_numbers` example above.

Additionally, static type checking may improve performance, potentially
improving performance by allowing the compiler to optimize based on known types.

## Automate

To minimize time spent on type-related bugs and maximize productivity,
automating type checks is crucial. `mypy` is a tool that can be installed and
run to check for type consistency:

We install via:

```bash
pip install mypy
mypy folder_path
```

`mypy` prints any potential errors found in the code. It is simple and
straightforward to use.

## Another example

Here is an example function that uses static typing to calculate distances:

```python
def calc_dist_two_cart_points(
    point1: list[float],
    point2: list[float],
) -> float:
    """
    Calculate the Euclidean distance between two points
    in Cartesian coordinates.
    """
    diff = np.array(point2) - np.array(point1)
    distance = float(np.linalg.norm(diff))

    return distance
```

## References

- https://peps.python.org/pep-0484/
- https://github.com/python/mypy
