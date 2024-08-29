#
# File: label_controller.py
# Description: This class is responsible for keeping the functions related to labels
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.
import csv


class LabelController:

    @staticmethod
    def find_label(labels, transaction_description):
        """
        Finds and returns a label for a transaction based on its description.

        Parameters:
        labels (list): A list of dictionaries where each dictionary contains a 'label' and a 'pattern'.
        transaction_description (str): The description of the transaction to be classified.

        Returns:
        str: The label corresponding to the matched pattern in the transaction description.
             Returns an empty string if no match is found.
        """
        for desc in transaction_description.split():
            for label in labels:
                if desc.lower() in label.get('pattern').lower() or label.get('pattern').lower() in desc.lower():
                    return label.get('label')
        return ''

    @staticmethod
    def get_dictionary(rules):
        """
        Reads a CSV file containing classification rules and returns its contents as a list of dictionaries.

        Parameters:
        rules (str): The path to the CSV file containing the rules. Each row in the file should represent
                     a rule with different fields stored as key-value pairs in a dictionary.

        Returns:
        list: A list of dictionaries where each dictionary corresponds to a row in the CSV file,
              with column headers as keys and row data as values.
        """
        data = []
        with open(rules, 'r', encoding='utf-8-sig') as csvfile:
            # Create a CSV reader object
            csv_reader = csv.DictReader(csvfile)

            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Append each row (as a dictionary) to the data list
                data.append(row)
        return data
