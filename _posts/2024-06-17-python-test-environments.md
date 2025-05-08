---
layout: post
title: Test dependencies and environments in Python (Ft. Tox)
categories: tutorial
---

## Motivation

Software packages should ideally be executable across various environments. The
goal here is to automate the process of setting up these environments using
`Tox`, a tool widely used in the Python community

### Installation

Download Tox via:

```bash
pip install tox
```

### Configuration

Create a file named `tox.ini` at the root of your project with the following
content:

```bash
[tox]
envlist = py38, py39, py310, py311, py312

[testenv]
deps =
    gemmi==0.6.6
    matplotlib==3.8.3
    numpy==1.26.4
    pyvista==0.43.9
    scipy==1.13.1
    setuptools==67.8.0
allowlist_externals =
    pytest
commands =
    pytest tests/
```

The `envlist` specifies the Python versions, ranging from 3.8 to 3.12. The
`deps` key lists the specific library versions to be tested. To generate a list
of the software packages currently in use, create a `requirements.txt` file with
the following steps:

```bash
# Install pipreqs via pip3
pip3 install pipreqs

# Overwrite requirements.txt, ignore tests directory
pipreqs . --force --ignore=tests
```

### Usage

Run Tox with:

```bash
# General command
tox
```

For linting integration, as discussed in
[Python styling automation tool (Ft. Black)](https://bobleesj.github.io/tutorial/2024/03/11/python-styling-guide.html),
update the `tox.ini` as follows:

Update `tox.ini` with the following:

```bash
[tox]
envlist = py38, py39, py310, py311, py312, lint

[testenv]
deps =
    gemmi==0.6.6
    matplotlib==3.8.3
    numpy==1.26.4
    pyvista==0.43.9
    scipy==1.13.1
    setuptools==67.8.0
allowlist_externals =
    pytest
commands =
    pytest -m fast tests/

[testenv:lint]
description = run linters
skip_install = true
deps =
    black==22.12
commands = black -l 79 .
```

Now, running `tox` will set up multiple Python environments and execute `black`
for linting.

To run only the `lint` environment:

```bash
tox -e lint
```

For verbose output during linting:

```bash
tox -e lint -vv
```

## Best practices

In practice, testing every possible combination of versions is not feasible. It is recommended to test using the minimum and maximum version bounds and assuming that the software will work with versions in between. Typically,
`requirements.txt` should specify precise versions for dependencies, whereas the
versions listed in tox.ini should be broader to allow more flexibility.

## References

- [Tox official website](https://tox.wiki/en/4.15.1/)
