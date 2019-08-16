{% set is_open_source = cookiecutter.license != 'other' -%}
{% for _ in cookiecutter.Step %}={% endfor %}=====
{{ cookiecutter.step }} Step
{% for _ in cookiecutter.step %}={% endfor %}_____

{% if is_open_source %}
.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
   :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

{%- endif %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg
   :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
      :alt: Updates

{% if is_open_source %}
.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name.replace('_', '-') }}/badge/?version=latest
   :target: https://{{ cookiecutter.repo_name.replace('_', '-') }}.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
{%- endif %}


{{ cookiecutter.description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.license }}
* Documentation: https://{{ cookiecutter.repo_name | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `molssi-seamm/cookiecutter-seamm-plugin`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`molssi-seamm/cookiecutter-seamm-plugin`: https://github.com/molssi-seamm/cookiecutter-seamm-plugin

