.. build_automation_pattern_language:

*********************************
Build Automation Pattern Language
*********************************

.. graphviz::

   digraph build_automation_language{
      // styling
      size="11";
      node [color=lightblue2, style=filled];

      // 1st to 2nd level node transitions
      bal -> ph;
      bal -> cfg;
      bal -> nlp;
      bal -> log;
      bal -> dist;

      // 1st to 3rd level node transitions
      bal -> fh;
      
      // 2nd to 3rd level node transitions
      ph -> fh;
      nlp -> kwdp;
      nlp -> tp;
      nlp -> rkwp;
      log -> pblog;

      // 3rd to 4th level node transitions
      kwdp -> kwr;
      kwdp -> kwm;

      // nodes
      bal [label="Build Automation Lanugage"];
      ph [label="Path Handling", URL="../design_languages/build_automation_language.html#path-handling"];
      cfg [label="Configuration", URL="../design_languages/build_automation_language.html#configuration"];
      nlp [label="Natural Language Processing"];
      log [label="Logging"];
      dist [label="Distribution"];
      fh [label="File Handling", URL="../design_languages/build_automation_language.html#file-handling"];
      kwdp [label="Keyword Processing"];
      tp [label="Token Processing"];
      rkwp [label="Relative-to-Token Processing"];
      pblog [label="Pre-buffered Logging"];
      kwr [label="Keyword Replacement"];
      kwm [label="Keyword Modification"];
   }

.. configuration:

Configuration
=============

:Context:
 The behaviour of the application has to be defined equal in many use cases.
 and needs to be stored
 consistent.

:Problem:
 If CLIs do provide many arguments one gets confused very fast (the "cognitive
 limit of humans" is known to be 7 contexts). The principle of single
 responsibility is violated, because the application is stored in the calling
 scipts instead in relation to the application itself. The maintainanance
 effort of scripts which call these CLIs increase.

:Forces:
 - configuration complexity
 - overall IT infrastrutcure ("communication" with other applications over the
   configuration files)

:Solution:
 Store the configuration in a separate file.

:Resulting context:
 The behaviour of the script may be defined in a flexible manner. In many
 cases it is required to keep the application and specific configuration
 settings consistent over time. You may apply the versioning pattern to ease
 the consistent versioning of the application and its configuration(s).

.. image:: python_configuration_pattern_language.png
   :width: 600 px
   :scale: 100 %
   :alt: The graphical representation of a Configuration Pattern Language.
   :align: center

.. file-handling:

File Handling
=============

.. image:: python_file_handling_pattern_language.png
   :width: 600 px
   :scale: 100 %
   :alt: The graphical representation of File Handling Pattern Language.
   :align: center

.. path-handling:

Path Handling
=============

.. image:: python_path_handling_pattern_language.png
   :width: 200 px
   :scale: 100 %
   :alt: The graphical representation of a Path Handling Pattern Language.
   :align: center

