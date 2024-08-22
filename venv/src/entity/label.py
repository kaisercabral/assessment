#
# File: label.py
# Description: This class associates transaction with labels
# Author: Arthur Paim Kaiser Cabral
# Student ID: 110298623
# Email ID: paiay005@mymail.unisa.edu.au
# This is my own work as defined by
#    the University's Academic Misconduct Policy.


class Label:

    def __init__(self, pattern, name):
        self.pattern = patern
        self.name = name

    def __repr__(self):
        return f"Label(pattern='{self.pattern}', name='{self.name}')"

    def __str__(self):
        return f"{self.pattern} | {self.name}"