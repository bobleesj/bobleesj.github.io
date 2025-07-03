.. _workflows:

Development workflows
=====================

Here I document the workflows and commands I use in practice to develop and maintain software projects. Many of the commands are aliased to make them easier to remember and use. You can find the full list of commands in :ref:`keyboard-shortcuts-setup`.

.. _tools-used-daily:

Tools I use daily
-----------------

.. list-table::
  :header-rows: 1

  * - Category
    - Tools
    - URL
  * - IDE
    - Visual Studio Code (Copilot)
    - 
  * - Version control
    - Git, GitHub CLI, GitHub
    - `Tutorial on GitHub workflow for beginners <https://scikit-package.github.io/scikit-package/support/frequently-asked-questions.html#github-workflow>`_
  * - Command line interface (CLI)
    - `Warp <https://www.warp.dev//>`_
    - 
  * - Development productivity
    - `scikit-package <https://scikit-package.github.io/scikit-package/>`_, `bobleesj.utils <https://bobleesj.github.io/bobleesj.utils/>`_
    - 
  * - CLI shortcuts
    - Bash shell
    - :ref:`keyboard-shortcuts-setup`
  * - Text expander/shortcut
    - `espanso <https://espanso.org/>`_
    - :ref:`text-expander-with-espanso`
  * - Web browser
    - `Brave <https://brave.com/>`_
    - 
  * - Documentation
    - `Sphinx <https://www.sphinx-doc.org/>`_
    - 

GitHub pull request
-------------------

If you are not familiar with GitHub, please first read my guide on the `GitHub workflow <https://scikit-package.github.io/scikit-package/support/frequently-asked-questions.html#github-workflow>`_. I also recommend starting with the `Level 4 tutorial <https://scikit-package.github.io/scikit-package/tutorials/tutorial-level-4.html>`_ of ``scikit-package`` to actually use GitHub, GitHub Actions, and the GitHub pull request workflow using your own project. Then you should be able to utilize the commands in this section.

.. note::
  
  The alias commands like ``gsub`` are defined in :ref:`keyboard-shortcuts-setup`.

Make a new pull request
^^^^^^^^^^^^^^^^^^^^^^^^

#. Type ``gsub <branch-name>`` or ``gsob <branch-name>`` to sync with ``origin/main`` or ``upstream/main`` and create a new branch.

#. Make changes to the codebase.

#. Type ``gs`` to see the overall changes.

#. Type ``gcam "<Add commit message>"`` to commit files already tracked. If the files are not staged, run ``ga <file-or-folder>`` then run ``gcm "<Add commit message>"``.

#. Type ``ptc`` to run ``pytest`` and ``pre-commit run --all-files`` to ensure everything is working correctly.

#. Type ``napr "<Add news file>."`` to create a new news entry in ``news/<branch-name>``, stage, commit, and push the changes, and make the PR title the news content.

    .. note::
      
      To submit the PR right away without choosing PR template, type ``naprf "<Add news file>."`` This may be useful for trivial changes that do not require a detailed PR description.

Modify a pull request
^^^^^^^^^^^^^^^^^^^^^^

Imagine you have a pull request (PR) that has been created but needs some modifications or review comments addressed.

#. Type ``gpl`` to list the PRs.

#. Type ``gpch <PR-number>`` to checkout the PR branch.

#. Address the review comments and make changes.

#. Type ``gcam "<Add commit message>"`` to add a commit message for the changes made in response to the review comments.

    .. note::

        If the changes are trivial that you don't need to run tests and ``pre-commit``, type ``gcamp <Add commit message>`` to add, commit, and push the changes for the files that are already Git tracked.

#. Type ``ptc`` to run pytest and lint.

#. Type ``p`` to push the changes to the remote branch.

Create a new branch after a pull request is merged
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Imagine the PR has been merged. Now you want to sync with the latest changes in ``main`` and create a new branch for the next feature or bug fix.

#. Type ``gsub <branch-name>`` to sync with ``upstream/main`` and create a new branch. If you want to sync with ``origin/main``, type ``gsob <branch-name>``.

GitHub task management
----------------------

Create issues
^^^^^^^^^^^^^^

#. If you are working alone and need to **quickly create an issue**, ``cd`` into the project directory and type ``gi <Descriptive issue title>`` to create and submit an empty issue with the given title. This is useful when the title is descriptive enough and a description is not required.

#. If you need to submit the **same issue across multiple GitHub repositories**, type ``bci`` (``bob create issues``) to create an issue with a description. You need to define ``dev_dir_path`` in ``~/.bobrc`` to point to the directory containing your GitHub repositories. To set up ``~/.bobrc``, refer to the `Getting started <https://bobleesj.github.io/bobleesj.utils/cli.html#getting-started>`_ section of ``bobleesj.utils``

#. If you want to **submit a detailed issue** to communicate and persuade your collaborators, if you are already on the project, type ``ghbi`` to visit the issues page. If you just opened your Terminal, type ``g<proj-name>i`` to open the GitHub issue page of the project. On the issue page, press ``C`` to create a new issue. Use the ``tab`` key to choose the template, then enter the title and description. Preview your rendered markdown using ``shift-P``. To submit, press ``shift-cmd-enter``.

View issues
^^^^^^^^^^^

#. Type ``bli`` (``bob list issues``). You need to define ``dev_dir_path`` in ``~/.bobrc`` to point to the directory containing your GitHub repositories. To set up ``~/.bobrc``, refer to the `Getting started <https://bobleesj.github.io/bobleesj.utils/cli.html#getting-started>`_ section of ``bobleesj.utils``

  .. image:: ./img/issue-list.png
      :alt: List of issues by running bob list issues

GitHub notifications
^^^^^^^^^^^^^^^^^^^^

#. In your terminal, type ``gn`` to visit the GitHub notifications page. If you are already on GitHub, type ``G-N`` to visit the notifications page.

#. Use the ``J`` and ``K`` keys to navigate through the notifications. Press ``o`` to open a notification.

#. To reply, press ``R``. To submit the reply, press ``cmd-enter``. Then, to mark the selected page (PR or issue) from the notification as ``done``, press ``E``.

#. To select multiple notifications, use ``J`` and ``K`` to navigate and press ``X`` to select. Then, you may press ``shift-U`` to mark as unread and ``shift-I`` to mark as read.


scikit-package maintenance
--------------------------

These are custom instructions for releasing a package to PyPI, GitHub, and conda-forge. If you are new to ``scikit-package``, please feel free to read the `PyPI and GitHub release tutorial <https://scikit-package.github.io/scikit-package/release-guides/pypi-github.html>`_.

Release workflow
^^^^^^^^^^^^^^^^^

#. Create a release issue on GitHub.

#. Type ``m`` to switch to ``main`` and pull the latest change.

#. Type ``testrelease`` to check if the package can be uploaded to PyPI.

#. Type ``gtu <version-rc.0>`` to upload a pre-release tag to ``upstream``.

#. Type ``testpypi <package-name> rc`` to install and test the pre-release version on PyPI.

#. Type ``gtu <version>`` or ``gto <version>`` to release the package to ``upstream`` or ``origin``.

#. Type ``testpypi <package-name>`` to install the full release version from PyPI and run tests.

#. Type ``package update conda-forge`` to update the feedstock ``meta.yaml``.

#. Type ``testcf <package-name>`` to test the conda-forge package in a new conda environment.

#. Close the release issue.

Update online documentation without a release
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For minor changes, often making a whole pull request is not necessary, such as fixing a minor typo in this website. While the changes are made through a pull request, you may not want to make a new release.

#. Type ``gbd`` (GitHub build documentation) to trigger the GitHub Actions workflow to deploy the online documentation built from the ``main`` branch.

    .. note::
    
      If you want to run ``git push`` and ``gbd`` at the same time, type ``pd``. So typically, for minor fixes, I run ``gcam <Add commit message>`` and run ``pd``.
 

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

        # Single letter shortcuts
        alias g='open https://github.com'
        alias m='git checkout main && git pull'
        alias b='git branch'
        alias c='code .'
        alias d='sphinx-reload docs'
        alias l='git log'
        alias o='open .'
        alias cl='clear'
        # Set the "dev" path based on the hostname
        case "$(hostname)" in
          imacs-iMac.local | imac* )
            export DEVROOT="/Users/imac/downloads/dev/bob"
            ;;
          macbook* )
            export DEVROOT="/Users/macbook/downloads/dev/bob"
            ;;
        esac

        # File navigations using functions
        dev()        { cd "$DEVROOT"; }
        # skpkg-related directories
        skpkg()   { cd "$DEVROOT/skpkg" && ma skpkg-env; }
        skpkgw()  { cd "$DEVROOT/skpkg-baby/skpkg-workspace" && ma skpkg-env; }
        skpkgs()  { cd "$DEVROOT/skpkg-baby/skpkg-system" && ma skpkg-env; }
        skpkgc()  { cd "$DEVROOT/skpkg-baby/skpkg-conda-forge" && ma skpkg-env; }
        skpkgm()  { cd "$DEVROOT/skpkg-baby/skpkg-manuscript" && ma skpkg-env; }
        skpkgr()  { cd "$DEVROOT/skpkg-baby/release-scripts" && ma skpkg-env; }
        # bob-env projects
        but()     { cd "$DEVROOT/my-package/bobleesj.utils" && ma bob-env; }
        bw()    { cd "$DEVROOT/bobleesj.github.io" && ma bob-env && git pull ; }
        bwd()    { cd "$DEVROOT/bobleesj.github.io" && ma bob-env && code . && d ; }
        # cifkit-env projects
        caf()     { cd "$DEVROOT/my-package/CAF" && ma cifkit-env; }
        cba()     { cd "$DEVROOT/my-package/CBA" && ma cifkit-env; }
        saf()     { cd "$DEVROOT/my-package/SAF" && ma cifkit-env; }
        cifkit()  { cd "$DEVROOT/my-package/cifkit" && ma cifkit-env; }
        cif()     { cd "$DEVROOT/my-package/cifkit" && ma cifkit-env; }
        cifc()    { cd "$DEVROOT/cif-cleaner" && ma cifkit-env; }
        cafapp()  { cd "$DEVROOT/CAF-app" && ma cifkit-env; }

        # Editable installs
        iskpkg()  { pip install -e "$DEVROOT/skpkg"; }
        ibut()    { pip install -e "$DEVROOT/my-package/bobleesj.utils"; }

        # URL navigations
        alias ggl='function _ggl() { open "https://www.google.com/search?q=$(echo "$*" | sed "s/ /+/g")"; }; _ggl "$@"'
        alias g='open https://github.com/bobleesj'
        alias gn='open https://github.com/notifications'
        alias gpt='open https://chatgpt.com'
        alias gcifkit='open https://github.com/bobleesj/cifkit'
        alias gsaf='open https://github.com/bobleesj/structure-analyzer-featurizer'
        alias gcaf='open https://github.com/bobleesj/composition-analyzer-featurizer'
        alias gcba='open https://github.com/bobleesj/cif-bond-analyzer'
        alias gskpkg='open https://github.com/scikit-package/scikit-package'
        alias gskpkgi='open https://github.com/scikit-package/scikit-package/issues'
        alias gskpkgp='open https://github.com/scikit-package/scikit-package/pulls'
        alias gbutils='open https://github.com/bobleesj/bobleesj.utils'
        alias gbweb='open https://github.com/bobleesj/bobleesj.github.io'
        # Single letter aliases

        # CV
        alias cv='nodemon --exec python cv.py --watch . --ext py,json'
        # bobleesj.utils
        alias bdlb='bob delete local-branches'
        alias bli='bob list issues'
        alias sc='code . ~/.zshrc'
        alias bc='code . ~/.bobrc'
        alias spc='code . ~/.skpkgrc'
        alias ss='source ~/.zshrc'
        alias ec='code /Users/imac/Library/Application\ Support/espanso'
        # git
        alias ga='git add'
        alias gc='git checkout'
        alias gp='git pull'
        alias p='git push'
        alias pd='git push && gbd'
        alias grau='git remote add upstream'
        alias grao='git remote add origin'
        alias gpso='git push --set-upstream origin'
        alias gfa='git fetch --all'
        alias grv='git remote -v'
        alias gcm='git commit -m'
        alias gac='git add . && git commit -a -m'
        alias gacp='git add . && git commit -a -m "test commit" && git push --set-upstream origin $(git rev-parse --abbrev-ref HEAD)'
        alias gcam='git commit -a -m'
        gcamp() {
          git commit -a -m "$@" && gpsuo
        }
        alias gce='git commit --allow-empty -m "ci: re-run CI with empty commit"'
        alias gcb='git checkout -b'
        alias gpum='git pull upstream main'
        alias gs='git status'
        alias gd='git diff'
        alias gr='git restore'
        # for a new branch, set upstream to origin and push
        alias gpsuo='git push --set-upstream origin $(git rev-parse --abbrev-ref HEAD)'
        # Sync with main and create a new branch
        alias gsub='gc main && git pull upstream main && gcb'
        alias gsob='gc main && git pull && gcb'
        alias gdsub='gc main && bdlb && git pull upstream main && gcb'
        alias gdsob='gc main && bdlb && git pull && gcb'
        # github CLI
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
        alias grsd='gh repo set-default'
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
            PR_URL=$(gh pr create --title "$TITLE" --fill)
            open "$PR_URL"
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
        alias nn='package add news -n -m'
        napr()  { _make_pr "na" "$1" ""; }
        naprf() { _make_pr "na" "$1" "fill"; }
        nfpr()  { _make_pr "nf" "$1" ""; }
        nfprf() { _make_pr "nf" "$1" "fill"; }
        nrpr()  { _make_pr "nr" "$1" ""; }
        nrprf() { _make_pr "nr" "$1" "fill"; }
        nspr()  { _make_pr "ns" "$1" ""; }
        nsprf() { _make_pr "ns" "$1" "fill"; }
        ncpr()  { _make_pr "nc" "$1" ""; }
        ncprf() { _make_pr "nc" "$1" "fill"; }
        ndpr()  { _make_pr "nd" "$1" ""; }
        ndprf() { _make_pr "nd" "$1" "fill"; }
        nnpr()  { _make_pr "nn" "$1" ""; }
        nnprf() { _make_pr "nn" "$1" "fill"; }
        gict() {
          gh issue create -t "$1" -b ""
        }
        gi() {
          gh issue create -t "$1" -b ""
        }
        gto() {
          TAG="$1"
          git tag "$TAG" && git push origin "$TAG"
        }
        gtu() {
          TAG="$1"
          git tag "$TAG" && git push upstream "$TAG"
        }

        # Edit news file for the current branch
        alias ne='vim news/$(git rev-parse --abbrev-ref HEAD).rst'
        alias api='package build api-doc'
        # Python, pip, conda (mamba)
        alias pi='pip install'
        alias pir='pip install -r'
        alias pie='pip install -e . && pip install -r requirements/tests.txt'
        alias mc='mamba create -y -n'
        alias mi='mamba install -y \
            --file requirements/tests.txt \
            --file requirements/conda.txt \
            --file requirements/docs.txt && \
            pip install -e . --no-deps && \
            pip install sphinx-reload pre-commit'
        alias ma='mamba activate'
        alias mif='mamba info'
        alias mao='mamba activate ophus-env'
        alias mab='mamba activate bob-env'
        mce() {
            folder_name=$(basename "$PWD")
            env_name="${folder_name}-env"
            mamba create -y -n "$env_name" python=3.13 \
                --file requirements/tests.txt \
                --file requirements/conda.txt \
                --file requirements/docs.txt && \
                mamba activate "$env_name" && \
                pip install -e .
        }
        # Jupyter Lab
        alias ji='jupyter lab'
        # Test
        alias pt='pytest'
        alias pc='pre-commit run --all-files'
        alias ptc='pytest && pre-commit run --all-files'
        alias pb='python -m build'
        # cookiecutter
        alias cc='cookiecutter .'

        # Test whether the wheel and sdist can be built and checked
        testrelease() {
          echo "📦 Installing build and twine..."
          pip install --upgrade build twine || return 1
          echo "🧹 Cleaning previous builds..."
          rm -rf dist/ build/ || true
          echo "🛠 Building package..."
          python -m build || return 1
          echo "🔍 Checking package with twine..."
          twine check dist/* || return 1
          echo "✅ Build and check successful!"
        }

        # Usage 1: testpypi <package-name> rc
        # Usage 2: testpypi <package-name>
        testpypi() {
          if [ -z "$1" ]; then
            echo "❌ Error: Package name is required"
            echo "Usage: test <package-name> [rc]"
            return 1
          fi
          PKG="$1"
          MODE="$2"
          ENV_NAME="${PKG}-${MODE:-stable}"
          echo "🔧 Creating environment: $ENV_NAME"
          mamba create -y -n "$ENV_NAME" python=3.13 || return 1
          echo "🚀 Activating environment..."
          source "$(conda info --base)/etc/profile.d/conda.sh"
          conda activate "$ENV_NAME" || return 1
          echo "📦 Installing $MODE version of $PKG..."
          if [ "$MODE" = "rc" ]; then
            pip install --pre "$PKG" || return 1
          else
            pip install "$PKG" || return 1
          fi
          echo "📄 Installing requirements/tests.txt..."
          mamba install -y --file requirements/tests.txt || return 1
          echo "🧪 Running tests with pytest..."
          pytest
        }

        # Usage 1: testcf <package-name>
        testcf() {
          PKG="$1"
          ENV_NAME="${PKG}-cf"
          echo "🔧 Creating environment: $ENV_NAME"
          mamba create -y -n "$ENV_NAME" "$PKG" || return 1

          echo "🚀 Activating environment..."
          source "$(conda info --base)/etc/profile.d/conda.sh"
          conda activate "$ENV_NAME" || return 1

          echo "📄 Installing requirements/tests.txt..."
          mamba install -y --file requirements/tests.txt || return 1

          echo "🧪 Running tests with pytest..."
          pytest
        }



#. Run ``source ~/.bashrc`` to apply the changes.

#. To add or modify commands, type ``sc`` to open ``~/.bashrc`` in Visual Studio Code, make your changes, and save the file.

#. To apply the changes, instead of running ``source ~/.bashrc``, type ``ss`` to apply the changes to your current terminal session.

.. _text-expander-with-espanso:

Use text expander to prevent typing the same text
-------------------------------------------------

The goal is to **minimize the amount of typing** by setting custom aliases for nouns, pharses, and sentences. This aligns with :ref:`principle-minimum-effort-same-output`.

The following instructions are tested on macOS.

#. Install `espanso <https://espanso.org/>`_.

#. Type ``ec`` defined in :ref:`keyboard-shortcuts-setup` to open the espanso configuration folder.

#. In ``match/base.yml``, copy and paste the following configuration into the espanso configuration file 

    .. code-block:: yaml

      # espanso match file
      # For a complete introduction, visit the official docs at: https://espanso.org/docs/
      matches:
        # GitHub
        - trigger: "lgtm"
          replace: "Looks good to me!"
        - trigger: "prr"
          replace: "This is ready for review."
        - trigger: "prc1"
          replace: "Great start! Please see my in-line comments." 
        - trigger: "prc2"
          replace: "Almost there... just a few more tweaks needed."
        - trigger: "prm"
          replace: "Looking good. Merging this PR!"
        - trigger: "g1"
          replace: "I think this is a great idea. I have a few thoughts."
        - trigger: "g2"
          replace: "This is great. Could you please implement this?"
        - trigger: "c1"
          replace: "Sorry I am a bit confused by this section because "
        - trigger: "c2"
          replace: "I might be missing something. Do you mind explaining "
        - trigger: "i1"
          replace: "Closes "
        - trigger: "i2"
          replace: "Closed by issue "
        # Appreciate
        - trigger: "a1"
          replace: "Thanks!"
        - trigger: "a2"
          replace: "Thanks a lot!"
        - trigger: "a3"
          replace: "Thank you so much!"
        - trigger: "a4"
          replace: "Wow, this is awesome. Thank you so much!"
        - trigger: "gbl"
          replace: "@bobleesj "
        # Billinge
        - trigger: "gsb"
          replace: "@sbillinge "
        - trigger: "gtz"
          replace: "@Tieqiong "
        - trigger: "gcm"
          replace: "@cadenmyers13 "
        - trigger: "gyx"
          replace: "@ycexiao "
        - trigger: "gem"
          replace: "@EmilJaffal "
        # Oliynyk
        - trigger: "gbs"
          replace: "@balaranjan "
        - trigger: "gds"
          replace: "@dshirya "
        # Projects
        - trigger: "butils"
          replace: "`bobleesj.utils` "
        - trigger: "skpkgn"
          replace: "`scikit-package` "
        - trigger: "skpkgc"
          replace: "`scikit-package-conda-forge` "
        - trigger: "skpkgm"
          replace: "`scikit-package-manuscript` "
        - trigger: "skpkgs"
          replace: "`scikit-package-system` "
        - trigger: "skpkgw"
          replace: "`scikit-package-workspace` "  
        # Checklist & pomodoro
        - trigger: "po1"
          replace: "Pomodoro #1 "
        - trigger: "po2"
          replace: "Pomodoro #2 "
        - trigger: "po3"
          replace: "Pomodoro #3 "
        - trigger: "po4"
          replace: "Pomodoro #4 "
        - trigger: "po5"
          replace: "Pomodoro #5 "
        - trigger: "po6"
          replace: "Pomodoro #6 "
        - trigger: "po7"
          replace: "Pomodoro #7 "
        - trigger: "po8"
          replace: "Pomodoro #8 "
        - trigger: "po9"
          replace: "Pomodoro #9 "
        - trigger: "po10"
          replace: "Pomodoro #10 "
        - trigger: "poc"
          replace: "[ ] "
        - trigger: "pod"
          replace: "[x] "
        # Date, time
        - trigger: ":date"
          replace: "{{mydate}}"
          vars:
            - name: mydate
              type: date
              params:
                format: "%b %-d, %Y"
        - trigger: ":time"
          replace: "{{mytime}}"
          vars:
            - name: mytime
              type: date
              params:
                format: "%I:%M %p"
        # Print the output of a shell command
        - trigger: ":shell"
          replace: "{{output}}"
          vars:
            - name: output
              type: shell
              params:
                cmd: "echo 'Hello from your shell'"

#. Now, you can use the defined triggers in any application. For example, typing ``lgtm`` will replace it with ``Looks good to me!``.

  - To turn off/on espanso, in ``config/default.yml``, uncomment ``toggle_key: ALT``. Now, you can toggle espanso on and off by pressing the ``Opt`` key twice.
  - To see the list of matches, presss the ``Opt-Space`` keys together.

