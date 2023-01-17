# -*- coding: utf-8 -*-

"""Non-graphical part of the {{ cookiecutter.substep }} step in a {{ cookiecutter.step }} flowchart
"""

import logging
from pathlib import Path
import pkg_resources
import pprint  # noqa: F401

import {{ cookiecutter.repository }}
import molsystem
import seamm
from seamm_util import ureg, Q_  # noqa: F401
import seamm_util.printing as printing
from seamm_util.printing import FormattedText as __

# In addition to the normal logger, two logger-like printing facilities are
# defined: "job" and "printer". "job" send output to the main job.out file for
# the job, and should be used very sparingly, typically to echo what this step
# will do in the initial summary of the job.
#
# "printer" sends output to the file "step.out" in this steps working
# directory, and is used for all normal output from this step.

logger = logging.getLogger(__name__)
job = printing.getPrinter()
printer = printing.getPrinter("{{ cookiecutter.step }}")

# Add this module's properties to the standard properties
path = Path(pkg_resources.resource_filename(__name__, "data/"))
csv_file = path / "properties.csv"
if path.exists():
    molsystem.add_properties_from_file(csv_file)


class {{ cookiecutter.class_name }}(seamm.Node):
    """
    The non-graphical part of a {{ cookiecutter.substep }} step in a flowchart.

    Attributes
    ----------
    parser : configargparse.ArgParser
        The parser object.

    options : tuple
        It contains a two item tuple containing the populated namespace and the
        list of remaining argument strings.

    subflowchart : seamm.Flowchart
        A SEAMM Flowchart object that represents a subflowchart, if needed.

    parameters : {{ cookiecutter.class_name }}Parameters
        The control parameters for {{ cookiecutter.substep }}.

    See Also
    --------
    Tk{{ cookiecutter.class_name }},
    {{ cookiecutter.class_name }}, {{ cookiecutter.class_name }}Parameters
    """

    def __init__(
        self,
        flowchart=None,
        title="{{ cookiecutter.substep }}",
        extension=None,
        logger=logger
    ):
        """A substep for {{ cookiecutter.substep }} in a subflowchart for {{ cookiecutter.step }}.

        You may wish to change the title above, which is the string displayed
        in the box representing the step in the flowchart.

        Parameters
        ----------
        flowchart: seamm.Flowchart
            The non-graphical flowchart that contains this step.

        title: str
            The name displayed in the flowchart.
        extension: None
            Not yet implemented
        logger : Logger = logger
            The logger to use and pass to parent classes

        Returns
        -------
        None
        """
        logger.debug(f"Creating {{ cookiecutter.substep }} {self}")

        super().__init__(
            flowchart=flowchart,
            title="{{ cookiecutter.substep }}",
            extension=extension,
            module=__name__,
            logger=logger,
        )  # yapf: disable

        self._calculation = "{{ cookiecutter.substep }}"
        self._model = None
        self._metadata = {{ cookiecutter.repository }}.metadata
        self.parameters = {{ cookiecutter.repository }}.{{ cookiecutter.class_name }}Parameters()

    @property
    def header(self):
        """A printable header for this section of output"""
        return "Step {}: {}".format(".".join(str(e) for e in self._id), self.title)

    @property
    def version(self):
        """The semantic version of this module."""
        return {{ cookiecutter.repository }}.__version__

    @property
    def git_revision(self):
        """The git version of this module."""
        return {{ cookiecutter.repository }}.__git_revision__

    def description_text(self, P=None):
        """Create the text description of what this step will do.
        The dictionary of control values is passed in as P so that
        the code can test values, etc.

        Parameters
        ----------
        P: dict
            An optional dictionary of the current values of the control
            parameters.
        Returns
        -------
        str
            A description of the current step.
        """
        if not P:
            P = self.parameters.values_to_dict()

        text = (
            "Please replace this with a short summary of the "
            "{{ cookiecutter.substep}} step, including key parameters."
        )

        return self.header + "\n" + __(text, **P, indent=4 * " ").__str__()

    def run(self):
        """Run a {{ cookiecutter.substep }} step.

        Parameters
        ----------
        None

        Returns
        -------
        seamm.Node
            The next node object in the flowchart.
        """
        next_node = super().run(printer)

        # Get the values of the parameters, dereferencing any variables
        P = self.parameters.current_values_to_dict(
            context=seamm.flowchart_variables._data
        )

        # Print what we are doing
        printer.important(__(self.description_text(P), indent=self.indent))

        directory = Path(self.directory)
        directory.mkdir(parents=True, exist_ok=True)

        # Get the current system and configuration (ignoring the system...)
        _, configuration = self.get_system_configuration(None)

        # Results data
        # data = {}

        # Temporary code just to print the parameters. You will need to change
        # this!
        for key in P:
            print("{:>15s} = {}".format(key, P[key]))
            printer.normal(
                __(
                    "{key:>15s} = {value}",
                    key=key,
                    value=P[key],
                    indent=4 * " ",
                    wrap=False,
                    dedent=False,
                )
            )

        # Analyze the results
        self.analyze()

        # Add other citations here or in the appropriate place in the code.
        # Add the bibtex to data/references.bib, and add a self.reference.cite
        # similar to the above to actually add the citation to the references.

        return next_node

    def analyze(self, indent="", **kwargs):
        """Do any analysis of the output from this step.

        Also print important results to the local step.out file using
        "printer".

        Parameters
        ----------
        indent: str
            An extra indentation for the output
        """
        printer.normal(
            __(
                "This is a placeholder for the results from the {{ cookiecutter.substep }} step",
                indent=4 * " ",
                wrap=True,
                dedent=False,
            )
        )
