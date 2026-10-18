class TestCase:
    def __init__(self, test_name, operation, a, b, expected):
        self.test_name = test_name
        self.operation = operation
        self.a = a
        self.b = b
        self.expected = expected

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        else:
            raise ValueError("Unsupported operation")