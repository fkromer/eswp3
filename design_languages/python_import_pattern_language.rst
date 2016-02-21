.. python_import_pattern_language:

==============================
Python Import Pattern Language
==============================

.. graphviz::

   digraph python_import_pattern_language{
      // styling
      size="10";
      
      // node transitions
      pipl -> esci -> ersci;
      esci -> emci;

      // nodes
      pipl [label="Python Import Pattern Language", href="../design_languages/python_import_pattern_language.html#", target="_top"];
      esci [label="Explicite Single Class Import", href="../design_languages/python_import_pattern_language.html#explicite_single_class_import", target="_top"];
      ersci [label="Explicite Renaming Single Class Import"];
      emci [label="Explicite Multi Class Import"];
      emi [label="Explicite Module Import"];
   }

Import Pattern
==============

:Context:
 - need for funtionality which is already available as
   class, method or function defined in another module

:Problem:
 - do not re-invent the wheel

:Solution:
 - `import` at the beginning of the client file

:Resulting Context:
 - imported functionality may be used
 - client code with more or less maintainability

Explicite Single Class Import
=============================

:Context:
 - you need the funtionality of one class defined in another module

:Solution:
 - import with `from <module> import <class>`
 - access with `<instance> = <class>()`
   (Phillips 2010, section **Modules and packages**/page 43)

:Resulting Context:
 - good maintainability (you may locate the class in the other class)
 - editor code completion is available
 - naming conflicts can occur (-> use **Explicit Renaming Single Class Import** instead)

Explicite Renaming Single Class Import
======================================

:Context:
 - you need funtionality of one class whose name is already used in your code

:Solution:
 - import with `from <module> import <class> as <renamed class>`
   (Phillips 2010, section **Modules and packages**/page 44)
 - access with `<instance> = <renamed class>()`

:Resulting Context:
 - no naming conflicts of imported classes

Explicite Multi Class Import
============================

:Context:
 - you need functionality of multiple classes from one module

:Problem:
 - importing with "Single Multi Class Import" may blow up the file
 - if imports are not sorted it is not obvious which classes are
   imported from which module

:Solution:
 - import with `from <module> import <class 1>, <class 2>, <class ...>`
 - access with `<instance 1> = <class 1>()`

:Resulting Context:
 - increased maintainability: obvious which classes are imported
   from the module
 - naming conflicts of imported classes may occur (-> "Explicit Renaming Multi Class Import")

Explicite Module Import
=======================

:Context:
 - you need the functionality of the majority of the classes/functions in a module

:Solution:
 - import with `import <module>`
 - access with `instance = <module>.<class>()`

:Resulting Context:
 - good maintain: obvious where the classes come from
 - better read-ability than "Explicite Multi Class Import"
 - you will probably import something implicitly which you do not need