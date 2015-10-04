.. _inverse_ata_strucutre:

***********************
Inverse data structures
***********************

Idiomatic unit test pattern to verify redundant data structures holding inverse
values.

:Problem:
 Redundant data structures (variables, structures, etc.) holding
 bit-inverted values during runtime are required in safety-critical contexts.
 It is also required to check the correctness of this data strucutures
 periodically and to call an error handling if the redundance is violated. The
 related if-else structures decrease the code coverage if not considered.

:Solution:
 Define inverted values as input value for the checking
 functions dependent on the data type of the variable. The value range of
 unsigned data types is 0..(2*n)-1 with n = # bits. So the bit-interted value
 of an e.g. 8-bit unsigned integer (0..255) of 1 is 254. The range of signed
 data types with two's complement representation is -2*(n-1)..0..2*(n-1)-1 wit
 n = # bits. So the bit-inverted value of an e.g. 8-bit signed integer
 (-128,..,-1,0,+1,..,127) of 5 is -6.
