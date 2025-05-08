---
layout: post
title: Python unit test cheatsheet (Ft. Pytest)
categories: cheatsheet
---

## Motivation

It is the main reference for my own Python development for open-source
development. All code snippets are written by me.

## Why pytest

- It avoids subclassing by using only functions, making the test structure flat
  and simple.
- There is no need for direct execution with `__main__` since the script is
  executed by pytest.
- pytest provides excellent state control with its fixture system, which is used
  for setting up and tearing down global resources.
- It manages temporary folders efficiently using `tmp_path`, a built-in fixture,
  which allows access to a temporary folder in any test function.
- pytest uses `caplog` to test log output

## Best practices for testing with pytest

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

## Test types

### Expect a value

```python
assert full_occupancy_dir_cif_count == 2, "Not all expected files were copied."
```

### Expect no error

```python
for cif_file_path in cif_file_path_list:
    try:
        preprocess_supercell_operation(cif_file_path)
    except Exception as e:
        assert False, f"An unexpected error occurred for {cif_file_path}: {str(e)}"
```

### Expect error to occur

```python
for cif_file_path in cif_file_path_list:
    with pytest.raises(Exception):
        preprocess_supercell_operation(cif_file_path)
```

## Test for file generation

Often, it is difficult to test `.png`. But we can check whether the file exists
and the size.

A function for checking the size:

```python
# folder.py
def check_file_exists(file_path: str) -> bool:
    """Check if the specified file exists."""
    if not os.path.exists(file_path):
        # Using enum value and formatting it with file_path
        raise FileNotFoundError(
            FileError.FILE_NOT_FOUND.value.format(file_path=file_path)
        )
```

Error message:

```python
# utils/error_messages.py
class FileError(Enum):
    FILE_NOT_FOUND = "The file at {file_path} was not found."
    FILE_IS_EMPTY = "The file at {file_path} is empty."
```

Test file:

```python
# test_folder.py
def test_check_file_exists(tmp_path):
    # Setup: create a temporary file
    test_file = tmp_path / "testfile.txt"
    test_file.touch()  # This creates the file

    # Test file exists
    assert check_file_exists(test_file) == True

    # Test file does not exist
    non_existent_file = tmp_path / "nonexistent.txt"
    with pytest.raises(FileNotFoundError) as e:
        check_file_exists(str(non_existent_file))
    assert str(e.value) == FileError.FILE_NOT_FOUND.value.format(
        file_path=non_existent_file
    )
```

## Test log

Function:

```python
def log_save_file_message(file_type: str, file_path: str):
    logging.info(f"{file_type} has been saved in {file_path}.")
```

Test function:

Use the `caplog` input default by `pytest`.

```python
def log_save_file_message(caplog):
    file_type = "Histogram"
    file_path = "/path/to/histogram.png"

    # Check that the log message as expected
    with caplog.at_level(logging.INFO):
        log_save_file_message(file_type, file_path)
    assert f"{file_type} has been saved in {file_path}." == caplog.text
```

I discuss here
[Intro to Python logging for beginners](https://bobleesj.github.io/tutorial/2024/05/23/python-logging.html)

## Test random numbers

```python
def generate_random_numbers(
    count: int, low: int | float, high: int | float, is_float=True
):
    random.seed(42)
    """
    Generate a list of random numbers (floating-point or integer).
    """
    if is_float:
        return [random.uniform(low, high) for _ in range(count)]
    else:
        return [random.randint(int(low), int(high)) for _ in range(count)]
```

```python
def test_generate_random_numbers():
    count = 10
    low = 20
    high = 30
    float_results = generate_random_numbers(count, low, high)
    int_results = generate_random_numbers(count, low, high, is_float=False)
    # Test bound
    assert all(low <= x <= high for x in float_results)
    assert all(low <= x <= high for x in int_results)

    # Test type and lengths
    assert (
        all(isinstance(x, int) for x in int_results) and len(int_results) == 10
    )
    assert (
        all(isinstance(x, float) for x in float_results)
        and len(float_results) == 10
    )
```

## Test CSV

```python
import pandas as pd
import numpy as np
from filter.info import get_cif_folder_info
from os.path import join, exists
from util.folder import (
    remove_file,
    get_cif_file_count_from_directory
)

def test_cif_folder_info():
    base_dir = "test/info_cif_files"
    csv_file_path = join(base_dir, "csv", "info_cif_files_info.csv")

    # Setup
    remove_file(csv_file_path)
    initial_cif_file_count = get_cif_file_count_from_directory(base_dir)

    # Start
    get_cif_folder_info(base_dir, False)
    assert exists(csv_file_path), "CSV log file was not created."
    csv_data = pd.read_csv(csv_file_path)
    assert len(csv_data.index) == initial_cif_file_count, "CSV log does not match the # of moved files."

    # Test atom count
    URhIn_supercell_atom_count = csv_data[csv_data['CIF file'] == 'URhIn.cif']['Number of atoms in supercell'].iloc[0]
    error_msg_supercell_atom_count = f"Incorrect number of atoms for URhIn, expected 206"
    assert URhIn_supercell_atom_count == 206, error_msg_supercell_atom_count

    # Test shortest distance from Excel
    error_msg_shortest_dist = "Incorrect shortest distance for URhIn, expected ~2.69678, got {urhIn_min_distance}"
    URhIn_shortest_dist = csv_data[csv_data['CIF file'] == 'URhIn.cif']['Min distance'].iloc[0]
    assert np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4), error_msg_shortest_dist

    # Cleanup
    remove_file(csv_file_path)
```

### Test log

```python
def print_save_file_message(caplog):
    file_type = "Histogram"
    file_path = "/path/to/histogram.png"
    with caplog.at_level(logging.INFO):
        print_save_file_message(file_type, file_path)

    # Check that the log message as expected
    assert (
        f"{file_type} has been saved in {file_path}." in caplog.text
    )


def print_save_file_message(file_type: str, file_path: str):
    logging.info(f"{file_type} has been saved in {file_path}.")
```

### Pytest Collectonly

In pytest, collectonly is a command-line option that allows you to quickly
gather information about the test cases in your project without actually running
them.

```bash
pytest --collect-only
pytest --collectonly tests/test_fixture.py
```

### Pytest Fixture

A fixture in pytest is a function that sets up a test environment before the
tests run and cleans it up afterwards. This is extremely handy for handling
repetitive tasks like establishing database connections, creating test data, or
preparing system state before executing tests.

Our use of the `conftest.py` file is central to our fixture strategy. This
special file is recognized by pytest and is used for sharing fixtures across
multiple test files. By defining fixtures in conftest.py, we make them
accessible to any test in the same directory or subdirectories without the need
for imports.

```python
#conftest.py
import pytest

@pytest.fixture
def resource_setup():
    print("Setup resource")
    resource = {"data": 123}  # Setup code
    yield resource  # This value is passed to the test function
    # Teardown code follows
    print("Teardown resource")
    del resource

@pytest.fixture
def initial_value():
    return 5
```

```python
# test_fixture.py
import pytest

def square(num):
    return num * num

def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value**2

def test_using_fixture(resource_setup):
    assert resource_setup["data"] == 123
```

> No need for a `del` statement to release resources in pytest fixtures.
> Resource management is handled by the setup and teardown logic encapsulated
> within the fixture itself, using the pattern of initializing resources before
> yield and cleaning them up after `yield`.

### Run test automatically

Download `nodemon` via `npm`.

```bash
sudo npm install -g nodemon
```

Use `nodemon` to automatically run pytest when `.py` files change. The command
should be as follows:

```bash
nodemon --exec "python -m pytest" --ext py
```

### Get test coverage

```bash
pip install pytest-cov
pytest --cov

# create an html file
coverage html
```

### Path error

```bash
ERROR tests/test_format.py
ERROR tests/test_info.py
ERROR tests/test_occupancy.py
ERROR tests/test_supercell_size.py
ERROR tests/test_tags.py
```

If your project's directory isn't being recognized like above, you might need to
add it to the PYTHONPATH environment variable. You can do this by running the
following command in your terminal (adjust the path as necessary for your
project):

```bash
export PYTHONPATH="${PYTHONPATH}:/Users/imac/Documents/GitHub/cif-cleaner-main"
```

## Concept of `yield`

`fixture` provides a centralized source of data across all of the test files.
`yield` is used to

```python

```

## Cheatsheet for command line

```bash
# Run tests marked as 'slow'
pytest -m slow

# Disable output capturing, allowing print statements to show up in the console
pytest -s

# Increase verbosity for more detailed test output
pytest -v

# Reduce verbosity for a more concise test output
pytest -q

# Control traceback printing for test failures (options: long, short, line, native, no, auto)
pytest --tb=style

# Report the durations of the N slowest tests
pytest --durations=N

# Measure code coverage (requires pytest-cov plugin)
pytest --cov

# Ignore a specific file or directory during test discovery
pytest --ignore=path

# Stop the test session after N failures
pytest --maxfail=num
```

## Cheatsheet for Pytest Cov

```bash
# Install
pip install pytest-cov

# Create HTML files containing test info
coverage html
```

```python
@pytest.mark.slow
def test_some_slow_process():
    # slow test logic here

@pytest.mark.fast
def test_quick_function():
    # fast test logic here

@pytest.mark.skip(reason="not implemented yet")
def test_feature_x():
    # test logic here

@pytest.mark.parametrize("input,expected", [(1, 2), (3, 4)])
def test_addition(input, expected):
    assert input + 1 == expected

@pytest.mark.usefixtures("setup_database")
def test_database_query():
    # use the fixtures
```

## References

I have collected the examples from many places.

- [https://www.youtube.com/watch?v=mTMu8AtdG-E](https://www.youtube.com/watch?v=mTMu8AtdG-E)
- [https://docs.pytest.org/](https://docs.pytest.org/)
- ChatGPT
