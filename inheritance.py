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



        
