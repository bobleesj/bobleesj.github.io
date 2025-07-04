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

If the above does not work, set it globally by running the following command in your terminal:

.. code-block:: bash

    $ gh config set editor vim

Keyboard shortcuts in Visual Studio Code
----------------------------------------

- Fix multiple lines at once? Press ``opt + cmd + up/down``.
- View other parts of the file? Press ``cmd + PageUp/PageDown``. Press ``ctrl + g`` to move the cursor.
- View recently closed files? Use ``ctrl + tab``. This mimics the way you switch recent applications using ``cmd + tab``. 
- Switch between tabs in the current window? Press ``opt + cmd + left/right``.
- Go to the file after ``cmd + shift + F``? Press˙ ``F4`` and ``shift + F4``. This allows you to quickly jump to the next or previous search result.
- Globally replace text? Press ``cmd + shift + h``.
- Move previous cursor position. Press ``cmd + u``
- Remove line space below? Press ``ctrl + j``.
- Highlight a line? Press ``cmd + l``.
- Duplicate a line? Press ``opt + shift + up/down``.
- Switch cursor between widnwos? ``cmd + k`` and then ``→`` or ``←``.

Vim 
---

- When writing a GitHub issue, you may want to write under each header. A simple way is to go to the line with ``<line-number>G`` and then press ``o``. If you want to append text at the end of the file or in the middle, use ``G`` or ``L``, and then press ``o``. To modify the title, use ``gg`` to go to the first line and press ``A`` to append text at the end of the line.
- To navigate easily, use the arrow replacements: ``h``, ``j``, ``k``, and ``l``. Use ``w`` and ``e`` to move forward by word, and ``b`` and ``ge`` to move backward. If you don't want to count every punctuation mark or space, use ``W``, ``E``, ``B``, and ``gE`` to move by word without counting punctuation marks or spaces.
- To insert before the cursor, use ``i``; after the cursor, use ``a``. To insert at the beginning of the line, use ``I``. To insert at the end of the line, use ``A``.
- **Fix quick typos?** Press ``x`` to delete the character under the cursor or ``r`` to replace the character. Use ``X`` to delete the character before the cursor. To delete more than one character, use ``<number>x`` or ``<number>r``. For example, to delete 3 characters, use ``3x`` or ``3r``. To delete 3 characters to the left of the cursor, use ``3X``.
- **Want to make bigger fixes?** Use ``dd`` to delete the current line, or ``D`` to delete from the cursor to the end of the line. To change a word, use ``cw`` (deletes the word from the cursor to the right and enters insert mode). Use ``cc`` to delete the current line and enter insert mode.
- **Tired of counting the number of characters?** You can simply identify the start of the word you want to modify. The key commands are ``f`` and ``t``. ``f<char>`` moves the cursor to the next ``<char>`` on the right. ``t<char>`` moves the cursor to the character before the next ``<char>`` on the right. ``F<char>`` and ``T<char>`` do the same in the opposite direction. This is useful when you need to delete a few characters using ``df<char>`` or ``dt<char>``. To repeat the last command, use ``;``. To repeat in the opposite direction, use ``,``.
- **Want to copy and paste?** Press ``yy`` to copy the line, and ``p`` or ``P`` to paste below or above the cursor.
- **Made a mistake?** Use ``u`` to undo and ``ctrl-r`` to redo. To undo multiple times, use ``<number>u``. For example, ``3u`` will undo the last three changes.

Some other decisions to speed up my development workflow
--------------------------------------------------------

Using Visual Studio Code's built-in terminal

    **While developing** software—such as adding new content to my personal website—I prefer using Visual Studio Code's built-in terminal instead of an external terminal. There are a few reasons for this.

    First, I can open the terminal within VS Code by pressing ``ctrl + ``` the first time, and then ``cmd + j`` for subsequent uses, which is much more convenient ergonomically. In contrast, accessing an external terminal requires ``cmd + tab`` or using Spotlight search. Often, it is necessary to press ``cmd + tab`` multiple times to find the terminal application. For Spotlight search, I have to type the first letter of the terminal application, which adds both physical and cognitive overhead. Using the principle of "same output, minimum input," the ``cmd + j`` shortcut in VS Code requires the least effort (Principle #1).

    Second, the external terminal window is often positioned differently or displayed alongside other applications, requiring me to constantly switch focus between the terminal and the VS Code editor. This increases my cognitive load (Principle #1).

    Third, reading GitHub issues is much easier in full-screen mode within VS Code. In contrast, the external terminal usually opens in a smaller window to work side by side with other applications like Visual Studio or when hosting a server, which often requires resizing to match the content. This adds both physical effort and additional mental overhead (Principle #1).

    Fourth, I use ``sc`` and ``ec`` alias shortcuts to open Visual Studio Code to modify configuration files. Running these commands opens the configuration file within the current VS Code editor, so it saves time (Principle #3) and reduces cognitive overload since my brain doesn't have to process a new window being created or require me to type an extra shortcut to adjust the window size (Principle #1).

How to upload .tex using minted package from Overleaf to ArXiv
--------------------------------------------------------------

The ``minted`` package for code highlighting isn't natively supported by ArXiv, while it is natively rendered in Overleaf. We need to do some extra steps to render the minted code blocks since we can't upload a PDF file directly to ArXiv as a result. The following steps are adapted from https://tex.stackexchange.com/a/558082.

#. Enter the project in Overleaf.

#. On the :guilabel:`Menu` icon at the top left, ensure the designated ``.tex`` file is set as the ``Main document``.

#. On the top right corner, click :guilabel:`Submit` and then :guilabel:`Download source`.

#. Unzip the downloaded file on your local machine.

#. Open the designated ``.tex`` file in a text editor.

#. Replace ``\usepackage{minted}`` with ``\usepackage[finalizecache=true]{minted}`` in the relevant ``.tex`` file. This will create ``.pyg`` cache files in the ``_minted-<manuscript-name>`` directory.

#. Run ``pdflatex -shell-escape manuscript.tex`` to scan for ``\cite{}`` and ``\ref{}`` and write to ``.aux``.

#. Run ``bibtex manuscript`` to read ``.aux``, pull the ``.bib`` file, and write to the ``.bbl`` file. Ensure the ``.bbl`` isn't empty.

#. Run ``pdflatex -shell-escape manuscript.tex`` to read the ``.bbl`` and write the references into the PDF. 

#. Run ``pdflatex -shell-escape manuscript.tex`` again to resolve internal links, figure, and table references.

#. Replace ``\usepackage[finalizecache=true]{minted}`` with ``\usepackage[frozencache=true]{minted}`` in the relevant ``.tex`` file. This will ensure that the minted code blocks are frozen so that it can be built without enabling the ``-shell-escape`` option. This is important when submitting to ArXiv or building on restricted environments where ``Pygments`` is not installed.

#. Save and zip the folder.

#. Upload the zipped folder to ArXiv. This will also upload the full ``_minted-<manuscript-name>`` cache directory with the submission.

#. In the :guilabel:`Add Files` stage, upload the zipped folder you just created.

#. In the :guilabel:`Review Files` stage, ensure you don't delete the ``_minted-<manuscript-name>`` directory even though it says "Not used". You may delete other files such as ``.bib`` that are not needed.

#. Then, finish the rest of the submission, which is entering metadata.

Dependencies
------------

List the dependencies:

.. code-block:: bash

    pip intsall pipreqs
    pipreqs . --force --ignore=tests
    conda list -e > requirements.txt

Update dependencies:

.. code-block:: bash

  conda update --all
  pip list --outdated
  pip install --upgrade <package>


Project checklist
-----------------

The checklist below can be used to improve usability, marketability, and open-source development experience.

- **Naming the project**
    - I have chosen an easy-to-remember name for the project
- **Addressing the problem**
    - Does the documentation clearly state the problem that the project addresses at the beginning
- **Project description**
    - Have you included a compelling one-liner for the project
- **Installation instructions**
    - Is there a one-line installation solution provided in the documentation
- **Visual guidance**
    - Have you used GIFs or screenshots to visually demonstrate how to use the project or what the outputs look like
- **Roadmap**
    - Is there a roadmap included in the documentation to outline future plans and features
- **Authors and acknowledgements**
    - Have you listed the authors and provided acknowledgements to contributors or third-party resources
- **License information**
    - Is the license clearly stated and included in the project documentation
- **Project status**
    - Have you indicated the current status of the project (e.g., active development, maintenance mode)
- **Contribution guidelines**
    - Are there clear guidelines on how to contribute to the project
- **Seeking help**
    - Have you provided instructions on how to ask for help or report issues
- **Version control** (Optional)
    - Have you made a simple log or version control system visible or mentioned in the documentation

.. code-block:: python

  # Naming method 1
  CN_min, CN_max, CN_avg

  # Naming method 2
  max_CN, min_CN, avg_CN

I choose Method 2. The first method starts with ``CN_``, which allows the user to
identify that this is related to the coordination number. In practice, when we
speak, we say "maximum coordination number" instead of "coordination number
maximum". Therefore, it is more natural from a behavioral point of view.

Mistakes to avoid when naming variables
---------------------------------------

- Using non-standardized abbreviations.
- Using words that conflict with Python keywords: Avoid names like ``list``,
  ``str``, ``dict``.
- Using long words without purpose: For example, ``users_with_access_to_database``
  can be ``authorized_users``, and ``number_of_items`` can be ``item_count``.
- Using general names: Names such as ``data``, ``info``, or ``my_string`` do not
  provide context.

Software is developed using the English language. Writing is an art that
requires both skills and intuition. Just like learning to ride a bicycle for the
first time, we need to learn from experience, as it is not possible to gain the
same insights solely from books and knowledge.

Ruff
----

``ruff`` is fast. According to a post by Marsh (https://astral.sh/blog/the-ruff-formatter), formatting about 250,000
lines of code took only 0.1 seconds with ``ruff`` compared to 3.20 seconds for ``black`` and 17.77 seconds for ``yapf``. Run either ``ruff check`` or ``ruff format`` to check and modify the code.

Difference between ``pip`` and ``conda``
--------------------------------------

``pip`` and ``conda`` can be used as dependency managers. ``pip`` does not try to be a virtual environment manager. ``conda`` does not try to be Python package developer. ``conda`` can work with Python packages but also other programming languages.

- ``pip`` communicates with PyPI to upload and download Python packages. ``conda`` communicates with repositories/channels like conda-forge to upload and download packages, including but not limited to Python packages.
- Using ``conda`` allows you to reach a wider audience beyond the Python community since conda-forge is a language-agnostic platform.

Best practices for mathematical typesetting (Ft. MathJax and LaTeX)
-------------------------------------------------------------------

MathJax is used to write mathematical equations on the current website with simple commands within a Markdown file. It renders LaTeX code as a PNG file.

I will primarily use the following content as a reference to aid my writing and setup. Since MathJax and LaTeX keywords can be found online, I will focus on best practices and example snippets.

- Start with ``\begin{align}`` for aligning multiple equations or ``\begin{equation}`` for a single equation to provide a number for each equation. Examples are in the following section.

- It is generally a good practice to indent at the ``&=`` sign and also to indent after ``\begin``.

  .. code-block:: latex

    \begin{align}
    a &= b + c \\
    &= d + e
    \end{align}

MathJax code:

.. code-block:: latex

  \begin{equation}
  [\sigma] =
  \begin{bmatrix}
  \sigma_{11} & \sigma_{12} & \sigma_{13} \\ % Row 1
  \sigma_{21} & \sigma_{22} & \sigma_{23} \\ % Row 2
  \sigma_{31} & \sigma_{32} & \sigma_{33} % Row 3
  \end{bmatrix}
  \end{equation}

1. Add comments using ``%``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have a preview for both LaTeX and Markdown files. Comments are not needed if the documentation itself provides enough context for the equation. However, they can be useful for two reasons.

First, we may add remarks without making them explicitly available in the output, especially when the document is in draft form. Second, we may use ``%`` to strategically navigate and modify the equations.

To help navigate within the equation:

.. code-block:: latex

  \begin{bmatrix}
  \sigma_{11} & \sigma_{12} & \sigma_{13} \\ % Row 1
  \sigma_{21} & \sigma_{22} & \sigma_{23} \\ % Row 2
  \sigma_{31} & \sigma_{32} & \sigma_{33} % Row 3
  \end{bmatrix}

To comment out parts of the document:

.. code-block:: latex

  % The following will be restored once we have...
  % \begin{equation}
  % ...
  % \end{equation}

4. Avoid using fixed ``()`` or ``[]`` without ``\left`` or ``\right`` modifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We do not want to use a fixed ``()`` or ``[]`` without using ``\left`` or ``\right``.

Using ``\left`` and ``\right``:

.. math::

  \begin{align}
    c &= \left(\frac{a}{b}\right) \quad \text{} \\
    c &= (\frac{a}{b}) \quad \text{:(}
  \end{align}

MathJax code:

.. code-block:: latex

  \begin{align}
  c &= \left(\frac{a}{b}\right) \\
  c &= (\frac{a}{b})
  \end{align}

5. Use proper notation
^^^^^^^^^^^^^^^^^^^^^^

.. math::

  \begin{align}
    & \sin(x) \quad \log(y) \quad \ln(x)  \\
    & sin(x) \quad log(y) \quad ln(x) \quad \text{:(}
  \end{align}

Notice that function names are not italicized if properly formatted.

MathJax code:

.. code-block:: latex

  \begin{align}
  & \sin(x) \quad \log(y) \quad \ln(x) \\
  & sin(x) \quad log(y) \quad ln(x)
  \end{align}

6. Distinguish between vectors and matrices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally, a bold lowercase letter is used for vectors, while a capitalized non-bold letter is used for matrices.

.. math::

  \begin{align}
    \mathbf{v} &= \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \\
    M &= \begin{bmatrix}
    m_{11} & m_{12} \\
    m_{21} & m_{22}
    \end{bmatrix}
  \end{align}

7. Use correct ``\begin`` setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| Environment  | Description                                                                                                                   |
+==============+===============================================================================================================================+
| align        | Align multiple equations at the ``&`` symbol. Each line is numbered by default.                                               |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| align*       | Same as ``align``, no line numbering.                                                                                         |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| aligned      | Sub-environment used within another environment like ``equation`` to align multiple lines, no new equation number.            |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| equation*    | Same as ``equation``, no line numbering.                                                                                      |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| gather       | Center multiple equations without aligning them to a particular symbol. Each line is numbered.                                |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| gather*      | Same as ``gather`` but with no line numbering.                                                                                |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| gathered     | Sub-environment used within another environment, like ``equation``, to center multiple lines                                  |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| alignat      | Allows for the alignment of multiple equations, similar to ``align``, but gives you control over the spacing between columns. |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| alignat*     | Same as ``alignat`` but without equation numbering.                                                                           |
+--------------+-------------------------------------------------------------------------------------------------------------------------------+

Example 1. ``aligned`` within ``equation``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Align with a single line number.

.. math::

  \begin{equation}
    \begin{aligned}
    a + b + c &= d \\
    a + c &= h
    \end{aligned}
  \end{equation}

MathJax code:

.. code-block:: latex

  \begin{equation}
  \begin{aligned}
  a + b + c &= d \\
  e + f + g &= h
  \end{aligned}
  \end{equation}

Example 2. ``gather*``
~~~~~~~~~~~~~~~~~~~~~~

Center without line numbering.

.. math::

  \begin{gather*}
    x^2 + y^2 = r^2 \\
    e^{i\pi} + 1 = 0 \\
    y = mx + c
  \end{gather*}

MathJax code:

.. code-block:: latex

  \begin{gather*}
  x^2 + y^2 = r^2 \\
  e^{i\pi} + 1 = 0 \\
  y = mx + c
  \end{gather*}

Example 3. ``gather``
~~~~~~~~~~~~~~~~~~~~~

Center with line numbering for each equation.

.. math::

  \begin{gather}
    x^2 + y^2 = r^2 \\
    e^{i\pi} + 1 = 0 \\
    y = mx + c
  \end{gather}

MathJax code:

.. code-block:: latex

  \begin{gather}
  x^2 + y^2 = r^2 \\
  e^{i\pi} + 1 = 0 \\
  y = mx + c
  \end{gather}

Example 4. ``equation`` with ``gathered``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Center with only one line numbering.

.. math::

  \begin{equation}
    \begin{gathered}
    x^2 + y^2 = r^2 \\
    e^{i\pi} + 1 = 0 \\
    y = mx + c
    \end{gathered}
  \end{equation}

MathJax code:

.. code-block:: latex

  \begin{equation}
  \begin{gathered}
  x^2 + y^2 = r^2 \\
  e^{i\pi} + 1 = 0 \\
  y = mx + c
  \end{gathered}
  \end{equation}

