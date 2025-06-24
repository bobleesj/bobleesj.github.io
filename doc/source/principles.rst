.. _principles:

My optimization principles
==========================

We brush our teeth without thinking about where to put the toothbrush. When we wake up, these tasks are automatic. These neck and hand movements, refined through decades of practice and the mistakes that accompany the feedback loop of pain, have led us exert barely any mental effort to accomplish this crucial morning ritual.

This ritual, with barely any effort, frees up time and also leaves us with the mental capacity to do useful work for the rest of the day. Hence, the goal is to **protect the limited amount of consciousness** each day and allocate this toward *useful* work only. It begins with the very first principle of optimization: turning conscious effort into a subconscious and streamlined process that requires minimal effort to achieve the same output, just like brushing our teeth, with our eyes closed.

Principle 1. **Use minimum effort** to attain the **same output**.
------------------------------------------------------------------

It starts with the very basic use of our muscle movements. The first goal is to internalize all relevant shortcuts in the IDE, browser, GitHub, terminal, and operating system. Here is a list a portion of the shortcuts I use daily:

    - Switch between tabs in the browser using ``cmd-1``, ``cmd-2``, etc., and ``cmd-[`` and ``cmd-]``. Create a new tab with ``cmd-t`` and close the current tab with ``cmd-w``. Use ``cmd-shift-t`` to reopen the last closed tab.
    - On GitHub, visit the notifications page, issues, and PRs using ``G-N``, ``G-I``, and ``G-P`` respectively. Create a new issue with ``C`` on the issues page. Create a new PR with ``C``. See all the shortcuts by pressing ``shift-/`` on github.com.
    - On macOS, use the ``Magnet`` application to manage and arrange my windows without the need to use the mouse, splitting my apps onto the screen and maximizing them using ``cmd-<`` for the left half and ``cmd->`` for the right half.
    - In the IDE (e.g., Visual Studio Code), use ``cmd-t`` or ``cmd-p`` to search for files, ``cmd-shift-p`` to search for commands, and ``cmd-``, ``cmd-1``, etc., to switch between tabs. Determine the most effective ways to navigate lines, cursors, files, and to delete and modify content.
    - When needed, set custom keyboard shortcuts to reduce strain on the fingers and wrists.

I also create my own shortcuts with custom ``alias`` commands. To write this content, I woke up and simply typed ``bweb``; it (a) navigates to my ``bobleesj.github.io`` project path, (b) activates the relevant conda environment, (c) displays the latest commit messages, and (d) opens Visual Studio Code. To learn how to set up keyboard shortcuts in your terminal, see :ref:`keyboard-shortcuts-setup`.

Principle 2. **Attain maximum output** with the **same input**.
---------------------------------------------------------------

It is common for open-source scientific packages to release a package using the ``git tag <version>`` command to tag the release version on GitHub. In ``scikit-package``, I led the development of a `reusable workflow <https://github.com/scikit-package/release-scripts/blob/main/.github/workflows/_build-wheel-release-upload.yml>`_ so that uploading the tag also checks admin privileges, releases on GitHub, uploads code to PyPI, updates the ``CHANGELOG``, and deploys the documentation.

For my daily work, I use the pomodoro technique to maximize my output, with 50 minutes of focus and 10 minutes of rest in between. I have found that this is the most optimal way to maximize my output instead of working many hours straight without breaks. You can read more about my pomodoro technique described in :ref:`essay-daily-work`.

Principle 3. **Minimum process** with the **same input and output**.
---------------------------------------------------------------------

Another reason we want to use a minimum process is that automation and processes are often maintained and developed by a team of people. A simple process means less maintenance and development effort is required. Hence, while inputs and outputs are the priority, the process is also important when it comes to long-term maintenance, where changes are inevitable. For example, we have Python version 3.13 hard-coded in our ``scikit-package`` `GitHub Actions workflows <https://github.com/scikit-package/release-scripts/blob/main/.github/workflows/_tests-on-pr.yml>`_. The simpler it is to maintain these Python versions across multiple files when a new Python version is released, the more time and effort it saves the team in maintaining the codebase.

Another example is that I consider "time" as part of the process. So, instead of using the input ``conda install``, I started using ``mamba install`` to install packages to reduce installation time. I use a web browser that does automatic ad blocking. I find the `Brave browser <https://brave.com/>`_ to be the best for this purpose, as it saves time in loading and also prevents me from using my consciousness on inadvertently reading ads.

Exceptions and questions
------------------------

There is one exception when the **principles should be violated**: when **\|effort required for optimization\|** is greater than **\|total effort saved\|** over the entire lifecycle of the workflow.

Here are some questions I ask when I am about to embark on a new task or workflow:

    - Which principle can I apply to this workflow? (Choose Principle #1, #2, or #3)
    - How can I reduce the effort required for the same task? (Principle #1)
    - How can I maximize impact with the same effort? (Principle #2)
    - How can I simplify the automation process? (Principle #3)
