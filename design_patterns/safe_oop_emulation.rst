.. _safe_oop_emulation:

******************
Safe OOP emulation
******************

:Context:
 Complex safety/availability-critical software for hardware with limited stack/heap
 shall be written in a structural programming language shall be run on hardware with limited stack/heap 

:Problem:
 A programming language with object oriented features would ease the development,
 maintainability of the software.

:Solution:
 Implement the OO features you need in the language in use.

:Implementation example in C:
 The standard library functions (malloc(), free()) which could be used to
 implement OOP are know to be not "safe". In addition this standard library
 functions have been implmented in the "personal computer" context and do not
 consider the fragmentation of memory which can lead to a crash of the software.
 Implement own versions of the functions (malloc(), free()) with safety/availability

:Resulting context:
 Basic OOP capabilities (create, modify, destroy instance of an object) can be
 used and speed-up development.
