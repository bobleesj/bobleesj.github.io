---
layout: post
title: How to test multiple Python versions with GitHub Actions
categories: tutorial
---

## Introduction

If you are new to Python package management, I have a tutorial for you.
[How to use Python package manager for beginners (Ft. Conda with Cheatsheet)](https://bobleesj.github.io/tutorial/2024/02/26/intro-to-python-package-manager.html).
Terms and file names unfamiliar may be found in the above tutorial.

## Step 1. Generate `requirements.txt`

Python packages can be installed using `pip3` if a `requirements.txt` file
exists in the project directory.

```bash
pip3 install -r requirements.txt
```

I discovered 3 ways to generate `requirements.txt`.

### Method 1. `pip3 freeze`

```bash
pip3 freeze > requirements.txt
```

`freeze` lists all libraries installed regardless usage in the project. In one
of my projects, which focuses on pre-processing crystal files
([see here](https://github.com/bobleesj/cif-cleaner)), the `freeze` command
listed 76 packages.

### Method 2. `pipreqs`

```bash
# Install pipreqs via pip3
pip3 install pipreqs

# Overwrites requirements.txt, ignores tests
pipreqs . --force --ignore=tests
```

`pipreqs` will only list the packages used. Instead of all the packages 6
packages were listed using `pipreqps` shown below.

```text
# with pipreqs
click==8.1.7
gemmi==0.6.5
matplotlib==3.8.3
numpy==1.26.4
pandas==2.2.1
pytest==8.0.1
```

### Method 3. `Conda list`

The following can be used to generate if Conda is used. It generated 17
packages.

```bash
# List 17 packages
conda list -e > requirements.txt
```

### My decision

The following table containing the number of packages listed justifies my
decision to use `pipreqs`.

| Method     | # of packages listed | Reaction |
| ---------- | -------------------- | -------- |
| 1. pipreqs | 6                    | :)       |
| 2. pip3    | 17                   | :\|      |
| 3. conda   | 76                   | :(       |

## Step 2. Test multiple Python versions

I use GitHub Actions to test my project on various Python versions since my
projects are simple enough to build and run via GitHub remotely. If you are new
to GitHub Actions, please read my tutorial on How to use GitHub Actions for
effective testing in Python open-source projects
[here](https://bobleesj.github.io/tutorial/2024/03/03/github-actions.html).

To run multiple Python versions, replace your `.yml` GitHub Actions file with
the following.

```
on: [push, pull_request]

jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 5
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Create virtual environment and install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
```

> Check out
> [Github Actions Advanced Usage](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md)
> how to configure Python versions in GitHub Actions and the official website
> documentation on
> [GitHub Building and testing Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

Below is an image showing how GitHub Actions successfully processes the
`requirements.txt` for each Python version.

![GitHub Actions](/files/blog/2024-03-12-python-test-multiple-versions/img/1.png)

### Changelog

- 20240312 published tutorial
