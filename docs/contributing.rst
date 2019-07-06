============
Contributing
============
*******************
Submitting an issue
*******************

Please submit any issues to our `issues tracker <https://github.com/mrz1988/lilies/issues>`_ on github. For now this can include basic improvements, bugs found, or failures that you are curious about. Issues surrounding bugs that are created should describe reproduction steps as clearly as possible, and list the OS, python install, and terminal used. Please be courteous, and include only details necessary to describe and replicate the issue. Any tickets opened that are deemed insignificant, against the grain of our goals, or needlessly hostile will be closed.

If you see an issue or potential hazard with the code, we encourage you to submit a Pull Request with fixes!

*************************
Submitting a pull request
*************************

Anyone is allowed to submit a pull request including new features, documentation, or bug fixes. There is no guarantee that your pull request will be approved for merging into lilies, and may be closed with a description for why we do not want it. That's okay! We love anyone coming in to help out, but try to be consistent with our goals. In some cases, new features or API changes may be better left to a competing project, or a new library that utilizes lilies.

Documentation is *great to have* and we want as much as possible. Please gear any vague documentation towards naive developers, and all API documentation should be geared towards developers who have good familiarity with python. Brevity is valued, although I often fail to practice this.

In your pull request description, please describe what you did, why it's useful to the project, and any technical implications/decisions that you made getting there. Code should include unit tests, and be linted to PEP8 standards. Lilies does not currently have a formal style guide, but assume that anything not explicitly stated in PEP8 should be roughly consistent with the surrounding code.

*************************
Development setup (MacOS)
*************************

If you are using a modern installation of MacOS, good news, this should be fairly easy for you:

.. code-block:: bash

    $ git clone https://github.com/mrz1988/lilies.git
    $ cd lilies
    $ sh bootstrap-macos.sh

This will take quite a while, so it might be good to go grab a coffee. It installs several virtualenv python versions, and configures the lilies directory to prefer execution on python-3.7. This will not pollute any of your other python installs. It then installs all dev testing prerequisites, and runs lilies tests on all related environments.

If for whatever reason, you need to tear it down again:

.. code-block:: bash

    $ sh bootkill-macos.sh

**Note:** It's important to run the shell scripts from the lilies root directory, or you may have issues. If you messed this up, you might be able to fix it by going back to the root directory and running the kill script, before re-running the bootstrap script.

***************************
About the dev environment
***************************

Lilies development uses `tox <https://github.com/tox-dev/tox>`_ to run unit tests on numerous python environments via `pyenv <https://github.com/pyenv/pyenv>`_. If you are not running on MacOS, you will need to follow the breadcrumbs yourself. Some important tools that can help you:

`pyenv-win <https://github.com/pyenv-win/pyenv-win>`_ for Windows development
`pyenv-installer <https://github.com/pyenv/pyenv-installer>`_ to help install in other Unix-like environments
`tox-pyenv <https://pypi.org/project/tox-pyenv/>`_ will bridge tox to your pyenv setups

*****************
Running the tests
*****************

**Via tox:**
If your development setup is done correctly, you should be able to run all tests from the lilies root directory via:

.. code-block:: bash

    $ tox

If you really struggle getting tox and pyenv playing correctly, you may need to set up lots of global installs on your machine and do it that way. If *even that* sucks, which it might if you're on Windows, I'd recommend just saying screw it and running tests on whatever development python version suits you. Someone, somewhere will run your tests before any created PRs are merged. At the time of writing this, no CI server is set up, but it should be one day.

**Via pytest:**
To run just the tests on your local install, you can install ``pytest`` via pip, and run it on whatever your local pyenv is set to with:

.. code-block:: bash
    $ python -m pytest

It's important to run it this way rather than running the ``pytest`` alias directly, so that pytest is run on the same python version that you are running the rest of your code from. I've patched this over locally by removing the system install of ``pytest``, then re-aliasing ``pytest`` to the above command in my ``~/.bash_profile``:

.. code-block:: bash
    $ alias pytest='python -m pytest'

This should also allow you to do things like run a partial set of tests via ``-k``:

.. code-block:: bash
    $ pytest -k <partial_test_name>


**Via lilies itself:**
Failing all other things, lilies is set up to run its tests from wherever it is installed. This is great for checking pre-installed lilies libraries for functionality:

.. code-block:: bash
    $ python -m lilies -t

The above command will run all tests for lilies. You can also play around with ``--help`` to see other ways to execute the tests from the command line in this way.