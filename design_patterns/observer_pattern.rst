.. _observer_pattern:

****************
Observer Pattern
****************

Notification of clients about the status of a data server.

:Implementation example: C - Gas data (server) of a gas sensor is observed by a display, gas mixer and a safety monitor (clients) in C (Douglass 2011, chapter 3.5.8).

:Implementation example: C++ - System time (server) is observed by a digital and an analog clock (clients) in C++ (Gamma et al. 1995, chapter "Observer").

:Implementation example: Python - The system time (subject) notifies its
 observers (12 hour formatter, 24 hour formatter) about a change which
 convert and print the time accordingly (Zlobin 2013, chapter "Observer design
 pattern", subsection "Implementation in Python" / Kindle pos. 924).

:Implementation example: Python - The value (subject) notifies its observers
 (hex formatter, binary formatter) about a change which convert an print the
 value accoringly (Kasampalis 2015, section "Chapter 13. The
 Observer Pattern", subsection "Implementation" / Kindle pos. 2416).
