==============================================
2026-05-14 SEAMM Cookiecutter Repair Campaign
==============================================

Goal of v1
==========

The SEAMM Cookiecutter is the entry point for every new plug-in. Recent
plug-in development (xTB; ORCA on the horizon) has surfaced several
patterns in the generated code that are wrong, deprecated, or
mis-shape the responsibilities between the top-level step and its
substeps. The cookiecutter HISTORY has not been updated since
2021-02-17, while the rest of the SEAMM ecosystem moved through
several rounds of internal modernization in 2025-2026 (notably the
``pkg_resources`` → ``importlib.resources`` sweep landing as
``2026.3.1`` in many plug-ins). The cookiecutter has fallen out of
sync.

The goal of this campaign is to bring the cookiecutter back into
alignment with current SEAMM conventions, with a particular focus on
the subflowchart plug-in pattern that is shared by MOPAC, FHI-aims,
xTB, and (soon) ORCA.

Scope and phasing
=================

This campaign is organized in phases. Each phase has its own
``NOTES_<phase>.rst`` document.

Phase A -- Subflowchart pattern fixes and ``pkg_resources`` sweep
-----------------------------------------------------------------

Four problems, all interacting:

1. Top-level ``run()`` for subflowchart plug-ins is templated after
   the LAMMPS pattern (build a single combined input, invoke the
   binary once). This is wrong for codes where each substep invokes
   the binary independently (FHI-aims, xTB, future ORCA). It needs
   the iterate-and-invoke pattern.
2. Top-level ``__init__`` unconditionally sets ``self._metadata``,
   which mis-shapes responsibilities -- for subflowchart plug-ins the
   top level merely dispatches to substeps and should own neither
   ``_metadata`` nor ``parameters``. Substeps own them. This is the
   pattern MOPAC follows.
3. Deprecated ``pkg_resources`` calls in both the top-level and the
   substep templates. The ecosystem migrated to
   ``importlib.resources`` in early 2026.
4. No ``Substep`` base class is generated for subflowchart plug-ins.
   Each generated substep ends up duplicating ``version``,
   ``git_revision``, and ``header`` properties, and has no natural
   home for common attributes like ``input_only`` or ``is_runable``.
   FHI-aims solves this with a hand-rolled ``Substep`` base class;
   the cookiecutter should generate that base class.

See ``NOTES_A.rst`` for the detailed plan, the files changed, and
verification steps.

Phases beyond A
---------------

Not yet planned. Candidates that may surface as phases are kept here
as a parking lot:

* Generator hooks for adding a substep to an existing plug-in
  (currently the substep cookiecutter is separate and the integration
  must be done by hand in ``setup.py``'s ``entry_points``).
* Audit of the GUI template (``tk_*.py``) for the
  ``columnconfigure(0, minsize=w1-w2+30)`` pattern and other
  conditional-widget layout issues.
* Standardizing the ``_calculation`` value casing (substep template
  currently emits ``self._calculation = "{{ cookiecutter.substep }}"``,
  which gives a title-cased string; MOPAC uses lowercase like
  ``"energy"``, ``"optimization"``).
* Modernizing the CI / packaging boilerplate.

Files in this campaign
======================

The phase deliverables live under
``docs/developer_guide/campaigns/2026-05-14/``::

    scope.rst       -- this file
    NOTES_A.rst     -- Phase A: subflowchart fixes and pkg_resources sweep
