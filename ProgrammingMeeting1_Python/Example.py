class Example:
    """Represents an example."""
    def __init__(self, value):
        self.value = value

    def increase_value(self, amount):
        """Increases the value by the specified amount."""
        self.value = self.value + amount
        return self.value > 0

    def __repr__(self):
        """Returns a string that represents the current object."""
        return "The value of this example is %i" % self.value