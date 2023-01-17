Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

step
    The name of your code or step in SEAMM, e.g. MOPAC or Polymer
    Builder

use_subflowchart
    Whether this step needs a subflowchart. If the step has an
    internal language, such as LAMMPS or MOPAC has, where the user can
    specify multiple steps, a subflowchart may be appropriate. If,
    however, the code takes a simple input and does one thing you
    propbably shouldn't use a subflowchart.

repo_name
    The name of the GitHub repository, which defaults to the
    lowercased version of the step suffixed with '_step'. This name
    should not have blanks or hyphens ('-'). Use underscores ('_')
    instead.

class_name
    The name of the main class in the module, should be in Camel Case.

github_username
    The GitHub name or the organization where you will put the
    repository. This forms the first part of the full path to the
    GitHub repository, e.g. 'MOLSSI_SEAMM' for MolSSI_SEAMM/seamm

author_name
    Your name or your organization's name, as appropriate. This is
    text for a human to read, e.g. Paul Saxe or the MolSSI.

author_email
    The email of the appropriate contact, either you or the
    responsible person in the organization.

description
    A short description of the project, used as a one-liner in various
    places.

pypi_username
    Your PyPi user name, or the username for the appropriate owner in
    your ogranization.

Options
-------

The following package configuration options set up different features for your project.

dependency_source
    Whether to use Conda for the testing environment, and if so
    whether to prefer conda-forge or the default Anaconda channel for
    dependencies, with a fall back on pip. Otherwise use a Python
    environment and rely on pip for depednecies.

Include_Windows_continuous_integration
    Whether to include CI on Windows using AppVeyor.com

license
    The license to use. Options:

    1. BSD-3-Clause

    2. MIT

    3. GNU General Public License v3+

    4. GNU Lesser General Public License v3+

    5. other
