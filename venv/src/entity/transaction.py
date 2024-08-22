#
# File: transaction.py
# Description: This class is responsible for keeping the transaction data
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.


class Transaction:

    def __init__(self, date, description, amount, label):
        self.date = date
        self.description = description
        self.amount = amount
        self.label = label

    def __repr__(self):
        return f"Transaction(date='{self.date}', description='{self.description}', amount={self.amount}, label={self.label})"

    def __str__(self):
        return f"{self.date} | {self.description} | {self.amount} | {self.label}"
