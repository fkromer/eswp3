.. function_wrapped_macro_pattern:

******************************
Function wrapped macro pattern
******************************

:Context:
 You need to implement time critical functionality or functionality related to
 hardware access in safety-critical software.

:Forces:
 - complexity of functionality
 - where does the funtionality need to be called?
 - execution time
 - stack consumption

:Problem:
 In some situations (e.g. time critical functionality) it is required to
 implement functionality as defines/macros which are "resolved" (inserted as "string")
 at compile time. If macros are called directly from within the UUTs this lead
 to trouble during whitebox unit testing: To beeing able to access every function
 path it is required to manipulate the macros "output" (return, manipulation of
 global data, e.g.). In other cases it is required to spy the macros input
 parameters. In all cases for every combination of the macro "manipulation" there
 needs to be compiled a different test harness which increases the unit test
 maintenance effort. 

Solution:
 Implement a function for every macro as wrapper.

:Resulting context:
 - additional function call increases stack usage (slightly)
 - additional function call increases execution time (influence ~ complexity of
   macro functionality)
 - macro needs to be tested
