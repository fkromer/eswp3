.. _container_pattern:

=================
Container Pattern
=================

Abstracts away data structuring from application domain classes.

:Implementation example:
 C++ - The Standard Template Library (STL) as part of the ANSI C++ provides many
 container and iterators.

:Implementation example:
 Python - The standard library of Python 3 provides many built-in containers
 (dict, list, set, tuple) and specialized container datatypes (namedtuple, deque,
 ChainMap, Counter, OrderedDict, defaultDict, UserDict, UserList, UserString)
 in the module *collections*.

:Model example:
 Generic model example with client (user of parts), iterator (mediates access to
 parts, inserts/delets parts), container (manages part collection, provides access
 operations) and two parts (data) (Douglass 1998, p. 271).
