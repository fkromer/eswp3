.. _adapter_pattern:

***************
Adapter Pattern
***************

Makes two incompatible interfaces compatible.

:Context:
 - need for functionality which could be achieved by modifying or slightly
   extending preexisting code

:Problem:
 - modifying preexinsting code is not efficient or if provided by a third partiy
   not possible
 - adding "translating" code where ever the existing code is used adds code
   dublication which violates the DRY principle (with all its disadvantages ->
   increased risks for implementation errors, decreased maintainability, etc.)

:Solution:
 - use a component (not neccessarily a class e.g. in strucutral languages) which
   "translates" between preexisting components
 - the adapter compontent needs to implement the expected interface and maps the
   existing interface to it

:Resulting context:
 - preexisting code can be used with a new interface
 - implement the required functionality with less resources consumption (manpower, time, money)
