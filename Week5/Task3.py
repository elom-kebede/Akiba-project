class Student:
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        return self.name, self.score, self.department, self.school_name

student1 = Student("ella", 90, "CS")
student2 = Student("neba", 95, "bussines")
student3 = Student("Hirut", 90, "nurse")

print("Original student information:")
print(student1.display())
print(student2.display())
print(student3.display())

student1.score = 95

print("\nAfter updating Elias's score:")
print(student1.display())
print(student2.display())
print(student3.display())

