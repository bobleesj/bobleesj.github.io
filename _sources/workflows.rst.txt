.. _workflows:

Development workflows
=====================

Here I document the workflows and commands I use in practice to develop and maintain software projects. Many of the commands are aliased to make them easier to remember and use. You can find the full list of commands in :ref:`keyboard-shortcuts-setup`.

Tools I use daily
-----------------

.. list-table::
  :header-rows: 1

  * - Category
    - Tools
  * - IDE
    - Visual Studio Code
  * - Version control
    - Git, GitHub CLI, GitHub
  * - CLI
    - Warp
  * - Development productivity
    - `scikit-package <https://scikit-package.github.io/scikit-package/>`_, `bobleesj.utils <https://bobleesj.github.io/bobleesj.utils/>`_.
  * - CLI shortcuts
    - ``~/.bashrc`` for setting up aliases.

Make a pull request
-------------------

#. Type ``gsub <branch-name>`` or ``gsob <branch-name>`` to sync with ``origin/main`` or ``upstream/main`` and create a new branch.

#. Make changes to the codebase.

#. Type ``gs`` to see the overall changes.

#. Type ``gcam "<Add commit message>"`` to commit files already tracked. If the files are not staged, run ``git add <file-or-folder>`` then run ``gcm "<Add commit message>"``.

#. Type ``ptc`` to run ``pytest`` and ``pre-commit run --all-files`` to ensure everything is working correctly.

#. Type ``napr "<Add news file>."`` to create a new news entry in ``news/<branch-name>``, stage, commit, and push the changes, and make the PR title the news content. To submit the PR right away, type ``naprf "<Add news file>."``

Modify a pull request
---------------------

#. Type ``gpl`` to list the PRs.

#. Type ``gpch <PR-number>``.

#. Address the review comments and make changes.

#. Type ``gcam "<Add commit message>"`` to add a commit message for the changes made in response to the review comments.

#. Type ``ptc`` to run pytest and lint.

#. Type ``gs`` to see the overall changes and ensure all changes are staged and committed.

#. Type ``git push``.

GitHub notifications workflow
-----------------------------

#. In your terminal, type ``gn`` to visit the GitHub notifications page. If you are already on GitHub, type ``G-N`` to visit the notifications page.

#. Use the ``J`` and ``K`` keys to navigate through the notifications. Press ``o`` to open a notification.

#. To reply, press ``R``. To submit the reply, press ``cmd-enter``. Then, to mark the selected page (PR or issue) from the notification as ``done``, press ``E``.

#. To select multiple notifications, use ``J`` and ``K`` to navigate and press ``X`` to select. Then, you may press ``shift-U`` to mark as unread and ``shift-I`` to mark as read.

GitHub issue creation workflow
------------------------------

#. If you are working alone and need to **quickly create an issue**, ``cd`` into the project directory and type ``gi <Descriptive issue title>`` to create and submit an empty issue with the given title. This is useful when the title is descriptive enough and a description is not required.

#. If you need to submit the **same issue across multiple GitHub repositories**, type ``bob create issues`` to create an issue with a description. You need to define ``dev_dir_path`` in ``~/.bobrc`` to point to the directory containing your GitHub repositories. For more information, visit https://bobleesj.github.io/bobleesj.utils/cli.html.

#. If you want to **submit a detailed issue** to communicate and persuade your collaborators, if you are already on the project, type ``ghbi`` to visit the issues page. If you just opened your Terminal, type ``g<proj-name>i`` to open the GitHub issue page of the project. On the issue page, press ``C`` to create a new issue. Use the ``tab`` key to choose the template, then enter the title and description. Preview your rendered markdown using ``shift-P``. To submit, press ``shift-cmd-enter``.

Release workflow (TBA)
----------------------

#. If you are working alone and want to make a quick edit directly to ``main``, after you have staged and committed, type ``pd`` to push the changes to ``main`` and run the GitHub Actions workflow to update the documentation.

Update documentation workflow without a release
-----------------------------------------------

This is for ``scikit-package`` Level 5 projects.

#. Stage and commit the changes. Then run ``gdb`` to push the changes to ``main`` and run the GitHub Actions workflow to update the documentation.

.. _keyboard-shortcuts-setup:

How to use keyboard shortcuts in your CLI
-----------------------------------------

.. note::

  If you are a Windows user, install "Git for Windows" from https://git-scm.com/download/win.

#. Ensure you have ``GitHub CLI`` installed. Run ``gh`` to check if it is installed. If not, install it by following the instructions at https://cli.github.com/manual/installation.

#. In Visual Studio Code, press ``cmd-shift-p`` and type ``Shell Command: Install 'code' command in PATH`` to enable the ``code`` command in your terminal.

#. Ensure you have ``scikit-package`` and ``bobleesj.utils`` installed.

#. Type ``code ~/.bashrc`` to open ``~/.bashrc``.

#. Copy and paste the following commands into your ``~/.bashrc``.

    .. code-block:: bash

        # Navigate (Replace with your actual path and conda environment)
        alias dev='cd <path-to-the-directory> && mamba activate <env-name>'
        alias g='open https://github.com'
        alias gn='open https://github.com/notifications'
        # bobleesj.utils
        alias bdlb='bob delete local-branches'
        # Visual Studio
        alias c='code .'
        # Shortcuts
        alias sc='code ~/.bashrc'
        alias ss='source ~/.bashrc'
        # git
        alias ga='git add'
        alias gc='git checkout'
        alias gpsh='git push'
        alias gp='git pull'
        alias grau='git remote add upstream'
        alias grao='git remote add origin'
        alias gpso='git push --set-upstream origin'
        alias gfa='git fetch --all'
        alias grv='git remote -v'
        alias gcm='git commit -m'
        alias gcam='git commit -a -m'
        alias gce='git commit --allow-empty -m "ci: re-run CI with empty commit"'
        alias gcb='git checkout -b'
        alias gpum='git pull upstream main'
        alias gpo='git push origin'
        alias gl='git log'
        alias gs='git status'
        alias gd='git diff'
        alias gb='git branch'
        alias gr='git restore'
        # For a new branch, set upstream to origin and push
        alias gpsuo='git push --set-upstream origin $(git rev-parse --abbrev-ref HEAD)'
        # Sync with main and create a new branch
        alias gsub='gc main && git pull upstream main && gcb'
        alias gsob='gc main && git pull && gcb'
        # GitHub CLI
        alias gpcr='gh pr create'
        alias gpl='gh pr list'
        alias gpch='gh pr checkout'
        alias gpvw='gh pr view --web'
        alias gil='gh issue list'
        alias ghb='gh browse'
        alias ghbi='gh issue list --web'
        alias gpv='gh pr view'
        alias gbd='gh workflow run publish-docs-on-release.yml'
        alias gbds='gh run list --workflow=publish-docs-on-release.yml'
        # Combined
        alias gpsuop='gpsuo && gpcr'
        # Create news file, add, commit, push, and create PR with the same news title.
        _make_pr() {
        TOOL="$1"        # e.g. "na" (which is aliased to a full package command)
        TITLE="$2"       # PR title
        FILL_FLAG="$3"   # "fill" or empty
        eval "$TOOL \"$TITLE\"" || return 1
        git add news/ || return 1
        git commit -m "news: $TITLE" || return 1
        BRANCH=$(git rev-parse --abbrev-ref HEAD)
        git push --set-upstream origin "$BRANCH" || return 1
        if [ "$FILL_FLAG" = "fill" ]; then
          gh pr create --title "$TITLE" --fill
        else
          gh pr create --title "$TITLE"
        fi
        }
        # scikit-package
        alias na='package add news -a -m'
        alias nf='package add news -f -m'
        alias nc='package add news -c -m'
        alias nr='package add news -r -m'
        alias nd='package add news -d -m'
        napr()  { _make_pr "na" "$1" ""; }
        naprf() { _make_pr "na" "$1" "fill"; }
        nrpr()  { _make_pr "nr" "$1" ""; }
        nrprf() { _make_pr "nr" "$1" "fill"; }
        nspr()  { _make_pr "ns" "$1" ""; }
        nsprf() { _make_pr "ns" "$1" "fill"; }
        ncpr()  { _make_pr "na" "$1" ""; }
        ncprf() { _make_pr "na" "$1" "fill"; }
        ndpr()  { _make_pr "nd" "$1" ""; }
        ndprf() { _make_pr "nd" "$1" "fill"; }
        gict() {
        gh issue create -t "$1" -b ""
        }
        # Python, pip, conda (mamba)
        alias pi='pip install'
        alias pir='pip install -r'
        alias pie='pip install -e . && pip install -r requirements/test.txt'
        alias mi='mamba install \
          --file requirements/test.txt \
          --file requirements/conda.txt'\
        alias ma='mamba activate'
        alias mao='mamba activate ophus-env'
        alias mab='mamba activate bob-env'
        alias mcn='mamba create -n'
        mce() {
          folder_name=$(basename "$PWD")
          env_name="${folder_name}-env"
          mamba create -y -n "$env_name" python=3.13 \
            --file requirements/test.txt \
            --file requirements/conda.txt \
            --file requirements/docs.txt && \
            mamba activate "$env_name" && \
            pip install -e .
        }
        # Combined
        alias pt='pytest'
        alias pc='pre-commit run --all-files'
        alias ptc='pytest && pre-commit run --all-files'
        alias pb='python -m build'
        alias pd='git push && gbd'
        alias doc='sphinx-reload doc'
        # VS Code
        alias c='code .'
        # cookiecutter
        alias cc='cookiecutter .'

#. Run ``source ~/.bashrc`` to apply the changes.

#. To add or modify commands, type ``sc`` to open ``~/.bashrc`` in Visual Studio Code, make your changes, and save the file.

#. To apply the changes, instead of running ``source ~/.bashrc``, type ``ss`` to apply the changes to your current terminal session.
