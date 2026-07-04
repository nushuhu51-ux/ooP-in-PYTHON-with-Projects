# class variables = Shared among all instance of a class
#                  Defined outside the constructor
#                  Allow you to share data across all in stances of a class    


class Student:
    
    class_year = 2024
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("sami", 24)
student2 = Student("samir", 22)
student3 = Student("samuel", 23)

print(Student.num_students)
print(student1.name)
print(student1.age)
print(student1.class_year)

print(f"My graduation year of {Student.class_year}  has {Student.num_students} students in my class")
print(student1.name)
print(student2.name)
print(student3.name)
