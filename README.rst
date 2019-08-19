======================
Cookiecutter PyPackage
======================

.. image:: https://pyup.io/repos/github/audreyr/cookiecutter-pypackage/shield.svg
     :target: https://pyup.io/repos/github/audreyr/cookiecutter-pypackage/
     :alt: Updates

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/audreyr/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4, 3.5
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Auto-release to PyPI_ when you push a new tag to master (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/audreyr/cookiecutter-pypackage.svg
    :target: https://travis-ci.org/audreyr/cookiecutter-pypackage
    :alt: Linux build status on Travis CI

Windows:

.. image:: https://ci.appveyor.com/api/projects/status/github/audreyr/cookiecutter-pypackage?branch=master&svg=true
    :target: https://ci.appveyor.com/project/audreyr/cookiecutter-pypackage/branch/master
    :alt: Windows build status on Appveyor

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

My steps
~~~~~~~~
After running cookie cutter, do the following to create the initial local git repository::
   
   cd mypackage
   git init .
   git add .
   git commit -m "Initial skeleton."
   git remote add origin git@github.com:myusername/mypackage.git

Then create the same-named repository in GitHub, just giving the LICENSE type.
Now you need to merge the two::

   bash-3.2$ git remote add origin git@github.com:paulsaxe/forcefield_step.git
   bash-3.2$ git pull --allow-unrelated-histories origin master
   warning: no common commits
   remote: Counting objects: 3, done.        
   remote: Compressing objects: 100% (2/2), done.        
   remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0        
   Unpacking objects: 100% (3/3), done.
   From github.com:paulsaxe/forcefield_step
    * branch            master     -> FETCH_HEAD
    * [new branch]      master     -> origin/master
   error: Terminal is dumb, but EDITOR unset
   Not committing merge; use 'git commit' to complete the merge.
   bash-3.2$ git push --set-upstream origin master
   Counting objects: 54, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (48/48), done.
   Writing objects: 100% (54/54), 20.43 KiB | 261.00 KiB/s, done.
   Total 54 (delta 10), reused 0 (delta 0)
   remote: Resolving deltas: 100% (10/10), completed with 1 local object.        
   To github.com:paulsaxe/forcefield_step.git
      30251d7..e2761fc  master -> master
   Branch master set up to track remote branch master from origin.
   bash-3.2$ 

I do the commit (of LICENSE) via emacs git-status.

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

* `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, ``_compat`` module and module/doc conventions.
  See ``README.rst`` or the `github comparison view`_ for exhaustive list of
  additions and modifications.

* `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements files rather than a requirements list in the ``setup.py`` file.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _PyPi: https://pypi.python.org/pypi

.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
