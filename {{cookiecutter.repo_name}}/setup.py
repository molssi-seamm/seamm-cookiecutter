#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{ cookiecutter.project_slug }}
{{ cookiecutter.project_short_description }}
"""
import sys
from setuptools import setup, find_packages
import versioneer

short_description = __doc__.split("\n")

{%- if cookiecutter.use_pytest == 'y' %}
# from https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

{%- endif %}
with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Pmw>=2.0.1<3',
    'seamm>=0.2.0<1',
    'seamm-widgets>=0.2.1<1',
    'seamm-util>=0.2.1<1',
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'GNU Lesser General Public License v3': 'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    'Not open source': 'License :: Other/Proprietary License',
} %}

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Materials Science',
        'Topic :: Scientific/Engineering :: Computational Materials Science',
        'Topic :: Scientific/Engineering :: Computational Molecular Science',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3  :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    entry_points={
        'org.molssi.workflow': [
            '{{ cookiecutter.step }} = {{ cookiecutter.project_slug }}:{{ cookiecutter.class_name }}Step',
        ],
        'org.molssi.workflow.tk': [
            '{{ cookiecutter.step }} = {{ cookiecutter.project_slug }}:{{ cookiecutter.class_name }}Step',
        ],
    }
)