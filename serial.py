"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Creates the serial number to start, with default start being 100"""
        self.start = self.serial = start
        

    def generate(self):
        """Increments the serial number by one"""
        self.serial += 1
        return self.serial

    def __repr__(self):
        """Shows string representation of object"""
        return f"<SerialGenerator where start is {self.start} and the next number is {self.serial + 1}>"

    def reset(self):
        """Resets serials number to start"""
        self.serial = self.start