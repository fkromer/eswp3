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

Python common module selection pattern
======================================

:Context:
 You whant to add functionality to a python application and the probability is high that someone else already implemented
 the same functionality.

:Problem:
 Implementing the functionality is often like reinventing the wheel because someone else already implemented
 the functionality
 and deployed it as a python module which may be imported into your project.
 You need to invest time (= money)

:Forces:

 - supported Python versions
 - Python programming experience of people which develop/maintain the application
 - module experience of developers/maintainers

:Solution:
 Find modules

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

