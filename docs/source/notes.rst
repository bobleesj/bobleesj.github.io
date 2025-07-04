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
- Go to the file after ``cmd + shift + F``? Press ``F4`` and ``shift + F4``. This allows you to quickly jump to the next or previous search result.
- Globally replace text? Press ``cmd + shift + H``.

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

Get dependencies for the project
--------------------------------

.. code-block:: bash

    pip intsall pipreqs
    


conda update --all
pip list --outdated
pip install --upgrade <package>


Project checklist
-----------------

The checklist below can be used to improve usability, marketability, and open-source development experience.

- **Naming the project**
    - Have you chosen an easy-to-remember name for the project?
- **Addressing the problem**
    - Does the documentation clearly state the problem that the project addresses at the beginning?
- **Project description**
    - Have you included a compelling one-liner for the project?
- **Installation instructions**
    - Is there a one-line installation solution provided in the documentation?
- **Visual guidance**
    - Have you used GIFs or screenshots to visually demonstrate how to use the project or what the outputs look like?
- **Roadmap**
    - Is there a roadmap included in the documentation to outline future plans and features?
- **Authors and acknowledgements**
    - Have you listed the authors and provided acknowledgements to contributors or third-party resources?
- **License information**
    - Is the license clearly stated and included in the project documentation?
- **Project status**
    - Have you indicated the current status of the project (e.g., active development, maintenance mode)?
- **Contribution guidelines**
    - Are there clear guidelines on how to contribute to the project?
- **Seeking help**
    - Have you provided instructions on how to ask for help or report issues?
- **Version control** (Optional)
    - Have you made a simple log or version control system visible or mentioned in the documentation?

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

- Using non-standardized abbreviations: One might choose to write ``min`` for
  ``minimum`` and ``std`` for ``standard deviation``.
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

``pip`` does not try to be a virtual environment manager. ``conda`` does not try to be Python package developer. But both can be used as dependency managers. ``conda``. ``conda`` can work with Python packages but also other programming languages.

- ``pip`` communicates with PyPI to upload and download Python packages. ``conda`` communicates with repositories/channels like conda-forge to upload and download packages, including but not limited to Python packages.
- Some users may want to use one package manager instead of mixing ``pip`` and ``conda``.
- Reach a wider audience beyond the Python community since conda-forge is a language-agnostic platform. Users can access it even those without prior experience in the Python community and jargon.

Intro to logging
----------------

Logs record activities. They are used for debugging and analyzing user behavior.
While ``print()`` serves as a perfectly good solution for simple programs, there
are specific needs that it cannot fulfill:

- Saving logs in a separate folder or periodically
- Turning on/off certain types of logs globally
- Providing information on line numbers, file names, etc.
- Categorizing logs into ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, and ``CRITICAL``

For these requirements, we may want to use Python's built-in logging tool.

Initial Setup
~~~~~~~~~~~~~

First, copy the following code to a Python file:

.. code-block:: python

    import logging

    def main():
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    if __name__ == "__main__":
        main()

Add log messages by modifying the file like this:

.. code-block:: python

    import logging

    def main():
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        logging.debug("This is a debug log.")
        logging.info("This is an info log.")
        logging.warning("This is a warning log.")
        logging.error("This is an error log.")
        logging.critical("This is a critical log.")

    if __name__ == "__main__":
        main()

Understand log levels
~~~~~~~~~~~~~~~~~~~~~

The log level ``DEBUG`` is the lowest, meaning all messages from all severity
levels (``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``) will be logged. Refer
to the table below:

+-----------------+--------------------------------------+
| Log Level Set   | Messages Printed                     |
+=================+======================================+
| DEBUG           | DEBUG, INFO, WARNING, ERROR, CRITICAL|
+-----------------+--------------------------------------+
| INFO            | INFO, WARNING, ERROR, CRITICAL       |
+-----------------+--------------------------------------+
| WARNING         | WARNING, ERROR, CRITICAL             |
+-----------------+--------------------------------------+
| ERROR           | ERROR, CRITICAL                      |
+-----------------+--------------------------------------+
| CRITICAL        | CRITICAL                             |
+-----------------+--------------------------------------+

For example, if you modify from ``logging.DEBUG`` to ``logging.ERROR``:

.. code-block:: text

    python main.py (logging.DEBUG)
    2024-05-23 16:28:07 INFO This is an info log.
    2024-05-23 16:28:07 WARNING This is a warning log.
    2024-05-23 16:28:07 ERROR This is an error log.
    2024-05-23 16:28:07 CRITICAL This is a critical log.

    python main.py (logging.ERROR)
    2024-05-23 16:28:14 ERROR This is an error log.
    2024-05-23 16:28:14 CRITICAL This is a critical log.

Save logs
~~~~~~~~~

Modify the ``basicConfig`` by adding ``filename`` and ``filemode``:

.. code-block:: python

    logging.basicConfig(
        level=logging.DEBUG,
        filename='app.log',
        filemode='w',  # 'w' to write, 'a' to append
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

As of this writing, I currently have no further solutions needed beyond the
above at the current level. I may add more details if more advanced
functionalities from the ``logging`` library are needed for my projects.


Best practices for mathematical typesetting (Ft. MathJax and LaTeX)
-------------------------------------------------------------------

Motivation
~~~~~~~~~~

MathJax is used to write mathematical equations on the current website with simple commands within a Markdown file. It renders LaTeX code as a PNG file.

I will primarily use the following content as a reference to aid my writing and setup. Since MathJax and LaTeX keywords can be found online, I will focus on best practices and example snippets.

MathJax
-------

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


Export dependencies
-------------------


.. code-block:: python

    # Install pipreqs via pip3
    pip3 install pipreqs

    # Overwrites requirements.txt, ignores tests
    pipreqs . --force --ignore=tests


.. code-block:: python

    conda list -e > requirements.txt


Section 1. Best practices
--------------------------

``isclose`` instead of ``round`` for comparing values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For comparing values, it's best to compare deviation from the truth.

.. code-block:: python

  URhIn_shortest_dist = 2.6967
  print(np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4))
  # True

  URhIn_shortest_dist = 2.670
  print(np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4))
  # False

Check for simpler solutions
---------------------------

It is our job to validate whether the implementation is optimized for human communication and performance.

Adding two arrays
~~~~~~~~~~~~~~~~~

.. code-block:: python

  # :( - slower, overkill
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  combined_list = list(map(lambda x, y: x + y, list1, list2))
  print(combined_list)
  # [5, 7, 9]

  # :) - faster, simple
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  combined_list = np.add(list1, list2)
  print(combined_list)
  # [5 7 9]

Whether an element exists
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  my_list = [1, 2, 3]

  # :|
  exists = any([x for x in my_list if x == 3])
  print(exists) # True
  # :)
  exists = 3 in my_list
  print(exists) # True

Applying element-wise simple operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For multiplying

.. code-block:: python

  # i.g. Square each element

  # :(
  squared = []
  for x in my_list:
    squared.append(x**2)

  # :|
  squared = list(map(lambda x: x**2, my_list))
  # :)
  squared = [x**2 for x in my_list]

For filtering

.. code-block:: python

  # :(
  filtered = []
  for x in my_list:
    if x > 10:
      filtered.append(x)

  # :)
  filtered = [x for x in my_list if x > 10]

``|`` to merge two dictionaries
------------------------------

Python has a concise syntax for this particular job.

.. code-block:: python

  # Define two dictionaries with different keys
  person_details = {"name": "Bob", "age": 56}
  person_location = {"city": "New York", "country": "USA"}

  # Merge the two dictionaries
  merged_dict = person_details | person_location

  print(merged_dict)
  # {'name': 'Bob', 'age': 56, 'city': 'New York', 'country': 'USA'}

``Counter`` to find frequency
----------------------------

In scientific computing, we like to count and draw histograms. For one of my projects, I determine a set of atoms from the supercell to determine the coordination number. The reference is chosen with the atoms with the greatest number of atoms surrounding it. Here, ``Counter`` is our friend.

.. code-block:: python

  from collections import Counter

  # Define the list with different numbers
  my_list = [15, 15, 15, 7, 7, 3, 12, 12, 12, 12, 12]

  # Create a Counter object to count the frequencies of each element in the list
  counter = Counter(my_list)
  print(counter)
  # Counter({12: 5, 15: 3, 7: 2, 3: 1})

  # Find the two most common elements
  most_common = counter.most_common(2)

  # Find the two most common elements
  most_common = counter.most_common(1)
  print(most_common)
  # [(12, 5)]

  two_most_common = counter.most_common(2)
  print(two_most_common)
  # [(12, 5), (15, 3)]

``lambda`` function
-------------------

Lambda functions or called "closure" in Swift, a function. It must be defined after ``lambda``.

.. code-block:: python

  # Return "even" or "odd" based on the value
  classify_number = lambda x: "even" if x % 2 == 0 else "odd"
  print(classify_number(2))
  print(classify_number(3))

Example 1. Sort ``dict``
~~~~~~~~~~~~~~~~~~~~~~~~

The way to sort or modify values across a collection of items in Python is using ``lambda`` function.

.. code-block:: python

  # Sort complex iterables with sorted()
  data = [
    {"name": "Alice", "age": 12},
    {"name": "Bob", "age": 56},
    {"name": "Charlie", "age": 17}
  ]

  sorted_data = sorted(data, key=lambda x: x["age"])

  print(sorted_data)
  # [{'name': 'Alice', 'age': 12},
  # {'name': 'Charlie', 'age': 17},
  # {'name': 'Bob', 'age': 56}]

.. code-block:: python

  data = [
    {"name": "Alice", "age": 12, "score": 85},
    {"name": "Bob", "age": 56, "score": 90},
    {"name": "Charlie", "age": 56, "score": 88}
  ]

  # Sort by age, then by score (ascending order)
  sorted_data = sorted(data, key=lambda x: (x["age"], x["score"]))
  print(sorted_data)
  # [{'name': 'Alice', 'age': 12, 'score': 85},
  # {'name': 'Charlie', 'age': 56, 'score': 88},
  # {'name': 'Bob', 'age': 56, 'score': 90}]

Example 2. Sort ``list``
~~~~~~~~~~~~~~~~~~~~~~~~

Based on increasing or decreasing

.. code-block:: python

  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  sorted_numbers_asc = sorted(numbers)
  print(sorted_numbers_asc)
  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
  sorted_numbers_desc = sorted(numbers, key=lambda x: -x)
  print(sorted_numbers_desc)
  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

Based on string length

.. code-block:: python

  words = ["banana", "apple", "cherry", "date"]
  sorted_words = sorted(words, key=lambda x: len(x))
  print(sorted_words)
  # Output: ['date', 'apple', 'banana', 'cherry']

``open`` instead of ``finally``
-------------------------------

Python offers a cleaner, more efficient way to handle files opening and closing.

.. code-block:: python

  # :(
  file = open('my_file.txt', 'r')
  try:
    data = file.read()
    # process data
  finally:
    file.close()

.. code-block:: python

  # :)
  with open('my_file.txt', 'r') as file:
    data = file.read()
    # process data

We simply do not forget to close the file. It is handled automatically with ``open``.

``enumerate`` instead of ``range`` for loop
-------------------------------------------

Example 1. ``list``
~~~~~~~~~~~~~~~~~~~

We want both the index and the value without the need to use ``[i]``.

.. code-block:: python

  # List data
  my_list = [1, 2, 3]

  # :(
  for i in range(len(my_list)):
    print(i, my_list[i])

  # :) - Get both index and value in the loop
  for idx, num in enumerate(my_list):
    print(idx, num)

Example 2. ``dict``
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  # Dictionary data
  my_dict = {'a': 1, 'b': 2, 'c': 3}

  # :( - Iterating over a dictionary without using enumerate
  for key in my_dict:
    print(key, my_dict[key])

  # :) - Using enumerate to get both the index and key-value pairs
  for index, (key, value) in enumerate(my_dict.items()):
    print(index, key, value)

  # If index is not needed
  for key, value in my_dict.items():
    print(key, value)

Use ``_`` for large numbers
---------------------------

We do not want to count the zeros.

.. code-block:: python

  # :|
  number_of_stars = 1000000000

  # :)
  number_of_stars = 1_000_000_000

Return ``None``
---------------

.. code-block:: python

  def function_that_does_not_return_value():
    # some operations
    return None

``main()``
----------

Certain code is only executed when the script is run directly, and not when it's imported as a module.

.. code-block:: python

  def main():
    # Main code here

  if __name__ == "__main__":
    main()

Documentation
-------------

.. code-block:: python

  def calculate_means(numbers1, numbers2):
    """
    Calculate and return the means of two lists of numbers separately.

    :param numbers1: First list of float or integers.
    :param numbers2: Second list of float or integers.
    :return: A tuple containing the means of both lists.
    """
    mean1 = sum(numbers1) / len(numbers1) if numbers1 else 0
    mean2 = sum(numbers2) / len(numbers2) if numbers2 else 0
    return mean1, mean2

Use type hints
--------------

Python infers types automatically. But it is difficult for us to infer them based on variable names. I am hoping to implement this in my next Python project. Cons are increased maintenance if type hints need to be updated.

Regardless, with my first in-depth programming background in Swift where the type must be defined before compilation, I generally like the ability to know types ahead. This is particularly important for projects with many classes which are found in mobile development SDKs.

.. code-block:: python

  from typing import List, Dict

  def calculate_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

  def merge_dicts(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    return {**dict1, **dict2}

Comprehensions
--------------

A comprehension in Python is a concise syntax for constructing a new sequence based on the values from an existing sequence or iterable.

Example 1. Modify
~~~~~~~~~~~~~~~~~

.. code-block:: python

  # Dictionary comprehension
  dict_comp = {i: (i + 1) ** 2 for i in range(5)}

  # List comprehension
  list_comp = [(x + 1) ** 2 for x in range(5)]

  # Set comprehension
  set_comp = {(i + 3) % 5 for i in range(5)}

  print("Dict Comprehension:", dict_comp)
  print("List Comprehension:", list_comp)
  print("Set Comprehension:", set_comp)
  # Dict Comprehension: {0: 1, 1: 4, 2: 9, 3: 16, 4: 25}
  # List Comprehension: [1, 4, 9, 16, 25]
  # Set Comprehension: {0, 1, 2, 3, 4}

Example 2. Add condition
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  list_comp = [(x + 1) == 2 for x in range(5)]
  print(list_comp)
  # [False, True, False, False, False]

Zip
---

The ``zip()`` function combines several iterables (like lists, tuples, etc.) element-wise, creating a new iterator of tuples.

Example 1. iterate two arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  a = [1, 2, 3]
  b = [4, 5, 6]

  zipped = zip(a, b)  # Creates an iterator of tuples

  for pair in zipped:
    print(pair)  # (1, 4), (2, 5), and (3, 6)

Example 2. ``enumerate``
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  a = [1, 2, 3]
  b = [4, 5, 6]

  for i, (av, bv) in enumerate(zip(a, b)):
    # 'i' is the index, 'av' is the element from 'a', 'bv' is the element from 'b'
    print(f"Index: {i}, a: {av}, b: {bv}")

Use ``perf_counter()`` for time
-------------------------------

.. code-block:: python

  import time

  # :( Using time.time()
  start_time = time.time()
  time.sleep(1)  # Sleep for 1 second
  end_time = time.time()
  time_duration = end_time - start_time

  # :) Using time.perf_counter()
  start_perf = time.perf_counter()
  time.sleep(1)  # Sleep for 1 second
  end_perf = time.perf_counter()
  perf_duration = end_perf - start_perf

  print(time_duration)
  print(perf_duration)

``time.perf_counter()`` provides the highest available resolution timer to measure a short duration. It includes time elapsed during sleep and is system-wide.

``time.time()`` returns the current time in seconds since the Epoch (a fixed point in time used for time calculations, typically January 1, 1970, 00:00:00 (UTC)). It's suitable for getting the current timestamp.

Use comprehension
-----------------

- When creating a list, set, dictionary from existing iterables and applying conditions to filter or transform the elements.

Use Lambda
----------

- When a function is needed for an argument such as ``filter()``, ``sorted()``, ``map()``.

.. code-block:: python

  even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
  print(even_numbers)

Section 2. NumPy
----------------

Create array
^^^^^^^^^^^^

.. code-block:: python

  # Create an empty 1D array
  arr_1d = np.arange(10)
  # [0, 1, ..., 8, 9]

  arr_1d = np.empty(5)
  # [0, 0, 0, 0, 0]

  # Create an empty 2D array
  arr_2d = np.empty((3, 4))
  #[[0. 0. 0. 0.]
  # [0. 0. 0. 0.]
  # [0. 0. 0. 0.]]

Reshape array
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  arr_1d = np.arange(10)
  arr_2d = arr_1d.reshape((5, 2)) # 5 rows, 2 cols

Broadcast
^^^^^^^^^^^^

Example 1. Constant addition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  # Create a 2D array (e.g., 3x3)
  arr_2d = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

  # Constant to add
  constant = 10

  # The constant is "broadcast" across the 2D array, adding it to every element
  result = arr_2d + constant

Example 2. Addition between two arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  arr_1d = np.array([1, 0, -1])

  # The 1D array is broadcast across each row of the 2D array
  result = arr_2d + arr_1d
  print(result)
  # Output:
  # [[2 2 2]
  #  [5 5 5]
  #  [8 8 8]]

Example 3. Multiplication between two arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
  arr_1d = np.array([1, 2])

  result = arr_2d * arr_1d
  '''
   [1, 2]    [1*1, 2*2]    [1,  4]
   [1, 2] -> [3*1, 4*2] -> [3,  8]
   [1, 2]    [5*1, 6*2]    [5, 12]
  '''

  print(result)
  # Output:
  # [[ 1  4]
  #  [ 3  8]
  #  [ 5 12]]

Apply universal functions
-------------------------

.. code-block:: python

  arr = np.array([1, 2, 3, 4, 5])
  result_add = np.add(arr, 10)  # Adds 10 to each element
  result_multiply = np.multiply(arr, 2)  # Multiplies each element by 2
  result_sin = np.sin(arr)  # Computes the sine of each element

Section 3. Prompt
------------------

Get user input with option selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  # Get the directory of the script being executed
  script_directory = os.path.dirname(os.path.abspath(__file__))

  print("\nWelcome! Please choose an option to proceed:")

  options = {
    "1": "Move files based on unsupported CIF format",
    "2": "Move files based on unreasonable distance",
    "3": "Move files based on tags",
    "4": "Move files based on supercell atom count",
    "5": "Copy files based on atomic occupancy and mixing",
    "6": "Get file info in the folder",
    "7": "Check CIF folder content against Excel file"
  }

  # Print options
  for key, value in options.items():
    print(f"[{key}] {value}")

  # Get user input
  choice = input("Enter your choice (1-7): ")

  if choice in options:
    print(f"You have chosen: {options[choice]}\n")
  else:
    print("Invalid choice!")
    return

Section 4. Pandas
-----------------

Read CSV
^^^^^^^^^^^^

.. code-block:: python

  csv_file_path = join(base_dir, "csv", "info_cif_files_info.csv")
  csv_data = pd.read_csv(csv_file_path)
  # 'CIF file' column matches 'URhIn.cif' and selects the 'Min distance' column
  # iloc[0] refers to the first element
  URhIn_min_dist = csv_data[csv_data['CIF file'] == 'URhIn.cif']['Min distance'].iloc[0]

Save CSV
^^^^^^^^^^^^

.. code-block:: python

  def save_to_csv_directory(folder_info, df, base_filename):
    """
    Saves the dataframe as a CSV inside a 'csv' sub-directory of the provided folder.
    """

    csv_directory = join(folder_info, "csv")
    if not os.path.exists(csv_directory):
      os.mkdir(csv_directory)

    # Extract the name of the chosen folder
    folder_name = os.path.basename(folder_info)

    # Set the name for the CSV file based on the chosen folder
    csv_filename = f"{folder_name}_{base_filename}.csv"

    # Save the DataFrame to the desired location (within the 'csv' sub-directory)
    df.to_csv(join(csv_directory, csv_filename), index=False)

    print(csv_filename, "saved")

Section 5. Math
-----------------

Sympy
^^^^^^^^^^^^

Generate symbolic answers

.. code-block:: python

  import sympy as sp

  # Define the symbols
  a11, a12, a21, a22, t11, t12, t21, t22 = sp.symbols('a11 a12 a21 a22 t11 t12 t21 t22')

  # Define the matrix A and its inverse A_inv
  A = sp.Matrix([[a11, a12], [a21, a22]])
  A_inv = A.inv()

  # Define the matrix T
  T = sp.Matrix([[t11, t12], [t21, t22]])

  # Calculate the transformed matrix T' using the formula T' = A * T * A_inv
  T_prime = A * T * A_inv

  # Extract the elements of the transformed matrix T'
  T_prime_elements = T_prime.tolist()

  # Output the elements of T' as a list of lists (matrix form)
  print(T_prime_elements) # Symbolic answers
  # [[-a21*(a11*t12 + a12*t22)/(a11*a22 - a12*a21)...]]

Section 6. Object-oriented programming
---------------------------------------

For the project of my scale, I did not feel the urgency to implement object-oriented programming. When I used Python for training neural networks and material science projects, calling functions directly with variables passed through parameters was sufficient for implementation and testing.

In addition, from the "Stop Writing Classes" video on `YouTube <https://www.youtube.com/watch?v=o9pEzgHorH0>`_, I agree with the following bullet points directly from the video:

- Simple is better than complex.
- Flat is better than nested.
- Readability counts.
- Ship features not code.
- Customers love features, not code.

Whether to use OOP depends on the above points. For my projects, I didn't need to. However, I may consider OOP later if I need to build projects that can be easily exported and imported.

General cons of OOP
^^^^^^^^^^^^^^^^^^^

- Hidden states within objects make it hard to reason about what is contained within an object from outside a function. By design, this is a feature known as encapsulation, a principle of OOP. It provides safety preventing external entities from directly changing the object's state.
- OOP tends to give a feeling of being more organized, like an organization. It also means modules and tasks are more tightly coupled.
- OOP tends to create boilerplate code such as getters and setters often employed in JAVA without adding significant value.

General pros of OOP
^^^^^^^^^^^^^^^^^^^

- A well-designed object can be reused in other projects, like ``ndarray`` in NumPy.

General OOP best practices
^^^^^^^^^^^^^^^^^^^^^^^^^^
- Each class should have a single responsibility
- Avoid deep inheritance

Data class
~~~~~~~~~~

.. code-block:: python

  # Source- https://docs.python.org/3/tutorial/classes.html#
  from dataclasses import dataclass

  @dataclass
  class Employee:
    name: str
    dept: str
    salary: int

  john = Employee('john', 'computer lab', 1000)
  >>> john.dept
  'computer lab'
  >>> john.salary
  1000

Abstract class
~~~~~~~~~~~~~~

.. code-block:: python

  # Example source - https://www.geeksforgeeks.org/abstract-classes-in-python/
  from abc import ABC, abstractmethod

  class Polygon(ABC):

    @abstractmethod
    def print_sides(self):
      pass

  class Triangle(Polygon):

    # overriding abstract method
    def print_sides(self):
      print("I have 3 sides")

  class Pentagon(Polygon):

    # overriding abstract method
    def print_sides(self):
      print("I have 5 sides")

Property decorator
~~~~~~~~~~~~~~~~~~

.. code-block:: python

  # Example source - https://www.programiz.com/python-programming/property
  class Celsius:
    def __init__(self, temperature=0):
      self.temperature = temperature

    def to_fahrenheit(self):
      return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
      print("Getting value...")
      return self._temperature

    # setter
    def set_temperature(self, value):
      print("Setting value...")
      if value < -273.15:
        raise ValueError("Temperature below -273.15 is not possible")
      self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)

The above code can be improved using ``@property``

.. code-block:: python

  # Example source - https://www.programiz.com/python-programming/property
  # Using @property decorator
  class Celsius:
    def __init__(self, temperature=0):
      self.temperature = temperature

    def to_fahrenheit(self):
      return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
      print("Getting value...")
      return self._temperature

    @temperature.setter
    def temperature(self, value):
      print("Setting value...")
      if value < -273.15:
        raise ValueError("Temperature below -273 is not possible")
      self._temperature = value

Output

.. code-block:: bash

  >>> human = Celsius(37)
  >>>  print(human.temperature)
  >>>  print(human.to_fahrenheit())
  >>>  human.temperature = -300
  Output:
  Setting value...
  Getting value...
  37
  Getting value...
  98.60000000000001
  Setting value...
  Traceback (most recent call last):
    File "<string>", line 31, in <module>
    File "<string>", line 18, in set_temperature
  ValueError: Temperature below -273 is not possible
