.. _in_out_range_check:

******************
In/out range check
******************

:Problem:
 The API of a function/method shall be verified.

:Solution:
 Define the following input values for every input parameter:

  * minimal value (related to intended parameter range) - 1
  * mid value (related to intended parameter range)
  * maximal value (related to intended parameter range) + 1

 To every combination of parameter input values a (a) return value or (b) output
 parameter is expected to have an expected value.

 Consider that some programming languages support more than one return parameter
 (e.g. Python).
