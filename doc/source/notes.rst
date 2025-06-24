Bob's notes
===========

How to add Jupyter notebooks to Sphinx
--------------------------------------

1. Add ``ipykernal`` and ``nbsphinx`` and remove ``m2r`` under ``requirements.docs.txt`` .
2. Add  ``nbsphinx_allow_errors = True`` in ``conf.py``.
3. Cross check with ``bobleesj.utils`` (http://github.com/bobleesj/bobleesj.utils).

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

How to install ``mamba`` (TBA)
------------------------------

