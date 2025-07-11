Bob's notes
===========

Sphinx
-------

Add Jupyter notebook
^^^^^^^^^^^^^^^^^^^^^

You may want to render Jupyter notebooks and show outputs as shown in https://bobleesj.github.io/bobleesj.utils/notebooks/Oliynyk.

#. Add ``ipykernel`` and ``nbsphinx``, and remove ``m2r`` from ``requirements/docs.txt``.
#. Add ``nbsphinx_allow_errors = True`` in ``conf.py``.
#. Done! 

  .. note::
    
    Did you encounter and problems? I recommend you to cross-check with the ``conf.py`` file of ``bobleesj.utils`` in https://github.com/bobleesj/bobleesj.utils.

Add citation
^^^^^^^^^^^^

You may want to have a single of ``.bib`` where you put all citations and then use it throuhgout the documentation. For example, check this page how I cite papers in :ref:`decision-making-guide`.

#. Add ``sphinxcontrib-bibtex`` to ``requirements/docs.txt``.

#. Add ``sphinxcontrib.bibtex`` to ``extensions`` in ``conf.py``.

#. Add ``bibtex_bibfiles = ['refs.bib']`` in ``conf.py``.

#. Run ``mamba --file requirements/docs.text``.

#. Create ``refs.bib`` under ``docs``. 

#. Copy and paste the following into ``refs.bib``:

    .. code-block:: bib

        @article{nature22336,
          author = {Schlebusch, Carina M. and others},
          title = {Southern African ancient genomes estimate modern human divergence to 350,000 to 260,000 years ago},
          journal = {Nature},
          volume = {546},
          pages = {293--296},
          year = {2017},
          url = {https://www.nature.com/articles/nature22336}
        }

#. In your ``.rst`` file, write ``This is from :cite:`nature22336`.``.

#. At the botton of the ``.rst`` file, add 

    .. code-block:: text

      .. bibliography:: refs.bib
         :style: plain

#. Done! Add more to the ``refs.bib`` file as needed. You should see a nicely rendered cited section as shown in :ref:`decision-guide-ref`

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
  - An easy-to-remember name for the project has been chosen
- **Addressing the problem**
  - The documentation clearly states the problem that the project addresses at the beginning
- **Project description**
  - A compelling one-liner for the project is included
- **Installation instructions**
  - A one-line installation solution is provided in the documentation
- **Visual guidance**
  - GIFs or screenshots are used to visually demonstrate how to use the project or what the outputs look like
- **Roadmap**
  - A roadmap is included in the documentation to outline future plans and features
- **Authors and acknowledgements**
  - Authors are listed and acknowledgements to contributors or third-party resources are provided
- **License information**
  - The license is clearly stated and included in the project documentation
- **Project status**
  - The current status of the project (e.g., active development, maintenance mode) is indicated
- **Contribution guidelines**
  - Clear guidelines on how to contribute to the project are provided
- **Seeking help**
  - Instructions on how to ask for help or report issues are provided
- **Version control** (Optional)
  - A simple log or version control system is visible or mentioned in the documentation

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


지식 경영 
-------

2025년 7월 초, 한국에서 친구를 만났다. 지인의 회사 일정은 1학기와 2학기로 나뉘어 있으며, 진급에 필요한 학점을 이용해 필요한 수업을 들어야 한다. 회사가 학교처럼 운영된다니... 몇 주 전, 이순철 박사 및 경영 컨설턴트의 '지식 경영 메뉴얼'이라는 아버지의 책장에 꽃인 책을 읽었다. 25년이 넘은 책이지만, 학습 조직이라는 개념에 대해 좀 더 알고 싶었다. 책을 읽고 중요한 내용을 아래에 정리했다. 먼저 지식경영의 정의를 알고, 책에 나온 내용을 나에게 맞게 정리했다. 책 내용 이외에도 지식경영에 대한 나의 생각을 추가했다.

知識經營의 目標

저자는 다음과 같이 지식경영을 정의한다. "지식경영은 조직이 지닌 지적 자산뿐만 아니라 구성원 개개인의 지식이나 노하우를 체계적으로 발굴하여 조직 내부의 보편적인 지식으로 공유하고, 이를 활용해 조직 전체의 경쟁력을 향상시키는 경영 이론이다."

간단한 예시가 있다. 새로운 기계가 도입되어도 엔지니어가 사용법과 매뉴얼에 대한 지식이 부족하면, 고장 시 대처 등 추후 문제가 생겼을 때 적절히 대응하지 못한다. 이는 결국 더 큰 문제를 야기한다.

교육의 목적은 창의력과 효율이라는 두 마리 토끼를 잡아야 한다. 스티브잡스는 창의력을 다양한 관점의 집합으로 인해 만들어진다라고 말했다. 교육은 경험의 일종이다. 창의력의 발판을 마련한다.  OJT (On the job training) 같이 일을 하면서 지식을 배워 업무 효율을 높일 수 있다. 예를 들어, 내가 속한 연구 조직에서는 Git과 GitHub를 배워야지만 기여가 가능하다. 주로, 처음 온 연구자는 Public database에 자신 프로파일을 업데이트 하면서 업무 workflow를 배운다.

두 마리의 토끼를 잡아야하는 이유는 다음과 같다. 효율이 높다고 해서 같은 방식으로만 일을 처리하면, AI의 모델과 같이 누군가의 새로운 접근에 의해 도태될 수 있다. 반대로 창의력만 추구하고 실무 능력과 효율이 낮다면, 이 또한 조직이 이윤, 등 부분에서 도태되는 원인이 된다. 

지식의 조회가 쉬워야 한다. 누구나 쉽게 사례별로 지식을 조회하고 활용할 수 있어야 한다. 또한, 지식이 쉽게 업데이트될 수 있도록 지식 데이터베이스를 구축하고, 적절한 보상을 제공해야 한다. 예를 들어, 학습 활동을 대외적으로 인정하는 것, 승진 체계, 지식 공유 시상, 컨퍼런스 발표, 뉴스레터 기고, 감사 편지 등이 있다.

학습은 미래의 기회를 창출하기 위한 투자이다. 업무 이외의 학습 시간을 따로 주어 조직원이 새로운 기술을 익혀 새로운 먹거리 기술을 창출할 수 있도록 한다. 또한, 학습은 조직의 단기적 사업 목표를 이루게 한다. 학습을 권장하는 문화를 만든다. 나도 저자와 동의한다. 교육과 학습은 비용 또는 복지 관점이 아닌 투자 관점에서 바라보아야 한다.

리더는 학습에 필요한 인적 자원, 회의실, 컴퓨터, 책, 강의, 세미나, 학비, 수업료 등을 제공하여 성장할 수 있도록 격려해야 한다. 개인의 성취와 조직의 성취가 함께 일맥상통해야 한다. 따라서, 리더는 조직원과 어떠한 학습을 할지 고민한다. 단순한 업무가 아닌 고차원 결정을 하는 조직원에게는 스스로 학습 과정을 설계하게 하는 기회를 준다.

지식 공유를 권장하는 문화를 만든다. 자신의 지식을 공유하는 조직원은 구조조정의 대상이 아닌, 신뢰를 주고 존경의 대상이 됨을 알린다.

전문가의 지식이 조직의 지식 자산이 될 수 있도록 한다. 나는 현재 학생으로서 조직을 운영하지 않는다. 오히려 나는 조직에 속해 있다. 그러나, 내가 책에서 읽은 내용을 나의 웹사이트에 올려 쉽게 조회할 수 있다. 지식은 사용하지 않으면 사라진다. 사용하고 싶어도 의식 위에 떠오르지 않으면 간단하게 구조화하기 어려워 적용하기 어렵다. 이미 간단하게 구조화된 프레임워크를 글로 영구화시킨다. 또는 나의 지식을 쉽게 조직원과 공유하기 위해 :ref:`workflows` 와 같이 내가 업무 효율을 높이기 위한 장치를 공개적으로 올리고 있다.

나머지 생각
^^^^^^^^

상황에 따라 실수 또는 실패를 용인하는 조직이어야 한다. 나느 둘 다 같은 말이다라고 생각한다. 실수는 원래 잘해야 하는 것을 하지 못한 것이고, 실패는 성공할 줄 알았지만 이루지 못한 것이다. 공통점은 둘 다, expectation에 부합하지 않는 것이다. 실수를 용납하지 않는 조직은 경직된다. 실패 또는 실수도 종류가 다양하다. 나는 이미 4가지 실패 프레임워크를 제시 했다.(:ref:`essay-failure-framework`). Experimental과 Expensive failures에 대해서는 상황에 맞게 용납하는 조직이 되어야 창의성이 비로소 실무가 될 수 있다.

부서 간 신뢰가 중요하다. 신뢰를 통해 서로 도움이 되는 관계를 형성하고, 조직의 이익과 서로의 이익을 위해 협력한다. 조직 계층을 넘나드는 발표회, 프로젝트 회의, 기술 세미나 등을 통해 지식을 공유하며 서로 간의 접점을 늘려 신뢰 관계를 형성한다. 선입견과 편견을 버리고 서로 신뢰하는 것이 중요하다. 이를 위해 서로 물리적으로 접촉하는 것이 중요하다.

종업원 모두가 피드백을 줄 수 있도록 참여하게 한다. 반대 의견에 중점을 두지 않고, 가급적 많은 의견을 수렴한다.

原則

- 最高經營層 學習 目標 樹立 參與

討論方法

- 反對 意見 自制
- 發言權 獨占 自制

技術敎育 戰略

- 教育 前, 매니저는 교육 목적 및 사업 연관성을 파악
- 教育 前, 매니저는 피교육자의 역량을 파악
- 教育 前, 기술 사용 경험을 피교육자가 제공
- 教育 後, 매니저는 피교육자의 사업 활용 여부를 모니터링하고 현장 교육을 실시

