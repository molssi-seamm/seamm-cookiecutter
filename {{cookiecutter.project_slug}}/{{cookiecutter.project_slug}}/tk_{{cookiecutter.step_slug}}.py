# -*- coding: utf-8 -*-
"""The graphical part of a {{ cookiecutter.step }} step"""

import molssi_workflow
import molssi_util.molssi_widgets as mw
import {{ cookiecutter.project_slug }}
import Pmw
import pprint  # nopep8
import tkinter as tk
import tkinter.ttk as ttk


class Tk{{ cookiecutter.step }}(molssi_workflow.TkNode):
    """The node_class is the class of the 'real' node that this
    class is the Tk graphics partner for
    """

    node_class = {{ cookiecutter.project_slug }}.{{ cookiecutter.step }}

    def __init__(self, tk_workflow=None, node=None, canvas=None,
                 x=None, y=None, w=None, h=None):
        '''Initialize a node

        Keyword arguments:
        '''

        self.dialog = None

        super().__init__(tk_workflow=tk_workflow, node=node,
                         canvas=canvas, x=x, y=y, w=w, h=h)

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

        # self._widget, which is inherited from teh base class, is
        # a place to store the pointers to the widgets so that we can access
        # them later. We'll set up a short hand 'w' just to keep lines short
        w = self._widget
        frame = ttk.Frame(self.dialog.interior())
        frame.pack(expand=tk.YES, fill=tk.BOTH)
        w['frame'] = frame

        # Set the first parameter -- which will be exactly matched
        method_label = ttk.Label(
            frame, text='Example value'
        )
        w['method_label'] = method_label

        method = ttk.Combobox(
            frame, state='readonly', values=['is', 'from variable'],
            justify=tk.RIGHT, width=15
        )
        method.set(self.node.method)
        w['method'] = method

        # Unit entry field for example
        example = mw.UnitEntry(frame, width=15)
        example.set(self.node.example)
        w['example'] = example

        # Variable for example
        example_variable = ttk.Entry(frame, width=15)
        example_variable.insert(0, self.node.example_variable)
        w['example_variable'] = example_variable

        self.reset_dialog()

    def reset_dialog(self, widget=None):
        # set up our shorthand for the widgets
        w = self._widget

        # and get the method, which in this example controls
        # how the widgets are laid out.
        method = w['method'].get()

        # Remove any widgets previously packed
        frame = w['frame']
        for slave in frame.grid_slaves():
            slave.grid_forget()

        # keep track of the row in a variable, so that the layout is flexible
        # if e.g. rows are skipped to control such as 'method' here
        row = 0
        w['method_label'].grid(row=row, column=0, sticky=tk.E)
        w['method'].grid(row=row, column=1, sticky=tk.EW)
        if method == 'is':
            w['example'].grid(row=row, column=2, sticky=tk.W)
        elif 'variable' in method:
            w['example_variable'].grid(row=row, column=1, sticky=tk.W)
        else:
            raise RuntimeError(
                "Don't recognize the method {}".format(method))
        row += 1

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
        if result == 'Cancel':
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

        # set up our shorthand for the widgets
        w = self._widget

        # and get the method, which in this example tells
        # whether to use the value ditrectly or get it from
        # a variable in the workflow
        method = w['method'].get()

        self.node.method = method
        if method == 'is':
            self.node.example = w['example'].get()
        elif 'variable' in method:
            self.node.example_variable = w['example_variable'].get()
        else:
            raise RuntimeError(
                "Don't recognize the method {}".format(method))

    def handle_help(self):
        """Not implemented yet ... you'll need to fill this out!"""
        print('Help!')
