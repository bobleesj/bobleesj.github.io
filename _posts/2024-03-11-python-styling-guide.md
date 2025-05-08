---
layout: post
title: Python styling automation tool (Ft. Black)
categories: tutorial
---

## Motivation

I strive to write reusable, well-tested, and modular scripts. It is recommended
to write code that follows the general principles and standards shared by the
community, such as the [PEP 8](https://peps.python.org/pep-0008/). In contrast,
we must prioritize value. Well-formatted code with no unique value is time
misspent, whereas ill-formatted code that provides tremendous value is used.
Therefore, formatting is secondary, and we must automate it, similar to
generating references.

Update: I now use `ruff` instead of `black` due to speed. Please read the new
tutorial [here](https://bobleesj.github.io/tutorial/2024/07/01/ruff.html).

## Automate style guide

Here we have styling guide formatting tools known as `yapf` and `black`. They
are installed via

```bash
pip install yapf
yapf --in-place main.py

pip install black
black main.py
```

### Use Black or YAPF

I use "Black" for two reasons. First, Black does not offer customization but the
line lenght. Second, Black is faster. Based on my brief research online, I have
summarized my findings below.

- YAPF scales quadratically ([Case 1](https://github.com/google/yapf/issues/39),
  [Case 2](https://github.com/google/yapf/issues/264))
- Black produces deterministic codes amongst collaborators by design. We do not
  argue on single quote vs. double quote, etc. No "point" of argument.
  ([Case 1](https://www.reddit.com/r/Python/comments/sidqze/black_vs_yapf_vs/?rdt=61802))
- Black is used by Facebook, Dropbox, Lyft, and Tesla.
  ([README.md](https://github.com/psf/black?tab=readme-ov-file))
- Black is an official Python community project shown below.

![Black Python VS Code](/files/blog/2024-03-11-python-styling-guide/1.png)

### How to use `Black`

Enter the name of the file or the folder containing `.py` after `black`.

```bash
black src
```

To change the line-width,

```bash
black -l 80 tests
```

To lint multiple files and folders,

```bash
black -l 80 postprocess preprocess tests util main.py filter
```

### Line-width debate

I have noticed that every linter often has a differnt line-width limitation. PEP
8 concludes:

> _"Some teams strongly prefer a longer line length. For code maintained
> exclusively or primarily by a team that can reach agreement on this issue, it
> is okay to increase the line **length limit up to 99 characters**, provided
> that **comments and docstrings are still wrapped at 72 characters**."
> <https://peps.python.org/pep-0008/#maximum-line-length>_

### My decision on line-width

I choose the below 80 character limit for two reasons. First, I do not use a
dual monitor to minimize neck strain and mouse usage. Second, I carry a laptop
as a student. I want to maximize productivity using the limited screen real
estate. I must be able to view content with Terminal and two panels open.
