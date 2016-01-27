# -*- coding: utf-8 -*-

from sphinx_testing import with_app

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

with_svg_app = with_app(srcdir='tests/docs',
                        buildername='html',
                        write_docstring=True)

class TestSphinxcontribP3HTML(unittest.TestCase):
    @with_svg_app
    def test_href_in_p1(self, app, status, warning):
        app.builder.build_all()
        source = (app.outdir / 'index.html').read_text(encoding='utf-8')
        self.assertRegexpMatches(source, 'p1 [label=&quot;Pattern node without pattern section&quot;];')

"""
<p class="graphviz">
<object data="../_images/graphviz-a639471fe6a8f860de9a38e5e2cc7a3a75dab0de.svg" type="image/svg+xml">
            <p class="warning">digraph pattern_language{
   // styling
   size=&quot;10&quot;;
   node [color=lightblue2, style=filled];

   // 1st to 2nd level node transitions
   p1 -&gt; p2;
   p2 -&gt; p3;

   // nodes
   p1 [label=&quot;Pattern node without pattern section&quot;];
   p2 [label=&quot;Pattern node with section in same dir and href and target&quot;, href=&quot;../index.html#pattern-node-with-section-in-same-dir-and-href-and-target&quot;, target=&quot;_top&quot;];
   p3 [label=&quot;Pattern node with section in subdir and href and target&quot;, href=&quot;../subdir/subpage.html#pattern-node-with-section-in-subdir-and-href-and-target&quot;]
}</p></object>
</p>
"""
