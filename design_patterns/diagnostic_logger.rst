.. _diagnostic_logger:

*****************
Diagnostic Logger
*****************

:Intend:
 Separates logging from the rest of the application.

:Context:
 

:Problem:
 

:Forces:
 - diagnostic messages must be accesible for whole application
 - consistent look and feel
 - easy to use
 - specification of message destination
 - order of messages
 - specific (context) information
 - retain information from one error to the next

:Solution:
 - diagnostic logger (implemented as singleton) object handles logging
 - handle different output types (cli, file) to subclasses
 - 

:Resulting Context:
 

References:
 
