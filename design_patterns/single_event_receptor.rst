.. _single_event_receptor:

*****************************
Single Event Receptor Pattern
*****************************

Handling of asynchronous or synchonous events from a single event server using one event receptor for all events (single event receptor finite state machine).

:Pattern dependences:
 * Asynchronous version -> Queueing Pattern
 * Synchronous version -> Guarded Call Pattern

:Implementation examples:
 C - Tokenizer for strings holding floating point numbers implemented as
 asynchronous and as synchronous event handling state machine in C
 (Douglass 2011, chapter 5.3.8).
