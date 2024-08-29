#
# File: transaction_controller.py
# Description: This class orchestrates the transactions actions
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by the University's Academic Misconduct Policy.

import csv
import tempfile
import os
from collections import defaultdict
from datetime import datetime
from helper.util import Util
from controller.label_controller import LabelController

FILE_PATH = '../files/new_transactions.csv'


class TransactionController:

    @staticmethod
    def import_transactions(transactions_file):
        """
       Imports transactions from a given CSV file, adds a 'label' column for classification,
       and writes the modified data to a new CSV file.

       Parameters:
       transactions_file (str): The path to the input CSV file containing the transactions.

       Returns:
       None
       """
        count = 0
        with open(transactions_file, "r") as transaction_file, open(FILE_PATH, 'w', newline='') as output:
            reader = csv.reader(transaction_file)
            writer = csv.writer(output)

            headers = next(reader)  # get the headers
            headers.append('label')  # add column label for classification
            writer.writerow(headers)

            for row in reader:
                writer.writerow(row)
                count += 1
        print(f"Imported {count} transactions")

    @staticmethod
    def classify_transactions(rules, start_date, end_date):
        """
        Classifies transactions based on provided rules and updates the transactions with the corresponding labels.
        Only transactions within the specified date range are processed.

        Parameters:
        rules (str): The path to the CSV file containing the classification rules.
        start_date (str): The start date for filtering transactions (in 'YYYY-MM-DD' format).
        end_date (str): The end date for filtering transactions (in 'YYYY-MM-DD' format).

        Returns:
        None
        """
        result = LabelController.get_dictionary(rules)

        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, newline='')
        count = 0

        with  open(FILE_PATH, 'r', newline='') as transactions:
            reader = csv.DictReader(transactions)
            fieldnames = reader.fieldnames

            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if Util.compare_dates(row.get('date'), start_date, end_date):
                    label = LabelController.find_label(result, row.get('description'))
                    count += 1
                    Util.print_update_message(row, label)
                    row['label'] = label

                writer.writerow(row)
        print(f'{count} transactions processed')
        temp_file.close()
        os.replace(temp_file.name, FILE_PATH)

    @staticmethod
    def list_transactions(label, start_date, end_date):
        """
        Lists and prints transactions that match a specific label within a given date range.
        If 'Unclassified' is specified as the label, it lists transactions that have no label.

        Parameters:
        label (str): The label to filter transactions by. If 'Unclassified', lists transactions without a label.
        start_date (str): The start date for filtering transactions (in 'YYYY-MM-DD' format).
        end_date (str): The end date for filtering transactions (in 'YYYY-MM-DD' format).

        Returns:
        int: The total count of transactions that match the label within the specified date range.
        """
        count = 0
        with open(FILE_PATH, "r") as transaction_file:
            reader = csv.DictReader(transaction_file)

            for row in reader:
                if Util.compare_dates(row.get('date'), start_date, end_date):
                    date = datetime.strptime(row["date"], '%d/%m/%Y').strftime('%Y-%m-%d')
                    if (label == 'Unclassified' and not row['label']) or (not label) or (
                            row['label'].lower() == label.lower()):
                        count += 1
                        print(f'{date} {row["description"]}: {float(row["amount"]):.2f} [{row["label"]}]')

        return count

    @staticmethod
    def summarise_transactions(start_date, end_date):
        """
        Summarizes transactions within a specified date range by calculating the total amount
        spent for each label category and prints the summary in a predefined order.

        Parameters:
        start_date (str): The start date for filtering transactions (in 'YYYY-MM-DD' format).
        end_date (str): The end date for filtering transactions (in 'YYYY-MM-DD' format).

        Returns:
        None
        """
        # Initialize a defaultdict to store the sum of amounts for each label
        sums_by_label = defaultdict(float)

        with open(FILE_PATH, "r") as transaction_file:
            reader = csv.DictReader(transaction_file)
            for row in reader:
                if Util.compare_dates(row.get('date'), start_date, end_date):
                    label = row['label'] or 'Other'  # Handle empty labels
                    amount = float(row["amount"])
                    sums_by_label[label] += amount

        # Could not get the print on the same order as requested on the document so I decided to define the order to be printed
        order = ['Food', 'Clothing', 'Home', 'Utilities', 'Other']
        for order_label in order:
            if order_label in sums_by_label:
                print(f'{order_label}: {sums_by_label[order_label]:.2f}')
        print(f'Total: {float(sum(sums_by_label.values())):.2f}')
