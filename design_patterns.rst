.. _design_patterns:

***************
Design Patterns
***************

Categorization of design patterns
=================================

Patterns may be categorized according to their intend of optimization and according to their scope of influence regarding the level of abstraction (Gamma et al., chapter „Creational Patterns“ „Structural patterns“ „Behavioral patterns“). Threads can be added as scope of influence (Douglass 2011, 2002).

* creational

 * Abstract Factory
 * Builder
 * Factory Method
 * Singleton
 * Prototype

* structural

 * structural subsystem and component patterns

  * Blackboard
  * Broker
  * Component-based
  * Channel
  * Microkernel
  * Model View Controller
  * Layer
  * Reflection
  * ROOM
  * Pipes and Filters
  * Virtual Machine

 * structural class patterns

  * Adapter

 * structural object patterns

  * Composite

   * Proxy
   * Flyweight
   * Facade
   * Bridge
   * Decorator

* behavioral

 * behavioral thread patterns

  * Critical Region
  * Cyclic Executive
  * Dynamic Priority
  * Guarded Call
  * Ordered Locking
  * Round Robin
  * Static Priority

 * behavioral class patterns

  * Template Method
  * Interpreter

 * behavioral object patterns

  * Chain of Responsibility
  * Command
  * Decomposed AND-State
  * Iterator
  * Mediator
  * Multiple Event Receptor
  * Single Event Receptor
  * State
  * State Table
  * Strategy
  * Observer
  * Visitor

All design patterns in alphabetic order
=======================================

Adapter Pattern
---------------

Makes two incompatible interfaces compatible.

:Implementation example: Python - Abstract but running example of the Adapter Pattern implemented with the internal dictionary of a class instead of the traditional implementation based on inheritance (Kasampalis 2015, chapter "4. The Adapter pattern", subchapter "Implementation").

Abstract Factory Pattern
------------------------

Creates families of related objects without depending on their specific classes.

:Implementaion example: Python - App which lets the user decide weather connect to a website over http, https or ftp to list the directories of the corresponding web server (Zlobin 2013, chapter "The Factory Method Implementation").

:Implementaion example: Python - Creation of a game dependent on the user age for childs ("frog world") or adults ("wizard world"). (Kasampalis 2015, chapter "1. The Factory Pattern", subchapter "Abstract Method", subsubchapter "Implementation").

Builder Pattern
---------------

Composition of a complex object consisting of different parts step by step.

:Implementation example: Python - The configuration of imaginary computers with different configurations points out the differences between the Builder Pattern and the Factory Pattern (Kasampalis 2015, chapter "2. The Builder Pattern", subchapter "Uses cases").

:Implementaion example: Python - Preparing imaginary pizzas with different ingredients but whose preparation follow a common procedure (Kasampalis 2015, chapter "2. The Build Pattern", subchapter "Implementation").

Critical Region Pattern
-----------------------

Serializing access from tasks on resources to prevent data corruption by disabling task switching.

:Advantages: easy

:Disadvantages: high priority tasks which do not necessarily use the "critical" resource are blocked

:Implementation example: C - A task which manages a robot arm includes the movement of the robot arm as critical region (Douglass 2011, chapter 4.4.8).

Cyclic Executive Pattern
------------------------

Minimalistic thread scheduling for hardware with limited resources (memory).

:Use Cases: The literature states the following use cases for this pattern (Douglass 2002, p. 156).

* small systems
* avionics flight systems

 * aircraft applications
 * spacecraft applications

:Advantages: simple

:Disadvantages: bad responsiveness to incoming events

:Implementaion example: C - Gas flow application with 3 threads (updating the display, controlling a valve, measure gas flow) accessing the same data (configured gas flow, measured gas flow) of a data server (Douglass 2011, chapter 4.2.9).

Dynamic Priority Pattern
------------------------

Task scheduling by assignment and update of task priorities during runtime.

Facade Pattern
--------------

:Implementaion example: Python - Access layer to a SQLite database for blog and related post objects (Lott 2014, chapter "Designing an access layer for SQLite").

Factory Method Pattern
----------------------

Defines an interface for creating an instance of an object but lets the class which implements the interface decide which class to instantiate.

Guarded Call Pattern
--------------------
     
Layer Pattern
-------------

Organizes the software components in a hierarchical manner based on their level of abstraction.

Mediator Pattern
----------------

Centralization of the coordination of other components.

Model-View-Controller Pattern
-----------------------------

Separates the application (or part of it) into the parts model (data and logic), view (HMI) and controller (links the model and the view).

Multiple Event Receptor Pattern
-------------------------------

Handling of synchonous events from a single event server using an event receptor for each event (multiple event receptor finite state machine).

Observer Pattern
----------------

Notification of clients about the status of a data server.

Ordered Locking Pattern
-----------------------

Prevention of resource-based deadlock by forcing ordered locking of resources.

Pipes and Filters Pattern
-------------------------
     
Prototype Pattern
-----------------

Creation of an exact copy of an object.

Proxy Pattern
-------------

Standardization of component interface for better maintainability.
Round Robin Pattern
     
Single Event Receptor Pattern
-----------------------------

Handling of asynchronous or synchonous events from a single event server using one event receptor for all events (single event receptor finite state machine).

Singleton Pattern
-----------------

Ensures that only one instance of a class may be created.

State Pattern
-------------

:Implementation example: Python - Emulation of basic operation system process states and transitions using the module "state_machine" (Kasampalis 2015, chapter "Chapter 14. The State Pattern", subchapter "Implementation").

Static Priority Pattern
-----------------------

Task scheduling using priorities.
