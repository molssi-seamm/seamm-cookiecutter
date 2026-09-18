{% set is_open_source = cookiecutter.license != 'other' -%}
======{% for _ in cookiecutter.step %}={% endfor %}========
SEAMM {{ cookiecutter.step }} Plug-in
======{% for _ in cookiecutter.step %}={% endfor %}========

.. image:: https://img.shields.io/github/issues-pr-raw/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}
   :target: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/pulls
   :alt: GitHub pull requests

.. image:: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/workflows/CI/badge.svg
   :target: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/actions
   :alt: Build Status

.. image:: https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}
   :alt: Code Coverage

.. image:: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/workflows/CodeQL/badge.svg
   :target: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/security/code-scanning
   :alt: Code Quality

.. image:: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}/workflows/Release/badge.svg
   :target: https://{{ cookiecutter.organization }}.github.io/{{ cookiecutter.repository }}/index.html
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repository }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.repository }}
   :alt: PyPi VERSION

{{ cookiecutter.description }}

{% if is_open_source -%}
* Free software: {{ cookiecutter.license }}
{% else %}
* License: {{ cookiecutter.license }}
{% endif -%}
* Documentation: https://{{ cookiecutter.organization }}.github.io/{{ cookiecutter.repository }}/index.html
* Code: https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.repository }}

Features
--------

* Please edit this section!

Acknowledgements
----------------

This package was created with the `molssi-seamm/cookiecutter-seamm-plugin`_ tool, which
is based on the excellent Cookiecutter_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`molssi-seamm/cookiecutter-seamm-plugin`: https://github.com/molssi-seamm/cookiecutter-seamm-plugin

{% if cookiecutter.organization == "molssi-seamm" -%}
Developed by the Molecular Sciences Software Institute (MolSSI_),
which receives funding from the `National Science Foundation`_ under
award CHE-2136142.

.. _MolSSI: https://molssi.org
.. _`National Science Foundation`: https://www.nsf.gov
{% endif -%}

