.. _cyclic_executive_pattern:

************************
Cyclic Executive Pattern
************************

Minimalistic thread scheduling for hardware with limited resources (memory).

:Use Cases: The literature states the following use cases for this pattern (Douglass 2002, p. 156).

* small systems
* avionics flight systems

 * aircraft applications
 * spacecraft applications

:Advantages: simple

:Disadvantages: bad responsiveness to incoming events

:Implementaion example: C - Gas flow application with 3 threads (updating the display, controlling a valve, measure gas flow) accessing the same data (configured gas flow, measured gas flow) of a data server (Douglass 2011, chapter 4.2.9).
