"""Austin Drenski - July 2017"""
#
# The StaticBaseClass module provides the StaticBaseClass which provides strongly-typed internal semantics to Python classes.
#
import abc
from abc import ABC, ABCMeta, abstractmethod

class StaticBaseClass(ABC):
    """Abstract base class defining semantics restricting dynamic behavior.."""
    __metaclass__ = ABCMeta

    def __init__(self):
        """Base constructor"""
        self._locked = True
   
    def __setattr__(self, key, value):
        """Overrides default dynamic behavior for property assignment."""
        if hasattr(self, "_locked"):
            if self._locked and not hasattr(self, key):
                raise TypeError("This class does not support dynamic property assignment.")
            if self._locked and not isinstance(value, type(self.__getattribute__(key))):
                raise TypeError("Expected type %s but received %s." % (type(self.__getattribute__(key)), type(value)))
        object.__setattr__(self, key, value)
    
    def __hash__(self):
        """Calculates a hash code for this Observation."""
        return reduce(lambda current, next: 23 * current + next, [hash(x) for x in self.__dict__.items()])

    @abstractmethod
    def __str__(self):
        """Returns a string representation of this Observation."""
        pass

    @abstractmethod
    def __repr__(self):
        """Returns a the Python expression that created this Observation."""
        pass

    @abstractmethod
    def __eq__(self, other):
        """Defines equality with another Observation"""
        pass

    @abstractmethod
    def __ne__(self, other):
        """Defines inequality with another Observation"""
        pass

    @abstractmethod
    def __copy__(self):
        """Creates a copy of this Observation"""
        pass
