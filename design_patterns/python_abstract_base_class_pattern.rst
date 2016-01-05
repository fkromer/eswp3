.. _python_abstract_base_class_pattern:

**********************************
Python abstract base class pattern
**********************************

:Context:
 You are going to implement a python library which will be used by other
 developers frequently.

:Problem:
 - application classes which do not exactly implement a predefined API chrash
   applications which use these API
 - application classes need to be implement according to pythons built-in
   features to beeing able to integrate seamlessly with python

:Solution:
 - use the module **collections.abc** from the python standard library
 - define abstract superclasses (parent classes) whose API have to be implemented by
   application classes (child classes)

