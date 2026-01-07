# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method:
        Returns the sum of two numbers.
        Does not depend on class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method:
        Prints the class attribute and returns the product of two numbers.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
