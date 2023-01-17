# -*- coding: utf-8 -*-

"""The main module for running the SEAMM cookiecutter.
"""
import argparse
import datetime
import logging
import os.path

from cookiecutter.main import cookiecutter

logging.basicConfig(level=logging.WARNING)


def run():
    # Parse the commandline
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--replay", action="store_true", help="Replay the last installation."
    )
    parser.add_argument(
        "-t",
        "--type",
        action="store",
        choices=["plug-in", "substep", "forcefield"],
        default="plug-in",
        help=(
            "The type of SEAMM object to create, one of %(choices)s.\n"
            "Defaults to %(default)s"
        ),
    )
    options = parser.parse_args()

    curdir = os.path.dirname(os.path.abspath(__file__))

    today = datetime.datetime.today()
    date = today.date().isoformat()
    version = today.strftime("%Y.%-m.%-d")

    extra_context = {"_release_date": date, "_plugin_version": version}

    step_type = options.type
    print(f"Preparing a {step_type}")
    if step_type == "substep":
        overwrite = True
    else:
        overwrite = False

    if options.replay:
        cookiecutter(
            curdir, replay=True, directory=step_type, overwrite_if_exists=overwrite
        )
    else:
        cookiecutter(
            curdir,
            extra_context=extra_context,
            directory=step_type,
            overwrite_if_exists=overwrite
        )


if __file__ == "__main__":
    run
