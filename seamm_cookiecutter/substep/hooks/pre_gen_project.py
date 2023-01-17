"""
Pre Cookie Generation script(s)

If any error is raised, the cookie cutter creation fails and crashes
"""

from pathlib import Path
import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
CLASS_REGEX = r"^[a-zA-Z][a-zA-Z0-9]*$"

repository = "{{ cookiecutter.repository }}"
class_name = "{{ cookiecutter.class_name }}"

cwd = Path.cwd()
if cwd.name != repository or cwd.parent.name != repository:
    print(f"Do not appear to be running in the correct repository ({repository}).")
    print(f"  Current directory is {cwd.parent}")
    sys.exit(1)

if not re.match(MODULE_REGEX, repository):
    print(key, re.match(MODULE_REGEX, key))
    print('ERROR: "{}", the repo name, is not a valid Python module name!'.format(key))

    # exits with status 1 to indicate failure
    sys.exit(1)

if not re.match(CLASS_REGEX, class_name):
    print(key, re.match(CLASS_REGEX, key))
    print('ERROR: "{}", the class name, is not a valid Python class name!'.format(key))

    # exits with status 1 to indicate failure
    sys.exit(1)
