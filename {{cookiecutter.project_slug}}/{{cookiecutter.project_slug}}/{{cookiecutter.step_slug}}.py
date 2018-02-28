# -*- coding: utf-8 -*-
"""Non-graphical part of the {{ cookiecutter.step }} step in a MolSSI workflow"""

import molssi_workflow
from molssi_workflow import units, Q_, data  # nopep8
import logging

logger = logging.getLogger(__name__)


class {{ cookiecutter.step }}(molssi_workflow.Node):
    def __init__(self, workflow=None, extension=None):
        '''Setup the non-graphical part of the {{ cookiecutter.step }} step in a
        MolSSI workflow.

        Keyword arguments:
        '''
        logger.debug('Creating {{ cookiecutter.step }} {}'.format(self))

        self.method = 'is'
        self.example = Q_(2, 'angstrom')
        self.example_variable = 'my_variable'

        super().__init__(
            workflow=workflow,
            title='{{ cookiecutter.step }}',
            extension=extension)

    def run(self):
        """Run a {{ cookiecutter.step }} step.
        """

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

        return super().run()
