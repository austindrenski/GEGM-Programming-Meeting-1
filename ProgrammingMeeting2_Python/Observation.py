"""Austin Drenski - July 2017"""
#
# This module provides basic data management logic for reading a delimited file into a list of class objects. 
#
# pylint: disable=C0103, C0301

import csv
import os
import StaticBaseClass
from StaticBaseClass import StaticBaseClass

def read_delimited_file(filePath, constructorLambda, delimiter=",", headerRow=True):
    """Reads a delimited file and constructs objects based on the provided lambda function."""
    with open(filePath, newline=os.linesep) as reader:
        csvReader = csv.reader(reader, delimiter=delimiter, quotechar="\"")
        if headerRow:
            next(csvReader)
        return list(map(constructorLambda, [[y.strip() for y in x] for x in csvReader]))

class Observation(StaticBaseClass):
    """Represents an observation of data."""
    
    def __init__(self, source, destination, sector, year, value):
        """Constructs an Observation with the given inputs."""
        if source is None:
            raise ValueError("Argument null: source.")
        if destination is None:
            raise ValueError("Argument null: destination.")
        if sector is None:
            raise ValueError("Argument null: sector.")
        if year is None:
            raise ValueError("Argument null: year.")
        if value < 0:
            raise ValueError("value should be greater than zero.")
        self.source = source
        self.destination = destination
        self.sector = sector
        self.year = year
        self.value = value
        StaticBaseClass.__init__(self)

    def __str__(self):
        """Returns a string representation of this Observation."""
        return "(%s, %s, %s, %s, %.2f)" % (self.source, self.destination, self.sector, self.year, self.value)

    def __repr__(self):
        """Returns a the Python expression that created this Observation."""
        return "Observation%s" % self.__str__()

    def __eq__(self, other):
        """Defines equality with another Observation"""
        return isinstance(other, Observation) and \
               self.source == other.source and \
               self.destination == other.destination and \
               self.sector == other.sector and \
               self.year == other.year and \
               self.value == other.value

    def __ne__(self, other):
        """Defines inequality with another Observation"""
        return not self.__eq__(other)

    def __copy__(self):
        """Creates a copy of this Observation"""
        return Observation(self.source, self.destination, self.sector, self.year, self.value)
