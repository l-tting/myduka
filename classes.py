class Person:
    def __init__(self,name,age,height,address,is_married):
        self.name = name #person1.name = "Alice"
        self.age = age #person1.age = 25
        self.height = height #person1.height = "170cm"
        self.address = address
        self.is_married = is_married #person1.is_married = False

    def greet(self):
        return f"Hi my name is {self.name}"


person1 = Person("Alice",25,"170cm","Kimathi St",False)
person2 = Person("Alvin",20,"178cm","Kimathi St",False)
print(person1)
print(type(person1))
print(person1.name) 
print(person1.address)

print(person1.greet())
print(person2.greet())