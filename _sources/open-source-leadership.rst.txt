.. _open-source-leadership:

Guide for leading open-source software
==================================================

About 10 years ago, I started using GitHub to distribute tutorial source code for the Swift programming language. Here I document open-source software development leadership lessons. Many are learned from building ``scikit-package`` (https://scikit-package.github.io/scikit-package/) as a contributor and maintainer with Prof. Simon Billinge. It first begins with the **core principles**, followed by practices.

**Core principles**

1. The path of **least resistance (pain) guides human behavior**. It is the leader’s responsibility to provide this path for contributors in every aspect of the project, from installation and tutorials to documentation and development guides.
2. **Joy is the driving force.** Volunteer-based contributors seek joy and meaning in exchange for their time. The leader must recognize that time and effort are valuable and treat them with respect.
3. **No contributor wants to sabotage the project**. Contributors join the community with good intentions but may have different experiences and skills. The leader must ensure that even those with the least experience can contribute and attain joy from the process.
4. **How we work is often more important than what we work on**. What we work on is temporary, but how we work forms the *culture*. There are multiple routes to achieve the same goal. The leader must ensure the process is enjoyable and rewarding. Without joy, the reason to contribute diminishes, and the project may lose valuable contributors.

Using the principles above, I detail practices adopted in my open-source projects that align with these principles.

The leader must design and provide a path with the least resistance.
-------------------------------------------------------------------

Contributors have different levels of training, especially in scientific software projects. We should utilize automated tools like ``pre-commit CI`` to reduce resistance. While intermediate to advanced contributors may run ``pre-commit install`` or ``pre-commit run --all-files`` locally, novice contributors can still contribute to the project from the GitHub interface without knowing about ``pre-commit`` or linting to fix quick issues. In the end, ``pre-commit CI`` ensures uniformity of the codebase and reduces the burden on maintainers to review code that does not follow the project's coding standards. The path of least resistance is crucial for first-time contributors, as it allows them to focus on the joy of contributing rather than getting bogged down by technical details and PEP standards.

In ``scikit-package``, we also provide CLI commands such as ``package add news --add -m <Enter news item for the PR.>`` to generate a news file that is later compiled into the `CHANGELOG <https://github.com/scikit-package/scikit-package/blob/main/CHANGELOG.rst>`_. Previously, it was required to manually create a news file by running ``cp news/TEMPLATE.rst <branch-name>.rst`` and then manually adding the news item either from the terminal or a text editor. This was a barrier for first-time contributors. Now, the CLI command automatically generates the news file with the correct name and format, making it easier for contributors to add news items without worrying about the details. This is an example of how we can provide a path of least resistance for contributors.

Of course, writing the news for each PR can feel strange for first-time contributors. This is valid because they are new users and have not yet used the stremalined release process and how much time it saves for scineitsts in maintaining software. In the PR comment, we should provide step-by-step guides and write them out after explaining why a certain practice is beneficial for the overall project mission, aiming to persuade and not dictate. People want to be persuaded because it implies there is no right or wrong way, but a well-thought-out way to do things. Recall everyone contributes in good faith. **It is the leader's responsibility to convince contributors that we are doing the least resistance path**. In fact, often times, contributors are excited to learn new practices and would appreciate the leader taking the time to explain the reasoning behind them.

How we work is often more important than what we work on at the moment.
-----------------------------------------------------------------------

When I wake up, I open my GitHub mobile app. When I see a **purple notification indicating my pull request has been merged** with a thumbs-up emoji, it makes me smile. From this, we can learn an important lesson: joy matters. Joy attracts attention. Joy creates a positive feedback loop that encourages further contributions. Therefore, **the leader's ability to generate joy is essential for keeping contributors engaged**. Anything that induces joy is good behavior. Anything that diminishes it is undesirable. When we communicate, the one principle is to maintain joy in the process. Thanks to Git and GitHub, nothing is truly in danger; in fact, anything can be reverted. How we work matters, not just what we work on, because how we work and how we communicate determine the degree of joy in the process. The greater the joy, the more attention and engagement we receive from contributors.

The leader should acknowledge every contributor's idea, bug finding, and feature in detail
------------------------------------------------------------------------------------------

To lower the barrier for first-time contributors, we kept the GitHub issue and pull request template as simple as possible. For example, the issue template at https://github.com/scikit-package/scikit-package/blob/main/.github/ISSUE_TEMPLATE/bug_feature.md is sufficient. It consists of “Problem” and “Proposed solution.” The “Proposed solution” section encourages the issue writer to think about the issue, explore, and develop a sense of ownership. It is like building IKEA furniture: as we spend more time with the tool, we own the process and the final product.

When a bug is reported in a project and I fix it, in the pull request description, I thank the contributor for reporting the bug and explain in detail how it was fixed. This way, we keep contributors engaged. When a contributor suggests or implements a new feature, first, acknowledge that on the first page of the documentation and also, from time to time, tag the contributor when the feature is used so that we engage the contributor. The goal is to communicate their value and shore appreciation for their contributions. That's the least we can do. It must come from the leader of the project.

The leader should provide every resource to help spread via word-of-mouth
-------------------------------------------------------------------------

If useful, the software will be shared. GIFs can help, especially for interactive CLI tools and GUI-based applications. A simple list of selling points also helps with copy and paste via email when sharing with colleagues. If applicable, a URL link to Jupyter or web-based demos (for example, Google Colab) helps so people do not need to install anything to try it. The step-by-step “Getting Started” section should not be too long so first-time visitors are not overwhelmed. The path of least resistance is fundamental for early adopters.


*First draft Jun 25, 2025 (Incheon, South Korea)*