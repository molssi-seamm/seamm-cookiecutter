# -*- coding: utf-8 -*-
"""Non-graphical part of the {{ cookiecutter.step }} step in a MolSSI workflow

In addition to the normal logger, two logger-like printing facilities are
defined: 'job' and 'printer'. 'job' send output to the main job.out file for
the job, and should be used very sparingly, typically to echo what this step
will do in the initial summary of the job.

'printer' sends output to the file 'step.out' in this steps working
directory, and is used for all normal output from this step.
"""

import logging
import molssi_workflow
from molssi_workflow import ureg, Q_, data  # nopep8
import molssi_util.printing as printing
from molssi_util.printing import FormattedText as __
import {{ cookiecutter.project_slug }}

logger = logging.getLogger(__name__)
job = printing.getPrinter()
printer = printing.getPrinter('lammps')


class {{ cookiecutter.class_name }}(molssi_workflow.Node):
    def __init__(self,
                 workflow=None,
                 title='{{ cookiecutter.step }}',
{%- if cookiecutter.use_subflowchart == 'y' %}
                 namespace='org.molssi.workflow.{{ cookiecutter.step_slug }}',
{%- endif %}
                 extension=None):
        """A {{ cookiecutter.step }} step in a MolSSI flowchart.

        You may wish to change the title above, which is the string displayed
        in the box representing the step in the flowchart.

        Keyword arguments:
        """
        logger.debug('Creating {{ cookiecutter.step }} {}'.format(self))

{%- if cookiecutter.use_subflowchart == 'y' %}
        self.{{ cookiecutter.step_slug }}_workflow = molssi_workflow.Workflow(
            parent=self, name='{{ cookiecutter.step }}',
            namespace=namespace)
{%- endif %}

        super().__init__(
            workflow=workflow,
            title='{{ cookiecutter.step }}',
            extension=extension)

        self.parameters = {{ cookiecutter.project_slug }}.{{ cookiecutter.class_name }}_Parameters()

    def description_text(self, P):
        """Create the text description of what this step will do.
        The dictionary of control values is passed in as P so that
        the code can test values, etc.
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
        next_node = super().describe()

        # Local copies of variables in a dictionary
        P = self.parameters.values_to_dict()

        text = self.description_text(P)

        job.job(__(text, indent=self.indent+'    ', **P))

        return next_node

    def run(self):
        """Run a {{ cookiecutter.step }} step.
        """

{%- if cookiecutter.use_subflowchart == 'y' %}
        # Get the first real node
        node = self.{{ cookiecutter.step_slug }}_workflow.get_node('1').next()

        input_data = []
        while node is not None:
            keywords = node.get_input()
            input_data.append(' '.join(keywords))
            node = node.next()

        files = {'molssi.dat': '\n'.join(input_data)}
        logger.info('molssi.dat:\n' + files['molssi.dat'])

        local = molssi_workflow.ExecLocal()
        result = local.run(
            cmd=['{{ cookiecutter.step_slug }}', '-in', 'molssi.dat'],  # nopep8
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
        # Temporary code just to print the parameters. You will need to change
        # this!
        P = self.parameters
        for key in P:
            print('{:>15s} = {}'.format(key, P[key]))
            printer.normal(__(
                '{key:>15s} = {value}', key=key, value=P[key],
                indent=4*' ', wrap=False, dedent=False)
            )
{%- endif %}

        return super().run()


    def analyze(self, indent='', **kwargs):
        """Do any analysis needed for this step, and print important results
        to the local step.out file using 'printer'
        """

        printer.normal(__(
            'This is a placeholder for the results form step '
            '{{ cookiecutter.step }}', indent=4*' ', wrap=True,
            dedent=False
        ))
