.. _add_the_namespace:

*****************
Add the namespace
*****************

Idiomatic pattern emulates the programming feature "namespace" in languages not
offering this feature.

:Context:
 It is not obvious to what modules the functions in use belong to.

:Problem:
 Some programming languages lack the support for name spaces. This makes the
 programms harder maintain.

:Forces:
 * maintainability
 * redability

:Solution:
 Add a short version of the package/module/etc. name as prefix to its API
 funtions.

:Example in C: Add the name of the module (.c file) as prefix to its API funtions.

:Resulting context:
 The maintainability of the modules is increased. The trade-off is that the
 names are longer an the code where the functions are used harder to read.
