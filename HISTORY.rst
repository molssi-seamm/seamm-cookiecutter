=======
History
=======
2026.9.18 -- CI environment template takes pure-Python dependencies from PyPI
    * The generated ``devtools/conda-envs/test_env.yaml`` lists the SEAMM packages
      (and other pure-Python dependencies) in its ``pip:`` section and keeps only the
      compiled packages -- numpy, openbabel, rdkit -- in the conda section, so a
      plug-in's CI sees a new SEAMM release within minutes rather than waiting hours
      for conda-forge to build and propagate.
    * The generated Makefile has a ``make update`` target for the post-release
      main/dev sync, matching the other plug-ins.


2021.2.17 (17 February 2021)
----------------------------

* Initial working version on PyPi.
