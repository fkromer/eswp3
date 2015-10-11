.. _unit_test_patterns:

******************
Unit Test Patterns
******************

If and how the patterns may be applied in your actual situation strongly
depend on the unit test tool which is used. In the context of safety-critical
software it is common to use full-feature unit test tools. In this case you
do not have to worry about a lot of the problems which are addressed by
some unit test pattern categories related to "manage the test harness
yourself" test frameworks (e.g. xUnit Basics Patterns, Test
Organization Patterns). As "non-open-source" unit test tools in C/C++ implement
the "Test Automation Framework" unit test pattern some Unit Test Patterns
could be already implemented by the tool:

 * Assertion Method
 * Automated Teardown
 * Chained Tests
 * Configurable Test Double
 * Creation Method
 * Data-Driven Test
 * Delegated Setup
 * Delta Assertion
 * Implicit Setup
 * Implicit Teardown
 * In-line Setup
 * In-line Teardown
 * Prebuilt Fixture
 * Scripted Test
 * Standard Fixture
 * Test Discovery
 * Test Double
 * Test Runner
 * Test Selection
 * Testcase Object
 * Unfinished Test Assertion

The basics for the functionality of the following patterns are implemented by most "non-open source" unit test tools for C but some implementation work is left to the tester:

 * Behavior Verification
 * Derived Value
 * Fake Object

However it may be hard or even possible that some patterns can not be
implemented with full-fledged test frameworks due to their architecture:

 * Lazy Setup
 * Minimal Fixture
 * Mock Object
 * Testcase Class (~ C++)
 * Testcase Class per Class (~ C++)
 * Testcase Class per Feature (~ C++)
 * Testcase Class per Fixture (~ C++)
 * Testcase Superclass (~ C++)

In the safety/availability-critical contexts some patterns are not appliable
because the production code may be not modified before, during or after test
execution:

 * Test Hook
 * 

Beside of this "i do not have to care about the
pattern implementation" it is important to know the patterns to get an idea
about the tool in use can be used as efficient as possible. However some
pattern categories may be relevant independent of the tool in use and the
business domain (e.g. Value Patterns).

Categorization of unit test patterns
====================================

According to the problem context one can categorize unit test patterns like
follows (Meszaros 2007, chapter "Contents").

* Test Strategy Patterns

 * recorded test
 * scripted test
 * data-driven test
 * test automation framework
 * minimal fixture
 * standard fixture
 * fresh fixture
 * shared fixture
 * back dooor manipulation
 * layer test

xUnit Basics Patterns

 * test method
 * four-phase test
 * assertion method
 * assertion message
 * testcase class
 * test runner
 * testcase object
 * test suite object
 * test discovery
 * test enumeration
 * test selection

* Fixture Setup Patterns

 * in-line setup
 * delegated setup
 * creation method
 * implicit setup
 * prebuilt fixture
 * lazy setup
 * suite fixture setup
 * setup decorator
 * chained tests

* Result Verification Patterns

 * State verification
 * Behaviour verification
 * custom assertion
 * delta assertion
 * guard assertion
 * unfinished test assertion

* Fixture Teardown Patterns

 * garbage-collected teardown
 * automated teardown
 * in-line teardown
 * implicit teardown

* Test Double Patterns

 * test double
 * test stub
 * test spy
 * mock object
 * fake object
 * configurable test double
 * hard-coded test double
 * test-specific subclass

* Test Organization Patterns

 * named test suite
 * test utility method
 * parameterized test
 * testcase class per class
 * testcase class per feature
 * testcase superclass

* Database Patterns

 * database sandbox
 * stored procedure test
 * table truncation teardown
 * transaction rollback teardown

* Design-For-Testability Patterns

 * dependency injection
 * dependency lookup
 * humble object
 * test hook

* Value Patterns

 * Literal Value
 * Derived Value
 * Generated Value
 * Dummy Object

Value Patterns may be categorized further regarding the unit test context:

* whitebox patterns

 * Has it been called
 * Has it not been called

* blackbox patterns

 * In/out range check
 * Inverse data structures

About the meta-data
===================

Equivalent to other (code) smells indicating bad practice there also some smells
aka "Unit Test Antipatterns" related to unit tests
(Meszaros 2007, chapter "Contents"). Whenever one of the following smell occurs
the design of the unit test should be refactored.

* Code Smells

 * obscure test
 * conditional test logic
 * hard-to-test code
 * test code duplication
 * test logic in production

* Behavior Smells

 * assertion roulette
 * erratic test
 * fragile test
 * frequent debugging
 * manual intervention
 * slow tests

* project smells

 * buggy tests
 * developers not writing tests
 * high test maintenance cost
 * production bugs

However because this project is solution-oriented and not problem-oriented this
antipatterns will only be referenced as implicit meta-data in the **Problem**
section.

All unit test patterns in alphabetic order
==========================================

.. toctree::
   :glob:
   :maxdepth: 1

   unit_test_patterns/*

Assertion Message
 We include a descriptive string argument in each call to an Assertion Method
 (Meszaros 2007, page 370).

Assertion Method
 We call a utility method to evaluate whether an expected outcome has been 
 achieved (Meszaros 2007, page 362).

Automated Teardown
 We keep track of all resources that are created in a test and automatically
 destroy/free them during teardown (Meszaros 2007, page 503).

Back Door Manipulation
 We set up the test fi xture or verify the outcome by going through a back
 door (such as direct database access) (Meszaros 2007, page 327).

Behavior Verification
 We capture the indirect outputs of the system under test (SUT) as they occur
 and compare them to the expected behavior (Meszaros 2007, page 468).

Chained Tests
 We let the other tests in a test suite set up the test fixture
 (Meszaros 2007, page 454).

Configurable Test Double
 We configure a reusable Test Double with the values to be returned or
 verified during the fixture setup phase of a test (Meszaros 2007, page 558).

Creation Method
 We set up the test fi xture by calling methods that hide the mechanics of
 building ready-to-use objects behind Intent-Revealing Names
 (Meszaros 2007, page 415).

Custom Assertion
 We create a purpose-built Assertion Method that compares only those
 attributes of the object that define test-specific equality
 (Meszaros 2007, page 474).

Data-Driven Test
 We store all the information needed for each test in a data file and write
 an interpreter that reads the file and executes the tests
 (Meszaros 2007, page 288).

Database Sandbox
 We provide a separate test database for each developer or tester
 (Meszaros 2007, page 650).

Delegated Setup
 Each test creates its own Fresh Fixture by calling Creation Methods from
 within the Test Methods (Meszaros 2007, page 411).

Delta Assertion
 We specify assertions based on differences between the pre- and
 post-exercise state of the SUT (Meszaros 2007, page 485).

Dependency Injection
 The client provides the depended-on object to the SUT
 (Meszaros 2007, page 678).

Dependency Lookup
 The SUT asks another object to return the depended-on object before it uses
 it (Meszaros 2007, page 686).

Derived Value
 We use expressions to calculate values that can be derived from other values
 (Meszaros 2007, page 718).

Dummy Object
 We pass an object that has no implementation as an argument of a method
 called on the SUT (Meszaros 2007, page 728).

Fake Object
 We replace a component that the SUT depends on with a much lighter-weight
 implementation (Meszaros 2007, page 551).

Four-Phase Test
 We structure each test with four distinct parts executed in sequence
 (Meszaros 2007, page 358).

Fresh Fixture
 Each test constructs its own brand-new test fixture for its own private use
 (Meszaros 2007, page 311).

Garbage-Collected Teardown
 We let the garbage collection mechanism provided by the programming language
 clean up after our test (Meszaros 2007, page 500).

Generated Value
 We generate a suitable value each time the test is run
 (Meszaros 2007, page 723).

Guard Assertion
 We replace an if statement in a test with an assertion that fails the test
 if not satisfied (Meszaros 2007, page 490).

Hard-Coded Test Double
 We build the Test Double by hard-coding the return values and/or expected
 calls (Meszaros 2007, page 568).

Humble Object
 We extract the logic into a separate, easy-to-test component that is
 decoupled from its environment (Meszaros 2007, page 695).

Implicit Setup
 We build the test fixture common to several tests in the setUp method
 (Meszaros 2007, page 424).

Implicit Teardown
 The Test Automation Framework calls our clean up logic in the tearDown
 method after every Test Method (Meszaros 2007, page 516).

In-line Setup
 Each Test Method creates its own Fresh Fixture by calling the appropriate
 constructor methods to build exactly the test fixture it requires
 (Meszaros 2007, page 408).

In-line Teardown
 We include teardown logic at the end of the Test Method immediately after
 the result verification (Meszaros 2007, page 509).

Layer Test
 We can write separate tests for each layer of the layered architecture
 (Meszaros 2007, page 337).

Lazy Setup
 We use Lazy Initialization of the fi xture to create it in the first test
 that needs it (Meszaros 2007, page 435).

Literal Value
 We use literal constants for object attributes and assertions
 (Meszaros 2007, page 714).

Minimal Fixture
 We use the smallest and simplest fi xture possible for each test
 (Meszaros 2007, page 302).

Mock Object
 We replace an object the SUT depends on with a test-specific object that
 verifies it is being used correctly by the SUT (Meszaros 2007, page 544).

Named Test Suite
 We define a test suite, suitably named, that contains a set of tests that
 we wish to be able to run as a group (Meszaros 2007, page 592).

Parameterized Test
 We pass the information needed to do fixture setup and result verification
 to a utility method that implements the entire test life cycle
 (Meszaros 2007, page 607).

Prebuilt Fixture
 We build the Shared Fixture separately from running the tests
  (Meszaros 2007, page 429).

Recorded Test
 We automate tests by recording interactions with the application and playing
 them back using a test tool (Meszaros 2007, page 278).

Scripted Test
 We automate the tests by writing test programs by hand
 (Meszaros 2007, page 285).

Setup Decorator
 We wrap the test suite with a Decorator that sets up the shared test fixture
 before running the tests and tears it down after all the tests are done
 (Meszaros 2007, page 447).

Shared Fixture
 We reuse the same instance of the test fixture across many tests
 (Meszaros 2007, page 317).

Standard Fixture
 We reuse the same design of the test fi xture across many tests
 (Meszaros 2007, page 305).

State Verification
 We inspect the state of the SUT after it has been exercised and compare it
 to the expected state (Meszaros 2007, page 462).

Stored Procedure Test
 We write Fully Automated Tests for each stored procedure
 (Meszaros 2007, page 654).

Suite Fixture Setup
 We build/destroy the shared fi xture in special methods called by the Test
 Automation Framework before/after the fi rst/last Test Method is called
 (Meszaros 2007, page 441).

Table Truncation Teardown
 We truncate the tables modifi ed during the test to tear down the fi xture
 (Meszaros 2007, page 661).

Test Automation Framework
 We use a framework that provides all the mechanisms needed to run the test
 logic so the test writer needs to provide only the test-specifi c logic
 (Meszaros 2007, page 298).

Test Discovery
 The Test Automation Framework discovers all the tests that belong to the
 test suite automatically (Meszaros 2007, page 393).

Test Double
 We replace a component on which the SUT depends with a “test-specific
 equivalent” (Meszaros 2007, page 522).

Test Enumeration
 The test automater manually writes the code that enumerates all tests that
 belong to the test suite (Meszaros 2007, page 399).

Test Helper
 We defi ne a helper class to hold any Test Utility Methods we want to reuse
 in several tests (Meszaros 2007, page 643).

Test Hook
 We modify the SUT to behave differently during the test
 (Meszaros 2007, page 709).

Test Method
 We encode each test as a single Test Method on some class
 (Meszaros 2007, page 348).

Test Runner
 We define an application that instantiates a Test Suite Object and executes
 all the Testcase Objects it contains (Meszaros 2007, page 377).

Test Selection
 The Test Automation Framework selects the Test Methods to be run at runtime
 based on attributes of the tests (Meszaros 2007, page 403).

Test Spy
 We use a Test Double to capture the indirect output calls made to another
 component by the SUT for later verification by the test
 (Meszaros 2007, page 538).

Test Stub
 We replace a real object with a test-specifi c object that feeds the desired
 indirect inputs into the SUT (Meszaros 2007, page 529).

Test Suite Object
 We defi ne a collection class that implements the standard test interface
 and use it to run a set of related Testcase Objects
 (Meszaros 2007, page 387).

Test Utility Method
 We encapsulate the test logic we want to reuse behind a suitably named
 utility method (Meszaros 2007, page 599).

Test-Specific Subclass
 We add methods that expose the state or behavior needed by the test to a
 subclass of the SUT (Meszaros 2007, page 579).

Testcase Class
 We group a set of related Test Methods on a single Testcase Class
 (Meszaros 2007, page 373).

Testcase Class per Class
 We put all the Test Methods for one SUT class onto a single Testcase Class
 (Meszaros 2007, page 617).

Testcase Class per Feature
 We group the Test Methods onto Testcase Classes based on which testable
 feature of the SUT they exercise (Meszaros 2007, page 624).

Testcase Class per Fixture
 We organize Test Methods into Testcase Classes based on commonality of the
 test fixture (Meszaros 2007, page 631).

Testcase Object
 We create a Command object for each test and call the run method when we
 wish to execute it (Meszaros 2007, page 382).

Testcase Superclass
 We inherit reusable test-specific logic from an abstract Testcase
 Superclass (Meszaros 2007, page 638).

Transaction Rollback Teardown
 We roll back the uncommitted test transaction as part of the teardown
 (Meszaros 2007, page 668).

Unfinished Test Assertion
 We ensure that incomplete tests fail by executing an assertion that is
 guaranteed to fail (Meszaros 2007, page 494).

