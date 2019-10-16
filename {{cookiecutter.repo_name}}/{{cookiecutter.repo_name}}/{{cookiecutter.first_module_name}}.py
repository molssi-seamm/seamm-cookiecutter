# -*- coding: utf-8 -*-
"""Non-graphical part of the {{ cookiecutter.step }} step in a SEAMM flowchart

In addition to the normal logger, two logger-like printing facilities are
defined: 'job' and 'printer'. 'job' send output to the main job.out file for
the job, and should be used very sparingly, typically to echo what this step
will do in the initial summary of the job.

'printer' sends output to the file 'step.out' in this steps working
directory, and is used for all normal output from this step.
"""

import logging
import seamm
from seamm import data  # noqa: F401
from seamm_util import ureg, Q_  # noqa: F401
import seamm_util.printing as printing
from seamm_util.printing import FormattedText as __
import {{ cookiecutter.repo_name }}

logger = logging.getLogger(__name__)
job = printing.getPrinter()
printer = printing.getPrinter('{{ cookiecutter.step }}')


class {{ cookiecutter.first_module_name }}(seamm.Node):
    def __init__(self,
                 flowchart=None,
                 title='{{ cookiecutter.step }}',
{%- if cookiecutter.use_subflowchart == 'y' %}
                 namespace='org.molssi.seamm.{{ cookiecutter.step.lower().replace(' ', '_').replace('-', '_') }}',
{%- endif %}
                 extension=None):
        """A step for {{ cookiecutter.step }} in a SEAMM flowchart.

        You may wish to change the title above, which is the string displayed
        in the box representing the step in the flowchart.

        Keyword arguments:
        """
        logger.debug('Creating {{ cookiecutter.step }} {}'.format(self))

{%- if cookiecutter.use_subflowchart == 'y' %}
        self.sub_flowchart = seamm.Flowchart(
            parent=self, name='{{ cookiecutter.step }}',
            namespace=namespace)
{%- endif %}

        super().__init__(
            flowchart=flowchart,
            title='{{ cookiecutter.step }}',
            extension=extension)

        self.parameters = {{ cookiecutter.repo_name }}.{{ cookiecutter.first_module_name }}Parameters()

    def description(self, P):
        """Create the text description of what this step will do.
        The dictionary of control values is passed in as P so that
        the code can test values, etc.

        Keyword arguments:
            P: A dictionary of the current values of the control parameters.
        """

        text = ('Please replace this with a short summary of the '
                '{{ cookiecutter.step}} step, including key parameters.')

        return text

    def describe(self, indent='', json_dict=None):
        """Write out information about what this step will do
        If json_dict is passed in, add information to that dictionary
        so that it can be written out by the controller as appropriate.
        """

        # Call superclasses which will print some information
        next_node = super().describe(indent, json_dict)

        # Local copies of variables in a dictionary
        P = self.parameters.values_to_dict()

        text = self.description_text(P)

        job.job(__(text, **P, indent=self.indent+'    '))

        return next_node

    def run(self):
        """Run a {{ cookiecutter.step }} step.
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
