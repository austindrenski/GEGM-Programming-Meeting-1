"""Austin Drenski - July 2017"""
#
# This module provides basic data management logic for reading a delimited file into a list of class objects. 
#

import StaticBaseClass
from StaticBaseClass import StaticBaseClass

class TradeData(StaticBaseClass):
    """Represents an observation of trade data."""
    # Defines the properties for this class.
    __slots__ = ["source", "destination", "sector", "year", "value"]
    
    def __init__(self, source, destination, sector, year, value):
        """Constructs an observation of trade data with the given inputs."""
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
        """Returns a string representation of this observation."""
        return "(%s, %s, %s, %s, %.2f)" % (self.source, self.destination, self.sector, self.year, self.value)

    def __repr__(self):
        """Returns a the Python expression that created this observation."""
        return "Observation%s" % self.__str__()

    def __eq__(self, other):
        """Defines equality with another observation"""
        return isinstance(other, Observation) and \
               self.source == other.source and \
               self.destination == other.destination and \
               self.sector == other.sector and \
               self.year == other.year and \
               self.value == other.value

    def __ne__(self, other):
        """Defines inequality with another observation"""
        return not self.__eq__(other)

    def __copy__(self):
        """Creates a copy of this observation"""
        return Observation(self.source, self.destination, self.sector, self.year, self.value)
