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

Install the SEAMM Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U seamm-cookiecutter

Generate a Python package project::

    seamm-cookiecutter

And answer the prompts about your plug-in, etc. Then change to the new
directory::
   
   cd <plug-in name>

Then create repository in GitHub with exactly the same name, just
giving the LICENSE type. Note that GitHub has changed the default
branch to `main`, which is what the SEAMM cookiecutter also uses. Now
you need to merge the two:: 

   bash-3.2$ git remote add origin
   git@github.com:<organization>/<plug-in name> .git
   bash-3.2$ git pull --allow-unrelated-histories origin master
   warning: no common commits
   remote: Counting objects: 3, done.        
   remote: Compressing objects: 100% (2/2), done.        
   remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0        
   Unpacking objects: 100% (3/3), done.
   From github.com:<organization>/<plug-in name>
    * branch            main     -> FETCH_HEAD
    * [new branch]      main     -> origin/main
   error: Terminal is dumb, but EDITOR unset
   Not committing merge; use 'git commit' to complete the merge.

Depending on what happens here, you may have a conflict in LICENSE. If
so, edit the file and fix the problem by keeping the appropriate lines.

Once that is done, push to GitHub::

   bash-3.2$ git push --set-upstream origin main
   Counting objects: 54, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (48/48), done.
   Writing objects: 100% (54/54), 20.43 KiB | 261.00 KiB/s, done.
   Total 54 (delta 10), reused 0 (delta 0)
   remote: Resolving deltas: 100% (10/10), completed with 1 local object.        
   To github.com:<organization>/<plug-in name>.git
      30251d7..e2761fc  main -> main
   Branch main set up to track remote branch main from origin.
   bash-3.2$ 

Deploy to PyPi. Once the code is in reasonable shape and working, you
can deploy to PyPi so that users can `pip install` it. You need an
account at PyPi_. 

.. _packaging guide: https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _PyPi: https://pypi.python.org/pypi
