.. _gui-wrapped_configuration_pattern:

*************************
GUI-wrapped Configuration
*************************

An idiomatic variation of the wrapper pattern which uses a gui as wrapper for
the textual application configuration for more safe and user friendly
configuration.

:Context:
 You have an application which uses one or several textual configuration
 mechanisms.

:Problem:
 Textual configurations are often missused by the user. It is possible to inform
 the user about the error but the response is not immediate and the actual
 reason for the error not obvious.

:Solution:
 Use a graphical user interface to wrap the configuration. Analyze the textual
 entries entered, inform about errors and give advice for correct usage to the
 user immediatelly. If the entries are correct override the configuration with
 the new values.
