# -*- coding: utf-8 -*-
"""The graphical part of a {{ cookiecutter.step }} step"""

import seamm
from seamm_util import ureg, Q_, units_class  # nopep8
import seamm_widgets as sw
import {{ cookiecutter.repo_name }}
import Pmw
import pprint  # noqa: F401
import tkinter as tk
import tkinter.ttk as ttk


class Tk{{ cookiecutter.first_module_name }}(seamm.TkNode):
    """The graphical part of a {{ cookiecutter.step }} step in a flowchart.

    """

    def __init__(
        self,
        tk_flowchart=None,
        node=None,
{%- if cookiecutter.use_subflowchart == 'y' %}
        namespace='org.molssi.seamm.{{cookiecutter.repo_name}}.tk',{%- endif %}
        canvas=None,
        x=None,
        y=None,
        w=200,
        h=50
    ):
        """Initialize a graphical node

        Keyword arguments:
            tk_flowchart: The graphical flowchart that we are in.
            node: The non-graphical node for this step.
            namespace: The stevedore namespace for finding sub-nodes.
            canvas: The Tk canvas to draw on.
            x: The x position of the nodes cetner on the canvas.
            y: The y position of the nodes cetner on the canvas.
            w: The nodes graphical width, in pixels.
            h: The nodes graphical height, in pixels.
        """
{%- if cookiecutter.use_subflowchart == 'y' %}
        self.namespace = namespace
{%- endif %}
        self.dialog = None

        super().__init__(
            tk_flowchart=tk_flowchart,
            node=node,
            canvas=canvas,
            x=x,
            y=y,
            w=w,
            h=h
        )
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

        self.sub_tk_flowchart = seamm.TkFlowchart(
            master=self['frame'],
            flowchart=self.node.sub_flowchart,
            namespace=self.namespace
        )
        self.sub_tk_flowchart.draw()
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
    def update_flowchart(self, tk_flowchart=None, flowchart=None):
        """Update the nongraphical flowchart.

        This is only used in nodes that contain sub-flowcharts
        """

        super().update_flowchart(
            flowchart=self.node.sub_flowchart,
            tk_flowchart=self.sub_tk_flowchart
        )

    def from_flowchart(self, tk_flowchart=None, flowchart=None):
        """Recreate the graphics from the non-graphical flowchart.

        This is only used in nodes that contain sub-flowcharts.
        """

        super().from_flowchart(
            flowchart=self.node.sub_flowchart,
            tk_flowchart=self.sub_tk_flowchart
        )
{%- endif %}

    def handle_help(self):
        """Not implemented yet ... you'll need to fill this out!"""
        print('Help not implemented yet for {{ cookiecutter.step }}!')
