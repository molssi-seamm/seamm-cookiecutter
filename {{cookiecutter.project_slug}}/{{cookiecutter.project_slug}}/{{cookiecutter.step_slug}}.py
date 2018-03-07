# -*- coding: utf-8 -*-
"""Non-graphical part of the {{ cookiecutter.step }} step in a MolSSI workflow"""

import molssi_workflow
from molssi_workflow import units, Q_, data  # nopep8
import logging

logger = logging.getLogger(__name__)


class {{ cookiecutter.step.replace(' ', '') }}(molssi_workflow.Node):
    def __init__(self,
                 workflow=None,
{%- if cookiecutter.use_subflowchart == 'y' %}
                 namespace='org.molssi.workflow.{{ cookiecutter.step_slug }}',
{%- endif %}
                 extension=None):
        '''Setup the non-graphical part of the {{ cookiecutter.step }} step in a
        MolSSI workflow.

        Keyword arguments:
        '''
        logger.debug('Creating {{ cookiecutter.step }} {}'.format(self))

{%- if cookiecutter.use_subflowchart == 'y' %}
        self.{{ cookiecutter.step_slug }}_workflow = molssi_workflow.Workflow(
            parent=self, name='{{ cookiecutter.step }}',
            namespace=namespace)
{%- else %}
        self.method = 'is'
        self.example = Q_(2, 'angstrom')
        self.example_variable = 'my_variable'
{%- endif %}

        super().__init__(
            workflow=workflow,
            title='{{ cookiecutter.step }}',
            extension=extension)

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
        if self.method == 'is':
            print('The example value is {:~P}'.format(self.example))
            logger.info('The example value in {{ cookiecutter.step }} is ' +
                        '{:~P}'.format(self.example))
        elif 'variable' in self.method:
            print('The example value is in the variable {}'.format(
                self.example_variable)
            )
            logger.info('The example value in {{ cookiecutter.step }} is in ' +
                        'the variable {}'.format(self.example_variable))
{%- endif %}

        return super().run()
