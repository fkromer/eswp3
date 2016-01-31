.. python_distribution_language:

============================
Python Distribution Language
============================

Application Distribution
========================

:Forces:
 - python experience of users


Server Side Distribution
========================

:Context:
 - all potential users of the application have access to the global source
   control system

:Solution:
 - store release versions of the project directory

:Resulting context:
 - clients can download application from source control
 - clean dependency encapsulation increases stability (virtual environment)
 - overhead due to application specific virtual environment managed
   (activation/deactivation before/after each execution)
