# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

# Bring up the classes so that they appear to be directly in
# the {{ cookiecutter.project_slug }} package.

from {{ cookiecutter.project_slug }}.{{ cookiecutter.step_slug }} import {{ cookiecutter.step }}  # nopep8
from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.step }}Step  # nopep8
from {{ cookiecutter.project_slug }}.tk_{{ cookiecutter.step_slug }} import Tk{{ cookiecutter.step }}  # nopep8
