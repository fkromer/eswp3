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

Categorization related to the problem category in the architectural
abstraction layer of embedded software (Douglass 2002) may be applied as
follows:

* Subsystem and Component Architecture Patterns

 * Layered Pattern
 * Five-Layer Architecture Pattern
 * Microkernel Architecture Pattern
 * Channel Architecture Pattern
 * Recursive Containment Pattern
 * Hierarchical Control Pattern
 * Virtual Machine Pattern
 * Component-Based Architecture
 * ROOM Pattern

* Concurrency Patterns

 * Concurrency Pattern
 * Message Queuing Pattern
 * Interrupt Pattern
 * Guarded Call Pattern
 * Rendezvous Pattern
 * Cyclic Executive Pattern
 * Round Robin Pattern
 * Static Priority Pattern
 * Dynamic Priority Pattern

* Memory Patterns

 * Memory Management Patterns
 * Static Allocation Pattern
 * Pool Allocation Pattern
 * Fixed Sized Buffer Pattern
 * Smart Pointer Pattern
 * Garbage Collection Pattern
 * Garbage Compactor Pattern

* Resource Patterns

 * Critical Section Pattern
 * Priority Inheritance Pattern
 * Highest Locker Pattern
 * Priority Ceiling Pattern
 * Simultaneous Locking Pattern
 * Ordered Locking Pattern

* Distribution Patterns

 * Shared Memory Pattern
 * Remote Method Call Pattern
 * Observer Pattern
 * Data Bus Pattern
 * Proxy Pattern
 * Broker Pattern

* Safety and Reliability Patterns

 * Protected Single Channel Pattern
 * Homogeneous Redundancy Pattern
 * Triple Modular Redundancy Pattern
 * Heterogeneous Redundancy Pattern
 * Monitor-Actuator Pattern
 * Sanity Check Pattern
 * Watchdog Pattern
 * Safety Executive Pattern

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

About the pattern meta-data
===========================

:Advantages: In comparison with related patterns (e.g. Cyclic Executive Pattern vs. Static Priority Pattern).

:Disadvantages: In comparison with related patterns (e.g. Cyclic Executive Pattern vs. Static Priority Pattern).

:Implementation example: The implementation examples are not limited to the "embedded" domain. It is a good practice to transfer the examples to specific problems in other domains of software engineering.

:Pattern dependences: If the pattern or a specific implementation variant requires the usage of another pattern.

All design patterns in alphabetic order
=======================================

.. toctree::
   :glob:
   :maxdepth: 1

   design_patterns/*
