.. levelized_structure_map:

==============================
Levelized Strucuture Map (LSM)
==============================

:Context:
 - maintaining legacy code of a big project
 - start implementing code for a new project

:Problem:
 - software tends to violate design principles relating code structure
 - not considering design the code maintainability decreases
 - impact analysis (after code changes) is often difficult

:Forces:
 - source code size (the higher, the worse)
 - release cycle frequency (the faster, the worse)

:Solution:
 - use a tool which offers a LSM view of source code
 - verify the LSM continuously in parallel to the code implementation

:Examples for C/C++:
 - Structure101 Studio (depends on Scitools Understand)
 - Coverity Code Advisor (depends on analysis pack "Coverity Architecture Analysis")
 - Scitools Understand

:Resulting Context:
 - easier to understand very big code base
 - identify cyclic dependencies
 - easier to perform impact/dependency analysis ~ code changes
 - continuous use increases the code maintainability
 - continuos use decreased influence of the release cycle frequency on the design quality
 - good/maintainable design may be achieved without design documents which
   is the precondition to succeed in agile processes
 - as the value depends on continuous investigation you whant to integrate it
   into the source code editor or CI process
   (e.g. Structure101 Build + Structure101 WebApp)