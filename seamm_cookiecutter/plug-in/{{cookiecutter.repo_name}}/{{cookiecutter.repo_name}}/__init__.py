# -*- coding: utf-8 -*-

"""
{{cookiecutter.repo_name}}
{{cookiecutter.description}}
"""

# Bring up the classes so that they appear to be directly in
# the {{ cookiecutter.repo_name }} package.

from {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name[0:-5] }} import {{ cookiecutter.class_name }}  # noqa: F401, E501
from {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name[0:-5] }}_parameters import {{ cookiecutter.class_name }}Parameters  # noqa: F401, E501
from {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name[0:-5] }}_step import {{ cookiecutter.class_name }}Step  # noqa: F401, E501
from {{ cookiecutter.repo_name }}.tk_{{ cookiecutter.repo_name[0:-5] }} import Tk{{ cookiecutter.class_name }}  # noqa: F401, E501

# Handle versioneer
from ._version import get_versions

__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
