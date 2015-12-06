"""
Pre-build functionality before running "make html" of sphinx-doc.
"""

import glob
import os


class PreBuilder():
    """
    Class related to pre-build functionality of p3 projects.
    """
    def find_dot_files(self, dir):
        """
        Finds all files fitting the pattern "*.gv" within a directory recursively.

        :param: directory to be searched in
        :return: list of dot files
        """
        files = []

        for dirname, dirnames, filenames in os.walk(dir):
            # print path to all subdirectories first.
            #for subdirname in dirnames:
            #    print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                #print(os.path.join(dirname, filename))
                files.append(os.path.join(dirname, filename))
        return files

if __name__ == "__main__":
    print('not implemented yet, testing in progress')
