"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    Attributes:
        start (int): The number the generator should start with.
        now (int): The number after being incremented.
    
    Methods:
        __init__(self,start): Initialize the generator.
        generate(self): Increment number by 1. Returns now-1.
        reset(self): Reset now to start.
        
    Example/doctest:
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

    def __init__(self,start):
        "Initialize class"
        self.start = start
        self.now = start
    
    def generate(self):
        "Increment by one"
        self.now +=1 
        return self.now -1
    def reset(self):
        self.now = self.start


