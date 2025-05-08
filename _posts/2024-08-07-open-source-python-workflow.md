---
layout: post
title: Python open-source project workflow at Billinge group

categories: tutorial
---

This post assumes you have a background in the general GitHub workflow and you
have forked a repository and contributed to a project. If the previous sentence
is difficult to understand, I recommend you learn more about GitHub and revisit
this blog post.

First, I have recently joined Prof. Simon Billinge’s group
([https://github.com/Billingegroup](https://github.com/Billingegroup)). The
group manages highly cited open-source projects.

As I began to make a contribution and receive feedback, I decided to write this
blog post to document my learning from Prof. Billinge. He maintains all of the
repositories and merges all pull requests.

I will continue to update the document.

- [GitHub: Jargon](#github-jargon)
- [GitHub: Clone origin](#github-clone-origin)
- [GitHub: Clone upstream branch](#github-clone-upstream-branch)
- [GitHub: Make changes to main before PR merged](#github-make-changes-to-main-before-pr-merged)
- [GitHub: Stage](#github-stage)
- [GitHub: Delete remote branch](#github-delete-remote-branch)
- [GitHub: Handle commit mistake 1](#github-handle-commit-mistake-1)
- [GitHub: Pull request best practices](#github-pull-request-best-practices)
- [GitHub: Clean commit history with Rebase](#github-clean-commit-history-with-rebase)
- [GitHub: Visit specific commit state](#github-visit-specific-commit-state)
- [GitHub: Check differences between branches](#github-check-differences-between-branches)
- [GitHub: Reivew commits](#github-reivew-commits)
- [Conda: Create an environment and download files](#conda-create-an-environment-and-download-files)
- [Conda: Useful commands](#conda-useful-commands)
- [Pre-committer: Run all files](#pre-committer-run-all-files)
- [Unix Commands: Copy files](#unix-commands-copy-files)
- [Docs: Sphinx commands](#docs-sphinx-commands)
- [CHANGELOG](#changelog)
- [References](#references)

## GitHub: Jargon

First, we need to use the community technical jargon to facilitate
communication.

- `origin` refers to your forked repository.
- `upstream` refers to the repo you’ve forked.
- `PR` refers to pull request

## GitHub: Clone origin

Let us clone the `origin` repository.

```bash
# Method 1. Git clone (main branch) and download all branches
git clone <repo-URL>
git fetch --all

# Method 2. Git clone a specific branch
git clone --branch <branch-name> <repo-URL>

# Show all branches
git branch -a

# Checkout the branch called "cookie"
git checkout cookie
```

## GitHub: Clone upstream branch

Assume your pull request to `main` in the `upstream` repo has been instead
merged to a new branch, for example, called `cookie` by the reviewer. The
reviewer suggests I continue working from the `cookie` branch from the
`upstream` repo. (See
[https://github.com/diffpy/diffpy.snmf/pull/54](https://github.com/diffpy/diffpy.snmf/pull/54)
for details).

```bash
# Add a new remote repository called "upstream"
git remote add upstream https://github.com/diffpy/diffpy.snmf

# Fetch all branches and updates from the upstream repository
git fetch upstream

# Or you can fetch all, both origin/remote
git fetch --all


# Method 1. Creates a local branch named cookie that tracks upstream/cookie
git checkout -b cookie upstream/cookie

# Method 2. Also valid (tracks upstream/cookie automatically)
git checkout cookie

# Ensure you have the latest updates
git pull

# Make a local branch from "cookie"
git checkout -b flake8
```

The `-b` flag is to create a new branch.

## GitHub: Make changes to main before PR merged

The best practice is to make a separate branch from `main` instead of from the
branch that was just used for the PR. The goal is to make the reviewe process
modular and manageable without having commits from the previous PR in most
cases.

```bash
# Add the upstream repo
git remote add upstream https://github.com/diffpy/diffpy.nmf_mapping.git

# Switch to your local main branch
git checkout main

# Fetch origin/upstream remote branch info
git fetch --all

# Pull changes directly from upstream/main into your local main branch
git pull upstream main

# Make a new local branch for further development
git checkout -b branch-name

# Push to origin
git push origin branch-name
```

## GitHub: Stage

Once you modify the project files, `git add` is used to track/index files before
`git commit`.

```bash
# stage specific file format
git add *.rst

# stage specific file format within a directory
git add requirements/*.txt

# stage mutiple folders
git add doc/source/_static/ doc/source/api/ news/

# stage all files (not recommended during refactoring)
git add .

# To unstage all files
git reset
```

## GitHub: Delete remote branch

We may need to manually delete remote or local branches as needed.

```bash
# Delete remote branch
git push origin --delete cookierelease

# Delete local branch
git branch -D cookierelease
```

## GitHub: Handle commit mistake 1

You’ve made a commit. Now, you want to re-visit the previous commit.

```bash
# To reset local branch to previous commit (when working alone)
git reset --hard HEAD~1
git push --force
```

This is a valid practice for a personal project and you are working on a branch
alone. However, `--hard` and `--force` should not be used on shared branches.

`git pull` does both `git fetch` and `git merge`.

## GitHub: Pull request best practices

- Separate PRs for file relocation and modification
- Be in the reviewer's shoes. Keep a PR request reasonably short and concise
- Push a few commits in a PR for an easier review process
- Commit messages should contain unique information and provide purpose

## GitHub: Clean commit history with Rebase

Before requesting a merge, we often have commits that may not be as productive
or friendly for reviewers. To maintain a clean commit history, we may want to
squash multiple commits into a single commit.

TBA

## GitHub: Visit specific commit state

If you want to use files at a specific commit, use the following.

```bash
git remote add upstream https://github.com/diffpy/diffpy.snmf

# Go to the specific
git checkout fb9661e2abd5f1cc1fa15a8230813ce1ccc7cd21

# Make a local branch
git checkout -b new-branch-name
```

## GitHub: Check differences between branches

```bash
# Compare lines added/removed
git diff <branch1>..<branch2> --stat

# Compare specific files
git diff <branch1>..<branch2> -- path/to/file

```

## GitHub: Reivew commits

```bash
# Show commit details
git log

# Limit # of commits
git log -n 5

# Search by author
git log --author="Author Name"

# View detailed changes
git log -p

# Summary of changes
git log --stat
```

## Conda: Create an environment and download files

```bash
# Create an environment
conda env create -f environment.yml

# Update the existing environment (if needed)
conda env update -f environment.yml --prune

# Activate
conda install --file requirements/run.txt
conda install --file requirements/test.txt

# Download the package locally from "src"
pip install .
```

## Conda: Useful commands

```bash
# Get info activated environment
conda info

# List all environments
conda env list
```

Reviewer is future you Reviewer is the referee

Nothign is working - trying to fix it, i want to go back git log, if you write
good messages, that cause the problem

Add conda testgit

`make Conda env before install`

Visit
[https://github.com/diffpy/diffpy.snmf](https://github.com/diffpy/diffpy.snmf)
to see the specific `.txt` and `yml` files.

## Pre-committer: Run all files

Refer to https://bobleesj.github.io/tutorial/2024/07/01/precommiter for a
tutorial

tab complete

```bash
pre-commit run --all-files
```

## Unix Commands: Copy files

You may need to copy files systematically. See the details.

```bash
# Copy the content of "source"
cp -n -r ../doc/source/* <destination-path>

# Copy the folder of "source"
cp -n -r ../doc/source <destination-path>
```

- `n` "no-clobber" is used to prevent overwriting existing files, `r` refers to
  copying files recursively.

## Docs: Sphinx commands

```bash
# Build the HTML documentation
make html

# Open the generated documentation
open build/html/index.html
```

## CHANGELOG

The blog post is constantly updated.

- Aug 7, 2024 - posted a blog

## References

- https://github.com/diffpy/diffpy.snmf/pull/56
- https://github.com/diffpy/diffpy.snmf/pull/54
