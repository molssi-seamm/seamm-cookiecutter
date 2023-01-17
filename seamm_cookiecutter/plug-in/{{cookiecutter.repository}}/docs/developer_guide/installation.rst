.. highlight:: shell

============
Installation
============


Stable release
--------------

To install the {{ cookiecutter.step }} Step, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.repository }}

This is the preferred method to install {{ cookiecutter.step }} Step, as it will always
install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.step }} Step can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ pip install .

from inside the top-level directory of the source code.    


.. _Github repo: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}
.. _tarball: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/tarball/master
