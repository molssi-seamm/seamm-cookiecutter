==============================
Cookiecutter for SEAMM Plugins
==============================
Cookiecutter_ template for a SEAMM plugin.

* GitHub repo: https://github.com/molssi-seamm/cookiecutter-seamm-plugin
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* CI/CD: Ready for Continuous Integration/Continuous Deployment using
  GitHub Actions.
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Auto-release to PyPI_ when you push a new tag to master (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/molssi-seamm/cookiecutter-seamm-plugin.git

Then after running cookie cutter, do the following:
   
   cd mypackage

Then create the same-named repository in GitHub, just giving the LICENSE type.
Now you need to merge the two::

   bash-3.2$ git remote add origin git@github.com:molssi-seamm/forcefield_step.git
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

Depending on what happens here, you may have a conflict in LICENSE. If
so, edit the file and fix the problem by keeping the appropriate lines.

Once that is done, push to GitHub:

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

Go to ReadTheDocs_ and import the new repository. It is quite
simple and obvious (hopefully!). You will need to go to ADMIN /
Advanced Settings and check "Install project".

Deploy to PyPi. Once the code is in reasonable shape and working, you
can deploy to PyPi so that users can `pip install` it. You need an
account at PyPi_ and an api token. See the first part of the
`packaging guide`_ for how to get the api token and register it with
GitHub

.. _packaging guide: https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _PyPi: https://pypi.python.org/pypi
