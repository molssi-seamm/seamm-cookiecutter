#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""{{ cookiecutter.repo_name }}
A SEAMM plugin for {{ cookiecutter.description }}
"""
import sys
from setuptools import setup, find_packages
import versioneer


# from https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as fd:
    requirements = fd.read()

{%- set license_classifiers = {
    'BSD-3-Clause': 'License :: OSI Approved :: BSD License',
    'MIT': 'License :: OSI Approved :: MIT License',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3+': 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'GNU Lesser General Public License v3+': 'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    'other': 'License :: Other/Proprietary License',
} %}

setup(
    name='{{ cookiecutter.repo_name }}',
    author="{{ cookiecutter.author_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.author_email }}',
    description=__doc__.splitlines()[1],
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
{%- if cookiecutter.license in license_classifiers %}
    license="{{ cookiecutter.license }}",{%- endif %}
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',

    # Which Python importable modules should be included when your package is
    # installed, handled automatically by setuptools. Use 'exclude' to prevent
    # some specific subpackage(s) from being added, if needed
    packages=find_packages(include=['{{ cookiecutter.repo_name }}']),

    # Optional include package data to ship with your package. Customize
    # MANIFEST.in if the general case does not suit your needs. Comment out
    # this line to prevent the files from being packaged with your software
    include_package_data=True,

    # Allows `setup.py test` to work correctly with pytest
    setup_requires=[] + pytest_runner,

    # Required packages, pulls from pip if needed; do not use for Conda
    # deployment
    install_requires=requirements,

    test_suite='tests',

    # Valid platforms your code works on, adjust to your flavor
    platforms=['Linux',
               'Mac OS-X',
               'Unix',
               'Windows'],

    # Manual control if final package is compressible or not, set False to
    # prevent the .egg from being made
    zip_safe=True,

    keywords=['SEAMM', 'SEAMMplugin', 'flowchart'],
    classifiers=[
        'Environment :: Plugins',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
{%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'org.molssi.seamm': [
            '{{ cookiecutter.step }} = {{ cookiecutter.repo_name }}:{{ cookiecutter.class_name }}Step',
        ],
        'org.molssi.seamm.tk': [
            '{{ cookiecutter.step }} = {{ cookiecutter.repo_name }}:{{ cookiecutter.class_name }}Step',
        ],
{%- if cookiecutter.use_subflowchart == 'y' %}
        'org.molssi.seamm.{{ cookiecutter.repo_name[0:-5] }}': [
            # You will need something like the following for substeps
            # Energy = {{ cookiecutter.repo_name }}:EnergyStep
        ],

        'org.molssi.seamm.{{ cookiecutter.repo_name[0:-5] }}.tk': [
            # You will need something like the following for substeps
            # Energy = {{ cookiecutter.repo_name }}:EnergyStep
        ],
{%- endif %}
    }
)
