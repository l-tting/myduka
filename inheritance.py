class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return "General Sound"
    
class Dog(Animal):
    def speak(self):
        return "Barks"
    
class Horse(Animal):
    def speak(self):
        return "Neighs"
    
dog1 = Dog("Max")
print(dog1.name)
print(dog1.speak())
    
horse1 = Horse("Skip")
print(horse1.name)
print(horse1.speak())



# 2.Create a Schoo system program using Python classes to demnstraate inheritance
# -Create a parent class called Person with:
#     attributes - name , age 
#     method : displaay_info()

# -> Create child classes that inherit the parent class:
#        a)Student with:
#              -additional attributes - student_id, course
#              -override display_info() to include student_id and course
#        b)Teacher with:
#               -additional attributes - subject, salary
#               -override display_info() to include subject and salary
# -----------------school programme---------------------------



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def display_info(self):
        print(f"My name is {self.name}\nAge in years: {self.age}")

class Student(Person):
    def __init__(self, name, age,student_id,course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student Id: {self.student_id}\nCourse Name: {self.course}")
    
    def __str__(self):
        return f"Student name: {self.name}\nAge is {self.age}"
    


class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}\nSalary: {self.salary}")

    

student1 = Student("Mark",20,1,"Data Science")
print(student1) #<__main__.Student object at 0x1012d1610>
# student1.display_info()

teacher1 = Teacher("Ms. Alice",40,"Math",100000)
teacher1.display_info()


x = 5
print(x)

    
        