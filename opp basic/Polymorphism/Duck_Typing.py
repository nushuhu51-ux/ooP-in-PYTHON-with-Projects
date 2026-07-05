# "Duck Typing" = Another way to achive polymorphism besides Inheritance
#                Object must have the minimum necessary attributes/methods
#                "If it looks a duck and quacks like a duck, it must be a duck."
class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")
class Cat(Animal):
    def speak(self):
        print("MEOW!")
class Car:
    alive = False
    def speak(self):
        print("VROOM!")        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)