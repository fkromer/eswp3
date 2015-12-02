.. _redundancy:

**********
Redundancy
**********

Context:
 You depend on a subject with critical functionality whose absence or
 malfunction would lead to not managable problem in the overall system.

Problem:
 The absence or malfunction of the subject leads to a malfunction of the overall
 system.

Solution:
 "Use" more than one copy of the subject and implement a mechanism which allows
 to switch from one/all to one/the remaining subjects in case of the malfunction
 of one/many subject(s).

Use cases:
 - employees with key skills/in key positions
 - safety/availability critical software and systems

Resulting context:
 The malfunction or absence of up to n-1 of the n copies of the subject do not
 result in a malfunction of the overall system. The probability of the system
 failing (probability of all redundant copies failing) :math:`p_{system}`
 is :math:`p_{system} = \prod \limits_{i=1}^{n}p_{i}` with :math:`n` number of subjects and
 :math:`p_{i}` probability of subject i failing.
