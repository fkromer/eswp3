.. _sizeof_to_variables:

*******************
Sizeof to variables
*******************

:Problem:
 During the memory assignment of variables the data type of the variable has to
 correspond to the datatype handed over to the function sizeof(). During code
 evolution it may occur that not both sides of the assignment are kept redundant.

:Solution:
 Use the variable itself instead of the data type of the variable as parameter
 for sizeof().
