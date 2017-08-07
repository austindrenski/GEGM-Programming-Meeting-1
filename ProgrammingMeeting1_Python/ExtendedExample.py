from Example import Example

class ExtendedExample(Example):
    """Represents a class that inherits from the Example class."""
    def __init__(self, value):
        self.value = value

    def increase_value(self, amount):
        """Overrides the base class virtual method with new behavior."""
        super(self).increase_value(1)
        return self.value > 0

    def increment_and_print_value(self):
        """Increments the value and prints to console."""
        increase_value(1)
        print(self.value)
