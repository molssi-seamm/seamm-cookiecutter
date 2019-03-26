# -*- coding: utf-8 -*-
"""Helper class needed for the stevedore integration. Needs to provide
a description() method that returns a dict containing a description of
this node, and a factory() method for creating the graphical and non-graphical
nodes."""

import {{cookiecutter.project_slug}}


class {{cookiecutter.class_name}}Step(object):
    my_description = {
        'description':
        'An interface for {{cookiecutter.step}}',
        'group': 'Simulations',
        'name': '{{cookiecutter.step}}'
    }

    def __init__(self, workflow=None, gui=None):
        """Initialize this helper class, which is used by
        the application via stevedore to get information about
        and create node objects for the workflow
        """
        pass

    def description(self):
        """Return a description of what this extension does
        """
        return {{cookiecutter.class_name}}Step.my_description

    def create_node(self, workflow=None, **kwargs):
        """Return the new node object"""
        return {{cookiecutter.project_slug}}.{{cookiecutter.class_name}}(workflow=workflow, **kwargs)

    def create_tk_node(self, canvas=None, **kwargs):
        """Return the graphical Tk node object"""
        return {{cookiecutter.project_slug}}.Tk{{cookiecutter.class_name}}(canvas=canvas, **kwargs)
