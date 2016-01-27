==================
Test documentation
==================

.. graphviz::

   digraph pattern_language{
      // styling
      size="10";
      node [color=lightblue2, style=filled];

      // 1st to 2nd level node transitions
      p1 -> p2;
      p2 -> p3;

      // nodes
      p1 [label="Pattern node without pattern section"];
      p2 [label="Pattern node with section in same file"];
      p3 [label="Pattern node with section in same dir and href and target", href="../build_automation_language.html#pattern-node-with-section-in-same-dir-and-href-and-target", target="_top"];
      p4 [label="Pattern node with section in subdir and href and target", href="../subdir/page.html#pattern-node-with-section-in-subdir-and-href-and-target", target="_top"];
   }

Pattern node with section in same dir and href and target
=========================================================

