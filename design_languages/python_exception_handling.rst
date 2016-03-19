.. python_exception_handling_language:

==================================
Python Exception Handling Language
==================================

(Philipps 2010, section **4 Expecting the Unexpected**)

.. graphviz::

   digraph python_exception_handling_language{
      // styling
      size="10";

      // 1st to 2nd level node transitions
      ehl -> e;
      e -> becs;
      e -> cec;
      becs -> egfc;
      becs -> cec;
      cec -> seec -> egfc;
      cec -> eec -> iec -> egfc;

      // nodes
      ehl [label="Python Exception Handling Language", href="../design_languages/python_exception_handling.html#python-exception-handling-language", target="_top"];
      e [label="Exception", href="../design_languages/python_exception_handling.html#exception", target="_top"];
      becs [label="Built-in Exception Class Selection", href="../design_languages/python_exception_handling.html#built-in-exception-class-selection", target="_top"];
      cec [label="Customized Exception Class", href="../design_languages/python_exception_handling.html#customized-exception-class", target="_top"];
      seec [label="Self Explaining Exception Class", href="../design_languages/python_exception_handling.html#self-explaining-exception-class", target="_top"];
      iec [label="Intelligent Exception Class", href="../design_languages/python_exception_handling.html#intelligent-exception-class", target="_top"];
      eec [label="Enhanced Exception Class", href="../design_languages/python_exception_handling.html#enhanced-exception-class", target="_top"];
      egfc [label="Exception Guided Flow Control", href="../design_languages/python_exception_handling.html#exception-guided-flow-control", target="_top"];
   }

Exception
=========

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
 - create instances of exception classes in exception conditions

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

:Problem:
 - built-in exceptions do not suite the exception context

:Solution:
 - create error class which inherit from Exception or BaseException
 - just "pass" (in class body)

:Implementation Example:
 Exception class which just "pass" to communicate inalid withdrawals in a
 banking application (Philipps 2010, section **Definig our own extensions**).

:Resulting context:
 - exception context is made obvious by exception class name
 - no implementation and test overhead

Enhanced Exception Class
========================

:Problem:
 - need to pass additional information in form of values instead of string

:Solution:
 - create class with attributes which are set e.g. with __init__(self, <attributes>)

:Resulting context:
 - increased cross-class/module communication capabilities
 - client code may acces exception class attributes -> enhanced exception guided
   flow control

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
 - you raise one or more exceptions in server code
 - client code needs to act dependent on exception occured

:Problem:
 - flow control of application needs to address raised exceptions

:Solution:
 - use the 

:Implementation example:
 Exception communication and exception guided flow control of classes addressing
 authentication and authorization of an web application (Philipps 2010,
 section **Case study**/page 112).

:Resulting Context:
 - no need to explicitly check input parameters
 - inter-class communication of exception related information
