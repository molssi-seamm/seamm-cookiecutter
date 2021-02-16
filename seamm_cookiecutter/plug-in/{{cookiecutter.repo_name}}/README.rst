{% set is_open_source = cookiecutter.license != 'other' -%}
======{% for _ in cookiecutter.step %}={% endfor %}========
SEAMM {{ cookiecutter.step }} Plug-in
======{% for _ in cookiecutter.step %}={% endfor %}========

.. image:: https://img.shields.io/github/issues-pr-raw/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/pulls
   :alt: GitHub pull requests

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/CI/badge.svg
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions
   :alt: Build Status

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: Code Coverage

.. image:: https://img.shields.io/lgtm/grade/python/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/context:python
   :alt: Code Quality

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/Documentation/badge.svg
   :target: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.repo_name }}/index.html
   :alt: Documentation Status

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg
   :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
   :alt: Updates for Dependencies

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
   :alt: PyPi VERSION

A SEAMM plug-in for {{ cookiecutter.description }}

{% if is_open_source -%}
* Free software: {{ cookiecutter.license }}
{% else %}
* License: {{ cookiecutter.license }}
{% endif -%}
* Documentation: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.repo_name }}/index.html
* Code: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

Features
--------

* Please edit this section!

Acknowledgements
----------------

This package was created with Cookiecutter_ and the
`molssi-seamm/cookiecutter-seamm-plugin`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`molssi-seamm/cookiecutter-seamm-plugin`: https://github.com/molssi-seamm/cookiecutter-seamm-plugin

{% if cookiecutter.github_username == "molssi-seamm" -%}
Developed by the Molecular Sciences Software Institute (MolSSI_),
which receives funding from the `National Science Foundation`_ under
award ACI-1547580

.. _MolSSI: https://molssi.org
.. _`National Science Foundation`: https://www.nsf.gov
{% endif -%}

