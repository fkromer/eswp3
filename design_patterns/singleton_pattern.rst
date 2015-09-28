.. _singleton_pattern:

*****************
Singleton Pattern
*****************

Ensures that only one instance of a class may be created.

:Implementation example: Python - Abstract but running example of a singleton. (Zlobin 2013, chapter "A classic singleton")

Borg singleton
--------------

Uses a shared state to ensure that successors of a singleton class are also
singletons.

:Implementation example: Python - Borg singleton implements a shared resource (to store images) and a set of URLs which are accessed by 2 threads which fetch images of the URLs and stores them (Zlobin 2013, chapter "2. Creating Only One Object with the Singleton Pattern", subchapter "Implementation in Python")
