"""Asutin Drenski - July 2017"""
# Defines functions for constructing objects from delimited files.

import csv
import os

__all__ = ["read_delimited_file"]

def read_delimited_file(filePath, constructorLambda, delimiter=",", headerRow=True):
    """Reads a delimited file and constructs objects based on the provided lambda function."""
    with open(filePath, newline=os.linesep) as reader:
        csvReader = csv.reader(reader, delimiter=delimiter, quotechar="\"")
        if headerRow:
            next(csvReader)
        return list(map(constructorLambda, [[y.strip() for y in x] for x in csvReader]))