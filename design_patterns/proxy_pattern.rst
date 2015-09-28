.. _proxy_pattern:

*************
Proxy Pattern
*************

Standardization of component interface for better maintainability.

:Implementation example: C++ - An interface for graphical objects (proxy) may be used by the application (client) to access the implementation of a image class (Gamma et al. 1995, chapter „Proxy“).

Hardware Proxy
--------------

In the driver layer or HAL the access on hardware is encapsulated in a component.

:Implementation example: C - A motor (hardware) is accessed over an interface independent of the hardware-interface providing the control of speed and direction and monitoring the status (hardware proxy). The hardware is accessed per 16-bit wide memory-mapped interface (Douglass 2011, chapter 3.2.8).

Remote Proxy
------------

In distributed systems software may access neighbor systems as remote "device".

Security Proxy
--------------

In security applications it may be required to hold all component data within
the application in encrypted status. The data representation/format may not be
encapsulated within the proxy as usual then.
