# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          you need a "class" to create an object

# class = A blueprint for creating objects
from car import Car

car1 = Car("Mustage", 2024, "Red", False)
car2 = Car("Corvette", 2023, "Black", True)
car3 = Car("Camaro", 2022, "Yellow", True
           )

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print("---------------------------------------")
print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print("---------------------------------------")
print()

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
        