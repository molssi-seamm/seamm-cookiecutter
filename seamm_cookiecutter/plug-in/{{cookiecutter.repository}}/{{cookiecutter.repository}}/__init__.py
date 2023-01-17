# -*- coding: utf-8 -*-

"""
{{cookiecutter.repository}}
{{cookiecutter.description}}
"""

# Bring up the classes so that they appear to be directly in
# the {{ cookiecutter.repository }} package.

from .{{ cookiecutter.repository[0:-5] }} import {{ cookiecutter.class_name }}  # noqa: F401, E501
{%- if cookiecutter.use_subflowchart != "y" -%}
from .{{ cookiecutter.repository[0:-5] }}_parameters import {{ cookiecutter.class_name }}Parameters  # noqa: F401, E501
{%- endif %}
from .{{ cookiecutter.repository[0:-5] }}_step import {{ cookiecutter.class_name }}Step  # noqa: F401, E501
from .tk_{{ cookiecutter.repository[0:-5] }} import Tk{{ cookiecutter.class_name }}  # noqa: F401, E501

from .metadata import metadata  # noqa: F401

# Handle versioneer
from ._version import get_versions

__author__ = "{{ cookiecutter.author }}"
__email__ = "{{ cookiecutter.email }}"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
