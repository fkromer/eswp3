.. globetrotter:

*************
Globetrotters
*************

:Context:
 You want to version your work and do not have an internet/network connection to
 your company neccessarily.

:Problem:
 You would like to version your work on the local file system for better
 productivity and more confidence about the quality of your work.

:Forces:
 * data consistency
 * useability
 * maintainability
 * data security: less risc for lost "versions", risk of mistaces during merging

:Tool example: Git

:Solution:
 Use a decentralized versioning tool which allows to create versionized
 repositories on the local file system which can be merged into a/the companies
 versioning tool repository (remote repository).

:Resulting context:
 You can version your work on the local file system and you are a more confident
 about the quality of your work. The **data consistency** is not worse than
 without a local versioning tool. The **useability** is more complex due to the
 communication between local and remote repository. The **maintainability** is
 more complex because of the need for merging but the ability to version speeds-up
 development. The **data security** is worse due to the risk of mistaces during
 merging but a lot better because less risk of versions (information in a repo
 does not get lost, local file system copies get lost regularly).
