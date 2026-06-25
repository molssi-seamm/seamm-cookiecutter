#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.repo_name }}` package."""

import pytest  # noqa: F401
import {{ cookiecutter.repo_name }}  # noqa: F401


def test_construction():
    """Just create an object and test its type."""
    result = {{ cookiecutter.repo_name }}.{{ cookiecutter.class_name }}()
    assert str(type(result)) == "<class '{{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name[0:-5] }}.{{ cookiecutter.class_name }}'>"
