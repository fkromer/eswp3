.. python_exception_handling_language:

==================================
Python Exception Handling Language
==================================

(Philipps 2010, section **4 Expecting the Unexpected**)

.. graphviz::

   digraph build_automation_language{
      // styling
      size="10";
      

      // 1st to 2nd level node transitions
      eh -> becs;
      eh -> cec;
      becs -> egfc;
      becs -> cec;
      cec -> seec -> egfc;
      cec -> iec -> egfc;

      // nodes
      eh [label="Exception Handling", href="../design_languages/python_exception_handling.html#exception-handling", target="_top"];
      becs [label="Built-in Exception Class Selection", href="../design_languages/python_exception_handling.html#built-in-exception-class-selection", target="_top"];
      cec [label="Customized Exception Class", href="../design_languages/python_exception_handling.html#customized-exception-class", target="_top"];
      seec [label="Self Explaining Exception Class", href="../design_languages/python_exception_handling.html#self-explaining-exception-class", target="_top"];
      iec [label="Intelligent Exception Class", href="../design_languages/python_exception_handling.html#intelligent-exception-class", target="_top"];
      egfc [label="Exception Guided Flow Control", href="../design_languages/python_exception_handling.html#exception-guided-flow-control", target="_top"];
   }

Exception Handling
==================

:Context:
 - develop new application
 - maintenance of legacy application with bad debug-ability
 - maintenance of legacy application with bad logging capabilities
 - maintenance of legacy library/framework with bad useability

:Problem:
 - communication of unusual circumstances/error conditions
 - propagation of error conditions 
 - handling of error conditions without using input parameter checks

:Solution:
 - use the built-in exception handling features (try:, except:, etc.)

:Resulting context:
 - increased debug-ability
 - increased logging capabilities
 - increased useability of libraries/frameworks for client programmers
 - insignificant overhead

Built-in Exception Class Selection
==================================

:Context:
 - problem condition in a function/method needs to be raised with an exception

:Problem:
 - there do exist excptions in the python standard library
 - ... but it is not 

:Resulting context:
 - communicate the exception context 
 - no implementation and test overhead
 - features for customized info available (~ exception class)

Customized Exception Class
==========================

:Context:
 - problem condition in a function/method needs to be raised with an exception

:Problem:
 - no built-in exception suits the the exception context/condition

:Solution:
 - create customized error class which inherit from Exception or BaseException

:Resulting context:
 - increased readablility of error info


Self-Explaining Exception Class
===============================

:Context:
 
:Problem:
 -

:Solution:
 - create error class which inherit from Exception or BaseException
 - just "pass" (in class body)

:Implementation Example:
 Exception class which just "pass" to communicate inalid withdrawals in a
 banking application (Philipps 2010, section **Definig our own extensions**).

:Resulting context:
 - exception context is made obvious by exception class name
 - no implementation and test overhead

Intelligent Exception Class
===========================

:Context:
 - problem condition in a function/method needs to be raised with an exception

:Problem:
 - exception output may/needs to be derived from "input" values

:Implementation Example:
 Exception class with __init__ overriding (balance, amount) "intelligently"
 derived attribute (overage) from it (Philipps 2010,
 section **Definig our own extensions**).

:Resulting context:
 - self-explaining exception name
 - increased maintainability (just assignment of values instead of "info" string)

Exception Guided Flow Control
=============================

:Context:
 

:Problem:
 - flow control of application needs to address raised exceptions

:Solution:
 - use the 

:Resulting Context:
 
