---
layout: post
title: Automate Markdown formatting (Ft. Prettier)
categories: tutorial
---

## Motivation

Similar to the post on the Python automatic styling tool, Black, in my tutorial
[here](https://bobleesj.github.io/tutorial/2024/03/11/python-styling-guide.html),
we want to improve the readability and consistency of Markdown files using
`Prettier`.

This tutorial should take less than 5 minutes to complete.

### Step 1: Download and Install Node.js

Broadly speaking, Node.js is analogous to `Conda`. `npm` is analogous to `pip`.
Download Node.js from the
[Node.js official website](https://nodejs.org/en/download). `npm` will be
installed automatically.

### Step 2: Install Prettier

With Node.js and `npm` installed, install Prettier globally or in your project
directory:

```bash
npm install prettier
```

### Step 3: Run Prettier

Format all Markdown files in your project directory:

```bash
npx prettier --write "**/*.md"
```

### Step 4: Configure Prettier

Create a `.prettierrc` file in your project's root directory with the following
settings:

```json
{
  "printWidth": 80,
  "proseWrap": "always"
}
```

This configuration sets the maximum line width to 80 characters and ensures
proper wrapping of prose.

### Step 5: Use `.prettierignore`

To ignore certain files or directories from being formatted, create a
.prettierignore file in your project's root.

```txt
# Ignore artifacts:
_posts/2024-03-22-mathematical-typesetting.md

# Ignore all HTML files:
# **/*.html
```

## Bonus: Markdownlint

Markdownlint is another Markdown tool.

### Step 1: Install and Run markdownlint

Again, download via `npm`.

```bash
npm install markdownlint-cli
markdownlint --fix "**/*.md"
```

This command will automatically fix issues in all Markdown files according to
the rules defined in your markdownlint configuration.

## Source Code

You may see how the current website uses `Prettier` to format Markdown below.

[GitHub](https://github.com/bobleesj/bobleesj.github.io) |
[Markdown](https://github.com/bobleesj/bobleesj.github.io/blob/main/_posts/2024-03-24-markdown-prettier.md)
