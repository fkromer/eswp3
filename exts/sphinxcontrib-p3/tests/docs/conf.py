# -*- coding: utf-8 -*-

import sys
import os

extensions = [
    'sphinx.ext.graphviz',
    'sphinxcontrib.p3'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'test'
copyright = u'2016, thinwybk'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default' #sphinx_rtd_theme
html_static_path = ['_static']

graphviz_dot = 'dot'
graphviz_dot_args = ['-Tsvg']
graphviz_output_format = 'svg'
