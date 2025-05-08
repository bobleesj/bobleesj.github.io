---
layout: post
title: GitHub best practices and cheatsheet
categories: cheatsheet
---

I will update the document as I learn more about GitHub and best practices.

- [Project checklist](#project-checklist)
- [Pull request tips](#pull-request-tips)
  - [Template for pull request](#template-for-pull-request)
- [GitHub commands](#github-commands)
- [References](#references)

## Project checklist

The checklist below can be used to improve usability, marketability, and
open-source development experience.

- **Naming the project**
  - Have you chosen an easy-to-remember name for the project?
- **Addressing the problem**
  - Does the documentation clearly state the problem that the project addresses
    at the beginning?
- **Project description**
  - Have you included a compelling one-liner for the project?
- **Installation instructions**
  - Is there a one-line installation solution provided in the documentation?
- **Visual guidance**
  - Have you used GIFs or screenshots to visually demonstrate how to use the
    project or what the outputs look like?
- **Roadmap**
  - Is there a roadmap included in the documentation to outline future plans and
    features?
- **Authors and acknowledgements**
  - Have you listed the authors and provided acknowledgements to contributors or
    third-party resources?
- **License information**
  - Is the license clearly stated and included in the project documentation?
- **Project status**
  - Have you indicated the current status of the project (e.g., active
    development, maintenance mode)?
- **Contribution guidelines**
  - Are there clear guidelines on how to contribute to the project?
- **Seeking help**
  - Have you provided instructions on how to ask for help or report issues?
- **Version control** (Optional)
  - Have you made a simple log or version control system visible or mentioned in
    the documentation?

## Pull request tips

- Write small pull requests for faster and easier review
- For major changes, consult with the maintainer via `Issues` first
- Use or provide a pull request template like below

### Template for pull request

GitHub may display `pull_request_template.md` content when you request a pull
request like here.

![Pull request template](/files/blog/2024-03-12-github-best-practices/img/1.png)

```md
## What type of PR is this? (check all applicable)

- [ ] Refactor
- [ ] Feature
- [ ] Bug Fix
- [ ] Optimization
- [ ] Documentation Update

## Description (Screenshots, files, etc)

## Checklist

- [ ] Are the tests passing?
- [ ] If it's a new feature, have tests been written?
- [ ] Is the code linted using `Black`?
- [ ] Have you performed a self-review of your code?

## Added to documentation?

- [ ] README.md
- [ ] No documentation needed
```

## GitHub commands

`HEAD` refers to the last commit in the current branch.

```bash
# move to another existing branch
git switch develop

# create a new branch and move
git switch -c new-feature

# merge a branch into the current branch
git merge branch-name

# see previous commits
git log

# to provide the commit hash a tag name
git tag <TAG-NAME>

# move the current branch backward by 1 commit at the commit level
git reset HEAD~1

# to change to the specific commit at the code level
git checkout <hash> -- <name-of-file-to-revert-back>
```

## References

- Git Reset and Revert Commands by Steve Griffith
  [YouTube](https://www.youtube.com/watch?v=ipav1TCV8BI)
