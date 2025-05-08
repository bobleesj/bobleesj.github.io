---
layout: post
title: Python best practices and cheatsheet
categories: tutorial
---

My materials science projects matured with features. Now, I acquire and apply
best practices in Python.

Often the best way to learn or improve one's skill acquring the ability to
discern bad and good practices.

I use this documentation as the main reference to refactor and improve _my
code_.

This blog post remains updated. Examples were acquired from online sources and
documentation, as noted in the references section.

---

- [Section 1. Best practices](#section-1-best-practices)
  - [`isClose` instead of `round` for comparing values](#isclose-instead-of-round-for-comparing-values)
  - [Check for simpler solutions](#check-for-simpler-solutions)
    - [Adding two arrays](#adding-two-arrays)
    - [Whether an element exists](#whether-an-element-exists)
    - [Applying element-wise simple operations](#applying-element-wise-simple-operations)
  - [`|` to merge two dictionaries](#-to-merge-two-dictionaries)
  - [`Counter` to find frequency](#counter-to-find-frequency)
  - [`lambda` function](#lambda-function)
    - [Example 1. Sort `dict`](#example-1-sort-dict)
    - [Example 2. Sort `list`](#example-2-sort-list)
  - [`open` instead of `finally`](#open-instead-of-finally)
  - [`enumerate` instead of `range` for loop](#enumerate-instead-of-range-for-loop)
    - [Example 1. `list`](#example-1-list)
    - [Example 2. `dict`](#example-2-dict)
  - [Use `_` for large numbers](#use-_-for-large-numbers)
  - [Return `None`](#return-none)
  - [`main()`](#main)
  - [Documentation](#documentation)
  - [Use type hints](#use-type-hints)
  - [Comprehensions](#comprehensions)
    - [Example 1. Modify](#example-1-modify)
    - [Example 2. Add condition](#example-2-add-condition)
  - [Zip](#zip)
    - [Example 1. iterate two arrays](#example-1-iterate-two-arrays)
    - [Example 2. `enumerate`](#example-2-enumerate)
  - [Use `perf_counter()` for time](#use-perf_counter-for-time)
    - [Use comprehension](#use-comprehension)
    - [Use Lambda](#use-lambda)
- [Section 2. NumPy](#section-2-numpy)
  - [Create array](#create-array)
  - [Reshape array](#reshape-array)
  - [Broadcast](#broadcast)
    - [Example 1. Constant addition](#example-1-constant-addition)
    - [Example 2. Addition between two arrays](#example-2-addition-between-two-arrays)
    - [Example 3. Multiplication between two arrays](#example-3-multiplication-between-two-arrays)
  - [Apply universal functions](#apply-universal-functions)
- [Section 3. Prompt](#section-3-prompt)
  - [Get user input with option selection](#get-user-input-with-option-selection)
- [Section 4. Pandas](#section-4-pandas)
  - [Read CSV](#read-csv)
  - [Save CSV](#save-csv)
- [Section 5. Math](#section-5-math)
  - [Sympy](#sympy)
- [Section 6. Object-oriented programming](#section-6-object-oriented-programming)
  - [General cons of OOP](#general-cons-of-oop)
  - [General pros of OOP](#general-pros-of-oop)
  - [General OOP best practices](#general-oop-best-practices)
  - [Python OOP examples from official documentation](#python-oop-examples-from-official-documentation)
    - [Object initialization and class variable](#object-initialization-and-class-variable)
    - [Class method](#class-method)
    - [Method by another method](#method-by-another-method)
    - [Inheritance](#inheritance)
    - [Data class](#data-class)
    - [Abstract class](#abstract-class)
    - [Property decorator](#property-decorator)
- [Topics not covered](#topics-not-covered)
- [Other tips](#other-tips)
- [Source code](#source-code)
- [References](#references)

## Section 1. Best practices

### `isClose` instead of `round` for comparing values

For comparing values, it's best to compare devitation from the truth.

```python
URhIn_shortest_dist = 2.6967
print(np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4))
# True

URhIn_shortest_dist = 2.670
print(np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4))
# False
```

### Check for simpler solutions

It is our job to validate whether the implementation is optimized for human
communication and performance.

#### Adding two arrays

```python
# :( - slower, overkill
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list(map(lambda x, y: x + y, list1, list2))
print(combined_list)
# [5, 7, 9]

# :) - faster, simple
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = np.add(list1, list2)
print(combined_list)
# [5 7 9]
```

#### Whether an element exists

```python
my_list = [1, 2, 3]

# :|
exists = any([x for x in my_list if x == 3])
print(exists) # True

# :)
exists = 3 in my_list
print(exists) # True
```

#### Applying element-wise simple operations

For multiplying

```python
# i.g. Square each element

# :(
squared = []
for x in my_list:
    squared.append(x**2)

# :|
squared = list(map(lambda x: x**2, my_list))

# :)
squared = [x**2 for x in my_list]
```

For filtering

```python
# :(
filtered = []
for x in my_list:
    if x > 10:
        filtered.append(x)

# :)
filtered = [x for x in my_list if x > 10]
```

### `|` to merge two dictionaries

Python has a concise syntax for this particular job.

```python
# Define two dictionaries with different keys
person_details = {"name": "Bob", "age": 56}
person_location = {"city": "New York", "country": "USA"}

# Merge the two dictionaries
merged_dict = person_details | person_location

print(merged_dict)
# {'name': 'Bob', 'age': 56, 'city': 'New York', 'country': 'USA'}
```

### `Counter` to find frequency

In scientific computing, we like to count and draw histograms. For one of my
projects, I determine a set of atoms from the supercell to determine the
coordination number. The reference is chosen with the atoms with the greatest
number of atoms surrounding it. Here, `Counter` is our friend.

```python
from collections import Counter

# Define the list with different numbers
my_list = [15, 15, 15, 7, 7, 3, 12, 12, 12, 12, 12]

# Create a Counter object to count the frequencies of each element in the list
counter = Counter(my_list)
print(counter)
# Counter({12: 5, 15: 3, 7: 2, 3: 1})

# Find the two most common elements
most_common = counter.most_common(2)

# Find the two most common elements
most_common = counter.most_common(1)
print(most_common)
# [(12, 5)]

two_most_common = counter.most_common(2)
print(two_most_common)
# [(12, 5), (15, 3)]
```

### `lambda` function

Lambda functions or called "closure" in Swift, a function. It must be defined
after `lamdba`.

```python
# Return "even" or "odd" based on the value
classify_number = lambda x: "even" if x % 2 == 0 else "odd"
print(classify_number(2))
print(classify_number(3))
```

#### Example 1. Sort `dict`

The way to sort or modifying values across a collection of items in Pything is
using `lambda` function.

```python
# Sort complex iterables with sorted()
data = [
    {"name": "Alice", "age": 12},
    {"name": "Bob", "age": 56},
    {"name": "Charlie", "age": 17}
]

sorted_data = sorted(data, key=lambda x: x["age"])

print(sorted_data)
# [{'name': 'Alice', 'age': 12},
# {'name': 'Charlie', 'age': 17},
# {'name': 'Bob', 'age': 56}]
```

```python
data = [
    {"name": "Alice", "age": 12, "score": 85},
    {"name": "Bob", "age": 56, "score": 90},
    {"name": "Charlie", "age": 56, "score": 88}
]

# Sort by age, then by score (ascending order)
sorted_data = sorted(data, key=lambda x: (x["age"], x["score"]))
print(sorted_data)
# [{'name': 'Alice', 'age': 12, 'score': 85},
# {'name': 'Charlie', 'age': 56, 'score': 88},
# {'name': 'Bob', 'age': 56, 'score': 90}]
```

#### Example 2. Sort `list`

Based on increasing or decreasing

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers_asc = sorted(numbers)
print(sorted_numbers_asc)
# Output: [1, 1, 2, 3, 4, 5, 6, 9]
sorted_numbers_desc = sorted(numbers, key=lambda x: -x)
print(sorted_numbers_desc)
# Output: [9, 6, 5, 4, 3, 2, 1, 1]
```

Based on `string` length

```python
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
# Output: ['date', 'apple', 'banana', 'cherry']
```

### `open` instead of `finally`

Python offers a cleaner, more efficient way to handle files opening and closing.

```python
# :(
file = open('my_file.txt', 'r')
try:
    data = file.read()
    # process data
finally:
    file.close()
```

```python
# :)
with open('my_file.txt', 'r') as file:
    data = file.read()
    # process data
```

We simply do not forget to close the file. It is handled automatically with
`open`.

### `enumerate` instead of `range` for loop

#### Example 1. `list`

We want both the index and the value without the need to use `[i]`.

```python
# List data
my_list = [1, 2, 3]

# :(
for i in range(len(my_list)):
    print(i, my_list[i])

# :) - Get both index and value in the loop
for idx, num in enumerate(my_list):
    print(idx, num)
```

#### Example 2. `dict`

```python
# Dictionary data
my_dict = {'a': 1, 'b': 2, 'c': 3}

# :( - Iterating over a dictionary without using enumerate
for key in my_dict:
    print(key, my_dict[key])

# :) - Using enumerate to get both the index and key-value pairs
for index, (key, value) in enumerate(my_dict.items()):
    print(index, key, value)

# If index is not needed
for key, value in my_dict.items():
    print(key, value)
```

### Use `_` for large numbers

We do not want to count the zeros.

```python
# :|
number_of_stars = 1000000000

# :)
number_of_stars = 1_000_000_000
```

### Return `None`

```pyhton
def function_that_does_not_return_value():
    # some operations
    return None
```

### `main()`

Certain code is only executed when the script is run directly, and not when it's
imported as a module.

```python
def main():
    # Main code here

if __name__ == "__main__":
    main()
```

### Documentation

```python
def calculate_means(numbers1, numbers2):
    """
    Calculate and return the means of two lists of numbers separately.

    :param numbers1: First list of float or integers.
    :param numbers2: Second list of float or integers.
    :return: A tuple containing the means of both lists.
    """
    mean1 = sum(numbers1) / len(numbers1) if numbers1 else 0
    mean2 = sum(numbers2) / len(numbers2) if numbers2 else 0
    return mean1, mean2
```

### Use type hints

Python infers types automaticlaly. But it is difficult for us to infer them
based on variable names. I am hoping to implement this in my next Python
project. Cons are increased maintenance if type hints need to be updated.

Regardless, with my first in-depth programming background in Swift where the
type must be defined before complication, I generally like the ability to know
types ahead. This is particulalry important for projects with many clases which
are found in mobile development SDKs.

```python
from typing import List, Dict

def calculate_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

def merge_dicts(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    return {**dict1, **dict2}
```

### Comprehensions

A comprehension in Python is a concise syntax for constructing a new sequence
based on the values from an existing sequence or iterable.

#### Example 1. Modify

```python
# Dictionary comprehension
dict_comp = {i: (i + 1) ** 2 for i in range(5)}

# List comprehension
list_comp = [(x + 1) ** 2 for x in range(5)]

# Set comprehension
set_comp = {(i + 3) % 5 for i in range(5)}

print("Dict Comprehension:", dict_comp)
print("List Comprehension:", list_comp)
print("Set Comprehension:", set_comp)
# Dict Comprehension: {0: 1, 1: 4, 2: 9, 3: 16, 4: 25}
# List Comprehension: [1, 4, 9, 16, 25]
# Set Comprehension: {0, 1, 2, 3, 4}
```

#### Example 2. Add condition

```python
ist_comp = [(x + 1) == 2 for x in range(5)]
print(list_comp)
# [False, True, False, False, False]
```

### Zip

The `zip()` function combines several iterables (like lists, tuples, etc.)
element-wise, creating a new iterator of tuples.

#### Example 1. iterate two arrays

```python
a = [1, 2, 3]
b = [4, 5, 6]

zipped = zip(a, b)  # Creates an iterator of tuples

for pair in zipped:
    print(pair)  # (1, 4), (2, 5), and (3, 6)
```

#### Example 2. `enumerate`

```python
a = [1, 2, 3]
b = [4, 5, 6]

for i, (av, bv) in enumerate(zip(a, b)):
    # 'i' is the index, 'av' is the element from 'a', 'bv' is the element from 'b'
    print(f"Index: {i}, a: {av}, b: {bv}")
```

### Use `perf_counter()` for time

```python
import time

# :( Using time.time()
start_time = time.time()
time.sleep(1)  # Sleep for 1 second
end_time = time.time()
time_duration = end_time - start_time

# :) Using time.perf_counter()
start_perf = time.perf_counter()
time.sleep(1)  # Sleep for 1 second
end_perf = time.perf_counter()
perf_duration = end_perf - start_perf

print(time_duration)
print(perf_duration)
```

`time.perf_counter()` provides the highest available resolution timer to measure
a short duration. It includes time elapsed during sleep and is system-wide

`time.time()` returns the current time in seconds since the Epoch (a fixed point
in time used for time calculations, typically January 1, 1970, 00:00:00 (UTC)).
It's suitable for getting the current timestamp.

#### Use comprehension

- When creating a list, set, dictionary from existing iterables and applying
  conditions to filter or transform the elements.

#### Use Lambda

- When a function is needed for an argumnet such as `filtere()`, `sorted()`,
  `map()`.

```python
even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
print(even_numbers)
```

## Section 2. NumPy

### Create array

```python
# Create an empty 1D array
arr_1d = np.arange(10)
# [0, 1, ..., 8, 9]

arr_1d = np.empty(5)
# [0, 0, 0, 0, 0]

# Create an empty 2D array
arr_2d = np.empty((3, 4))
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]
```

### Reshape array

```python
arr_1d = np.arange(10)
arr_2d = arr_1d.reshape((5, 2)) # 5 rows, 2 cols
```

### Broadcast

#### Example 1. Constant addition

```python
# Create a 2D array (e.g., 3x3)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Constant to add
constant = 10

# The constant is "broadcast" across the 2D array, adding it to every element
result = arr_2d + constant
```

#### Example 2. Addition between two arrays

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_1d = np.array([1, 0, -1])

# The 1D array is broadcast across each row of the 2D array
result = arr_2d + arr_1d
print(result)
# Output:
# [[2 2 2]
#  [5 5 5]
#  [8 8 8]]
```

#### Example 3. Multiplication between two arrays

```python
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
arr_1d = np.array([1, 2])

result = arr_2d * arr_1d
'''
 [1, 2]    [1*1, 2*2]    [1,  4]
 [1, 2] -> [3*1, 4*2] -> [3,  8]
 [1, 2]    [5*1, 6*2]    [5, 12]
'''

print(result)
# Output:
# [[ 1  4]
#  [ 3  8]
#  [ 5 12]]
```

### Apply universal functions

```python
arr = np.array([1, 2, 3, 4, 5])
result_add = np.add(arr, 10)  # Adds 10 to each element
result_multiply = np.multiply(arr, 2)  # Multiplies each element by 2
result_sin = np.sin(arr)  # Computes the sine of each element
```

## Section 3. Prompt

### Get user input with option selection

```python
# Get the directory of the script being executed
script_directory = os.path.dirname(os.path.abspath(__file__))

print("\nWelcome! Please choose an option to proceed:")

options = {
    "1": "Move files based on unsupported CIF format",
    "2": "Move files based on unreasonable distance",
    "3": "Move files based on tags",
    "4": "Move files based on supercell atom count",
    "5": "Copy files based on atomic occupancy and mixing",
    "6": "Get file info in the folder",
    "7": "Check CIF folder content against Excel file"
}

# Print options
for key, value in options.items():
    print(f"[{key}] {value}")

# Get user input
choice = input("Enter your choice (1-7): ")

if choice in options:
    print(f"You have chosen: {options[choice]}\n")
else:
    print("Invalid choice!")
    return
```

## Section 4. Pandas

### Read CSV

```python
csv_file_path = join(base_dir, "csv", "info_cif_files_info.csv")
csv_data = pd.read_csv(csv_file_path)
# 'CIF file' column matches 'URhIn.cif' and selects the 'Min distance' column
# iloc[0] refers to the first element
URhIn_min_dist = csv_data[csv_data['CIF file'] == 'URhIn.cif']['Min distance'].iloc[0]
```

### Save CSV

```python
def save_to_csv_directory(folder_info, df, base_filename):
    """
    Saves the dataframe as a CSV inside a 'csv' sub-directory of the provided folder.
    """

    csv_directory = join(folder_info, "csv")
    if not os.path.exists(csv_directory):
        os.mkdir(csv_directory)

    # Extract the name of the chosen folder
    folder_name = os.path.basename(folder_info)

    # Set the name for the CSV file based on the chosen folder
    csv_filename = f"{folder_name}_{base_filename}.csv"

    # Save the DataFrame to the desired location (within the 'csv' sub-directory)
    df.to_csv(join(csv_directory, csv_filename), index=False)

    print(csv_filename, "saved")
```

## Section 5. Math

### Sympy

Generate symbolic answers

```python
import sympy as sp

# Define the symbols
a11, a12, a21, a22, t11, t12, t21, t22 = sp.symbols('a11 a12 a21 a22 t11 t12 t21 t22')

# Define the matrix A and its inverse A_inv
A = sp.Matrix([[a11, a12], [a21, a22]])
A_inv = A.inv()

# Define the matrix T
T = sp.Matrix([[t11, t12], [t21, t22]])

# Calculate the transformed matrix T' using the formula T' = A * T * A_inv
T_prime = A * T * A_inv

# Extract the elements of the transformed matrix T'
T_prime_elements = T_prime.tolist()

# Output the elements of T' as a list of lists (matrix form)
print(T_prime_elements) # Symbolic answers
# [[-a21*(a11*t12 + a12*t22)/(a11*a22 - a12*a21)...]]
```

## Section 6. Object-oriented programming

For the project of my scale, I did not feel the urgency to implement
object-oriented programming. When I used Python for training neural networks and
material science projects, calling functions directly with variables passed
through parameters was sufficient for implementation and testing.

In addition, from the "Stop Writing Classes" video on
[YouTube](https://www.youtube.com/watch?v=o9pEzgHorH0), I agree with the
following bullet points directly from the video:

- Simple is better than complex.
- Flat is better than nested.
- Readability counts.
- Ship features not code.
- Customers love features, not code.

Whether to use OOP depends on the above points. For my projects, I didn't need
to. However, I may consider OOP later if I need to build projects that can be
easily exported and imported.

### General cons of OOP

- Hidden states within objects make it hard to reason about what is contained
  within an object from outside a function. By design, this is a feature known
  as encapsulation, a principle of OOP. It provides safety preventing external
  entities from directly changing the object's state.
- OOP tends to give a feeling of being more organized, like an organization. It
  also means modules and tasks are more tightly coupled.
- OOP tends to create boilerplate code such as getters and setters often
  employed in JAVA without adding significant value.

### General pros of OOP

- A well-designed object can be reused in other projects, like `ndarray` in
  NumPy.

### General OOP best practices

- Each class should have a single responsibility
- Avoid deep inheritance

### Python OOP examples from official documentation

#### Object initialization and class variable

```python
# Example source - https://docs.python.org/3/tutorial/classes.html
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

#### Class method

```python
# Example source - https://docs.python.org/3/tutorial/classes.html
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

#### Method by another method

```python
# Example source - https://docs.python.org/3/tutorial/classes.html
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

#### Inheritance

```python
# Example source - https://realpython.com/python-classes/
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print("Starting engine...")
        self._started = True

    def stop(self):
        print("Stopping engine...")
        self._started = False
```

```python
# Example source - https://realpython.com/python-classes/
class Car(Vehicle):
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year)
        self.num_seats = num_seats

    def drive(self):
        print(f'Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'

>>> tesla = Car("Tesla", "Model S", 2022, 5)
>>> tesla.start() # Starting engine...
>>> tesla.drive() # Driving my "Tesla - Model S" on the road
>>> tesla.stop() # Stopping engine...
>>> print(tesla) # "Tesla - Model S" has 5 seats


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def ride(self):
        print(f'Riding my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_wheels} wheels'

>>> harley = Motorcycle("Harley-Davidson", "Iron 883", 2021, 2)
>>> harley.start() # Starting engine...
>>> harley.ride() # Riding my "Harley-Davidson - Iron 883" on the road.
>>> harley.stop() # Stopping engine...
>>> print(harley) # "Harley-Davidson - Iron 883" has 2 wheels
```

#### Data class

```python
# Source- https://docs.python.org/3/tutorial/classes.html#
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john.salary
1000
```

#### Abstract class

```python
# Example source - https://www.geeksforgeeks.org/abstract-classes-in-python/
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def print_sides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def print_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def print_sides(self):
        print("I have 5 sides")
```

#### Property decorator

```python
# Example source - https://www.programiz.com/python-programming/property
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)
```

The above code can be improved using `@property`

```python
# Example source - https://www.programiz.com/python-programming/property
# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
```

Output

```bash
>>> human = Celsius(37)
>>>  print(human.temperature)
>>>  print(human.to_fahrenheit())
>>>  human.temperature = -300
Output:
Setting value...
Getting value...
37
Getting value...
98.60000000000001
Setting value...
Traceback (most recent call last):
  File "<string>", line 31, in <module>
  File "<string>", line 18, in set_temperature
ValueError: Temperature below -273 is not possible
```

## Topics not covered

- Matplotlib
- Generator for memory management
- Scipy - Optimization
- Logging

## Other tips

- Do not import functions, but modules
- Do not use getter/setter if it does not add any extra value
- Do not code without a test in mind or being implemented
- Use NumPy for numerical operations, optimized C code

## Source code

[Google Codelab](https://colab.research.google.com/drive/1vgFlN-33wQKpQFoG1aaiRklZnNidlZtK?usp=sharing)

## References

- <https://www.youtube.com/watch?v=qUeud6DvOWI>
- <https://google.github.io/styleguide/pyguide.html>
- <https://www.programiz.com/python-programming/property>
- <https://www.geeksforgeeks.org/python-property-decorator-property/>
- <https://www.geeksforgeeks.org/abstract-classes-in-python/>
