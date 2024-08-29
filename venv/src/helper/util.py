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
        date_format = '%d/%m/%Y'
        date_obj = datetime.strptime(transaction_date, date_format)
        if start_date <= date_obj <= end_date:
            return True
        else:
            return False

    @staticmethod
    def print_update_message(transaction, label):
        frm_date = datetime.strptime(transaction.get("date"), '%d/%m/%Y').strftime('%Y-%m-%d')
        print(
            f'{frm_date} {transaction.get("description")}: {transaction.get("amount")} {"unable to classify" if not label else "classified as"} {label}')

    @staticmethod
    def read_labels_file(file_path):
        labels = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                labels.append({'label': row['label'], 'pattern': row['pattern']})
        return labels
