.. _ordered_locking_pattern:

***********************
Ordered Locking Pattern
***********************

Prevention of resource-based deadlock by forcing ordered locking of resources.

:Implementation strageties: This pattern is implemented with one type of resource ID assignment (dynamic or design-time) and one or both types of resource access (dyadic or monadic).

Dynamic resource ID assignment means that IDs are dynamically assigned to resources during runtime.

Design-time resource ID assignment means that IDs are assigned to resources during compile-time.

Dyadic access means that the resource client does explicitly need to lock and unlock the resource.

Monadic access means that the resource client does not need to unlock the resource (implicitly locked and unlocked). 

:Advantages:
 * easy (resource ID assignment: dynamic)
 * difficult for big systems (resource ID assignment: design-time)
 * flexible (access: dyadic)

:Disadvantages:
 * unsafe (resource ID assignment: dynamic)
 * safe (resource ID assignment: design-time)
 * unflexible (access: monadic)

:Implementation example:
 C - The attitude, velocity and position sensors of an aircraft (data servers)
 are accessed by a kinematic and a route planing control (data clients)
 (Douglass 2011, chapter 4.9.8).
