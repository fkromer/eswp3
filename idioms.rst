.. _idioms:

===========
Idioms in C
===========

Classification of idioms
------------------------

Idioms may be classified according to their scope of optimization (Peterson 2010):

* robustness

 * Array size by division
 * Compound types with {0}
 * Constants to the left
 * Sizeof to variables

* expressiveness

 * Assertion context
 * Magic numbers as variables
 * Named parameters
 * Add the name space

Idioms may be considered in coding style guides for particular programming languages.

Add the name space
------------------

:Problem: The language C does lack the support for name spaces.

:Solution: Add the name of the module (.c file) as prefix to its API funtions.

Constants to the left
---------------------

:Problem: Instead of comparing variables against a value it may be assigned to the variable.

:Solution: The value to be compared against can be placed to the left of the comparison. The compiler does the verification and warns you if applicable.

Magic numbers as variables
--------------------------

:Problem: Magic numbers are bad.

:Solution: Instead of using #defines the handling of magic numbers may increased further by defining constant variables. The tradeoff is memory size against code maintainability.

Namend parameters
-----------------

:Problem:
   C does not support named parameters as language feature.

:Solution: It is possible to emulate this feature by assigning a value to a variable while handed over as function parameter. The readabiliby of the code is increased.

Sizeof to variables
-------------------

:Problem: During the memory assignment of variables the data type of the variable has to correspond to the datatype handed over to the function sizeof(). During code evolution it may occur that not both sides of the assignment are kept redundant.

:Solution: Use the variable itself instead of the data type of the variable as parameter for sizeof().
