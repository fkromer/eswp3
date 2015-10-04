.. has_it_been_called:

******************
Has it been called
******************

Idiomatic pattern to verifiy that a function/method has been called.

:Problem:
 It is required to verify if a function/method has been called.

:Use cases:
 * Common functionality verification
 * error handling functions in safety-critical software

:Solution:
 (a) If the function has no parameters a help variable of the test
 harness may be used and be modified in the stubbed function. (b) If the
 function has input parameters they can be defined as expected values.
