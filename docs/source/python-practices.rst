Python
======

Here I document Python practices I have learned while developing packages like ``scikit-package`` and ``cifkit``. These practices are not exhaustive, but I hope they can guide you in your own projects. ``pytest`` is used for testing.

argparse (TBA)
----------------

pytest
------

To get started, ensure you have installed ``pytest`` and ``pytest-mock``:

.. code-block:: bash

    pip install pytest pytest-mock

Locating files and folders in the project directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To locate a file in your project directory, such as ``TEMPLATE.rst`` in the ``news`` folder, you can use the following approach:

.. code-block:: python

    from pathlib import Path

    project_root = Path(__file__).resolve().parents[1]
    real_template_path = project_root / "news" / "TEMPLATE.rst"

Working with temporary files using ``tmpdir`` and ``tmp_path``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a custom temporary folder using ``tmp_path``:

.. code-block:: python

    def setup_custom_folder(tmp_path):
        my_dir = tmp_path / "<folder-name>"
        my_dir.mkdir()
        return my_dir

To create a text file within a temporary folder using ``tmpdir``:

.. code-block:: python

    from pathlib import Path

    def setup_custom_file(tmpdir):
        my_text = """{%- set version = "1.1.1" -%}
    name: cifkit
    """
        my_file = Path(tmpdir) / "<file-name-with-extension>"
        my_file.write_text(my_text)
        return my_file.read_text()

Testing an argument parser
^^^^^^^^^^^^^^^^^^^^^^^^^^

To test a function that expects an ``args`` object (as used with ``argparse``), you can use ``SimpleNamespace`` to mimic CLI arguments in your tests. For example:

.. code-block:: python

    from types import SimpleNamespace

    args1 = SimpleNamespace(
        add=True,
        change=False,
        deprecate=False,
        remove=False,
        fix=False,
        security=False,
        message="Add first news.",
    )
    news_item(args1)

Assume ``news_item`` creates an ``.rst`` file in the ``news`` folder. The function might look like:

.. code-block:: python

    def news_item(args):
        message = args.message
        # Implementation here

You can set up your argument parser to use this function:

.. code-block:: python

    parser_news.set_defaults(func=add.news_item, subcommand="news")

This allows you to call the CLI as follows:

.. code-block:: bash

    package add news -a -m "Add first news."

Mocking a simple variable
^^^^^^^^^^^^^^^^^^^^^^^^^

To mock a simple variable, such as a directory path, use ``mocker.patch``. For example, to mock the ``NEWS_DIR`` variable in the ``scikit_package.cli.add`` module:

.. code-block:: python

    def test_mocker_variable(mocker):
        mocker.patch("scikit_package.cli.add.NEWS_DIR", str(test_news_dir))

Mocking a function
^^^^^^^^^^^^^^^^^^

To mock a function, such as ``scikit_package.cli.add.get_news_files``, use:

.. code-block:: python

    def test_mocker_function(mocker):
        mocker.patch("scikit_package.cli.add.get_news_files", return_value=[str(test_news_file)])

Mocking HTTP requests and capturing print output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use ``pytest-mock`` to replace the ``requests.get`` function with a mock object. This is useful for unit testing code that makes HTTP requests. The following example mocks the HTTP request to PyPI, captures the print output, and confirms that the mock was called with the expected URL.

.. code-block:: python

    import requests

    def check_pypi_package_exists(package):
        response = requests.get(f"https://pypi.org/pypi/{package}/json")
        if response.status_code == 200:
            data = response.json()
            version = data["info"]["version"]
            print(f"> {package} is available on PyPI (latest version: {version}).")
        else:
            raise ValueError("<error-message>")

Here is the test code (in ``test_pypi.py``):

.. code-block:: python

    def test_check_pypi_package_exists(mocker, capsys):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"info": {"version": "1.2.3"}}
        mock_get = mocker.patch(
            "scikit_package.utils.pypi.requests.get", return_value=mock_response
        )
        check_pypi_package_exists("my-package")
        captured = capsys.readouterr()
        assert (
            "> my-package is available on PyPI (latest version: 1.2.3)."
            in captured.out
        )
        mock_get.assert_called_once_with("https://pypi.org/pypi/my-package/json")

Explanation:

- The ``scikit_package.utils.pypi.requests.get`` function is patched to return ``mock_response`` instead of making an actual HTTP request.
- The ``capsys`` fixture captures the output printed by the function.
- The test confirms that ``requests.get`` was called once with the expected URL.

