# -*- coding: utf-8 -*-

"""
    sphinxcontrib-p3
    ~~~~~~~~~~~~~~~~
    Process inline sphinx.ext.graphviz code whcih is conform to the 'p3 pattern
    language syntax' embedded into sphinx-doc reST input files.
    Requires sphinx-doc v1.3.4

    :copyright: Copyright 2016 by thinwybk.
"""

__version__ = '0.1'
__author__ = 'thinwybk'

from sphinx.errors import SphinxError, VersionRequirementError, ConfigError
from sphinx.ext.graphviz import graphviz
import re, sphinx
from tempfile import NamedTemporaryFile

def check_sphinx_version():
    if (sphinx.__display_version__ < '1.3.4'):
        raise P3Error('sphinx-contrib-p3 requires sphinx-doc version v1.3.4')

def dye_node(graphviz_node, color):
    if ('color =' not in graphviz_node) and ((color == 'red') or (color == 'green')):
        colored_node = re.sub('\];', ', color = ' + color + '];', graphviz_node)
    else:
        colored_node = graphviz_node
    return colored_node

def doctree_read_handler(app, doctree):
    check_sphinx_version()
    for node in doctree.traverse(graphviz):
        tif = NamedTemporaryFile(delete=True)
        tof = NamedTemporaryFile(delete=True)
        with open(tif.name, 'w') as fin:
            for l in node['code']:
                fin.write(l)
        #with open(tif.name, 'r') as fin:
        #    print(fin.read())
        with open(tif.name, 'r') as fin, open(tof.name, 'w') as fout:
            for line in fin:
                if ('href="' or 'URL="') not in line:
                    fout.write(dye_node(line, 'red'))
                else:
                    fout.write(dye_node(line, 'green'))
        with open(tof.name, 'r') as fout:
            string=''
            for l in fout:
                string = string + l
            node['code'] = string
        #print(node['code'])

def setup(app):
    app.setup_extension('sphinx.ext.graphviz')
    app.connect('doctree-read', doctree_read_handler)
    return {'version': __version__}

class P3Error(SphinxError):
    category = 'p3 error'

