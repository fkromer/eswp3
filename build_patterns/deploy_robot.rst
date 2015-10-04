.. _deploy_robot:

************
Deploy robot
************

This most high-level build pattern sets the founation for the automation of the
deployment process.

:Context:
 Actually the project deliveries (software, documentation, etc.) are deployed
 manually. The start of a new project is right ahead an many with the same or a
 slightly different development toolchain will follow.

:Problem:
 In last projects the deployment of the software, documents, etc. took to much
 time an slowed down the development process.

:Solution:
 Automatize as much process steps as possible with a build environment.

:Forces:
 * operating system compatibility
 * tool compatibility
 * developer prouctivity
 * build server maintainance
 * time to market

:Resulting context:
 The basis for automating process steps has been set. Time has to be invested to
 set up the build environment. But in this an all following projects the project
 team will be much more productive and the time to market will be decreased.
 The **Is it automatable** pattern could be applied next to identify what
 process steps may be automated.
