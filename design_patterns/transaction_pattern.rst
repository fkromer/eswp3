.. _transaction_pattern:

===================
Transaction Pattern
===================

Ensures reliable communication over an unreliable communication channel.

:Model example:
 Generic example of a source (message source),
 sender (marshals, creates/destroys, send transactions),
 send transaction (tracks # ALO or EO message transmits and retry period),
 message (metadata and data),
 receiver (demarshals, creates/destroys receive transactions),
 receive transaction (tracks # EO message receives, TimeToLive handling) and
 target (message destination)
 with class diagram, sequence diagram for an EO transaction and textual
 explanation (Douglass 1998, p. 265).
 (BTW: AMO messages do not require the creation of send and receive transactions.)
