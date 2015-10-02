.. _ones_complement_pattern:

************************
One's Complement Pattern
************************

Adds a bitwise inverted copy of primitive data elements to identify when data is
corrupted in vivo (Powell 2011, page 359).

:Use Cases:
 * small safety/availability-critical data structures
 * simple safety/availability-critical data structures
 * primitive safety/availability-critical data types
 * static variables in safety/availability-critical functions

:Implementation Alternatives in C:
 * ~ operator for primitive data types + iteration over all primitive data types
   (Powell 2011, page 363)
 * macro encapsulated conversion operation for primitive data types + iteration
   over all primitive data types

:Implementation Alternatives in Python:
 * conversion of class data: @property decorator to use setter/getter methods
   like class properties -> good: same access syntax like attributes
 * conversion of class data: explicit private setter/getter methods -> bad:
   other access syntax than attributes

:Implementation Examples:
 C - The safety-relevant aircraft attitude (roll, yaw, pitch) is linked to an
 alarm mechanism which triggers an alarm handler (~ whole attitude data) if one
 of the data elements is identified as corrupted after getting the data set
 (Douglass 2011, p. 364)
