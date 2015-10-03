.. _smart_data_pattern:

******************
Smart Data Pattern
******************

Idiomatic pattern implements self-checking data types to satisfy defensive
programming. Adds behavior to the data to ensure that the data’s preconditions
and constraints are adhered to (Douglas 2011, page 359).

:Context:
 Requirements state there shall be implemented "safe" module or class data. Or
 the software does not behave as expected during unit testing and the lack of
 requirements mentioned before has been identified as the root cause.

:Use cases: safety/availability-critical data

:Implementation alternatives in C:
 * functions included from a util module to implement checks
 * #defines included from a util module to implement checks
 * smart data classe per data type (Douglas 2011, chapter "6.4.3 Pattern
   Structure")

:Forces:
 * performance
 * memory usage
 * heap usage
 * testability
 * debugability
 * useability
 * reusability

:Examples in C:
 Self-checking patient data (when initialized and set) encapsulates a smart
 integer data type (weight, age, heart rate, etc.) and a smart enumeration
 data type (patient condition visualization). If a data range is violated the
 corresponding error handler is called (Douglas 2011, chapter "6.4.8
 Examples") 

:Resulting context:
 The unit tests addressing defensive programming issues related to the data
 PASS.
