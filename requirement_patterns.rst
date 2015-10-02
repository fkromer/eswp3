.. _requirement_patterns:

********************
Requirement Patterns
********************

Categorization of requirement patterns
======================================

Software requirement patterns may be categorized **related to the context** and/or **according to software quality attributes** as follows (Withall 2007):

* Fundamental Requirement Patterns

 * Inter-System Interface Requirement Pattern
 * Inter-System Interaction Requirement Pattern
 * Technology Requirement Pattern
 * Comply-with-Standard Requirement Pattern
 * Refer-to-Requirements Requirement Pattern
 * Documentation Requirement Pattern

* Information Requirement Patterns

 * Data Type Requirement Pattern
 * Data Structure Requirement Pattern
 * ID Requirement Pattern
 * Calculation Formula Requirement Pattern
 * Data Longevity Requirement Pattern
 * Data Archiving Requirement Pattern
 * Living Entity Requirement Pattern
 * Transaction Requirement Pattern
 * Chronicle Requirement Pattern
 * Information Storage Infrastructure

* User Function Requirement Patterns

 * Inquiry Requirement Pattern
 * Report Requirement Pattern
 * Accesibility Requirement Pattern
 * User Interface Infrastructure
 * Reporting Infrastructure

* Performance Requirement Patterns

 * Response Time Requirement Pattern
 * Throughput Requirement Pattern
 * Dynamic Capacity Requirement Pattern
 * Static Capacity Requirement Pattern
 * Availability Requirement Pattern

* Flexibility Requirement Patterns

 * Scalability Requirement Pattern
 * Extendability Requirement Pattern
 * Unparochialness Requirement Pattern
 * Multiness Requirement Pattern
 * Multi-Lingual Requirement Pattern
 * Installability Requirement Pattern

* Access Control Requirement Patterns

 * User Registration Requirement Pattern
 * User Authentification Requirement Pattern
 * User Authorization Requirement Pattern
 * Specific Authorization Requirement Pattern
 * Configurable Authorization Requirement Pattern
 * Approval Requirement Pattern

* Commercial Requirement Patterns

 * Multi-Organization Unit Requirement Pattern
 * Fee/Tax Requirement Pattern

About the pattern meta-data
===========================

Some literature uses explicit meta-data **Basic details**, **Applicability**, **Discussion**, **Content**, **Template(s)**, **Example(s)**, **Extra requirements**, **Consideration for development** and **Considerations for testing** specific to requirement patterns (Withall 2007, chapter "The Anatomy of a Requirement Pattern"). **Basic details** include the **Related patterns**, **patter classification** and other information.

However this project uses the common explicit meta-data **Context**, **Problem**, **Solution** and **Resulting context** recommended for patterns in general by Bergin 2007. The meta-data **(Basic details/)Related patterns** mentioned before is "extracted". **Applicability** is merged into **Context**, **Discussion** (How to write? Consider what?) and **Content** (What to state?) and **Considerations for developement** (How to implement?) into **Solution**. The meta-data **Consideration for testing** and **Extra requirements** (What are higher-level patterns? What lower-level patterns do follow?) into **Resulting context**. The meta-data **Template(s)** (How to implement?) is merged into **Example(s)**.

:Context: Describes the situation before applying the pattern.

:Problem: Describes the problem which leads to the **Context**.

:Solution: Describes how the **Problem** can be addressed.

:Resulting context: Describes the situation after applying the **Solution**.

:Example(s): Describes exemplary "implementations".

All requirement patterns in alphabetic order
============================================

.. toctree::
   :glob:
   :maxdepth: 1

   requirement_patterns/*

