class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"department: {self.department}")
        print()

student1 = Student("Elias", 25, "cs")
student2 = Student("neba", 22, "art")
student3 = Student("hirut", 29, "bussines")

students = [student1, student2, student3]  

for student in students:
    student.display_info()
