.. dependency_structure_matrix:

===========================
Dependency Structure Matrix
===========================

:Category:
 - architecture development environment (ADE)

:Context:
 - you are interested in invalid dependencies in source code

:Problem:
 - looking at source code using an editor or IDEs gives you just a limited view
   about the overall code structure
 - -> it is hard to understand the overall functionality of source code
 - -> invalid dependencies may not be found methodological

:Solution:
 - use a tool which provides this functionality
 - write your own tool

:Examples for C/C++:
 - Lattix (depends on Scitools Understand for C++)
 - CppDepend

:Resulting context:
 - you have an overview over inter-module dependencies
 - violations geometric 