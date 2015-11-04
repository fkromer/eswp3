.. mock:

****
Mock
****

Hardware Mock
--------------

Emulatate the bevahior of hardware in software.

:Context:
 A driver function which shall be unit tested accesses real hardware during its
 execution.

:Problem:
 The execution of the unit test depends on the availability/existence of
 hardware.

:Solution:
 Emulate the behavior of the hardware in software.

:Resulting context:
 The unit test of the driver function is decoupled from the actual hardware. The
 unit test may be executed before actual hardware is available/existend for
 testing.

:Implementation example:

 C - Link-time mock of a flash driver with the mock object extension "CppUMock"
 of the unit test framework "CppUTest" (Greening 2011, section "10.1 Flash
 Driver").

 C - Fake-stub of the processor I/O registers of a LED driver in the unit test
 framework "CppUTest" (Greening 2011, p. 58).

