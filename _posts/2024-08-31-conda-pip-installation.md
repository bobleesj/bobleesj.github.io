---
layout: post
title: Why there are two Python installation methods (Feat. Conda and pip)
categories: tutorial
---

## Motivation

The blog post attempst to answer the question: Why is it necessary for an
open-source project to provide two installation methods for a Python package?

```bash
pip install bobkit
```

or

```bash
conda install bobkit
```

## Prerequsites

Recall that `conda install bobkit` downloads the package from `conda-forge` most
likely. If the previous sentence is unclear to you, read
[Distinguish key components in the Conda ecosystem (Ft. mamba, conda-forge, Miniconda, Anaconda, miniforge, and more)](https://bobleesj.github.io/tutorial/2024/08/30/conda-ecosystem.html).
If you are new to Conda and its motivation, read
[How to use the Python package manager for beginners (Ft. Conda with Cheat sheet)](https://bobleesj.github.io/tutorial/2024/02/26/intro-to-python-package-manager.html)

## Why Conda and pip are both used

`conda` and `pip` serve different purposes:

- `pip` is the simplest solution to build and maintain a Python package. e.g.,
  `pip install -e .` for install in editable mode.
- `Conda` is the community's solution to install packages written in any
  programming languages.

Here is what they do not attempt to do:

- `pip` does not attempt to be an environment manager.
- `Conda` does not attempt to build and maintain a Python package.

The confusion often starts here, which is the main point of this blog post:

- `pip` communicates with `PyPI` to upload and download Python packages.
- `conda` communicates with repositories like `conda-forge` to upload and
  download packages, including but not limited to Python packages.

When you make a `Conda` environment, you can still download Python packages
using `pip install <package-name>` or `conda install <package-name>`. So why
bother uploading the Python code both on PyPI and conda-forge?

- Some users may want to use one package manager instead of mixing `pip` and
  `conda`.
- Reach a wider audience beyond the Python community since conda-forge is a
  language-agnostic platform. Users can access it even those without prior
  experience in the Python community and jargon.
- Furthermore, during a new release, you can make a simple Python script to
  upload to `conda-forge` with a new release on `PyPI` within a minute.

## Best practices

While I am still learning, here is the workflow used in the research group.

### For package developers:

For a complex program, for any `README.md`, I would always provide an
instruction to create a Conda environment like here
https://github.com/Billingegroup/bg-mpl-stylesheet that I contribute to in the
group.

```bash
conda install --file requirements/run.txt
conda install bg-mpl-stylesheets
```

where `run.txt` would look like:

```text
numpy
pandas
matplotlib-base
```

Then, as the second option, I would also provide an instruction using `pip` for
those without prior experience with Conda.

### For package users:

If the package provides a package hosted on `conda-forge`, then, I would try to
download all of the packages using `conda install ...` as shown above. And then,
I would only `install pip packages` that are not available on `conda-forge`.

```bash
# Install all packages via conda-forge
conda install --file requirements/run.txt

# Use pip to install additional Python packages not available on Conda
pip install other-packages

# Regularly update your environment and test after updates
conda update --all
pip list --outdated
pip install --upgrade some-updated-package
```

## Last Remarks

`pip` and `conda` complement each other. It's easier to understand their
distinct roles by focusing on what they are not designed to do. `pip` can serve
as a _Python_ package development tool, which `conda` does not offer.
Conversely, `conda` serves as an environment manager for any programming
language, a role that `pip` does not fulfill. While both can install Python
packages, `conda` also supports the installation of non-Python packages.

It is best practice for package managers to distribute their Python packages on
`conda-forge` as well to streamline the installation process using `conda` and
to reach a wider audience beyond the Python community.

Please feel free to suggest any ideas.

## References

- https://github.com/billingegroup/bg-mpl-stylesheets
- https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/
- https://stackoverflow.com/questions/34398676/does-conda-replace-the-need-for-virtualenv
