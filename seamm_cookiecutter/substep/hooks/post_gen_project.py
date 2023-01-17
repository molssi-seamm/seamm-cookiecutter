#!/usr/bin/env python

"""
Post Cookie Generation script(s)

These scripts are executed from the output folder.
If any error is raised, the cookie cutter creation fails and crashes
"""

from pathlib import Path


def remove_unneeded_files():
    """Remove files that aren't needed, based on project type."""
    pass


def edit_init_file():
    """Add the needed lines to the __init__ file."""
    src_dir = Path.cwd()
    lines = (src_dir / "__init__.py").read_text().splitlines()

    # Find either the comment or import for versioneer
    for i, line in enumerate(lines):
        if "versioneer" in line or "from ._version" in line:
            break

    new = lines[0:i]
    # Lines to add
    basename = "{{ cookiecutter.substep.lower().replace(' ', '_').replace('-', '_') }}"
    class_name = "{{cookiecutter.class_name}}"
    new.append(f"from .{basename}_step import {class_name}Step  # noqa: F401")
    new.append(f"from .{basename} import {class_name}  # noqa: F401")
    new.append(
        f"from .{basename}_parameters import {class_name}Parameters  # noqa: F401"
    )
    new.append(f"from .tk_{basename} import Tk{class_name}  # noqa: F401")
    new.append("")

    new.extend(lines[i:])
    text = "\n".join(new)
    (src_dir / "__init__.py").write_text(text)


def edit_setup_file():
    """Make needed changes in the setup.py file's entry points."""
    cwd = Path.cwd()
    lines = (cwd / ".." / "setup.py").read_text().splitlines()

    namespace = "org.molssi.seamm.{{ cookiecutter.repository[0:-5] }}"
    tk_namespace = namespace + ".tk"
    class_name = "{{ cookiecutter.class_name }}"
    package = "{{ cookiecutter.repository }}"

    in_entry_points = False
    new = []
    found = False
    for i, line in enumerate(lines):
        new.append(line)
        if "entry_points" in line:
            in_entry_points = True
        if in_entry_points:
            if tk_namespace in line:
                new.append(f"            '{class_name} = {package}:{class_name}Step',")
                found = True
            elif namespace in line:
                new.append(f"            '{class_name} = {package}:{class_name}Step',")
                found = True
            if "}" in line and not found:
                new = new[0:-1]
                new.append(f"        '{namespace}': [")
                new.append(f"            '{class_name} = {package}:{class_name}Step',")
                new.append("        ],")
                new.append(f"        '{tk_namespace}': [")
                new.append(f"            '{class_name} = {package}:{class_name}Step',")
                new.append("        ],")
                new.append("    },")

    text = "\n".join(new)
    (cwd / ".." / "setup.py").write_text(text)


remove_unneeded_files()
edit_init_file()
edit_setup_file()
