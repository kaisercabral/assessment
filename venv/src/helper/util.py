#
# File: report_manager.py
# Description: This class orchestrates the use case processes
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
import csv
from datetime import datetime


class Util:

    @staticmethod
    def compare_dates(transaction_date, start_date, end_date):
        """
        Compares a transaction date with a start and end date.

        Parameters:
        transaction_date (str): The transaction date in the format 'dd/mm/yyyy'.
        start_date (str): The start date in the format 'dd/mm/yyyy'.
        end_date (str): The end date in the format 'dd/mm/yyyy'.

        Returns:
        bool: True if the transaction date is within the specified range, False otherwise.
        """
        date_format = '%d/%m/%Y'
        date_obj = datetime.strptime(transaction_date, date_format)
        if start_date <= date_obj <= end_date:
            return True
        else:
            return False

    @staticmethod
    def print_update_message(transaction, label):
        """
        Prints an update message for a transaction.

        Parameters:
        transaction (dict): A dictionary representing a transaction.
        label (str): The label for the transaction, or None if it could not be classified.
        """
        frm_date = datetime.strptime(transaction.get("date"), '%d/%m/%Y').strftime('%Y-%m-%d')
        print(
            f'{frm_date} {transaction.get("description")}: {transaction.get("amount")} {"unable to classify" if not label else "classified as"} {label}')

    @staticmethod
    def read_labels_file(file_path):
        """
        Reads labels from a CSV file.

        Parameters:
        file_path (str): The path to the CSV file.

        Returns:
        list[dict]: A list of dictionaries, where each dictionary represents a label.
        """
        labels = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                labels.append({'label': row['label'], 'pattern': row['pattern']})
        return labels
