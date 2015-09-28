.. _layer_pattern:

*************
Layer Pattern
*************

Organizes the software components in a hierarchical manner based on their level of abstraction.

5-Layer Architecture
--------------------

A variant of the Layer Pattern with 5 components common for embedded and
real-time systems (Douglass 2002, chapter 4.2) is separated into:

* Application,
* User Interface,
* Communication,
* Abstract OS,
* Abstract HW.

The communication is not uni-directional as usual for the "strict" Layer Pattern.

:Model example: C - An ECG monitor is composed of the software components ECG, Alarm, Trend, Data Transport, User Interface (5-tier Pattern) whose communication is not unidirectional "from top to bottom" (Douglass 2002, chapter 4.1.8).

:Model example: C - A ventilator consists of the Ventilator Application, the Graphical User Interface, Communication (CAN, Corba), the RTOS vxWorks and the ventilator hardware abstraction (Douglass 2002, chapter 4.2.8).
