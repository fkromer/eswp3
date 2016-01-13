.. python_module_selection_language:

****************************************
Python Module Selection Pattern Language
****************************************

.. graphviz::

   digraph python_module_selection_pattern_language{
   // styling
   size="11";
   node [color=lightblue2, style=filled];

   // node transitions
   pmspl -> pcmsp;
   pmspl -> pbmsp;

   // nodes 
   pmspl [label="Python Module Selection Pattern Lanugage"];
   pcmsp [label="Python Common Module Selection Pattern"];
   pbmsp [label="Python Build Module Selection Pattern"];
   }

.. python_common_selection_pattern:

Python Common Module Selection Pattern
======================================

:Context:
 You whant to add functionality to a python application and the probability is
 high that someone else already implemented the same functionality.

:Problem:
 Implementing the functionality is often like reinventing the wheel because
 someone else already implemented the functionality and deployed it as a python
 module which may be imported into your project. If you whant to implement it
 stable regarding future maintenance and imrovement you need to invest a lot of
 time = money (CI environment for deployment, testing with different).

:Forces:

 - supported Python versions
 - supported dependent-on Python package
 - supported dependent-on Python package versions
 - application developer/maintainer experience with Python
 - module experience of developers/maintainers
 - package "source" quality (official repository?)
 - maintainance quality (updates/time, # contributors to the project,
   downloads/time, issues/time, response time to issues, age of the project)

:Solution:
 - search modules in "trusted sources" [e.g. https://pypi.python.org]

:Resulting context:

 - if suiteable package found: be happy :)
 - if no suiteable package found at all you need to implement it:
  - "private" project
  - "public"/open source project (github.com, bitbucket.com, ...)
 - if familiar package found you may extend it:
  - "private" extended project: "fork" it and add features do not push to public
  - contribute to public project: same advantages like implementing it 

.. python_static_code_analysis_module_selection_pattern:

Python Static Code Analysis Module Pattern
==========================================

:Context:
 - high reliability application
 - application in the context of safety critical systems (build process)
 - library implementation

:Problem:
 - ensuring code quality manually without tool support is impossible
 - static code quality may influence the reliability (which may not always been
   tested using unit test, integration test and acceptance test tools)
 - static code quality influences design related quality attributes like
   maintainability, etc. (non-functional requirements)

:Forces:
 - code analysis features
  - file based configuration (for separate versioning ~ configuration management)
  - programming "errors"
  - code style (PEP8)
 - integration with existing develop infrastructure (ADEs, IDEs, ...)
 - integration with existing CI infrastructure (integration of report output into documentation or agile "dashboard")

:Solution:
 Evaluate the currently available python modules regarding the forces.
 
 - pylint (wide range of checks) [http://www.pylint.org/]
 - PyFlakes (limited checks, no style checking, all python versions supported) [https://pypi.python.org/pypi/pyflakes]
 - PyChecker (outdated!) [https://pypi.python.org/pypi/PyChecker]
 - pep8 (only style guide) [https://pypi.python.org/pypi/pep8]

:Resulting context:
 - run static code analysis on projects per cli
 - prerequisite to integrate static analysis into CI environment

.. python_build_module_selection_pattern:

Python Build Module Selection Pattern
=====================================

:Context:
 You are setting up a new project or you already begun a new project.
 Having already a project you either do not have a build concept
 or you are unsatisfied with your current concept. You have already
 applied the "Python Module Selection Pattern".

:Problem:
 If the build process of the python application is not automated
 you will miss important steps required to ensure a high quality
 deployment for sure.

:Forces:

 - build features

:Solution:
 Evaluate the currently available python modules regarding the forces.
 The following modules are adressing relevant functionalities:

 - paver (build/distribute/deploy) [http://pythonhosted.org/Paver/]
 - Invoke (build/distribute/deploy) [http://www.pyinvoke.org/]
 - SCons (build) [http://www.scons.org/]

:Resulting context:
 You can easily build, distribute and deploy your application running tasks
 (equal to make targets). Using one or several modules you are able to
 implement continuous integration up to continuous deployment.

Python Distribution Module Selection Pattern
============================================

:Forces:

 - distribute features

:Implementation:

 - distutils


Python Deploy Module Selection Pattern
======================================

:Forces:

 - deploy features

:Solution:

 - Fabric (deploy) [http://www.fabfile.org/]

