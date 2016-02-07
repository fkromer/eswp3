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
 - define abstract superclasses (parent classes) whose API have to be implemented by
   application classes (child classes)
 - >=python2.6: use the module **collections.abc** from the python standard library
 - <=python2.5 [https://dbader.org/blog/abstract-base-classes-in-python]

   class Base:
       def foo(self):
           raise NotImplementedError()

       def bar(self):
           raise NotImplementedError()


   class Concrete(Base):
       def foo(self):
           return "foo() called"

       # Oh no, we forgot to override `bar()`.
       # def bar(self):
       #     return "bar() called"

   >>> c = Concrete()
   >>> c.foo()
   'foo() called'
   >>> c.bar()
   NotImplementedError


   >>> b = Base()
   >>> b.foo()
   NotImplementedError

   


