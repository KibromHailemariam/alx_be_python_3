class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: doesn't need cls or self
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: can access class attributes via cls
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
