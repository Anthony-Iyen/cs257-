#cli.py
#Anthony Iyengunmwena
#4/17/25

#NAME: cli.py - command-line interface exercise

#SYNOPSIS: python3 cli.py by Anthony Iyengunmwena

#DESCRIPTION: Shows a list of the titles of all the movies with the action genre/type

import csv
import argparse
import kagglehub

...
with open('../data/books.csv') as f:
    reader = csv.reader(f)
    for book_row in reader:

