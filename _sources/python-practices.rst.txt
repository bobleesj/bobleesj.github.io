Python
======

Here I document Python practices I have learned while developing packages like ``scikit-package`` and ``cifkit``. These practices are not exhaustive, but I hope they can guide you in your own projects. ``pytest`` is used for testing.

pytest
------

Why pytest
^^^^^^^^^^

- Avoid subclassing by using only functions, making the test structure flat
  and simple.
- No direct execution with `__main__` since the script is executed by pytest.
- state control with its fixture system, for setting up and tearing down global resources.
- Temporary folders efficiently using `tmp_path`, a built-in fixture
- pytest uses `caplog` to test log output and ``capsys`` to capture print.

General practices for testing with pytest

- **Adopt test-driven development**: Write tests before implementing the
  functionality. Start with failing tests, then implement the function, make the
  tests pass, and refactor.
- **Avoid over-testing trivial code**: Refrain from testing trivial code, such
  as getters and setters, to prevent a bloated test suite. Focus on ensuring
  robustness rather than achieving 100% coverage.
- **Conduct integration testing**: Perform integration testing by starting from
  scratch and testing the outputs. Unit tests might pass due to the use of
  mocking, which simulates heavy latency tasks like database connections.
- **Import specific functions**: Prefer importing specific functions to clarify
  exactly which parts of the codebase are under test.
- **Use `Enum` to manage error messages**: Leverage `Enum` to organize and
  manage error messages consistently.
- **Catch specific errors**: Always catch specific errors instead of general
  type errors.

To get started, ensure you have installed ``pytest`` and ``pytest-mock``:

.. code-block:: bash

    pip install pytest pytest-mock

Locating files and folders in the project directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To locate a file in your project directory, such as ``TEMPLATE.rst`` in the ``news`` folder, you can use the following approach:

.. code-block:: python

    from pathlib import Path

    project_root = Path(__file__).resolve().parents[1]
    real_template_path = project_root / "news" / "TEMPLATE.rst"

Working with temporary files using ``tmpdir`` and ``tmp_path``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a custom temporary folder using ``tmp_path``:

.. code-block:: python

    def setup_custom_folder(tmp_path):
        my_dir = tmp_path / "<folder-name>"
        my_dir.mkdir()
        return my_dir

To create a text file within a temporary folder using ``tmpdir``:

.. code-block:: python

    from pathlib import Path

    def setup_custom_file(tmpdir):
        my_text = """{%- set version = "1.1.1" -%}
    name: cifkit
    """
        my_file = Path(tmpdir) / "<file-name-with-extension>"
        my_file.write_text(my_text)
        return my_file.read_text()

Testing an argument parser
^^^^^^^^^^^^^^^^^^^^^^^^^^

To test a function that expects an ``args`` object (as used with ``argparse``), you can use ``SimpleNamespace`` to mimic CLI arguments in your tests. For example:

.. code-block:: python

    from types import SimpleNamespace

    args1 = SimpleNamespace(
        add=True,
        change=False,
        deprecate=False,
        remove=False,
        fix=False,
        security=False,
        message="Add first news.",
    )
    news_item(args1)

Assume ``news_item`` creates an ``.rst`` file in the ``news`` folder. The function might look like:

.. code-block:: python

    def news_item(args):
        message = args.message
        # Implementation here

You can set up your argument parser to use this function:

.. code-block:: python

    parser_news.set_defaults(func=add.news_item, subcommand="news")

This allows you to call the CLI as follows:

.. code-block:: bash

    package add news -a -m "Add first news."

Mocking a simple variable
^^^^^^^^^^^^^^^^^^^^^^^^^

To mock a simple variable, such as a directory path, use ``mocker.patch``. For example, to mock the ``NEWS_DIR`` variable in the ``scikit_package.cli.add`` module:

.. code-block:: python

    def test_mocker_variable(mocker):
        mocker.patch("scikit_package.cli.add.NEWS_DIR", str(test_news_dir))

Mocking a function
^^^^^^^^^^^^^^^^^^

To mock a function, such as ``scikit_package.cli.add.get_news_files``, use:

.. code-block:: python

    def test_mocker_function(mocker):
        mocker.patch("scikit_package.cli.add.get_news_files", return_value=[str(test_news_file)])

Mocking HTTP requests and capturing print output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use ``pytest-mock`` to replace the ``requests.get`` function with a mock object. This is useful for unit testing code that makes HTTP requests. The following example mocks the HTTP request to PyPI, captures the print output, and confirms that the mock was called with the expected URL.

.. code-block:: python

    import requests

    def check_pypi_package_exists(package):
        response = requests.get(f"https://pypi.org/pypi/{package}/json")
        if response.status_code == 200:
            data = response.json()
            version = data["info"]["version"]
            print(f"> {package} is available on PyPI (latest version: {version}).")
        else:
            raise ValueError("<error-message>")

Here is the test code (in ``test_pypi.py``):

.. code-block:: python

    def test_check_pypi_package_exists(mocker, capsys):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"info": {"version": "1.2.3"}}
        mock_get = mocker.patch(
            "scikit_package.utils.pypi.requests.get", return_value=mock_response
        )
        check_pypi_package_exists("my-package")
        captured = capsys.readouterr()
        assert (
            "> my-package is available on PyPI (latest version: 1.2.3)."
            in captured.out
        )
        mock_get.assert_called_once_with("https://pypi.org/pypi/my-package/json")

Explanation:

- The ``scikit_package.utils.pypi.requests.get`` function is patched to return ``mock_response`` instead of making an actual HTTP request.
- The ``capsys`` fixture captures the output printed by the function.
- The test confirms that ``requests.get`` was called once with the expected URL.

Test log
^^^^^^^^^

You can use the ``caplog`` fixture to capture log. You can use ``capsys`` to capture the print output.

.. code-block:: python

    import logging
    
    def log_save_file_message(file_type: str, file_path: str):
        logging.info(f"{file_type} has been saved in {file_path}.")

Test function:

Use the `caplog` input default by `pytest`.

.. code-block:: python

    def log_save_file_message(caplog):
        with caplog.at_level(logging.INFO):
            log_save_file_message(file_type, file_path)
        assert f"{file_type} has been saved in {file_path}." == caplog.text



Object-oriented programming
----------------------------

From the "Stop Writing Classes" video on `YouTube <https://www.youtube.com/watch?v=o9pEzgHorH0>`_, I agree with the following bullet points directly from the video:

- Simple is better than complex.
- Flat is better than nested.
- Readability counts.
- Ship features not code.
- Customers love features, not code.

**General cons of OOP**

- Hidden states within objects make it hard to reason about what is contained within an object from outside a function. By design, this is a feature known as encapsulation, a principle of OOP. It provides safety preventing external entities from directly changing the object's state.
- OOP tends to give a feeling of being more organized, like an organization. It also means modules and tasks are more tightly coupled.
- OOP tends to create boilerplate code such as getters and setters often employed in JAVA without adding significant value.

**General pros of OOP**

- A well-designed object can be reused in other projects, like ``ndarray`` in NumPy.

**General OOP principles**

- Each class should have a single responsibility
- Avoid deep inheritance

Data class
^^^^^^^^^^

.. code-block:: python

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

Abstract class
^^^^^^^^^^^^^^

.. code-block:: python

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

Property decorator
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  # Example source - https://www.programiz.com/python-programming/property
  class Celsius:
    def __init__(self, temperature=0):
      self.temperature = temperature

    def to_fahrenheit(self):
      return (self.temperature * 1.8) + 32

    def get_temperature(self):
      print("Getting value...")
      return self._temperature

    def set_temperature(self, value):
      print("Setting value...")
      if value < -273.15:
        raise ValueError("Temperature below -273.15 is not possible")
      self._temperature = value
    
The above code can be improved using ``@property``

.. code-block:: python

  # Example source - https://www.programiz.com/python-programming/property
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


NumPy
-----

A matrix represents a set of values. Matrices are used in solving a system of equations, representing graphs, etc. The more concisely and clearly we represent matrices in scripts, the less time is required for debugging.

Assume ``X`` and ``Y`` represent matrices and ``vec`` is a 1-D array.

.. code-block:: python

    np.add(X,Y)       # Add
    np.substract(X,Y) # Substract
    np.divide(X,Y)    # Divide

    # Multiply, all same
    X @ Y             # recommended
    np.multiply(X,Y)
    np.matmul(X, Y)
    np.dot(X, Y)
    X.dot(Y)

Individual operations
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

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

.. code-block:: python

    X[0, 1]  # Get value from 1st row, 2nd col

1D slicing
^^^^^^^^^^

.. code-block:: python

    vec = list(range(10)) # [1, ..., 9]
    vec[4:8]       # [4, 5, 6, 7]
    vec[-5:-2]     # 5th last to 2nd last => [5, 6, 7]

    # Get every Nth index value
    vec[::2]      # [0, 2, 4, 6, 8]
    vec[::5]      # [0, 5]

    # Inverse
    vec[::-1]     # Temp inverse [9, 8, ... 1, 0]
    vec.reverse() # Permanent inverse

2D slicing
^^^^^^^^^^

.. code-block:: python

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
    # => [[3 2 1]
    #     [6 5 4]
    #     [9 8 7]]
    X[1:, ::-1]   # same as above but skip first row
    # => [[6 5 4]
    #     [9 8 7]]

Boolean Indexing
^^^^^^^^^^^^^^^^

.. code-block:: python

    cols = X[0, :] > 1  # select col(s) where first row > 1
    # => [False  True  True]
    X[:, cols]
    # => [[2 3]
    #     [5 6]
    #     [8 9]]

Matrix creation
^^^^^^^^^^^^^^^

.. code-block:: python

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

Others
^^^^^^

.. code-block:: python

    np.set_printoptions(
        precision=3,   # Set decimal places
        suppress=True, # Avoid scientific notations
        threshold=100, # Max number of elements to be printed
        linewidth=80,
        edgeitems=2    # Show two values per edge when truncated
    )

Element-wise addition
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import numpy as np

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined_list = np.add(list1, list2)
    print(combined_list)
    # [5 7 9]

Check if an element exists in a list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    my_list = [1, 2, 3]
    exists = any([x for x in my_list if x == 3])  # :(
    exists = 3 in my_list  # :)

List comprehensions vs. map vs. for loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # :(
    squared = []
    for x in my_list:
         squared.append(x**2)
    # :|
    squared = list(map(lambda x: x**2, my_list))
    # :)
    squared = [x**2 for x in my_list]

Filter a list
^^^^^^^^^^^^^

.. code-block:: python

  # :(
  filtered = []
  for x in my_list:
    if x > 10:
      filtered.append(x)
  # :)
  filtered = [x for x in my_list if x > 10]

Use ``|`` to merge two dictionaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python has a concise syntax for this particular job.

.. code-block:: python

  # Define two dictionaries with different keys
  person_details = {"name": "Bob", "age": 56}
  person_location = {"city": "New York", "country": "USA"}
  # Merge the two dictionaries
  merged_dict = person_details | person_location
  merged_dict
  >>> {'name': 'Bob', 'age': 56, 'city': 'New York', 'country': 'USA'}

``Counter`` to find frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In scientific computing, we like to count and draw histograms. For one of my projects, I determine a set of atoms from the supercell to determine the coordination number. The reference is chosen with the atoms with the greatest number of atoms surrounding it. Here, ``Counter`` is our friend.

.. code-block:: python

  from collections import Counter

  my_list = [15, 15, 15, 7, 7, 3, 12, 12, 12, 12, 12]
  counter = Counter(my_list)
  print(counter)
  # Counter({12: 5, 15: 3, 7: 2, 3: 1})
  # Find the two most common elements
  counter.most_common(1)  # [(12, 5)]
  counter.most_common(2) # [(12, 5), (15, 3)]
  
``lambda`` function
^^^^^^^^^^^^^^^^^^^^

Lambda functions or called "closure" in Swift, a function. It must be defined after ``lambda``.

.. code-block:: python

  # Return "even" or "odd" based on the value
  classify_number = lambda x: "even" if x % 2 == 0 else "odd"

Example 1. Sort ``dict``

The way to sort or modify values across a collection of items in Python is using ``lambda`` function.

.. code-block:: python

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

.. code-block:: python

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

Example 2. Sort ``list``

Based on increasing or decreasing

.. code-block:: python

  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  sorted_numbers_asc = sorted(numbers)
  print(sorted_numbers_asc)
  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
  sorted_numbers_desc = sorted(numbers, key=lambda x: -x)
  print(sorted_numbers_desc)
  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

Based on string length

.. code-block:: python

  words = ["banana", "apple", "cherry", "date"]
  sorted_words = sorted(words, key=lambda x: len(x))
  print(sorted_words)
  # Output: ['date', 'apple', 'banana', 'cherry']

``open`` instead of ``finally``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python offers a cleaner, more efficient way to handle files opening and closing.

.. code-block:: python

  # :(
  file = open('my_file.txt', 'r')
  try:
    data = file.read()
    # process data
  finally:
    file.close()

.. code-block:: python

  # :)
  with open('my_file.txt', 'r') as file:
    data = file.read()
    # process data

We simply do not forget to close the file. It is handled automatically with ``open``.

``enumerate`` instead of ``range`` for loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example 1. ``list``

We want both the index and the value without the need to use ``[i]``.

.. code-block:: python

  # List data
  my_list = [1, 2, 3]

  # :(
  for i in range(len(my_list)):
    print(i, my_list[i])

  # :) - Get both index and value in the loop
  for idx, num in enumerate(my_list):
    print(idx, num)

Example 2. ``dict``

.. code-block:: python

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

Use ``_`` for large numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We do not want to count the zeros.

.. code-block:: python

  # :|
  number_of_stars = 1000000000
  # :)
  number_of_stars = 1_000_000_000


Comprehensions
^^^^^^^^^^^^^^

A comprehension in Python is a concise syntax for constructing a new sequence based on the values from an existing sequence or iterable.

.. code-block:: python

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

Add condition

.. code-block:: python

  list_comp = [(x + 1) == 2 for x in range(5)]
  print(list_comp)
  # [False, True, False, False, False]

Example 1. Constant addition

.. code-block:: python

  # Create a 2D array (e.g., 3x3)
  arr_2d = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

  # Constant to add
  constant = 10

  # The constant is "broadcast" across the 2D array, adding it to every element
  result = arr_2d + constant

Example 2. Addition between two arrays

.. code-block:: python

  arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  arr_1d = np.array([1, 0, -1])

  # The 1D array is broadcast across each row of the 2D array
  result = arr_2d + arr_1d
  print(result)
  # Output:
  # [[2 2 2]
  #  [5 5 5]
  #  [8 8 8]]

Example 3. Multiplication between two arrays

.. code-block:: python

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

.. code-block:: python

  arr = np.array([1, 2, 3, 4, 5])
  # Adds 10 to each element
  result_add = np.add(arr, 10)
  # Multiplies each element by 2
  result_multiply = np.multiply(arr, 2)
  # Computes the sine of each element
  result_sin = np.sin(arr)  


Zip
^^^

The ``zip()`` function combines several iterables (like lists, tuples, etc.) element-wise, creating a new iterator of tuples.

Example 1. iterate two arrays

.. code-block:: python

  a = [1, 2, 3]
  b = [4, 5, 6]

  zipped = zip(a, b)  # Creates an iterator of tuples

  for pair in zipped:
    print(pair)  # (1, 4), (2, 5), and (3, 6)

Example 2. ``enumerate``

.. code-block:: python

  a = [1, 2, 3]
  b = [4, 5, 6]

  for i, (av, bv) in enumerate(zip(a, b)):
    # 'i' is the index, 'av' is the element from 'a', 'bv' is the element from 'b'
    print(f"Index: {i}, a: {av}, b: {bv}")

Use ``perf_counter()`` for time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

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

``time.perf_counter()`` provides the highest available resolution timer to measure a short duration. It includes time elapsed during sleep and is system-wide.

``time.time()`` returns the current time in seconds since the Epoch (a fixed point in time used for time calculations, typically January 1, 1970, 00:00:00 (UTC)). It's suitable for getting the current timestamp.

.. code-block:: python

  even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
  print(even_numbers)

Create array
^^^^^^^^^^^^

.. code-block:: python

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

Reshape array
^^^^^^^^^^^^^^

.. code-block:: python

  arr_1d = np.arange(10)
  arr_2d = arr_1d.reshape((5, 2)) # 5 rows, 2 cols


argparse (TBA)
----------------


logging
---------

Intro to Python logging
------------------------

Logs record activities. They are used for debugging and analyzing user behavior.
While ``print()`` serves as a perfectly good solution for simple programs, there
are specific needs that it cannot fulfill:

- Saving logs in a separate folder or periodically
- Turning on/off certain types of logs globally
- Providing information on line numbers, file names, etc.
- Categorizing logs into ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, and ``CRITICAL``

For these requirements, we may want to use Python's built-in logging tool.

Initial Setup
^^^^^^^^^^^^^

First, copy the following code to a Python file:

.. code-block:: python

    import logging

    def main():
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    if __name__ == "__main__":
        main()

Add log messages by modifying the file like this:

.. code-block:: python

    import logging

    def main():
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        logging.debug("This is a debug log.")
        logging.info("This is an info log.")
        logging.warning("This is a warning log.")
        logging.error("This is an error log.")
        logging.critical("This is a critical log.")

    if __name__ == "__main__":
        main()

Understand log levels
^^^^^^^^^^^^^^^^^^^^^

The log level ``DEBUG`` is the lowest, meaning all messages from all severity
levels (``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``) will be logged. Refer
to the table below:

+-----------------+--------------------------------------+
| Log Level Set   | Messages Printed                     |
+=================+======================================+
| DEBUG           | DEBUG, INFO, WARNING, ERROR, CRITICAL|
+-----------------+--------------------------------------+
| INFO            | INFO, WARNING, ERROR, CRITICAL       |
+-----------------+--------------------------------------+
| WARNING         | WARNING, ERROR, CRITICAL             |
+-----------------+--------------------------------------+
| ERROR           | ERROR, CRITICAL                      |
+-----------------+--------------------------------------+
| CRITICAL        | CRITICAL                             |
+-----------------+--------------------------------------+

For example, if you modify from ``logging.DEBUG`` to ``logging.ERROR``:

.. code-block:: text

    python main.py (logging.DEBUG)
    2024-05-23 16:28:07 INFO This is an info log.
    2024-05-23 16:28:07 WARNING This is a warning log.
    2024-05-23 16:28:07 ERROR This is an error log.
    2024-05-23 16:28:07 CRITICAL This is a critical log.

    python main.py (logging.ERROR)
    2024-05-23 16:28:14 ERROR This is an error log.
    2024-05-23 16:28:14 CRITICAL This is a critical log.

Save logs
^^^^^^^^^

Modify the ``basicConfig`` by adding ``filename`` and ``filemode``:

.. code-block:: python

    logging.basicConfig(
        level=logging.DEBUG,
        filename='app.log',
        filemode='w',  # 'w' to write, 'a' to append
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

As of this writing, I currently have no further solutions needed beyond the
above at the current level. I may add more details if more advanced
functionalities from the ``logging`` library are needed for my projects.
