#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.repository }}` package."""

import pytest  # noqa: F401
import {{ cookiecutter.repository }}  # noqa: F401


def test_construction():
    """Just create an object and test its type."""
    result = {{ cookiecutter.repository }}.{{ cookiecutter.class_name }}()
    assert str(type(result)) == "<class '{{ cookiecutter.repository }}.{{ cookiecutter.repository[0:-5] }}.{{ cookiecutter.class_name }}'>"
