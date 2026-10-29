class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price {self.price}, Quantity {self.quantity}"

    def total_value(self):
        return self.price * self.quantity

product1 = Product("pen", 25, 3)
product2 = Product("phone", 30000, 2)
product3 = Product("shoes", 5000, 1)

print(product1)
print(product2)
print(product3)

print(product1.name, ":", product1.total_value(), "Birr")
print(product2.name, ":", product2.total_value(), "Birr")
print(product3.name, ":", product3.total_value(), "Birr")
