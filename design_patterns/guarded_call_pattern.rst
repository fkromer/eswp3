.. _guarded_call_pattern:

********************
Guarded Call Pattern
********************

:Advantages:
   * better responsiveness (compared to Queueing Pattern)
   * does not interfere with the execution of higher priority tasks that don’t need access to the resource (compared to Critical Region Pattern)

:Disadvantages: if not combined with other patterns the naïve implementation/use can result in unbounded priority inversion

:Implementaion example: C - The attitude and position sensors of an aircraft (data servers) are accessed by a attitude control, a data displayer and a position control (data clients) (Douglass 2011, chapter 4.5.8).
