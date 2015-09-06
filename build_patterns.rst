.. _build_patterns:

**************
Build Patterns
**************

Categorization of build patterns
================================

Build patterns may be categorized according to the following scheme (Osherove 2015).

- Separation of concerns

 - Build Script Injection

 - Fill In The Blanks

- Productivity

 - Accumulative Builds

 - Gated Commit

 - Incremental Feedback Loops

 - Pipeline Disintegration

 - Shipping Skeleton

- Maintainability

 - Base Parameter

 - Extract Script

 - Fishbone Build Structure

 - Location Agnostic Script

- Team Collaboration

 - Dependency Stash

 - Public API Hook

 - Tipping Point

 - Version by Snapshots Dependencies

- Stakeholder

 - Deploy by Proxy

 - Parallel Fire-hose

- Branching

- Scalability

 - Fan Out Agents

 - Split to Parallel

- Trustworthy

 - Binary Result

 - Irrelevant Build

 - Big Ball of Mud

All build patterns in alphabetic order
======================================

.. accumulative_buils:

Accumulative Builds
-------------------

The single responsibility principle applied to build scipts by using artifacts (results) of scripts as input for dependent scripts to decrease build time (Osherove 2015, chapter 7 "Accumulative Builds").

CI Server Feature Requirements: artifacts

Build Script Injection
----------------------

Separation of the knowledge about the build process and the source file structure by "injection" of the info into the root directory of the source control repository (Osherove 2015, chapter 3 "Pattern: Build Script Injection").

Extract Script
--------------

Refactoring of duplicated script code into separate scripts with parameter or environment variable dependency which are called in the main script (Osherove 2015, chapter 13 "Extract Script").

Fill In The Blanks
------------------

Parametrization of script knowledge about IT infrastructure, deployment, variants, etc. within build scripts (Osherove 2015, chapter 4 "Build Pattern: Fill In The Blanks").

Gated Commit
------------

The CI server performs a pre-build of the developers code requested to be checked in on the master branch and does only check in the code into source control if all tests pass (Osherove 2015, chapter 9 "Pattern: Gated Commit").

Location Agnostic Script
------------------------

Ensuring that all information about server directories is available for the build script (Osherove 2015, chapter 12 "Build Pattern: Location Agnostic Script").

Shipping Skeletton
------------------

(Osherove 2015, chapter 5 "Pattern: Shipping Skeleton")

Parallel Fire-hose
------------------

Bridging the physical connection between staging environment (server) an production environment (server) with an isolated deploy server in a demilitarized zone (Osherove 2015, chapter 21 "Pattern: Parallel Fire-hose").

Pipeline Disintegration
-----------------------

A build process is set up in parallel to an existing build process to add additional features but not interfering the existing pipeline (Osherove 2015, chapter 6 "Pattern: Pipeline Disintegration").

Public API Hook
---------------

Separation of API and logic of sw component to decoupe the dependency between sw components (Osherove 2015, chapter 19 "Pattern: Public API Hook").

Version by Snapshot Dependencies
--------------------------------

Ensure that the build of a software component is only triggered if all builds of software components it depends on are build as "passed" (Osherove 2015, chapter 17 "Pattern: Version by Snapshot Dependencies").
