.. _critical_region_pattern:

***********************
Critical Region Pattern
***********************

Serializing access from tasks on resources to prevent data corruption by disabling task switching.

:Advantages: easy

:Disadvantages: high priority tasks which do not necessarily use the "critical" resource are blocked

:Implementation example: C - A task which manages a robot arm includes the movement of the robot arm as critical region (Douglass 2011, chapter 4.4.8).
