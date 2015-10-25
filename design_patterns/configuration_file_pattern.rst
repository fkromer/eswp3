.. _configuration_file_pattern:

******************
Configuration File
******************

Context:
 The configuration of an application needs to be stored persistent.

Problem:
 It is not obvious how to store the configuration.

Forces:
 - readability
 - editability
 - configuration data

  - data types (strings, integers, floating-point numbers, **code**)
  - data format (values, lists, **objects**)

Solution:
 Store the configuration in a data file.

Resulting Context:
 The configuration is stored persistent in a maintainable manner.
