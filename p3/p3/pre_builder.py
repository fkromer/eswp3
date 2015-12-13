"""
Pre-build functionality before running "make html" of sphinx-doc.
"""

import glob
import os
import subprocess


class PreBuilder():
    """
    Class related to pre-build functionality of p3 projects.
    """
    def find_dot_files(self, dir):
        """
        Finds all files fitting the pattern "*.gv" within a directory recursively.

        :param dir: directory to be searched in
        :return files: list of dot files
        """
        files = []

        for dirname, dirnames, filenames in os.walk(dir):
            # print path to all subdirectories first.
            #for subdirname in dirnames:
            #    print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                if filename.endswith('.gv'):
                    #print(os.path.join(dirname, filename))
                    files.append(os.path.join(dirname, filename))
        return files

    def convert_to_svg(self, dot_file):
        """
        Converts a dot file in the .gv format into a .svg file. Requires local
        installation of graphviz and 

        :param dot_file: dot file to be converted
        :return svg_file: generated svg file
        """
        gv_file = dot_file
        file_name = os.path.splitext(gv_file)[0]
        svg_file = file_name + '.svg'
        subprocess.call(["dot", "-Tsvg", "{}".format(gv_file), "-o", "{}".format(svg_file)])

    def find_and_convert(self, dir):
        """
        Finds all dot input files (*.gv) recursively in a directory and converts
        it to dot output files (*.svg).

        :param dir: the directory the processing shall be applied to
        """
        dot_files = self.find_dot_files(dir)
        for f in dot_files:
            try:
                self.convert_to_svg(f)
            except Exception as e:
                print('something went wrong during conversion')
                print(e)

if __name__ == "__main__":
    print('not implemented yet, testing in progress')
