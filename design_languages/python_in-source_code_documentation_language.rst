.. _python_in-source_code_documentation_pattern_language:

****************************************************
Python in-source code documentation pattern language
****************************************************

Automated command line interface documentation
==============================================

:Context:
 - develop an application with command line interface
 - maintain an application with command line interface
 - in-source code documentation is generated with sphinx-doc
 - in-source code documentation may be generated with sphinx-doc

:Problem:
 - manual documentation tend to be outdated

:Solution:
 - [sphinxcontrib.autoprogram](https://pythonhosted.org/sphinxcontrib-autoprogram/)

:Resulting context:
 - CLI documenation is updated with every sphinx-doc

Automated RESTful HTTP API documenation
=======================================

:Context:
 - develop an application with RESTful HTTP application interface
 - maintain an application with RESTful HTTP application interface
 - in-source code documentation is generated with sphinx-doc
 - in-source code documentation may be generated with sphinx-doc

:Problem:
 - manual documentation tend to be outdated

:Solution:
 - [sphinxcontrib.httpdomain](https://pythonhosted.org/sphinxcontrib-httpdomain/)
 - for flask app use [sphinxcontrib.autohttp.flask](https://pythonhosted.org/sphinxcontrib-httpdomain/#module-sphinxcontrib.autohttp.flask)
 - for bottle app use [sphinxcontrib.autohttp.bottle](https://pythonhosted.org/sphinxcontrib-httpdomain/#module-sphinxcontrib.autohttp.bottle)
 - for tornado app use [sphinxcontrib.autohttp.tornado](https://pythonhosted.org/sphinxcontrib-httpdomain/#module-sphinxcontrib.autohttp.tornado)

UML diagram documentation pattern
=================================

:Problem:
 - documentation of UML diagrams tend to be outdated with external tools

:Forces:
 - generation type

  - automated generation from source code (usually just possible for structural diagrams)
  - generation from extension tool syntax

 - supported UML diagram types
 - dependencies to other python modules
 - dependencies to external tools

Automated UML diagram generation pattern
========================================

:Implementation example:
 Generation of UML diagrams with the module
 **pyreverse** https://pypi.python.org/pypi/sphinx-pyreverse

:Resulting context:
 You will have up-to-date documentation of UML diagrams whenever the sphinx-doc
 build is run.

Automated database model diagram generation pattern
===================================================

:Implementation example:
 - Generation of database model diagram with the module **sadisplay**
   https://bitbucket.org/estin/sadisplay/wiki/Home

:Resulting context:
 You will have up-to-date documentation of database model diagrams whenever the
 sphinx-doc build is run.

Inline UML diagram generation pattern
=====================================

:Forces:
 - experience of developers (with tool specific UML description syntax)

:Solution:
 Write the dagrams in tool specific syntax and let sphinx-doc render the output.

:Implementation examples:
 - Diagrams (sequence diagram, usecase diagram, class diagram, activity diagram,
   component diagram, state diagram, deployment diagram, object diagram,
   **wireframe graphical interface = documentation of GUI elements**) generated
   from PlantUML syntax with module **sphinxcontrib-plantuml**
   [https://pypi.python.org/pypi/sphinxcontrib-plantuml].
 - Diagrams from yuml syntax with module **sphinxcontrib-yuml**
   [https://pypi.python.org/pypi/sphinxcontrib-yuml].
 - Diagrams (block, sequence, activity, network) from blockdiag
   [http://blockdiag.com/en/#] syntax with modules **blockdiag**,**seqdiag**,
   **actdiag**, **nwdiag**.

:Resulting context:
 - no need for managing external files
 - easy diffs of versions
 - UML diagrams could outdate, but risk is not as high as with UML diagram file
   embedding pattern

UML diagram file embedding pattern
==================================

:Solution:
 Embed external files of diagrams and let sphinx-doc render the output.

:Implementation example:
 - Embedding of MS visio diagram files into the sphinx-doc documentation with module
   **sphinxcontrib-visio** [https://pypi.python.org/pypi/sphinxcontrib-visio]
 - Embedding of TeX figures with the module **sphinxcontrib-texfigure**
   [https://pypi.python.org/pypi/sphinxcontrib-texfigure].

:Resulting context:
 - external files need to be managed (file names, locations, etc.)

