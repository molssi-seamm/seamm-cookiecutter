# -*- coding: utf-8 -*-
"""The graphical part of a {{ cookiecutter.step }} step"""

import molssi_workflow
from molssi_workflow import ureg, Q_, units_class  # nopep8
import molssi_util.molssi_widgets as mw
import {{ cookiecutter.project_slug }}
import Pmw
import pprint  # nopep8
import tkinter as tk
import tkinter.ttk as ttk


class Tk{{ cookiecutter.class_name }}(molssi_workflow.TkNode):
    """The graphical part of a {{ cookiecutter.step }} step in a MolSSI flowchart.

    """

    def __init__(self, tk_workflow=None, node=None, canvas=None,
{%- if cookiecutter.use_subflowchart == 'y' %}
                 namespace='org.molssi.workflow.{{cookiecutter.project_slug}}.tk',
{%- endif %}
                 x=None, y=None, w=None, h=None):
        '''Initialize a node

        Keyword arguments:
        '''
{%- if cookiecutter.use_subflowchart == 'y' %}
        self.namespace = namespace
{%- endif %}
        self.dialog = None

        super().__init__(tk_workflow=tk_workflow, node=node,
                         canvas=canvas, x=None, y=None, w=200, h=50)

{%- if cookiecutter.use_subflowchart == 'y' %}
        self.create_dialog()
{%- endif %}

    def create_dialog(self):
        """Create the dialog!"""
        self.dialog = Pmw.Dialog(
            self.toplevel,
            buttons=('OK', 'Help', 'Cancel'),
            defaultbutton='OK',
            master=self.toplevel,
            title='Edit {{ cookiecutter.step }} step',
            command=self.handle_dialog)
        self.dialog.withdraw()

        # The information about widgets is held in self['xxxx'], i.e. this
        # class is in part a dictionary of widgets. This makes accessing
        # the widgets easier and allows loops, etc.

        # Create a frame to hold everything. This is always called 'frame'.
        self['frame'] = ttk.Frame(self.dialog.interior())
        self['frame'].pack(expand=tk.YES, fill=tk.BOTH)

{%- if cookiecutter.use_subflowchart == 'y' %}
        # make it large!
        sw = self.dialog.winfo_screenwidth()
        sh = self.dialog.winfo_screenheight()
        w = int(0.9 * sw)
        h = int(0.8 * sh)
        x = int(0.05 * sw / 2)
        y = int(0.1 * sh / 2)

        self.dialog.geometry('{}x{}+{}+{}'.format(w, h, x, y))

        self.{{ cookiecutter.step_slug }}_tk_workflow = molssi_workflow.TkWorkflow(
            master=frame,
            workflow=self.node.{{ cookiecutter.step_slug }}_workflow,
            namespace=self.namespace
        )
        self.{{ cookiecutter.step_slug }}_tk_workflow.draw()
{%- else %}
        # Shortcut for parameters
        P = self.node.parameters

        # The create the widgets
        for key in P:
            self[key] = P[key].widget(self['frame'])

        # and lay them out
        self.reset_dialog()

    def reset_dialog(self, widget=None):
        """Layout the widgets in the dialog

        This initial function simply lays them out row by rows with
        aligned labels. You may wish a more complicated layout that
        is controlled by values of some of the control parameters.
        """

        # Remove any widgets previously packed
        frame = self['frame']
        for slave in frame.grid_slaves():
            slave.grid_forget()

        # Shortcut for parameters
        P = self.node.parameters

        # keep track of the row in a variable, so that the layout is flexible
        # if e.g. rows are skipped to control such as 'method' here
        row = 0
        widgets = []
        for key in P:
            self[key].grid(row=row, column=0, sticky=tk.EW)
            widgets.append(self[key])
            row += 1

        # Align the labels
        mw.align_labels(widgets)
{%- endif %}

    def right_click(self, event):
        """Probably need to add our dialog...
        """

        super().right_click(event)
        self.popup_menu.add_command(label="Edit..", command=self.edit)

        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)

    def edit(self):
        """Present a dialog for editing the {{ cookiecutter.step }} input
        """
        if self.dialog is None:
            self.create_dialog()

        self.dialog.activate(geometry='centerscreenfirst')

    def handle_dialog(self, result):
        """Handle the closing of the edit dialog

        What to do depends on the button used to close the dialog. If
        the user closes it by clicking the 'x' of the dialog window, 
        None is returned, which we take as equivalent to cancel.
        """
        if result is None or result == 'Cancel':
            self.dialog.deactivate(result)
            return

        if result == 'Help':
            # display help!!!
            return

        if result != "OK":
            self.dialog.deactivate(result)
            raise RuntimeError(
                "Don't recognize dialog result '{}'".format(result))

        self.dialog.deactivate(result)

{%- if cookiecutter.use_subflowchart == 'n' %}
        # Shortcut for parameters
        P = self.node.parameters

        # Get the values for all the widgets. This may be overkill, but
        # it is easy! You can sort out what it all means later, or
        # be a bit more selective.
        for key in P:
            P[key].set_from_widget()
{%- endif %}

{%- if cookiecutter.use_subflowchart == 'y' %}
    def update_workflow(self, tk_workflow=None, workflow=None):
        """Update the nongraphical workflow. Only used in nodes that contain
        workflows"""

        super().update_workflow(
            workflow=self.node.{{ cookiecutter.step_slug }}_workflow,
            tk_workflow=self.{{ cookiecutter.step_slug }}_tk_workflow
        )

    def from_workflow(self, tk_workflow=None, workflow=None):
        """Recreate the graphics from the non-graphical workflow.
        Only used in nodes that contain workflow"""

        super().from_workflow(
            workflow=self.node.{{ cookiecutter.step_slug }}_workflow,
            tk_workflow=self.{{ cookiecutter.step_slug }}_tk_workflow
        )
{%- endif %}

    def handle_help(self):
        """Not implemented yet ... you'll need to fill this out!"""
        print('Help not implemented yet for {{ cookiecutter.step }}!')
