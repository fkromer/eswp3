.. _static_priority_pattern:

***********************
Static Priority Pattern
***********************

Task scheduling using priorities.

:Advantages:
 * simplicity (Douglass 2002, p. 163)
 * stability in sense of predictability of failing tasks in an overload
   situation (Douglass 2002, p. 164)
 * optimality, you can't do better with other scheduling strategies
   (Douglass 2002, p. 164)
 * scale-ability for large amounts of tasks (Douglass 2002, p. 163)
 * analyze-ability for schedule-ability e.g. with the standard rate monotonic
   analysis methods (Douglass 2011, p. 170)
 * responsiveness to urgent asynchronous events (Douglass 2002, p. 163)

:Disadvantages:
 naive implementation with blocking resource sharing can lead to unbounded
 priority inversion (Douglass 2011, p. 170)

:Model example:
 C - Three threads (data acquisition, filtering, display) share the same two
 data sets (raw, processed) (Douglass 2002, chapter 5.9.8).

:Implementation example:
 C - The motor position sensing, the display of info and the motor control
 encapsulated in tasks of a RTOS (Douglass 2011, chapter 4.3.8).
