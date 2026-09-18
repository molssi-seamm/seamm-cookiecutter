================================================================
Phase A -- Subflowchart pattern fixes and pkg_resources sweep
================================================================

Status: in progress -- patches drafted, not yet committed or
released to the cookiecutter repository.

Summary
=======

This phase repairs four interlocking problems in the SEAMM
plug-in cookiecutter, all of which surfaced during xTB plug-in
development and would re-surface for any future subflowchart-based
plug-in (ORCA being the immediate concern).

The four problems and their fixes:

1. **Top-level ``run()`` shape.** The subflowchart branch of the
   generated ``run()`` followed the LAMMPS "build one combined input,
   invoke the binary once" pattern. xTB, FHI-aims, and MOPAC's
   intra-job substeps don't work that way -- each substep invokes the
   binary itself. Fixed by replacing the body with the FHI-aims
   iterate-and-invoke pattern.

2. **Top-level ``_metadata`` assignment.** The generated top-level
   ``__init__`` unconditionally did
   ``self._metadata = <repo>.metadata``. For subflowchart plug-ins,
   ``_metadata`` belongs on the substeps, not the dispatcher. MOPAC's
   ``MOPAC`` class doesn't set ``_metadata`` at all; only its substeps
   (``Energy``, ``Optimization``, ``IR``, ...) do. Fixed by moving
   the ``_metadata`` assignment inside the existing
   ``use_subflowchart != "y"`` branch alongside ``self.parameters``.

3. **Deprecated ``pkg_resources``.** Both ``<repo[0:-5]>.py`` and the
   substep template did
   ``Path(pkg_resources.resource_filename(__name__, "data/"))``. The
   rest of the SEAMM ecosystem migrated to
   ``importlib.resources.files("<package>") / "data"`` in the
   ``2026.3.1`` release (visible in ``seamm_widgets``, ``mopac_step``,
   ``psi4_step``, ``fhi_aims_step``, ``dftbplus_step``, and many
   others). Fixed by switching both files to the same idiom, using
   the explicit package name ``{{ cookiecutter.repository }}`` rather
   than ``__name__`` (which fixes a latent bug in the substep variant
   where ``__name__`` is the substep module, not the plug-in package).

4. **No ``Substep`` base class.** Generated subflowchart plug-ins had
   to duplicate ``version``, ``git_revision``, and ``header``
   properties in every substep, and had no natural home for
   ``input_only`` or ``is_runable``. FHI-aims solves this with a
   hand-rolled ``Substep`` base class. The cookiecutter now generates
   that base class as ``<repo[0:-5]>_substep.py`` when
   ``use_subflowchart == "y"``, and the substep cookiecutter
   subclasses it.

Why these are coupled
=====================

These look like four independent issues but they reinforce each
other:

* Problem 2 (top-level ``_metadata``) and problem 1 (LAMMPS-shaped
  ``run()``) are both symptoms of treating the top-level step as if
  it owned the calculation. Once you accept that for subflowchart
  plug-ins the top level is a dispatcher, both fixes follow.
* Problem 4 (no base class) is what made problems 1 and 2 hard to
  notice -- without a ``Substep`` base, ``is_runable`` doesn't exist
  on substeps, so the iterate-and-invoke pattern can't write
  ``if node.is_runable: node.run()`` cleanly.

Files changed
=============

All paths are relative to the cookiecutter repo root.

``seamm_cookiecutter/plug-in/{{cookiecutter.repository}}/{{cookiecutter.repository}}/{{cookiecutter.repository[0:-5]}}.py``
    The top-level step template. Three edits:

    * Import: ``import pkg_resources`` →
      ``import importlib.resources``.
    * Path: ``Path(pkg_resources.resource_filename(__name__, "data/"))``
      → ``importlib.resources.files("{{ cookiecutter.repository }}") / "data"``.
    * ``__init__``: wrap both ``self._metadata = ...`` and
      ``self.parameters = ...`` in the
      ``{%- if cookiecutter.use_subflowchart != "y" %}`` /
      ``{%- endif %}`` pair (previously only ``self.parameters`` was
      conditional).
    * ``run()`` body rewritten: the subflowchart branch is now the
      FHI-aims iterate-and-invoke loop. ``self.analyze()`` and
      ``self.store_results(...)`` moved inside the non-subflowchart
      branch only (substeps call their own ``analyze()`` from their
      own ``run()``; calling ``self.analyze()`` at the top level
      would double-analyze each substep).

``seamm_cookiecutter/plug-in/{{cookiecutter.repository}}/{{cookiecutter.repository}}/{{cookiecutter.repository[0:-5]}}_substep.py``
    **New file.** Defines a ``Substep(seamm.Node)`` base class.
    Provides:

    * ``__init__`` with ``_input_only`` initialization
    * ``header`` property
    * ``version`` / ``git_revision`` properties
    * ``options`` / ``global_options`` (delegated to the parent step)
    * ``input_only`` getter/setter
    * ``is_runable`` (default True; override to False for input-only
      substeps like a LAMMPS-style Initialization)

    The file is generated only when ``use_subflowchart == "y"``;
    ``post_gen_project.py`` removes it otherwise (symmetric with the
    existing removal of ``<repo[0:-5]>_parameters.py`` in the
    subflowchart case).

``seamm_cookiecutter/plug-in/{{cookiecutter.repository}}/{{cookiecutter.repository}}/__init__.py``
    Adds a conditional ``from .<repo[0:-5]>_substep import Substep``
    inside an ``{%- if cookiecutter.use_subflowchart == "y" %}`` block
    so generated substep modules can subclass
    ``{{ cookiecutter.repository }}.Substep``.

``seamm_cookiecutter/plug-in/hooks/post_gen_project.py``
    Extends ``remove_unneeded_files()`` with an ``else`` branch that
    deletes ``<repo[0:-5]>_substep.py`` when
    ``use_subflowchart == "n"``.

``seamm_cookiecutter/substep/{{cookiecutter.repository}}/{{cookiecutter.substep.lower().replace(...)}}.py``
    The substep template. Four edits:

    * Same ``pkg_resources`` → ``importlib.resources`` import and
      path replacement.
    * Parent class: ``seamm.Node`` →
      ``{{ cookiecutter.repository }}.Substep``.
    * Removes the duplicated ``header``, ``version``, and
      ``git_revision`` properties (now inherited from ``Substep``).

Anything still done? (Things to verify before merging)
======================================================

* The ``import pprint  # noqa: F401`` line stays in the top-level
  template, even though the rewritten ``run()`` no longer uses it.
  This is consistent with the original intent of leaving handy
  imports in place for the developer. It can be removed if desired.
* The ``import sys`` block in the top-level template
  (``{%- if cookiecutter.use_subflowchart == "y" %}``) is still used
  by ``description_text``'s ``sys.exc_info()[0]``, so it stays.
* The new ``Substep`` base class uses ``module=None`` default in
  ``__init__`` (rather than ``__name__``) so subclasses can pass
  their own ``__name__`` through. The current substep template
  already passes ``module=__name__`` explicitly, so the change is
  invisible to generated code; it just makes the base class behave
  sensibly if someone instantiates ``Substep`` directly.
* The substep template still has the
  ``# Add this module's properties to the standard properties``
  block. This is technically redundant -- the top-level plug-in
  module already adds the properties at import time -- but
  ``molsystem.add_properties_from_file`` is idempotent and the block
  matches the pattern in ``psi4_step``'s substep files. Left alone.

Verification
============

Manual smoke test (do this after merging):

1. Run the plug-in cookiecutter with ``use_subflowchart=y`` and a
   plug-in name like ``test_orca``.
2. Confirm that ``test_orca_step/test_orca_substep.py`` exists and
   ``test_orca_step/test_orca_parameters.py`` does NOT exist.
3. Run the plug-in cookiecutter with ``use_subflowchart=n`` and a
   plug-in name like ``test_simple``.
4. Confirm that ``test_simple_step/test_simple_parameters.py`` exists
   and ``test_simple_step/test_simple_substep.py`` does NOT exist.
5. ``cd`` into the subflowchart plug-in, run the substep cookiecutter
   with a substep name like ``Energy``, and confirm the generated
   ``energy.py`` has ``class Energy(test_orca_step.Substep):`` rather
   than ``class Energy(seamm.Node):``.
6. ``python -c "import test_orca_step"`` -- should not raise.
7. ``python -c "import test_simple_step"`` -- should not raise.

Open questions
==============

* Should the cookiecutter HISTORY be updated as part of Phase A
  (proposed entry below), or held until later phases land too?
  Suggested: update it now with a ``2026.5.<n>`` entry covering all
  four fixes, so that any user running ``pip install --upgrade``
  sees what changed.

Proposed HISTORY entry
======================

::

    2026.5.14 -- Subflowchart plug-in template fixes and pkg_resources sweep
        * Rewrote the top-level run() for subflowchart plug-ins to use the
          iterate-and-invoke pattern (each substep invokes the underlying code
          itself). The previous LAMMPS-shaped "build one input, invoke once"
          template was wrong for FHI-aims, xTB, and ORCA-style plug-ins.
        * Fixed the top-level _metadata assignment: it is now only set for
          non-subflowchart plug-ins. For subflowchart plug-ins the substeps own
          _metadata, matching MOPAC's pattern.
        * Added a Substep base class (<repo[0:-5]>_substep.py) for subflowchart
          plug-ins, providing version/git_revision/header/options/input_only/
          is_runable. Substep modules now subclass it instead of seamm.Node.
        * Migrated from deprecated pkg_resources.resource_filename to
          importlib.resources.files in both the top-level and substep
          templates.
