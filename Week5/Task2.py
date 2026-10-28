class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rec1 = Rectangle(10, 7)
rec2 = Rectangle(20, 13)

rectangles = [rec1, rec2]
for rectange in rectangles:
    print(f"Area: {rectange.area()}")
    print(f"Perimeter: {rectange.perimeter()}")
