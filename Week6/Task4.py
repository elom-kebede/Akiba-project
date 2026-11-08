# Polymorphism in Python
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

dog = Dog()
cat = Cat()
cow = Cow()

animals = [dog, cat, cow]
for animal in animals:
    print(animal.make_sound())


# Abstraction in Python

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 10)
circle = Circle(7)

print(f"\n\nArea of rectangle: {rectangle.calculate_area()}")
print(f"Area of circle: {circle.calculate_area()}") 