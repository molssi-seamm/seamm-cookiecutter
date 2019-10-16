==============================
Cookiecutter for SEAMM Plugins
==============================
Cookiecutter_ template for a SEAMM plugin.

* GitHub repo: https://github.com/molssi-seamm/cookiecutter-seamm-plugin
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* 
* Auto-release to PyPI_ when you push a new tag to master (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/molssi-seamm/cookiecutter-seamm-plugin.git

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


.. _Travis-CI: http://travis-ci.org/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _PyPi: https://pypi.python.org/pypi
