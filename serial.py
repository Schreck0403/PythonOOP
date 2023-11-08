"""Python serial number generator."""
class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start):
        """Initialize a SerialGenerator with a starting number."""
        self.start = start
        self.next_serial = start

    def generate(self):
        """Generate the next sequential number."""
        result = self.next_serial
        self.next_serial += 1
        return result

    def reset(self):
        """Reset the serial number back to the original start number."""
        self.next_serial = self.start

if __name__ == "__main":
    # Example 
    serial = SerialGenerator(start=100)
    print(serial.generate())  # Output: 100
    print(serial.generate())  # Output: 101
    print(serial.generate())  # Output: 102
    serial.reset()
    print(serial.generate())  # Output: 100


