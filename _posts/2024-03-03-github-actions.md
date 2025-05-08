---
layout: post
title: How to use GitHub Actions for effective testing in Python open-source projects
categories: tutorial
---

## Why use GitHub Actions

GitHub Actions **automates** tasks for your program, such as compiling blog
posts into HTML and uploading them to your domain. It runs in GitHub's
environment, automatically building and testing code changes made to your
repository.

This includes installing necessary packages and executing tests. If there's an
error during the process, it alerts you; if everything runs smoothly, it
confirms success with a green checkbox. GitHub Actions streamlines the build and
deployment process, making it efficient for both owners and contributors.

Here, we will learn how to use GitHub Actions to run our program locally.

### Prerequisite

I assume you have a basic understanding of GitHub and you use GitHub for your
project development.

## First step - create a `yml` file

Create a file called `python-run-pytest.yml` located at
`your-folder/.github/workflows/python-run-pytest.yml`.

![Image 6 - GitHub Actions YAML file](/files/blog/2024-03-04-github-actions/img/6.png)

See an example from a repository
[here](https://github.com/bobleesj/cif-cleaner/blob/main/.github/workflows/python-run-pytest.yml).
Copy and paste the following to `python-run-pytest.yml`

```yaml
name: Python Package using Pip and Venv

on: [push]

jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 5

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python 3.12
        uses: actions/setup-python@v3
        with:
          python-version: "3.12"

      - name: Create virtual environment and install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      # - name: Lint with flake8
      #   run: |
      #     source venv/bin/activate
      #     pip install flake8
      #     flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
      #     flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

      - name: Test with pytest and generate coverage report
        run: |
          source venv/bin/activate
          pip install pytest pytest-cov
          python -m pytest --cov=./ --cov-report=xml

      - name: Upload coverage reports to Codecov
        uses: codecov/codecov-action@v4.0.1
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          slug: bobleesj/cif-cleaner
```

### GitHub Actions with Pytest and Codecov

I use Python [Codecov](https://about.codecov.io/) to visualize the percentage of
my lines of code covered with tests. The following is used for the GitHub
Actions yaml file. If you are new to GitHub Actions, you may read my tutorial
[here](https://bobleesj.github.io/tutorial/2024/03/03/github-actions.html). No
tutorial has been covered on Codecov at the moment.

## Understand keywords

We shall be able to adjust GitHub Actions for each project. Let's go through
block by block.

### 1. Step Trigger

```yaml
on: [push]
```

- The workflow runs every time code is pushed to the repository.

### 2. Setup OS and job execution strategy

```yaml
jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 5
```

- Runs on the latest Ubuntu virtual environment (`runs-on: ubuntu-latest`).
- Allows up to five instances of the job to run in parallel (`max-parallel: 5`).

### 3. Setup Python version

```yaml
steps:
  - uses: actions/checkout@v3

  - name: Set up Python 3.12
    uses: actions/setup-python@v3
    with:
      python-version: "3.12"
```

- `uses: actions/checkout@v3` checks out the repository so it can be accessed by
  the workflow.
- `uses: actions/setup-python@v3` with `python-version: '3.12'` sets up Python
  3.12.

### 4. Create virtual environment and install dependencies

```yaml
 - name: Create virtual environment and install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
```

- Creates a Python virtual environment (`python -m venv venv`) and activates it
  (`source venv/bin/activate`).
- Installs dependencies with `pip install -r requirements.txt`.

### 5. Lint with flake8

```yaml
- name: Lint with flake8
  run: |
    source venv/bin/activate
    pip install flake8
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

- Typically used for catching errors and enforcing coding standards, but skipped
  in this workflow.
- The `flake8` linting step is commented out, indicating a temporary disablement
  of linting to focus on testing or troubleshooting.

### 6. Test with pytest

```yaml
- name: Test with pytest
  run: |
    source venv/bin/activate
    pip install pytest
    python -m pytest
```

- Activates the virtual environment and installs `pytest`
  (`pip install pytest`).
- Runs tests using `python -m pytest` to verify expected behavior.

## View GitHub Actions

After you've created the file and uploaded `python-run-pytest.yml` to your
repository, click on `Actions` on your repository. For my example, visit
[https://github.com/bobleesj/cif-cleaner/actions](https://github.com/bobleesj/cif-cleaner/actions).

![Image 1 - Github Actions Page](/files/blog/2024-03-04-github-actions/img/1.png)

Click on one of the runs. Explore as you wish.

![Image 2 - GitHub Actions page 2](/files/blog/2024-03-04-github-actions/img/2.png)

### Bonus - GitHub Actions via VS Code

Go to `extensions` and download GitHub Actions

![Image 5 - VS Code Extensions](/files/blog/2024-03-04-github-actions/img/5.png)

Press `cmd-shift-p` and click on GitHub Actions

![Image 3 - GitHub Actions on shift-p](/files/blog/2024-03-04-github-actions/img/3.png)

No need to visit the repository as shown below just to check whether your code
runs. It will save time for you since you do not have to wait and stare at
GitHub actions on the website compiling and executing your code.

![Image 4 - GitHub Actions on panel](/files/blog/2024-03-04-github-actions/img/4.png)

## Source code

[Markdown](https://github.com/bobleesj/bobleesj.github.io/blob/main/_posts/2024-03-03-github-actions.md)

If you have any questions, feel free to shoot me an email at
[sl5400@columbia.edu](mailto:sl5400@columbia.edu).
