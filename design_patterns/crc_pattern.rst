.. _crc_pattern:

***********
CRC Pattern
***********

Adds a cyclic redundancy check to identify when bits of the data have been
corrupted in vivo (Powell 2011, page 359).

:Use cases:
 * big memory segments
 * complex data structures
 * communication messaging
 * in-memory error detection for harsh EMI environments
 * in-memory error detection for mission-critical data

:Related patterns: One's Complement Pattern

:Implementation Alternatives in C:
 * table-driven algorithm -> fast, bigger memory consumption
   (Powell 2011, page 369)
 * polynominal calculation -> slower, smaller memory consumption
   (Powell 2011, page 369)

:Implementation exmaple:
 C - Safety-relevant patient data (some structures) is linked to an alarm
 mechanism which triggers data specific alarm handlers if the data is identified
 as corrupted after setting or getting a data set
 (Douglass 2011, p. 369).
