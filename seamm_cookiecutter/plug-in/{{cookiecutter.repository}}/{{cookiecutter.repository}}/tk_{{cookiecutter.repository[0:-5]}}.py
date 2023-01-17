# -*- coding: utf-8 -*-

"""The graphical part of a {{ cookiecutter.step }} step"""

import pprint  # noqa: F401

import {{ cookiecutter.repository }}  # noqa: F401
import seamm
from seamm_util import ureg, Q_, units_class  # noqa: F401
{% if cookiecutter.use_subflowchart == "n" -%}
import seamm_widgets as sw
{%- endif %}


class Tk{{ cookiecutter.class_name }}(seamm.TkNode):
    """
    The graphical part of a {{ cookiecutter.step }} step in a flowchart.

    Attributes
    ----------
    tk_flowchart : TkFlowchart = None
        The flowchart that we belong to.
    node : Node = None
        The corresponding node of the non-graphical flowchart
{%- if cookiecutter.use_subflowchart == "n" %}
    namespace : str
        The namespace of the current step.
    tk_subflowchart : TkFlowchart
        A graphical Flowchart representing a subflowchart{%- endif %}
    canvas: tkCanvas = None
        The Tk Canvas to draw on
    dialog : Dialog
        The Pmw dialog object
    x : int = None
        The x-coordinate of the center of the picture of the node
    y : int = None
        The y-coordinate of the center of the picture of the node
    w : int = 200
        The width in pixels of the picture of the node
    h : int = 50
        The height in pixels of the picture of the node
    self[widget] : dict
        A dictionary of tk widgets built using the information
        contained in {{ cookiecutter.step }}_parameters.py

    See Also
    --------
    {{ cookiecutter.class_name }}, Tk{{ cookiecutter.class_name }},
    {{ cookiecutter.class_name }}Parameters,
    """

    def __init__(
        self,
        tk_flowchart=None,
        node=None,
{%- if cookiecutter.use_subflowchart == "y" %}
        namespace="org.molssi.seamm.{{cookiecutter.repository[0:-5]}}.tk",{%- endif %}
        canvas=None,
        x=None,
        y=None,
        w=200,
        h=50,
    ):
        """
        Initialize a graphical node.

        Parameters
        ----------
        tk_flowchart: Tk_Flowchart
            The graphical flowchart that we are in.
        node: Node
            The non-graphical node for this step.
        namespace: str
            The stevedore namespace for finding sub-nodes.
        canvas: Canvas
           The Tk canvas to draw on.
        x: float
            The x position of the nodes center on the canvas.
        y: float
            The y position of the nodes cetner on the canvas.
        w: float
            The nodes graphical width, in pixels.
        h: float
            The nodes graphical height, in pixels.

        Returns
        -------
        None
        """
{%- if cookiecutter.use_subflowchart == "y" %}
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
            h=h,
        )
{%- if cookiecutter.use_subflowchart == "y" %}
        self.create_dialog()
{%- endif %}

    def create_dialog(self):
        """
        Create the dialog. A set of widgets will be chosen by default
        based on what is specified in the {{ cookiecutter.step }}_parameters
        module.

        Parameters
        ----------
        None

        Returns
        -------
        None

        See Also
        --------
        Tk{{ cookiecutter.class_name }}.reset_dialog
        """

        frame = super().create_dialog(title=" {{- cookiecutter.step -}} ")

{%- if cookiecutter.use_subflowchart == "y" %}
        # make it large!
        screen_w = self.dialog.winfo_screenwidth()
        screen_h = self.dialog.winfo_screenheight()
        w = int(0.9 * screen_w)
        h = int(0.8 * screen_h)
        x = int(0.05 * screen_w / 2)
        y = int(0.1 * screen_h / 2)

        self.dialog.geometry(f"{w}x{h}+{x}+{y}")

        self.tk_subflowchart = seamm.TkFlowchart(
            master=frame,
            flowchart=self.node.subflowchart,
            namespace=self.namespace
        )
        self.tk_subflowchart.draw()
{%- else %}
        # Shortcut for parameters
        P = self.node.parameters

        # Then create the widgets
        for key in P:
            if key[0] != "_" and key not in (
                "results",
                "extra keywords",
                "create tables",
            ):
                self[key] = P[key].widget(frame)

        # and lay them out
        self.reset_dialog()

    def reset_dialog(self, widget=None):
        """Layout the widgets in the dialog.

        The widgets are chosen by default from the information in
        {{ cookiecutter.step }}_parameter.

        This function simply lays them out row by row with
        aligned labels. You may wish a more complicated layout that
        is controlled by values of some of the control parameters.
        If so, edit or override this method

        Parameters
        ----------
        widget : Tk Widget = None

        Returns
        -------
        None

        See Also
        --------
        Tk{{ cookiecutter.class_name }}.create_dialog
        """

        # Remove any widgets previously packed
        frame = self["frame"]
        for slave in frame.grid_slaves():
            slave.grid_forget()

        # Shortcut for parameters
        P = self.node.parameters

        # keep track of the row in a variable, so that the layout is flexible
        # if e.g. rows are skipped to control such as "method" here
        row = 0
        widgets = []
        for key in P:
            if key[0] != "_" and key not in (
                "results",
                "extra keywords",
                "create tables",
            ):
                self[key].grid(row=row, column=0, sticky=tk.EW)
                widgets.append(self[key])
                row += 1

        # Align the labels
        sw.align_labels(widgets, sticky=tk.E)

        # Setup the results if there are any
        have_results = (
            "results" in self.node.metadata and len(self.node.metadata["results"]) > 0
        )
        if have_results and "results" in P:
            self.setup_results()
{%- endif %}

    def right_click(self, event):
        """
        Handles the right click event on the node.

        Parameters
        ----------
        event : Tk Event

        Returns
        -------
        None

        See Also
        --------
        Tk{{ cookiecutter.class_name }}.edit
        """

        super().right_click(event)
        self.popup_menu.add_command(label="Edit..", command=self.edit)

        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
