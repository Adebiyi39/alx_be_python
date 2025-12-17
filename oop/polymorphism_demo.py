import math


# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Example usage (optional, safe for testing)
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]

    for shape in shapes:
        print(shape.area())

