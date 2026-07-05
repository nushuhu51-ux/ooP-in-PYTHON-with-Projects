# polymorphism = Greek word meaning "have many forms or faces"
#                poly = many
#                morphism = forms

#            TWO WATY TO ACHIVE POLYMORPHISM IN PYTHON
#             1.Inheritance = An object could be treated of the same type as a parent class.
#             2.Duck Typing = An object must have necessary attributes/methods to be used for a specific purpose.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
#circle = Circle()

shapes =[Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    print(f"{shape.area()}cm^2")