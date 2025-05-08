---
layout: post
title: Pros and cons of pre-commiter framework and my verdict (Ft. pre-commit)
categories: tutorial
---

## Motivation

Before uploading or committing with `git commit`, it is essential to locally
check that the modified code adheres to the principles and styling guide
provided by the GitHub repository maintainer.

Here, `pre-commit` is a simple Python library that checks formatting and linting
so that contributors must follow the shared practices to maintain code quality
agreed upon by members.

## Installation

When you run `git init`, it generates files containing `.git/hooks/pre-commit`.

This folder contains `.sh` scripts that allow you to execute a set of tasks to
check for issues, like running tests for formatting and linting the code before
`git commit`.

Of course, `pre-commit` will automate the above process.

Install via:

```bash
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## How to use

Create a file named `.pre-commit-config.yaml` at the project level. Here, I want
to add a few hooks for checking yaml and running `ruff`.

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.5.0
    hooks:
      # Run the linter.
      - id: ruff
        args: [--fix]
      # Run the formatter.
      - id: ruff-format
```

Once the config file is in place, make a regular commit:

```text
git add .
git commit -m "Use a numpy version of 1.23"
```

`pre-commit` tests locally and either rejects or approves your commit as shown
below and modifies the files:

```text
[INFO] This may take a few minutes...
Check Yaml...............................................................Passed
Fix End of Files.........................................................Failed

- hook id: end-of-file-fixer
- exit code: 1
- files were modified by this hook

Fixing .pre-commit-config.yaml

Fixing [README.md](http://readme.md/)
```

Once they are fixed automatically by `pre-commit`, run the commit command again:

```
git commit -m "Use a numpy version of 1.23"
```

## Debates on usage

### Against

- Linting and formatting checks occur in CI, no need for duplication.
- Developers can format freely but must adhere to project standards before
  pushing to the branch.
- Precommit hooks can interrupt workflow.
- They often get disabled until PR merge due to their annoyance.
- When developers feel impeded, they tend to increase the size of their commits.

### For

- It prevents contributors from submitting ill-formatted code, saving time
  before CI checks.

### My verdict

As of now, I am overall optimistic about using `pre-commit`. Here is my
justification:

In my workflow, I use `nodemon` to run `mypy`, `ruff`, and `pytest` each time I
modify a file. However, not all users adopt my workflow. It is likely that I
will have no problem with `pre-commit` hooks since I regularly check them.

But the issue becomes more significant with open-source project contributions. I
want the codebase to remain consistent and adhere to the standard. While GitHub
Actions can perform the exact task, it requires 10-15 minutes. I want
contributors (mostly without formal CS background) to feel confident that when
the code passes at the commit level, it can be considered mergeable.

As long as `pre-commit` takes within 10 seconds or so, I am optimistic.

## References

- https://www.reddit.com/r/ExperiencedDevs/comments/144fcqo/what_are_your_precommit_hooks/
- https://www.reddit.com/r/git/comments/16ke0xa/arguments_for_and_against_precommit_hooks/
- https://www.thoughtworks.com/en-us/insights/blog/pre-commit-don-t-git-hooked
- https://pre-commit.com/
- https://medium.com/@josephbkahn/pre-commit-hooks-the-good-the-bad-the-ugly-5c5ff7a0d0d8
