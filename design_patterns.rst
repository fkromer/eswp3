.. _design_patterns:

***************
Design Patterns
***************

Categorization of "design" patterns
===================================

An obvious categorization scheme is **accoring to the level of abstraction** (Buschmann et al. 2001, chapter "The classification schema").

* Architectural
* Design
* Idioms

The literature adds further categorizations **according to the patterns scope of influence regarding the level of abstraction** (Gamma et al.). These schemas apply to the already mentioned architectural and/or design patterns.

* subsystem and component patterns
* class patterns
* object patterns

Patterns may also be categorized **according to their intend of optimization**  (Gamma et al. 1998).

* creational

 * Abstract Factory
 * Builder
 * Factory Method
 * Prototype
 * Singleton

* structural

 * Adapter
 * Bridge
 * Composite
 * Decorator
 * Facade
 * Flyweight
 * Proxy

* behavioral

 * Chain of Responsibility
 * Command
 * Interpreter
 * Iterator
 * Mediator
 * Memento
 * Observer
 * State
 * Strategy
 * Template Method
 * Visitor

Threads may be added as scope of influence to the categorization of behavioral patterns (Douglass 2011, 2002).

 * threads (Douglass 2011, 2002)

It is possible to add the **problem category as another dimension for categorization** which applies to all level of abstractions like (Buschann et al. 2001, chapter "The classification schema") :

* From Mud to Structure
* Distributed Systems
* Interactive Systems
* Adaptable Systems
* Strucutral Decomposition
* Organization of work
* Access Control
* Management
* Communication
* Ressource Handling

In the **context of concurrency and networking** the following schema related to the problem category may be applied (Schmidt et al. 2000, chapter "6.4 Pattern Languages vs. Pattern Systems"):

* Base-line Architecture

 * Architectural

  * Broker
  * Layers
  * Microkernel

* Communication

 * Architectural

  * Pipes and Filters

 * Design

  * Abstract Session
  * Command Processor
  * Forwarder-Receiver
  * Observer
  * Remote Operation
  * Serializer

* Initialization

 * Design

  * Activator
  * Client-Dispatcher-Server
  * Evictor
  * Locator
  * Object Lifetime Manager

* Service Access and Configuration

 * Architecural

  * Interceptor

 * Design

  * Component Configurator
  * Extension Interface
  * Half Object plus Protocol
  * Manager-Agent
  * Proxy

* Event Handling

 * Architectural

  * Proactor
  * Reactor

 * Design

  * Acceptor-Connector
  * Asynchronous Completion Token
  * Event Notification
  * Observer
  * Publisher-Subscriber

* Synchronization

 * Architectural

  * Object Synchronizer

 * Design

  * Balking
  * Code Locking
  * Data Locking
  * Guarded Suspension
  * Double-Checked Locking Optimization
  * Reader/Writer Locking
  * Specific Notification
  * Strategized Locking
  * Thread-Safe Interface

 * (Idioms)

  * (Scoped Locking)

* Concurrency

 * Architectural

  * Half-Sync/Half-Async Producer-Consumer
  * Leader/Followers

 * Design

  * Active Object
  * Master-Slave
  * Monitor Object
  * Producer-Consumer Scheduler
  * Two-phase Termination
  * Thread-Specific Storage

Categorization related to the problem category specific to "(...) a number of subject areas of particular interest to embedded C developers(.)" (Douglass 2011, p. 78) may be applied as follows:

* Design Patterns for Accessing Hardware

 * Hardware Proxy
 * Hardware Adapter
 * Mediator
 * Observer
 * Debouncing
 * Interrupt
 * Polling

* Design Patterns for Embedding Concurrency and Resource Management

 * Scheduling

  * Cyclic Executive
  * Static Priority

 * Task Coordination Patterns

  * Critical Region
  * Guarded Call
  * Queuing
  * Rendevouz

 * Deadlock Avoidance Patterns

  * Simultaneous Locking
  * Ordered Locking

* Design Patterns for State Machines

 * Single Event Receptor
 * Multiple Event Receptor
 * State Table
 * State
 * AND-States
 * Decomposed AND-States

* Safety and Reliability Patterns

 * One's Complement
 * CRC
 * Smart Data
 * Channel
 * Protected Single Channel
 * Dual Channel

An exemplary categorization scheme:

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

Pattern Selection Procedure
===========================

The literature states the following schema to choose an appropriate pattern (Buschmann et al. 2001, chapter "5.3 Pattern Selection"):

* Specify the problem
* Select the pattern category
* Select the problem category
* Compare the problem descriptions
* Compare benefits and liabilities
* Select the variant
* Select an alternative problem category

Legend to the design pattern sections
=====================================

:Advantages: In comparison with related patterns (e.g. Cyclic Executive Pattern vs. Static Priority Pattern).

:Disadvantages: In comparison with related patterns (e.g. Cyclic Executive Pattern vs. Static Priority Pattern).

:Implementation example: The implementation examples are not limited to the "embedded" domain. It is a good practice to transfer the examples to specific problems in other domains of software engineering.

:Pattern dependences: If the pattern or a specific implementation variant requires the usage of another pattern.

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

:Advantages: urgency (Douglass 2002, p.170)

:Disadvantages: criticality (Douglass 2002, p.170)

Task scheduling by assignment and update of task priorities during runtime.

:Implementaion example: C - Three threads (data acquisition, filtering, display) share the same two data sets (raw, processed) (Douglass 2002, chapter 5.10.8).

Facade Pattern
--------------

:Implementaion example: Python - Access layer to a SQLite database for blog and related post objects (Lott 2014, chapter "Designing an access layer for SQLite").

Factory Method Pattern
----------------------

Defines an interface for creating an instance of an object but lets the class which implements the interface decide which class to instantiate.

:Implementaion example: Python - App which lets the user decide weather connect to a website over http or ftp to list the directories of the corresponding web server (Zlobin 2013, chapter "The Factory Method Implementation").

:Implementaion example: Python - Creation of objects for handling the input data in XML format or in JSON format and parsing it correspondingly. (Kasampalis 2015, chapter "1. The Factory Pattern", subchapter "Factory Method", subsubchapter "Implementation").

Guarded Call Pattern
--------------------

:Advantages:
   * better responsiveness (compared to Queueing Pattern)
   * does not interfere with the execution of higher priority tasks that don’t need access to the resource (compared to Critical Region Pattern)

:Disadvantages: if not combined with other patterns the naïve implementation/use can result in unbounded priority inversion

:Implementaion example: C - The attitude and position sensors of an aircraft (data servers) are accessed by a attitude control, a data displayer and a position control (data clients) (Douglass 2011, chapter 4.5.8).

Layer Pattern
-------------

Organizes the software components in a hierarchical manner based on their level of abstraction.

:Variant "5-Layer Architecture":
   A variant of the Layer Pattern with 5 components common for embedded and real-time systems (Douglass 2002, chapter 4.2) is separated into:

* Application,
* User Interface,
* Communication,
* Abstract OS,
* Abstract HW.

The communication is not uni-directional as usual for the "strict" Layer Pattern.

:Model example: C - An ECG monitor is composed of the software components ECG, Alarm, Trend, Data Transport, User Interface (5-tier Pattern) whose communication is not unidirectional "from top to bottom" (Douglass 2002, chapter 4.1.8).

:Model example: C - A ventilator consists of the Ventilator Application, the Graphical User Interface, Communication (CAN, Corba), the RTOS vxWorks and the ventilator hardware abstraction (Douglass 2002, chapter 4.2.8).

Mediator Pattern
----------------

Centralization of the coordination of other components.

:Implementation example: C - Manager (mediator) for the coordination of the subcomponents (rotating joints, sliding joints, etc.) of a robot arm in C (Douglass 2011).

:Implementation example: C++ - Management of the update of Dialog elements (button, list box, entry field) in a graphical user interface (Gamma et al. 1995, chapter „Mediator“).

Model-View-Controller Pattern
-----------------------------

Separates the application (or part of it) into the parts model (data and logic), view (HMI) and controller (links the model and the view).

:Implementation examples: Python - Web interface URL-shortening service implemented with the framework flask which does not support the MVC pattern out-of-the-box (Zlobin 2013, chapter "1. Model-View-Controller", subchapter "Implementation in Python").

Multiple Event Receptor Pattern
-------------------------------

Handling of synchonous events from a single event server using an event receptor for each event (multiple event receptor finite state machine).

:Implementation example: C - Tokenizer for floating point number strings implemented as synchronous state machine with events (digit, white space, dot, end of string) triggered by the client (Douglass 2011, chapter 5.4.8).

Observer Pattern
----------------

Notification of clients about the status of a data server.

:Implementation example: C - Gas data (server) of a gas sensor is observed by a display, gas mixer and a safety monitor (clients) in C (Douglass 2011, chapter 3.5.8).

:Implementation example: C++ - System time (server) is observed by a digital and an analog clock (clients) in C++ (Gamma et al. 1995, chapter "Observer").

Ordered Locking Pattern
-----------------------

Prevention of resource-based deadlock by forcing ordered locking of resources.

:Implementation strageties: This pattern is implemented with one type of resource ID assignment (dynamic or design-time) and one or both types of resource access (dyadic or monadic).

Dynamic resource ID assignment means that IDs are dynamically assigned to resources during runtime.

Design-time resource ID assignment means that IDs are assigned to resources during compile-time.

Dyadic access means that the resource client does explicitly need to lock and unlock the resource.

Monadic access means that the resource client does not need to unlock the resource (implicitly locked and unlocked). 

:Advantages:

* easy (resource ID assignment: dynamic)
* difficult for big systems (resource ID assignment: design-time)
* flexible (access: dyadic)

:Disadvantages:

* unsafe (resource ID assignment: dynamic)
* safe (resource ID assignment: design-time)
* unflexible (access: monadic)

:Implementation example: C - The attitude, velocity and position sensors of an aircraft (data servers) are accessed by a kinematic and a route planing control (data clients) (Douglass 2011, chapter 4.9.8).

Pipes and Filters Pattern
-------------------------
     
Prototype Pattern
-----------------

Creation of an exact copy of an object.

:Implementation example: Python - Creation of information about the second version of a book based on the first version information by using pythons deepcopy functionality copy.deepcopy() (Kasampalis 2015, chapter "3. The Prototype Pattern").

Proxy Pattern
-------------

Standardization of component interface for better maintainability.

:Variant "Hardware Proxy": In the driver layer or HAL the access on hardware is encapsulated in a component.

:Variant "Remote Proxy": In distributed systems software may access neighbor systems as remote "device".

:Variant "Security Proxy": In security applications it may be required to hold all component data within the application in encrypted status. The data representation/format may not be encapsulated within the proxy as usual then.

:Implementation example: C - A motor (hardware) is accessed over an interface independent of the hardware-interface providing the control of speed and direction and monitoring the status (hardware proxy). The hardware is accessed per 16-bit wide memory-mapped interface (Douglass 2011, chapter 3.2.8).

:Implementation example: C++ - An interface for graphical objects (proxy) may be used by the application (client) to access the implementation of a image class (Gamma et al. 1995, chapter „Proxy“).

Round Robin Pattern
-------------------

:Implementation example: C - Two tasks (monitor, display) are scheduled with time-controlled preemption (Douglass 2002, chapter 5.8.8).
     
Single Event Receptor Pattern
-----------------------------

Handling of asynchronous or synchonous events from a single event server using one event receptor for all events (single event receptor finite state machine).

:Pattern dependences:

* Asynchronous version -> Queueing Pattern
* Synchronous version -> Guarded Call Pattern

:Implementation examples: C - Tokenizer for strings holding floating point numbers implemented as asynchronous and as synchronous event handling state machine in C (Douglass 2011, chapter 5.3.8).

Singleton Pattern
-----------------

Ensures that only one instance of a class may be created.

:Variant "Borg singleton": Uses a shared state to ensure that successors of a singleton class are also singletons.

:Implementation example: Python - Abstract but running example of a singleton. (Zlobin 2013, chapter "A classic singleton")

:Implementation example: Python - Borg singleton implements a shared resource (to store images) and a set of URLs which are accessed by 2 threads which fetch images of the URLs and stores them (Zlobin 2013, chapter "2. Creating Only One Object with the Singleton Pattern", subchapter "Implementation in Python")

State Pattern
-------------

:Implementation example: Python - Emulation of basic operation system process states and transitions using the module "state_machine" (Kasampalis 2015, chapter "Chapter 14. The State Pattern", subchapter "Implementation").

Static Priority Pattern
-----------------------

Task scheduling using priorities.

:Advantages:

* simplicity (Douglass 2002, p. 163)
* stability in sense of predictability of failing tasks in an overload situation (Douglass 2002, p. 164)
* optimality, you can’t do better with other scheduling strategies (Douglass 2002, p. 164)
* scale-ability for large amounts of tasks (Douglass 2002, p. 163)
* analyze-ability for schedule-ability e.g. with the standard rate monotonic analysis methods (Douglass 2011, p. 170)
* responsiveness to urgent asynchronous events (Douglass 2002, p. 163)

:Disadvantages: naive implementation with blocking resource sharing can lead to unbounded priority inversion (Douglass 2011, p. 170)

:Model example: C - Three threads (data acquisition, filtering, display) share the same two data sets (raw, processed) (Douglass 2002, chapter 5.9.8).

:Implementation example: C - The motor position sensing, the display of info and the motor control encapsulated in tasks of a RTOS (Douglass 2011, chapter 4.3.8).

