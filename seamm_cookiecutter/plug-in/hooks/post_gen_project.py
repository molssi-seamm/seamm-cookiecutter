#!/usr/bin/env python

"""
Post Cookie Generation script(s)

These scripts are executed from the output folder.
If any error is raised, the cookie cutter creation fails and crashes
"""

import subprocess as sp


def decode_string(string):
    """Helper function to convert byte-string to string, but allows normal
    strings"""
    try:
        return string.decode()
    except AttributeError:
        return string


def invoke_shell(command, expected_error=True, print_output=True):

    try:
        output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
    except sp.CalledProcessError as e:
        # Trap and print the output in a helpful way
        print(decode_string(e.output), decode_string(e.returncode))
        print(e.output)
        output = e.output
        if not expected_error:
            raise e
    if print_output:
        print(decode_string(output))
    return decode_string(output)


def git_init_and_tag():
    """Invoke the initial git and tag to make an initial version for
    Versioneer to ID if not already in a git repository."""

    # Check if we are in a git repository
    directory_status = invoke_shell(
        "git status", expected_error=True, print_output=False
    )
    # Create a repository and commit if not in one.
    if "fatal" in directory_status:
        # Initialize git
        invoke_shell("git init")

        # Add files created by cookiecutter
        invoke_shell("git add .")
        invoke_shell(
            'git commit -m "Initial commit after SEAMM plugin Cookiecutter '
            "creation, version '{{ cookiecutter._plugin_version }}'\""
        )
        invoke_shell("git branch -m main")

        # Check for a tag
        version = invoke_shell("git tag", expected_error=True)
        # Tag if no tag exists
        if not version:
            invoke_shell("git tag {{ cookiecutter._plugin_version }}")
    else:
        print(
            "\ngit repository detected. CookieCutter files have been created "
            "in {{ cookiecutter.repo_name }} directory."
        )


git_init_and_tag()
