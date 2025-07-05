.. _principles:

My optimization principles
==========================

We brush our teeth in the morning. When we wake up, these tasks are automatic. These automated movements, refined through decades of practice using the feedback loop of pain, have led us to use barely any mental effort to accomplish this morning ritual.

This ritual, while recommended, frees up time and also leaves us with the mental capacity to do useful work for the rest of the day. We can draw an important lesson: we want to **protect the limited amount of consciousness** each day and allocate this toward *useful* work only.

It begins with the very first principle of optimization: turning conscious effort into the subconscious with a streamlined, no-effort-requiring process, just like brushing our teeth. Only then can we truly utilize our consciousness for creative and productive work.

.. _principle-minimum-effort-same-output:

Principle 1. **Use minimum input** to attain the **same output**
----------------------------------------------------------------------------------

The ideal goal is to get the work done without unnecessary physical movements. For example, if you have 10 issues and pull requests to comment on, you might want to type "lgtm" to save time and physical effort, but this level of brevity should be used carefully. Hence, we recognize this gap.

I begin by recording relevant shortcuts in the IDE, browser, GitHub, terminal, and operating system. Here are some of the shortcuts I use daily:

    - Use a text expander to avoid typing the same text repeatedly. I use ``espanso`` to create text shortcuts. See :ref:`text-expander-with-espanso` for more details.
    - In a browser, switch between tabs using ``cmd-1``, ``cmd-2``, etc., and ``cmd-[`` and ``cmd-]``. Create a new tab with ``cmd-t`` and close the current tab with ``cmd-w``. Use ``cmd-shift-t`` to reopen the last closed tab.
    - On GitHub, visit the notifications page, issues, and PRs using ``G-N``, ``G-I``, and ``G-P`` respectively. Create a new issue with ``C`` on the issues page. Create a new PR with ``C``. See all the shortcuts by pressing ``shift-/`` on github.com and refer to the `Keyboard shortcuts <https://docs.github.com/en/get-started/accessibility/keyboard-shortcuts>`_ page.
    - On macOS, use the ``Magnet`` application to manage and arrange windows without the need to use the mouse, splitting apps onto the screen and maximizing them using ``cmd-<`` for the left half and ``cmd->`` for the right half.
    - In the IDE (e.g., Visual Studio Code), use ``cmd-t`` or ``cmd-p`` to search for files, ``cmd-shift-p`` to search for commands, and ``cmd-``, ``cmd-1``, etc., to switch between tabs. Determine the most effective ways to navigate lines, cursors, files, and to delete or modify content.
    - When needed, set custom keyboard shortcuts to reduce strain on your fingers and wrists.

I also create my own shortcuts with custom ``alias`` commands. To write this content, I woke up and simply typed ``bweb``; it (a) navigates to my ``bobleesj.github.io`` project path, (b) activates the relevant conda environment, (c) displays the latest commit messages, and (d) opens Visual Studio Code. To learn how to set up keyboard shortcuts in your terminal, see :ref:`keyboard-shortcuts-setup`.

Principle 2. **Attain maximum output** with the **same input**
----------------------------------------------------------------

It is common for open-source scientific packages to release a package using the ``git tag <version>`` command to tag the release version on GitHub. In ``scikit-package``, I led the development of a `reusable workflow <https://github.com/scikit-package/release-scripts/blob/main/.github/workflows/_build-wheel-release-upload.yml>`_ so that uploading the tag also checks admin privileges, releases on GitHub, uploads code to PyPI, updates the ``CHANGELOG``, and deploys the documentation.

For my daily work, I use the pomodoro technique to maximize my output, with 50 minutes of focus and 10 minutes of rest in between. I have found that this is the most optimal way to maximize my output instead of working many hours straight without breaks. You can read more about my pomodoro technique described in :ref:`essay-daily-work`.

.. _principle-minimum-process:

Principle 3. **Minimum process** with the **same input and ouput**
---------------------------------------------------------------------

Yes, the first two principles are key. Often, we need to update the process—the function between the input and the output. A simple process means less maintenance and development effort are required. For example, we have Python version 3.13 hard-coded in our ``scikit-package`` `GitHub Actions workflows <https://github.com/scikit-package/release-scripts/blob/main/.github/workflows/_tests-on-pr.yml>`_. The simpler it is to update these Python versions across multiple files, the more time and effort it saves the team in maintaining the codebase. Hence, processes are often modified, and the simpler the process, the less effort is required to maintain it. This is why we have adopted the reusable workflow in ``scikit-package``, where it is managed in a centralized way so that we can update these Python parameters in one place rather than modifying them across dozens of projects.

I also consider **time** as part of the process. So, instead of ``conda install``, I use ``mamba install`` because the time is reduced despite the same cognitive and physical input and outcome. Another example of applying this principle is finding the right web browser. I find the `Brave browser <https://brave.com/>`_ to be the best for this purpose, as it saves time in loading and also prevents me from using my consciousness on inadvertently reading ads.

Another example is the use of vectorization for computing distances between two points within a unit cell and its supercell as implemented in ``cifkit``. Using the ``for-loop`` method is often the first approach that comes to mind, but it is not the most efficient. Instead, I had a collaborator who made a significant contribution that boosted the algorithm's performance more than 10x. This is an example of how we can use the minimum process to achieve the same output with the same input.

Principle #3 is often intertwined with Principles #1 and #2. Using the minimum process may also mean using the minimum resources, such as electricity and time, to achieve the same output (Principle #1). However, I wanted to separate this principle from the first two because it is the perspective—input, output, or process—that we are trying to optimize. Each workflow may have different priorities, and the leader should be able to identify which principle to apply in a given situation.

Exceptions and questions
------------------------

There is one exception when the **principles should be violated**: when **\|effort required for optimization\|** is greater than **\|total effort saved\|** over the entire lifecycle of the workflow.

Here are some questions I ask when I am about to embark on a new task or workflow:

    - Which principle can I apply to this workflow? (Choose Principle #1, #2, or #3)
    - How can I reduce the effort required for the same task? (Principle #1)
    - How can I maximize impact with the same effort? (Principle #2)
    - How can I simplify the automation process? (Principle #3)

*First draft on Jun 24, 2025 (Incheon, South Korea)*ork
