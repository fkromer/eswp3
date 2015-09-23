.. _unit_test_patterns:

******************
Unit Test Patterns
******************

Categorization of unit test patterns
====================================

* whitebox patterns

 * Has it been called
 * Has it not been called

* blackbox patterns

 * In/out range check
 * Inverse data structures

All unit test patterns in alphabetic order
==========================================

In/out range check
------------------

:Problem: The API of a function/method shall be verified.

:Solution: Define the following input values for every input parameter:

* minimal value (related to intended parameter range) - 1
* mid value (related to intended parameter range)
* maximal value (related to intended parameter range) + 1

To every combination of parameter input values a (a) return value or (b) output parameter is expected to have an expected value.

Consider that some programming languages support more than one return parameter (e.g. Python).

Inverse data structures
-----------------------

:Problem: Redundant data structures (variables, structures, etc.) holding
 bit-inverted values during runtime are required in safety-critical contexts.
 It is also required to check the correctness of this data strucutures
 periodically and to call an error handling if the redundance is violated. The
 related if-else structures decrease the code coverage if not considered.

:Solution: Define inverted values as input value for the checking
 functions dependent on the data type of the variable. The value range of
 unsigned data types is 0..(2*n)-1 with n = # bits. So the bit-interted value
 of an e.g. 8-bit unsigned integer (0..255) of 1 is 254. The range of signed
 data types with two's complement representation is -2*(n-1)..0..2*(n-1)-1 wit
 n = # bits. So the bit-inverted value of an e.g. 8-bit signed integer
 (-128,..,-1,0,+1,..,127) of 5 is -6.

Has it been called
------------------

:Problem: It is required to verify if a function/method has been called.

:Use cases: common functionality verification, error handling functions in safety-critical software

:Solution: (a) If the function has no parameters a help variable of the test
 harness may be used and be modified in the stubbed function. (b) If the
 function has input parameters they can be defined as expected values.

Has it not been called
----------------------

:Problem: It is required to verify that a function/method has not been called.

:Use Cases: error handling functions (macros are also very common in C) in safety-critical software

:Solution: Compare the solution of "Has it been called".
