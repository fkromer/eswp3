.. _ini_configuration_file_pattern:

******************************
INI Configuration File Pattern
******************************

Idiomatic pattern to store configuration data of an application in an .ini file.

:Context:
 You need to configure an application with data in simple data types and simple
 data format on a windows operating system.

:Problem: See parent design pattern, **Configuration File**

:Forces: See parent design pattern, **Configuration File**

:Solution: Use the .ini configuration file format to store the configuration.

:Resulting Context:
 The configuration is stored in a format which is easy to read. Due to the
 similarity with the windows .ini file format the interoperability with this
 operating system is good.

:Example in Python:
 Use the python standard library module configparser to manage .ini like
 configuration files.
