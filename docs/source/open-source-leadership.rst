.. _open-source-leadership:

Guide for leading open-source software
=======================================

About 10 years ago, I started using GitHub to distribute tutorial source code for the Swift programming language. Here I document open-source software development leadership lessons. Many are learned from building ``scikit-package`` (https://scikit-package.github.io/scikit-package/) as a contributor and maintainer with Prof. Simon Billinge. It first begins with the **core principles**, followed by practices.

Core principles
---------------

1. The path of **least resistance (pain) guides human behavior**. It is the leader’s responsibility to provide this path for contributors in every aspect of the project, from installation and tutorials to documentation and development guides.
2. **Joy is the driving force.** Volunteer-based contributors seek joy and meaning in exchange for their time. The leader must recognize that time and effort are valuable and treat them with respect.
3. **No contributor wants to sabotage the project**. Contributors join the community with good intentions but may have different experiences and skills. The leader must ensure that even those with the least experience can contribute and attain joy from the process.
4. **How we work is often more important than what we work on**. What we work on is temporary, but how we work forms the *culture*. There are multiple routes to achieve the same goal. The leader must ensure the process is enjoyable and rewarding. Without joy, the reason to contribute diminishes, and the project may lose valuable contributors.

Using the principles above, I detail practices adopted in my open-source projects that align with these principles.

1. **The path with the least physical and cognitive resistance** is what the leader should provide
---------------------------------------------------------------------------------------------------

Potential contributors have varying levels of experience. For some, making their first commit is a big step. The leader should recognize this effort and create a welcoming environment while maintaining standards. While experienced contributors may run linting tools locally, beginners may not be familiar with linting tools or the forking and cloning workflow.

They might just want to help fix a typo or grammar issue in the documentation. Requiring them to set up ``pre-commit`` or configure a local repository can be discouraging. The workflow should be **flexible enough** that anyone can create a pull request directly from the GitHub interface. One solution is to implement ``pre-commit CI`` to enforce code standards automatically, reducing the burden on both maintainers and contributors.

With reduced resistance, we enable contributors to feel joy through the act of contributing instead of facing technical hurdles. Remember, we buy tape not because we love the tape, but because we need to hang birthday balloons on the wall to make the person happy and capture the moment. The same logic applies to GitHub and its workflow. **The goal is to make useful progress with the tool and find joy in the process**.

Another example is demonstrated in ``scikit-package``. Here, packages that are ``scikit-package`` standardized attach a news file for each PR that is later compiled into the `CHANGELOG <https://github.com/scikit-package/scikit-package/blob/main/CHANGELOG.rst>`_ during full release. Previously, there was physical resistance. It was required to manually create a news file by running ``cp news/TEMPLATE.rst <branch-name>.rst`` and then manually adding the news item either from the terminal or a text editor. This was a barrier for first-time contributors. In the ``0.2.0`` release, I developed a CLI command that automatically generates the news file with the correct name and format, making it easier for contributors to add news items without worrying about the details on how the news files are generated and where they are located. This is an example of how we can provide a path of least resistance for contributors. They will eventually know once they find more joy from the process and become more engaged with the project.

2. **How we work is often more important** than what we work on at the moment.
------------------------------------------------------------------------------

When I wake up, I open my GitHub mobile app. Seeing a **purple notification** indicating that my pull request has been merged—often accompanied by a thumbs-up emoji and a thank-you message—makes me smile. From this emotional response, we can draw an important lesson: **joy matters**. Joy attracts attention. It creates a positive feedback loop that encourages continued contributions and deepens engagement.

**The leader's ability to generate joy is essential for sustaining contributor involvement.** From this connection between joy and contribution, we can say: anything that induces joy is good behavior; anything that diminishes it is bad behavior. This is largely thanks to Git and GitHub, where we operate in a reversible world. If a contributor makes a mistake, they can easily revert it. **This reversibility allows us to experiment and learn without fear of permanent consequences. Open-source contribution becomes a safe space for learning and growth.**

The ``scikit-package`` example illustrates this well. First-time contributors are often asked to write a news entry after submitting a pull request. After putting in significant effort, this extra step may feel tedious or unrewarding. Their initial frustration is understandable. They haven't yet seen the value it adds during the release process or understood how much time it saves maintainers. Simply put, they're not yet **convinced** that the extra effort is worth it.

That's where leadership comes in and where culture is formed. In PR comments, we should **explain the reasoning** behind our design decisions before asking for follow-up actions. Then, we should provide clear, step-by-step guidance. Our goal is to **persuade, not dictate**. People don't want to be told what to do—doing so removes their sense of joy and autonomy.

Autonomy is crucial. It fosters a sense of ownership, which is a deeply ingrained human need tied to our instinct to manage and protect resources for survival. Contributors who feel ownership over a part of the project are more likely to stay engaged because their efforts accumulate practical value—ranging from community recognition to skill development.

In fact, contributors are often excited to learn highly optimized practices. They appreciate it when a leader takes the time to explain the rationale behind a workflow. Ultimately, when contributors feel included in the process and see their impact, they experience a rare and valuable emotion: **joy**. And with that joy comes learning, recognition, and growth for both the individual and the project.


3. The leader should **acknowledge every contributor**'s idea, bug finding, and feature in detail.
---------------------------------------------------------------------------------------------------------

To lower the barrier for first-time contributors, we kept the GitHub issue and pull request template as simple as possible. For example, the issue template at https://github.com/scikit-package/scikit-package/blob/main/.github/ISSUE_TEMPLATE/bug_feature.md is sufficient. It consists of “Problem” and “Proposed solution.” The “Proposed solution” section encourages the issue writer to think about the issue, explore, and develop a sense of ownership. It is like building IKEA furniture: as we spend more time with the tool, we own the process and the final product.

When a bug is reported in a project and I fix it, in the pull request description, I thank the contributor for reporting the bug and explain in detail how it was fixed. This way, we keep contributors engaged. When a contributor suggests or implements a new feature, first, acknowledge that on the first page of the documentation and also, from time to time, tag the contributor when the feature is used so that we engage the contributor. The goal is to communicate their value and shore appreciation for their contributions. That's the least we can do. It must come from the leader of the project.

(FIXME: - Here mention how I congratulated Bala for his first PR contribution in ``cifkit``.)

4. The leader should provide **every resource to help spread** via word-of-mouth.
---------------------------------------------------------------------------------

If useful, the software will be shared. GIFs can help, especially for interactive CLI tools and GUI-based applications. A simple list of selling points also helps with copy and paste via email when sharing with colleagues. If applicable, a URL link to Jupyter or web-based demos (for example, Google Colab) helps so people do not need to install anything to try it. The step-by-step “Getting Started” section should not be too long so first-time visitors are not overwhelmed. The path of least resistance is fundamental for early adopters.

*First draft Jun 25, 2025 (Incheon, South Korea)*
