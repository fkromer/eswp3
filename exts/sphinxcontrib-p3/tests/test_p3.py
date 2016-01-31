# -*- coding: utf-8 -*-

import sys
sys.path.append('./../sphinxcontrib')
import p3, sphinx

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

class Test(unittest.TestCase):

    def test_check_sphinx_version(self):
        """ Raise exception if sphinx-doc version is not supported. """
        sphinx.__display_version__ = '1.3.3'
        self.assertRaises(p3.P3Error, p3.check_sphinx_version)

class TestDyeNode(unittest.TestCase):

    def test_dye_node_without_color_with_valid_color(self):
        """ Node without color shall be dyed."""
        graphviz_node = 'pattern1 [label="Pattern 1", \
URL="../dir/of/sphinx-doc_file.html#pattern_1"];'
        color = 'green'
        output = p3.dye_node(graphviz_node, color)
        expected_result = 'pattern1 [label="Pattern 1", \
URL="../dir/of/sphinx-doc_file.html#pattern_1", color = green];'
        self.assertEqual(output, expected_result)

    def test_dye_node_with_color_with_valid_color(self):
        """ Node with color shall not be overriden. """
        graphviz_node = 'pattern1 [label="Pattern 1", \
URL="../dir/of/sphinx-doc_file.html#pattern_1", color = green];'
        color = 'red'
        output = p3.dye_node(graphviz_node, color)
        expected_result = 'pattern1 [label="Pattern 1", \
URL="../dir/of/sphinx-doc_file.html#pattern_1", color = green];'
        self.assertEqual(output, expected_result)

    def test_dye_node_without_color_with_invalid_color(self):
        """ Node without color shall not be dyed with invalid color."""
        graphviz_node = 'pattern1 [label="Pattern 1", \
URL="../dir/of/sphinx-doc_file.html#pattern_1"];'
        color = 'yellow'
        output = p3.dye_node(graphviz_node, color)
        expected_result = 'pattern1 [label="Pattern 1", \
URL="../dir/of/sphinx-doc_file.html#pattern_1"];'
        self.assertEqual(output, expected_result)

if __name__ == "__main__":
    unittest.main()
