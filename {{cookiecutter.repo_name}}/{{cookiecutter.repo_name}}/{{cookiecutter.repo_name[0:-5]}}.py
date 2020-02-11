# -*- coding: utf-8 -*-
"""Non-graphical part of the {{ cookiecutter.step }} step in a SEAMM flowchart
"""

import configargparse
import logging
import seamm
from seamm import data  # noqa: F401
from seamm_util import ureg, Q_  # noqa: F401
import seamm_util.printing as printing
from seamm_util.printing import FormattedText as __
import {{ cookiecutter.repo_name }}

#In addition to the normal logger, two logger-like printing facilities are
#defined: 'job' and 'printer'. 'job' send output to the main job.out file for
#the job, and should be used very sparingly, typically to echo what this step
#will do in the initial summary of the job.
#
#'printer' sends output to the file 'step.out' in this steps working
#directory, and is used for all normal output from this step.

logger = logging.getLogger(__name__)
job = printing.getPrinter()
printer = printing.getPrinter('{{ cookiecutter.step }}')


def upcase(string):
    """Return an uppercase version of the string.

    Used for the type argument in argparse
    """
    return string.upper()


class {{ cookiecutter.class_name }}(seamm.Node):
    """
    The non-graphical part of a {{ cookiecutter.step }} step in a flowchart.

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
        The control parameters for {{ cookiecutter.step }}.

    See Also
    --------
    Tk{{ cookiecutter.class_name }},
    {{ cookiecutter.class_name }}, {{ cookiecutter.class_name }}Parameters
    """
    def __init__(self,
                 flowchart=None,
                 title='{{ cookiecutter.step }}',
{%- if cookiecutter.use_subflowchart == 'y' %}
                 namespace='org.molssi.seamm.{{ cookiecutter.repo_name }}',
{%- endif %}
                 extension=None):
        """A step for {{ cookiecutter.step }} in a SEAMM flowchart.

        You may wish to change the title above, which is the string displayed
        in the box representing the step in the flowchart.

        Parameters
        ----------
            flowchart: seamm.Flowchart
                The non-graphical flowchart that contains this step.

            title: str
                The name displayed in the flowchart.
{%- if cookiecutter.use_subflowchart == 'y' %}
            namespace: The namespace for the plugins of the subflowchart

{%- endif %}
            extension: None
                Not yet implemented
        """
        logger.debug('Creating {{ cookiecutter.step }} {}'.format(self))

        # Argument/config parsing
        self.parser = configargparse.ArgParser(
            auto_env_var_prefix='',
            default_config_files=[
                '/etc/seamm/{{ cookiecutter.repo_name }}.ini',
                '/etc/seamm/seamm.ini',
                '~/.seamm/{{ cookiecutter.repo_name }}.ini',
                '~/.seamm/seamm.ini',
            ]
        )

        self.parser.add_argument(
            '--seamm-configfile',
            is_config_file=True,
            default=None,
            help='a configuration file to override others'
        )

        # Options for this plugin
        self.parser.add_argument(
            "--{{ cookiecutter.repo_name.replace('_', '-') }}-log-level",
            default=configargparse.SUPPRESS,
            choices=[
                'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'
            ],
            type=upcase,
            help="the logging level for the {{ cookiecutter.step }} step"
        )

        self.options, self.unknown = self.parser.parse_known_args()

        # Set the logging level for this module if requested
        if '{{ cookiecutter.repo_name }}_log_level' in self.options:
            logger.setLevel(self.options.{{ cookiecutter.repo_name }}_log_level)
        
{%- if cookiecutter.use_subflowchart == 'y' %}
        self.sub_flowchart = seamm.Flowchart(
            parent=self, name='{{ cookiecutter.step }}',
            namespace=namespace)
{%- endif %}

        super().__init__(
            flowchart=flowchart,
            title='{{ cookiecutter.step }}',
            extension=extension)

        self.parameters = {{ cookiecutter.repo_name }}.{{ cookiecutter.class_name }}Parameters()

    @property
    def version(self):
        """The semantic version of this module.
        """
        return {{ cookiecutter.repo_name }}.__version__

    @property
    def git_revision(self):
        """The git version of this module.
        """
        return {{ cookiecutter.repo_name }}.__git_revision__

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
            description : str
                A description of the current step.
        """

        if not P:
            P = self.parameters.values_to_dict()

        text = ('Please replace this with a short summary of the '
                '{{ cookiecutter.step}} step, including key parameters.')

        description = self.header + '\n' + __(text, **P, indent=4 * ' ').__str__()

        return description 

    def run(self):
        """Run a {{ cookiecutter.step }} step. 

        Returns
        -------
        
        next_node : seamm.Node
            The next node object in the flowchart.

        """

        next_node = super().run(printer)

{%- if cookiecutter.use_subflowchart == 'y' %}
        # Get the first real node
        node = self.sub_flowchart.get_node('1').next()

        input_data = []
        while node is not None:
            keywords = node.get_input()
            input_data.append(' '.join(keywords))
            node = node.next()

        files = {'molssi.dat': '\n'.join(input_data)}
        logger.info('molssi.dat:\n' + files['molssi.dat'])

        local = seamm.ExecLocal()
        result = local.run(
            cmd=['{{ cookiecutter.step }}', '-in', 'molssi.dat'],
            files=files,
            return_files=[])

        if result is None:
            logger.error('There was an error running {{ cookiecutter.step }}')
            return None

        logger.debug('\n' + pprint.pformat(result))

        logger.info('stdout:\n' + result['stdout'])
        if result['stderr'] != '':
            logger.warning('stderr:\n' + result['stderr'])
{%- else %}
        # Get the values of the parameters, dereferencing any variables
        P = self.parameters.current_values_to_dict(
            context=seamm.flowchart_variables._data
        )

        # Print what we are doing
        printer.important(__(self.description_text(P), indent=self.indent))

        # Temporary code just to print the parameters. You will need to change
        # this!
        for key in P:
            print('{:>15s} = {}'.format(key, P[key]))
            printer.normal(__(
                '{key:>15s} = {value}', key=key, value=P[key],
                indent=4*' ', wrap=False, dedent=False)
            )
{%- endif %}

        # Analyze the results
        self.analyze()

        return next_node


    def analyze(self, indent='', **kwargs):
        """Do any analysis of the output from this step.

        Also print important results to the local step.out file using
        'printer'.

        Parameters
        ----------
            indent: str
                An extra indentation for the output
        """

{%- if cookiecutter.use_subflowchart == 'y' %}
        # Get the first real node
        node = self.sub_flowchart.get_node('1').next()

        # Loop over the subnodes, asking them to do their analysis
        while node is not None:
            for value in node.description:
                printer.important(value)
                printer.important(' ')

            node.analyze()

            node = node.next()
{%- else %}
        printer.normal(__(
            'This is a placeholder for the results from the '
            '{{ cookiecutter.step }} step', indent=4*' ', wrap=True,
            dedent=False
        ))
{%- endif %}
