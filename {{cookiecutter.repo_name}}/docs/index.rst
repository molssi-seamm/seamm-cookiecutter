{% if cookiecutter.github_username != "molssi-seamm" -%}
Welcome to the documentation for the {{ cookiecutter.step }} SEAMM plug-in
====================================={% for _ in cookiecutter.step
%}={% endfor %}==============

Contents:

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   modules
   contributing
   authors
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
{% else -%}
.. include:: ../README.rst
.. include:: ../AUTHORS.rst

==============================
Versions of this Documentation
==============================

.. raw:: html

   <iframe
   src="https://molssi-seamm.github.io/{{ cookiecutter.step }}/dev/versions.html"
   title="Documentation Versions"  style="border:none;">
   </iframe>

.. toctree::
   :hidden:
   :maxdepth: 1
   :titlesonly:

   user/index
   developer/index
   history

.. toctree::
   :hidden:
   :maxdepth: 1
   :titlesonly:

   Main SEAMM documentation <https://molssi-seamm.github.io>
{% endif -%}
