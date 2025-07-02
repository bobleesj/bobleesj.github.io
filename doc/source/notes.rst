Bob's notes
===========

How to add Jupyter notebooks to Sphinx
--------------------------------------

1. Add ``ipykereal`` and ``nbsphinx`` and remove ``m2r`` under ``requirements.docs.txt`` .
2. Add  ``nbsphinx_allow_errors = True`` in ``conf.py``.
3. Add ``nbsphinx`` to ``extensions`` in ``conf.py``:

    .. code-block:: python

        extensions = [
            "nbsphinx",
            "sphinx.ext.autodoc",
            "sphinx.ext.napoleon",
            "sphinx.ext.todo",
            "sphinx.ext.viewcode",
            "sphinx.ext.intersphinx",
            "sphinx_rtd_theme",
        ]

4. Cross check with ``bobleesj.utils`` (http://github.com/bobleesj/bobleesj.utils).

How to setup SSH for GitHub
---------------------------

#. In your terminal, run the following commands to generate a new SSH key pair. Replace ``<email@example.com>`` with your email address.

    .. code-block:: bash

        cd ~/.ssh
        ssh-keygen -o -t rsa -C "<email@example.com>"
        cat id_rsa.pub

#. Visit https://github.com/settings/keys.

#. Click :guilabel:`New SSH key`.

#. Set the :guilabel:`Title` as ``<your-computer-name>-key``.

#. Under :guilabel:`Key`, copy and paste content of the ``id_rsa.pub`` file and paste it into the "Key" field. It should start with ``ssh-rsa`` and end with your email address.

#. Click :guilabel:`Add SSH key`.

#. Done!

Ref: https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GitHub-SSH-Key-Setup-Config-Ubuntu-Linux

How to install ``mamba``
------------------------

This tutorial is for macOS. For other platforms, please refer to the official documentation at https://github.com/conda-forge/miniforge.

#. Remove existing ``miniconda3`` and ``miniforge3`` directories if they exist:

    .. code-block:: bash

        rm -rf /Users/<macbook-username>/miniconda3
        rm -rf /Users/<macbook-username>/miniforge3

    Replace ``<macbook-username>`` with your actual username. You can see it after typing ``pwd`` in your terminal.

#. Install ``mamba`` using the following commands:

    .. code-block:: bash

        $ curl -L -O "[https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$)(uname -m).sh"

#. Make the script executable:

    .. code-block:: bash

        $ bash Miniforge3-$(uname)-$(uname -m).sh
        $ mamba shell init

#. Restart your terminal and type the following command to verify the installation:

    .. code-block:: bash

        $ mamba --version
