---
layout: post
title: Distinguish key components in Conda ecosystem (Ft. mamba, conda-forge,
  Miniconda, Anaconda, miniforge, and more)

categories: tutorial
---

## Motivation

The goal is to understand the differences between all of these snake-driven
names in the title. This post is written for those who have used Conda before,
including myself, but want to clarify the concepts.

## Create an environment with Conda

Conda is a package and environment manager. If the previous sentence is unclear
to you, please read my previous tutorial on
[How to use Python package manager for beginners (Ft. Conda with Cheatsheet)](https://bobleesj.github.io/tutorial/2024/02/26/intro-to-python-package-manager.html)

## Define Conda package

First, let us define a Conda package. A Conda package is code that has been
compiled for specific platforms (Windows, macOS, Linux) and can be immediately
used once installed. A Conda package can be installed via the
`conda install ...` command.

## Download and install Conda packages with conda-forge

Second, the developer must be able to host the Conda package online. The user
must be able download the package online.

`conda-forge` is an online repository of Conda packages. It functions similarly
to `PyPI`, allowing users to download packages. `conda-forge` is one of several
repositories in the Conda ecosystem. Anyone can create a channel or repository
to host Conda packages. `conda-forge` is the leading community-maintained
repository, backed by companies such as NVIDIA

## Install Conda with Miniconda, Miniforge, and Anaconda

While Conda is an environment manager, Conda itself is a piece of software that
needs to be installed locally. Hence, we need installers. There are multiple
installers.

First, Miniconda allows you to download only the packages needed to manage
packages and environments.

Second, Anaconda is another installer but much greater in size. It not only
installs Conda but also includes Python packages such as NumPy, pandas, and
Jupyter Notebook. This comprehensive solution is often used for educational
purposes. For example, in my undergraduate numerical methods class, we used
Python and its libraries like scikit-learn to implement numerical methods
without needing to download additional packages. Since all the core Python
packages are pre-installed, students did not have to run conda install.

Third, Miniforge is another installation that includes Conda, `mamba`, and
Python with the conda-forge channel pre-configured. Let us discuss `mamba` next.

## Use Mamba to manage Conda packages faster

Recall that Conda is a dependency manager. It has algorithms for identifying
compatible software given the software versions. As you can imagine, as the
number of dependencies increases, the sorting computation will be exponential.

For a complex environment, there was a need to do the sorting process faster.
Hence, `mamba` was developed. `mamba` is a “drop-in replacement” for Conda,
using the same commands and configuration options. It features a faster
dependency-solving algorithm written in C++.

`mamba` is also a standalone tool that can replace all the functionalities of
Conda, such as installing and managing packages. It is also compatible with
existing Conda environments for downloading packages, but still relies on the
Conda ecosystem for package distribution and formatting and utilizing the
community's install such as `conda-forge`.

```bash
# Create an environment
mamba create -n bobmamba <list of packages>

# Install a package
mamba install "matplotlib"
```

If you have any questions, please feel free to reach out for any.

## References

mamba: https://mamba.readthedocs.io/en/latest/user_guide/mamba.html

Miniforge: https://github.com/conda-forge/miniforge
