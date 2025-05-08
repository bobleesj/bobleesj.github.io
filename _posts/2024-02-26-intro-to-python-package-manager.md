---
layout: post
title: How to use Python package manager for beginners (Ft. Conda with Cheatsheet)
categories: tutorial
---

## Overview

By the end of this tutorial, you should be able to answer the following
questions in about 10 to 15 minutes.

1. What is the core problem in open-source development?
2. What is a package manager and why do we need one?
3. How do we use a package manager in practice?

## Motivation

Let's first discuss why we need a package manager. You might have used tools
such as `numpy` for mathematical functions as shown below.

```python
# my-fancy-code.py
from numpy import pi
print(pi) # 3.14...
```

NumPy is a Python collection of tools with functions and variables. However, we
must **import** this library or also known as “dependency”. If a program uses
`numpy`, it “depends” on the functions provided by `numpy`. One can install
`numpy` via a command-line interface such as terminal as shown below.

```bash
# install numpy (will download 1.26.4 as of Feb 2024)
pip install numpy
```

![Image 1 - numpy version](/files/blog/2024-02-26-intro-python-package-manager/img/1.png)

Imagine you are required to run `bob-software.py`, which relies on NumPy version
1.26.4 and Python version 3.11 or higher as shown below.

```bash
# bob-software.py (Python v3.11 or higher and NumPy v1.26.4)
import numpy as np
import sys

# Determine version compatibility
if np.__version__ == "1.26.4" and sys.version_info >= (3, 11):
    print("Good! Your NumPy version is 1.26.4 and your Python version is 3.11 or higher!")
else:
    print("Failed to compile. Check your Python and NumPy versions")
```

But what if you also have another software that you run daily,
`alice-software.py`, which requires a different NumPy version?

```bash
# alice-software.py (Python v3.11 or higher and NumPy v1.26.3)
import numpy as np
import sys

# Determine version compatibility
if np.__version__ == "1.26.3" and sys.version_info >= (3, 11):
    print("Good! Your NumPy version is 1.26.3 and your Python version is 3.11 or higher!")
else:
    print("Failed to compile. Check your Python and NumPy versions")
```

Here, we see a simple difference. However, in reality, there can be dozens of
dependencies with varying requirements. When collaborating as a team, your
script may work on your local machine because you're using specific versions.
Yet, when you share your code with colleagues, it might not work due to their
different software versions.

We want to avoid situations like this:

> “Dear Lee, Please install these 12 libraries with versions a, b, and c”.

This message can easily be lost in our email chain, leaving the collaborator
unable to run the code.

## Introducing package manager

The core issue is the difficulty of manually tracking each dependency
requirement. Understanding this issue helps us appreciate what a package manager
resolves.

In just four lines of code, we can graecfully both handle executing
`alice-software.py` and `bob-software.py` in just a few lines of commands. The
package manager will

1. create a folder (environment) with a specific Python version
2. activate the folder and installs Python libraries with specific versions
   within it
3. use the environment (Python and libraries inside the folder) to run
   `bob-software.py`

### Python package manager - Conda

Conda is one of the widely used package managers for Python. It is free,
well-maintained, and favored by the scientific community.

### Prerequisite: download & install

To install, visit
[https://docs.anaconda.com/free/miniconda/](https://docs.anaconda.com/free/miniconda/)
and follow the listed steps to download and install. The process is
straightforward—just copy and paste each line into your command line. It's
always recommended to download the latest version directly from the official
website.

![Image 2 - conda download](/files/blog/2024-02-26-intro-python-package-manager/img/2.png)
After successful installation, confirm by typing `conda --version`.

```**bash**
conda --version
# conda 23.11.0
```

> In case of any difficulties during installation, feel free to reach out via
> email.

## Run bob-software.py with Conda

Now, we will run `bob-software.py` with Conda.

### Step 1. create environment

For simplicity, let's create an environment called "bob", as in our hypothetical
example. Note that we're installing Python version 3.12.

```bash
conda create -n bob python=3.12
```

### Step 2. activate environment

By activating the environment, you're instructing your machine to use the Python
version and packages installed under "bob". You can name it as you wish.

```bash
conda activate bob
```

### Step 3. download Python libraries

Next, you'll download the exact version of NumPy required by `bob-software.py`.

```bash
pip install numpy==1.26.4
```

### Test bob-software.py

Now, let’s check this out!

```bash
python bob-software.py
"Good! Your Python version is 3.11 or higher and NumPy version is 1.26.4"
```

Great, you’ve mastered it. Now, if you want to deactivate or exit from using the
`bob` environment, simply type

```bash
 conda deactivate bob
```

### Test alice-software.py

But now, imagine you have `alice-software.py` we have encountered previously.
Alice is your collaborator and has a specific requirement for her code. This
would not work with the current `bob` environment since our numpy version is
different in that `bob` environment.

```bash
python alice-software.py
# FAIL to compile. Check your Python and NumPy versions
```

It fails as expected if you use the `bob` environment since the numpy version is
1.26.4 but Alice requires we use `1.26.3` instead. Now, it’s best to simply
create another environment shown below. Copy the line step by step except the
comment

you can create another environment called `alice` with the following lines of
code as we have seen

```bash
# exit from the "bob' environment
conda deactivate

# install new env called "allice"
conda create -n alice python=3.12
conda activate alice

# install numpy 1.26.3, recall bob required 1.26.4
pip install numpy==1.26.3
```

Now, finally run

```bash
python alice-software.py
# Good! Your NumPy version is 1.26.3 and your Python version is 3.11 or higher!")
```

Congratulations! Now, you’ve learned how to create Conda environments and switch
between them. If you are interested, keep going! We will be using a real life
example in the following.

## Bonus: relationship between Conda and pip

What is the relationship between `Conda` and `pip`? An analogy can clarify this.
Consider `Conda` as an island creator and `pip` as a ship that brings supplies
(Python packages) from the outside world (the internet) to the island. For
instance, `pip` delivers wonderful packages like numpy to the specific Python
v3.11 island.

## Real-life example with CIF Cleaner

Here, we will be using one of my Python packages that filters a list of CIF
**(Crystallographic Information File)**. A CIF is simply a file that stores
information about a crystal. The details about the program are not important.
The essence is that this package requires specific versions. Copy each line to
your command-line and see if that works!

```bash
# clone the software known as "cif-cleaner"
git clone https://github.com/bobleesj/cif-cleaner.git

# go to the folder
cd cif-cleaner

# create an environment called "cif" with the specific Python
conda create -n cif python=3.12

# activate the environment
conda activate cif

# install all the packages (see below)
pip install -r requirements.txt

# run the code
python main.py
```

When you run `python main.py` you should be able to see the following welcome
message

```bash
Welcome! Please choose an option to proceed:
[1] Move files based on unsupported CIF format
[2] Move files based on unreasonable distance
[3] Move files based on tags
[4] Copy files based on atomic occupancy and mixing
[5] Get file info in the folder
[6] Check CIF folder content against Excel file
Enter your choice (1-6):
```

One moment, do you see the `requirements.txt` file as shown below?

![Image 3 - pip install requirements](/files/blog/2024-02-26-intro-python-package-manager/img/3.png)

Well, when you run `pip install -r requirements.txt` instead of manually listing
dozens of Python libraries with specific versions, the developer, “Bob” in this
case, has simply laid out what to install. This makes everyone's life simple and
easy.

## Final remarks

How are you? I find it helpful to test my understanding by formulating questions
and answering them mentally. I encourage you to gauge your learning with the
following questions:

1. What is the main challenge in open-source development?
2. Can you define a package manager and explain its necessity?
3. How can a package manager be used in practice?
4. **Bonus:** Can you describe the step-by-step process of using Conda?
5. **Extra Bonus:** Can you explain the relationship between `Conda` and `pip`
   by using an analogy?

If you have found this tutorial useful for your scientific endeavor, please stay
tuned for more by following me on [GitHub](https://github.com/bobleesj) or
simply reaching out for any questions. Let's keep learning!

## Cheatsheet

Here is a list of commands I use frequently.

```bash
# create an environment called "bob"
conda create -n bob python=3.12

# activate the "bob" environment
conda activate bob

# install a package with a specific version
pip install numpy==1.26.4

# install a package with a version compatible with Python version
pip install numpy

# install packages in requirements.txt (only if the txt file is available)
pip install -r requirements.txt

# update your Python version in the activated environment
conda install python=3.xx

# list all packages associated with "bob"
conda list -n bob

# list all environments installed on your computer
conda env list

# remove the environment called "bob"
conda env remove --name bob
```

## Source code

[GitHub](https://github.com/bobleesj/bobleesj.github.io/tree/main/files/blog/2024-02-26-intro-python-package-manager/source-code)
|
[Markdown](https://github.com/bobleesj/bobleesj.github.io/blob/main/_posts/2024-02-26-intro-to-python-package-manager.md)
