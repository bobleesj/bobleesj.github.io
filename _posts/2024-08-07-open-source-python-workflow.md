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
