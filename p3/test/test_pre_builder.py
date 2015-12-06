"""
Unit tests for the p3/pre-buidler module.
"""

import p3.pre_builder as pb
import unittest
import os
import shutil


class DotBuilderTest(unittest.TestCase):
    """
    Wrapper for all unit test cases for pre_build.py
    """
    def setUp(self):
        print('\n--- Begin setUp ---')
        self.__create_files_in_test_dir()
        print('--- End setUp ---')

    def tearDown(self):
        print('\n--- Begin tearDown ---')
        self.__cleanup_test_dir()
        #pass
        print('\n--- End tearDown ---')

    def __create_files_in_test_dir(self):
        """
        Creates directories and files in the test directory /test/test_dir:
        /test
          /test_dir
            test_dir.gv
            /test_dir_1
              test_dir_1.gv
            /test_dir_2
              test_dir_2.gv
        """
        file_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = os.path.join(file_dir, 'test_dir')
        os.chdir(test_dir)
        open('test_dir.gv', 'w').close()
        os.mkdir('test_dir_1')
        open('test_dir_1/test_dir_1.gv', 'w').close()
        os.mkdir('test_dir_2')
        open('test_dir_2/test_dir_2.gv', 'w').close()
        print('Directory and file content: ')
        self.__print_dir_content()

    def __cleanup_test_dir(self):
        """
        Delete all sub directories and "*.gv" files in the test directory.
        """
        file_dir = os.path.dirname(os.path.realpath(__file__))
        folder = os.path.join(file_dir, 'test_dir')
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        print('Directory and file content: ')
        self.__print_dir_content()

    def __print_dir_content(self):
        """
        Finds all files and subdirectories and prints it (test code debugging).
        """
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            #for subdirname in dirnames:
            #    print(os.path.join(dirname, subdirname))

            # print path to all filenames.
            for filename in filenames:
                print(os.path.join(dirname, filename))

    def test_find_dot_file(self):
        """
        The function find_dot_files() shall find all files in the directory
        which fit the pattern "*.gv".
        """
        file_dir = os.path.dirname(os.path.realpath(__file__))
        destination_dir = os.path.join(file_dir, 'test_dir')
        builder = pb.PreBuilder()
        dir_entries = builder.find_dot_files(destination_dir)
        self.assertListEqual(dir_entries, [destination_dir + '/test_dir.gv',
                                           destination_dir + '/test_dir_1/test_dir_1.gv',
                                           destination_dir + '/test_dir_2/test_dir_2.gv'])

if __name__ == "__main__":
    # run all unit tests
    unittest.main()

