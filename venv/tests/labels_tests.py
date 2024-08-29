import unittest
import os
import sys
import csv

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SOURCE_PATH)

from controller.label_controller import LabelController
from helper.util import Util

FILE_PATH = '../files/patterns.csv'
NEW_FILE_PATH = '../files/new_transactions.csv'


class LabelTests(unittest.TestCase):
    """
    Unit tests for the LabelController class.
    """

    def test_reading_file(self):
        """
        Tests if the specified file exists.
        """
        self.assertTrue(os.path.isfile(FILE_PATH), f"File '{FILE_PATH}' does not exist.")

    def test_search_label(self):
        """
        Tests if the find_label method returns the correct label.
        """
        labels = Util.read_labels_file(FILE_PATH)
        self.assertEqual("Clothing", LabelController.find_label(labels, "shoe"),
                             "The return is not what is expected")


if __name__ == '__main__':
    unittest.main()
