#!/usr/bin/env python
import os
import subprocess as sp

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def decode_string(string):
    """Helper function to convert byte-string to string, but allows normal strings"""
    try:
        return string.decode()
    except AttributeError:
        return string


def invoke_shell(command):
    try:
        output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
    except sp.CalledProcessError as e:
        # Trap and print the output in a helpful way
        print(decode_string(e.output), decode_string(e.returncode))
        print(e.output)
        raise e
    print(decode_string(output))


def git_init_and_tag():
    """Invoke the initial git and tag with 0.0.0 to make an initial version for Versioneer to ID"""
    # Initialize git
    invoke_shell("git init")
    # Add files
    invoke_shell("git add .")
    invoke_shell(
        "git commit -m \"Initial commit after SEAMM Plugin Cookiecutter creation, version {}\"".format(
            '{{ cookiecutter._plugin_version }}'))
    # Set the 0.0.0 tag
    invoke_shell("git tag 0.0.0")


def remove_windows_ci():
    include_windows = '{{ cookiecutter.Include_Windows_continuous_integration }}'
    if include_windows == "n":
        # Remove with appveyor to be a safe delete
        remove_file("appveyor.yml")


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if 'other' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')

    remove_windows_ci()
    git_init_and_tag()
