import unittest
import os

FILE_PATH = '../files/transactions.csv'
NEW_FILE_PATH = '../files/new_transactions.csv'


class TransactionsTests(unittest.TestCase):

    def test_load_file(self):
        self.assertTrue(os.path.isfile(FILE_PATH), f"File '{FILE_PATH}' does not exist.")

    def test_new_transactions_file(self):
        self.assertTrue(os.path.isfile(NEW_FILE_PATH), f"File '{NEW_FILE_PATH}' does not exist.")


if __name__ == '__main__':
    unittest.main()
