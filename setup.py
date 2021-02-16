# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements_install.txt') as fd:
    requirements = fd.read()

setup(
    name='seamm-cookiecutter',
    version='2021.2.15',
    description='Cookiecutter for SEAMM plug-ins, substeps and forcefields',
    author='Paul Saxe',
    license='BSD',
    author_email='psaxe@molssi.org',
    url='https://github.com/molssi-seamm/cookiecutter-seamm-plugin',
    packages=find_packages(include=['seamm_cookiecutter']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords=['cookiecutter', 'template', 'package', 'SEAMM', 'MolSSI', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    entry_points={
        'console_scripts': [
            'seamm-cookiecutter=seamm_cookiecutter.seamm_cookiecutter:run',
        ],
    },
)
