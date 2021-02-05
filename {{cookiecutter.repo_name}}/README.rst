{% set is_open_source = cookiecutter.license != 'other' -%}
{% for _ in cookiecutter.step %}={% endfor %}=====
{{ cookiecutter.step }} Step
{% for _ in cookiecutter.step %}={% endfor %}=====

| |pull| |CI| |docs| |coverage| |lgtm| |PyUp|
| |Release| |PyPi|

{{ cookiecutter.description }}

{% if is_open_source -%}
* Free software: {{ cookiecutter.license }}
{% else %}
* License: {{ cookiecutter.license }}
{% endif -%}
* Documentation: https://molssi-seamm.github.io/{{ cookiecutter.repo_name }}/index.html

.. |pull| image:: https://img.shields.io/github/issues-pr-raw/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/pulls
   :alt: GitHub pull requests

.. |CI| image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/CI/badge.svg
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions?query=workflow%3ACI
   :alt: CI status

.. |docs| image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/Documentation/badge.svg
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions?query=workflow%3ADocumentation
   :alt: Documentation Status

.. |coverage| image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: Code coverage

.. |lgtm| image:: https://img.shields.io/lgtm/grade/python/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/context:python
   :alt: Code Quality

.. |PyUp| image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg
   :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
   :alt: Updates for requirements

.. |Release| image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/Release/badge.svg
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions?query=workflow%3ARelease
   :alt: CI status for releases

.. |PyPi| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
   :alt: Release version

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the
`molssi-seamm/cookiecutter-seamm-plugin`_ project template.

{% if cookiecutter.github_username == "molssi-seamm" -%}
Developed by the Molecular Sciences Software Institute (MolSSI_),
which receives funding from the National Science Foundation under
award ACI-1547580

.. _MolSSI: https://molssi.org
{% endif -%}
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`molssi-seamm/cookiecutter-seamm-plugin`: https://github.com/molssi-seamm/cookiecutter-seamm-plugin

