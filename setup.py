# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements_install.txt') as fd:
    requirements = fd.read()

setup(
    name='seamm-cookiecutter',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Cookiecutter for SEAMM plug-ins, substeps and forcefields',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
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
