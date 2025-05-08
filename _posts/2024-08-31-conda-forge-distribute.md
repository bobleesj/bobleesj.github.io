---
layout: post
title: Distribute Python package on conda-forge from PyPI
categories: tutorial
---

## Motivation

Let's distribute a package on `conda-forge` that is already distributed on PyPI.
This is one of two methods to distribute packages on `conda-forge`.

## Prerequsites

`conda-forge` is a place to host a Conda package. If the previous sentence is
not clear to you, please read my tutorial on
[Distinguish key components in Conda ecosystem (Ft. mamba, conda-forge, Miniconda, Anaconda, miniforge, and more](https://bobleesj.github.io/tutorial/2024/08/30/conda-ecosystem.html)

The blog is also written for those who have published a package on PyPI because
the hosted package on PyPI will be used. If you are new, please read my tutorial
on
[How to distribute Python package via pip (Ft. Twine)](https://bobleesj.github.io/tutorial/2024/03/22/python-package-distribution.html).

## Step 1: Make a "recipe"

A recipe is a folder containing files to build a conda package including
`meta.yaml` . `meta.yaml` contains information on dependencies, package version,
license, documentation link, and the maintainer(s) for the package. The file we
need to modify is `meta.yaml` and the rest is provided. Check the `meta.yaml`
file of a Python package:
[https://github.com/conda-forge/staged-recipes/pull/15860/files](https://github.com/conda-forge/staged-recipes/pull/15860/files).

To make the recipe:

- Fork and clone the
  [https://github.com/conda-forge/staged-recipes](https://github.com/conda-forge/staged-recipes)
  repository.
- Create a new branch named `<package-name>`.
- Create a new file at `recipes/<package-name>/meta.yaml`. Use the template from
  [https://github.com/conda-forge/staged-recipes/pull/27408/files](https://github.com/conda-forge/staged-recipes/pull/27408/files).
- Modify the file, updating the `name`, `version`, `sha256`, and the sections
  under `requirements` and `about`.
- Pay close attention to the `sha256` value. It's unique for each version. For
  example, visit
  [https://pypi.org/project/cifkit/1.0.2/#files](https://pypi.org/project/cifkit/1.0.2/#files)
  and click "view hashes" to find the correct value.
- **Important** - After the CI tests pass, create a new comment for the
  conda-forge team to review the PR. Use this format: '@conda-forge/help-python
  Hello Team, ready for review!'

## Step 2. Maintain a “feedstock”

Once a conda-forge community member merges the PR, a new repository at
`https://github.com/conda-forge/<package-name>-feedstock` will be automatically
generated and the Conda package will be now available. Check
[https://github.com/conda-forge/bg-mpl-stylesheets-feedstock](https://github.com/conda-forge/bg-mpl-stylesheets-feedstock).

### How to update a Conda package version

A feedstock is a repository for making updates on the conda package. To update
the version, you'll need to modify the `meta.yaml` file in the feedstock
repository. Specifically, you'll update two fields: `version` and `sha256`. This
process assumes you have a new version available on PyPI.

```yaml
version = "new_PyPI_version"
sha256: hash_value_for_new_PyPI_version
```

Then, follow the steps:

1. Fork and clone the feedstock repository.
2. Create a PR with the updated `sha256` and `version`.
3. **Important** - In the PR, write `@conda-forge-admin please rerender` as a
   new comment.
4. Wait for CI tests to pass.
5. Merge the PR.

Once the PR is merged, the cond-forge CI infrastructure automatically updates
the Conda package version.

Check:
[https://anaconda.org/conda-forge/bg-mpl-stylesheets](https://anaconda.org/conda-forge/bg-mpl-stylesheets)

Now, one can download the package with

```bash
conda install <package-name>
```

## Other tips

### Python script for conda-forge update

I created a script called `cf_release.py`. You can download here and read more
here
[https://github.com/Billingegroup/release-scripts/pull/14](https://github.com/Billingegroup/release-scripts/pull/14).

The script automates the process of updating a PyPI package version and its
`SHA256 hash` in a `meta.yaml` file. Behind the scenes, it enters the feedstock
repository, checks out and syncs with the upstream `main` branch, and creates a
pull request (PR) from a new branch. Once a maintainer merges the PR, the Conda
package version is automatically updated.

Folder setup:

1. Ensure the feedstock and release-scripts repositories are in the same folder.
   For example: `…/dev/<package-name>-feedstock/` and `…/dev/release-scripts/`

Running the release script:

1. Execute the script using its absolute path:
   `python .../dev/release-scripts/cf_release.py`
2. The script will ask:
   1. PyPI package name (e.g., `diffpy.pdfgui`)
   2. Python version (e.g., `0.1.3`)

Re-rendering the feedstock repository:

1. If you've manually modified any parts of the feedstock folder, add a new
   comment to the PR: `@conda-forge-admin please rerender`. If not, no action is
   needed.

Finally, wait for the CI tests to pass. Then, tag the maintainer to merge the
PR.

### How to add a maintainer

You may want to add a maintainer to the feedstock repository. `conda-forge`
provides a GitHub bot.

- Create an issue in the feedstock repository.
- Add a new comment: `@conda-forge-admin, please add user @bobleesj`. For an
  example, see
  [this issue](https://github.com/conda-forge/bg-mpl-stylesheets-feedstock/issues/19).
- Wait for a new PR to appear.
- Merge the PR.

## References

- https://conda-forge.org/docs/maintainer/
