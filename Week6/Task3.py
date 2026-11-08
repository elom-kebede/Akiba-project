class Employee:
    def __init__(self, name, salary):
        self.name  = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


Employee1 = Employee("Elias", 50000)
Manager1 = Manager("Nabe", 60000, "IT")
Developer1 = Developer("Fikadu", 70000, "Python")

Employee1.display_info()
print()
Manager1.display_info()
print()
Developer1.display_info()

