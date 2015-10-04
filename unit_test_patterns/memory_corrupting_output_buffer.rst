.. _memory_corrupting_output_buffer:

*******************************
Memory Corrupting Output Buffer
*******************************

Idiomatic pattern which tries to corrupt the memory through the output parameter
of a function/method (Greening 2011, p. 40).

:Context:
 You have to write a unit test for a function/method with an output parameter
 pointing to buffer.

:Problem:
 You do not know how to test if the memory in front of the buffer is corrupted
 after the function is called.

:Solution:
 Write a unit test which sets the start element of the buffer to element[1] and
 make the buffer one element larger. After calling the function the element[0]
 has to contain the same data.

:Resulting context:
 You know if the functions output parameter does corrupt the memory in
 front of the parameter. 
