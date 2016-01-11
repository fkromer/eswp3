.. classification-tree_method:

**************************
Classification-tree method
**************************

High level informal test design pattern for systematic definition of blackbox tests.

:Context:
 There is no good test basis (specifications, etc.) available to define
 blackbox test cases but the tester has some or good (dependent on the quality
 of the test basis) knowledge of the system under test.

:Problem:
 It is required to verify if a function/method has been called.

:Solution:
 Apply the classification-tree method (CTM). The CTM includes the application of
 the **equivalence partitioning pattern** to define the aspect related classes
 of input values.

:Model example:
 Test cases for software which controls the speed of a car dependent on
 different aspects of the input domain (own speed difference "shall" and "is",
 actual speed, car ahead?, speed difference to car ahead, distance to car
 ahead) are designed (Broekman and Notenboom, section "11.5
 Classification-tree method").

:Resulting Context:
 Blackbox test cases are designed in a strucutured manner with a wide variaty
 of possible # of test cases (minimal ~ # lowest level aspects, maximal ~ # of
 all possible combinations of aspect value classes).
