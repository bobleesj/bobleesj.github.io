.. _open-source-leadership:

Guide for Leading Open-Source Software
--------------------------------------

About 10 years ago, I started using GitHub to distribute tutorial source code for the Swift programming language. As I take on leadership roles, I document the principles I strive to follow. Many of these were learned from ``scikit-package`` (https://scikit-package.github.io/scikit-package/), where I learned from Prof. Simon Billinge.

**Core Principles in Open-Source Leadership**

1. The path of **least resistance (pain) guides human behavior**. It is the leader’s responsibility to provide this path for contributors in every aspect of the project, from installation and tutorials to documentation and development guides.
2. **Joy is the driving force.** Participation is often **volunteer-based**. Contributors seek joy and meaning in exchange for their time. The leader must recognize that time and effort are valuable and treat them with respect.
3. **No contributor wants to sabotage the project**. Everyone joins with good intentions but may have different experiences. This is especially true in life sciences, where contributors have diverse backgrounds. The leader must ensure that even those with the least experience can contribute and find joy.
4. **How we work is often more important than what we work on**. What we work on is temporary, but how we work forms the *culture* and is lasting. There are many ways to achieve the same goal, but the process defines us. The leader must ensure the process is enjoyable and rewarding. Without joy, there is no reason to contribute.

Using the principles above, let us answer important questions that arise in open-source leadership.

**Am I providing the path of least resistance for contributors?**

Contributors have different levels of training, especially in scientific software projects. Automated tools help ensure uniformity. ``pre-commit CI`` is a solution. Intermediate and advanced programmers should use ``pre-commit install`` or run ``pre-commit run --all-files`` locally, while novice contributors can fix and improve wording directly from the GitHub interface without knowing about ``pre-commit`` or linting. In the end, ``pre-commit CI`` ensures uniformity of the final source code for incoming PRs.

**Is joy generated? How we work matters.**

When I wake up, the first app I use is the GitHub mobile app. I am excited to see how my PRs and issues are doing for projects such as ``scikit-package``. What makes me smile is the **purple color indicating my pull request has been merged.** We watch movies and play sports because we find joy. The goal is to make contribution enjoyable. When we communicate, the main goal is to maintain joy in the process. Thanks to Git and GitHub, anything can be reverted, and it probably has not been merged to ``main``. First-time contributors may not follow standard practices. While it is the leader's failure to provide the path of least resistance, **the worst scenario is removing joy from the process**. From the principle of joy being the driving force, we lose potential value from willing contributors. How we work matters, not just what we work on, because how we work determines the degree of joy in the process.

**How can I help potential contributors suggest new ideas, features, and report bugs?**

To lower the barrier for first-time contributors, I ensure the GitHub issue template is simple. For example, the issue template at https://github.com/scikit-package/scikit-package/issues/515 is sufficient. It consists of “Problem” and “Proposed solution.” The “Proposed solution” section encourages the issue writer to think about the issue, explore, and develop a sense of ownership. It is like building IKEA furniture: as we spend more time with the tool, we own the process and the final product.

**How can I help with word-of-mouth?**

It is important to market the project. In other words, it needs to be shared and adopted. GIFs can help, especially for interactive CLI tools and GUI-based applications. A simple list of features also helps with copy and paste via email when sharing with colleagues. If applicable, a URL link to Jupyter or web-based demos (for example, Google Colab) helps so people do not need to install anything to try it. The step-by-step “Getting Started” section should not be too long so first-time visitors are not overwhelmed. The path of least resistance is fundamental for early adopters.

**Daily Checklist**

Many of these guides should be practiced daily. Here are items to do almost every day:

- Recognize and compliment incoming code, especially from first-time contributors, as well as issues and each PR review iteration.
- Provide step-by-step guides and write them out after explaining why a certain practice is beneficial for the overall project goal, aiming to persuade and not dictate. People want to be persuaded because it implies there is no right or wrong way, but a well-thought-out way to do things.
- Ensure that when new contributions are created, relevant documentation is updated to recognize the contributor's work.
- Actively look for volunteers so that we communicate the importance of tasks for the project.
