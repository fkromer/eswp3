.. _singleton_pattern:

*****************
Singleton Pattern
*****************

Ensures that only one instance of a class may be created.

:Implementation example: Python - Basic "class" singleton (Zlobin 2013, section
 "A classic singleton").

:Implementation example: Python - Pythonic "modul instead of class" singleton
 (Zlobin 2013, section "A module-level singleton").

:Implementation example: Python - Webcrawler which scans for website-local
 hyperlinks, follows the links and downloads the pictures on it (Zlobin 2013,
 section "Chapter 2. Creating Only One Object with teh Singleton Pattern",
 subsection "Implementation in Python" / Kindle pos. 417)

Borg singleton
--------------

Uses a shared state to ensure that successors of a singleton class are also
singletons.

:Implementation example: Python - Borg singleton implements a shared resource (to store images) and a set of URLs which are accessed by 2 threads which fetch images of the URLs and stores them (Zlobin 2013, chapter "2. Creating Only One Object with the Singleton Pattern", subchapter "Implementation in Python")
