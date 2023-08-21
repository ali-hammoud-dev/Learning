# student = {"name":"Rolf","grades":(89,90,100,200)}

# def average(*args):
#     return sum(args) / len(args)

# print(*student["grades"])
# print(student["grades"])
# print(average(*student["grades"]))

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print("Student 1:", student1.name, student1.age)
print("Student 2:", student2.name, student2.age)
