Bob's notes
===========

How to add Jupyter notebooks to Sphinx
--------------------------------------

1. Add ``ipykernel`` and ``nbsphinx``, and remove ``m2r`` from ``requirements/docs.txt``.
2. Add ``nbsphinx_allow_errors = True`` in ``conf.py``.
3. Cross-check with ``bobleesj.utils`` (http://github.com/bobleesj/bobleesj.utils).

How to set up SSH for GitHub
----------------------------

#. In your terminal, run the following commands to generate a new SSH key pair. Replace ``<email@example.com>`` with your email address.

    .. code-block:: bash

        $ cd ~/.ssh
        $ ssh-keygen -o -t rsa -C "<email@example.com>"
        $ cat id_rsa.pub

#. Visit https://github.com/settings/keys.

#. Click :guilabel:`New SSH key`.

#. Set the :guilabel:`Title` as ``<your-computer-name>-key``.

#. Under :guilabel:`Key`, copy and paste the content of the ``id_rsa.pub`` file into the "Key" field. It should start with ``ssh-rsa`` and end with your email address.

#. Click :guilabel:`Add SSH key`.

#. Done!

Ref: https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GitHub-SSH-Key-Setup-Config-Ubuntu-Linux

How to install ``mamba``
------------------------

This tutorial is for macOS. For other platforms, please refer to the official documentation at https://github.com/conda-forge/miniforge.

#. Remove existing ``miniconda3`` and ``miniforge3`` directories if they exist:

    .. code-block:: bash

        $ rm -rf /Users/<macbook-username>/miniconda3
        $ rm -rf /Users/<macbook-username>/miniforge3

    Replace ``<macbook-username>`` with your actual username. You can see it after typing ``pwd`` in your terminal.

#. Install ``mamba`` using the following command:

    .. code-block:: bash

        $ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

#. Make the script executable and run it:

    .. code-block:: bash

        $ bash Miniforge3-$(uname)-$(uname -m).sh
        $ mamba shell init

#. Restart your terminal and type the following command to verify the installation:

    .. code-block:: bash

        mamba --version

Set ``VIM`` as the default editor
---------------------------------

In ``.zshrc`` or ``.bashrc``, add the following lines:

.. code-block:: bash

    export GIT_EDITOR=vim
    export VISUAL=vim
    export EDITOR=vim

If above does not work, set it globally by running the following command in your terminal:

.. code-block:: bash

    $ gh config set editor vim

Keyboard shortcuts in Visual Studio Code
----------------------------------------

- Fix multiple lines at once? Press ``opt-cmd-up/down``.
- View other parts of the file? Press ``cmd-PageUp/PageDown``. Press ``ctrl-g`` to move the cursor.
- View recently closed file? Use ``ctrl-tab``. This mimics the way you switch recent applications using ``cmd-tab``. 
- Switch between tabs in the current window? Press ``opt-cmd-left/right``.
- Go to the file after ``cmd-shift-F``? Press ``F4`` and ``shift-F4``. This allows you to quickly jump to the next or previous search result.
- Globally replace a text? Press ``cmd-shift-H``.

Vim 
---

- When writing a GitHub issue, you may want to write under each header. A simple way is to go to the line with ``<line-number>G`` and then press ``o``. If you want to append text at the end of the file or in the middle, use ``G`` or ``L``, and then press ``o``. To modify the title, use ``gg`` to go to the first line and press ``A`` to append text at the end of the line.
- To navigate easily, use the arrow replacements: ``h``, ``j``, ``k``, and ``l``. Use ``w`` and ``e`` to move forward by word, and ``b`` and ``ge`` to move backward. But of often, we don't want to count every punctuation mark or space, then you can use ``W``, ``E``, ``B``, and ``gE`` to move by word without counting punctuation marks or spaces.
- To insert before the cursor, use ``i``; after the cursor, use ``a``. To insert at the beginning of the line, use ``I``. To insert at the end of the line, use ``A``.
- **Fix quick typos?** Press ``x`` to delete the character under the cursor or ``r`` to replace the character. Use ``X`` to delete the character before the cursor. To delete more than one character, use ``<number>x`` or ``<number>r``. For example, to delete 3 characters, use ``3x`` or ``3r``. To delete 3 characters to the left of the cursor, use ``3X``.
- **Want to make bigger fixes?** Use ``dd`` to delete the current line, or ``D`` to delete from the cursor to the end of the line. To change a word, use ``cw`` (deletes the word from the cursor to the right and enters insert mode). Use ``cc`` to delete the current line and enter insert mode.
- **Tired of counting the number of characters?** You can simply identify start of the word you want to modify. The key commands are ``f`` and ``t``. ``f<char>`` moves the cursor to the next ``<char>`` on the right. ``t<char>`` moves the cursor to the character before the next ``<char>`` on the right. ``F<char>`` and ``T<char>`` do the same in the opposite direction. This is useful when you need to delete a few characters using ``df<char>`` or ``dt<char>``. To repeat the last command, use ``;``. To repeat in the opposite direction, use ``,``.
- **Want to copy and paste?** Press ``yy`` to copy the line, and ``p`` or ``P`` to paste below or above the cursor.
- **Made a mistake?** Use ``u`` to undo and ``ctrl-r`` to redo. To undo multiple times, use ``<number>u``. For example, ``3u`` will undo the last three changes.