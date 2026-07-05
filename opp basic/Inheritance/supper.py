# super() = Function used in a child class to call methods
#           from a parent class.

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.filled = is_filled
    def describe(self):
        print(f"It is a {self.color} and {"filled" if self.filled else "not filled"}")



class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 *self.radius *self.radius}")


class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side


class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height


circle = Circle(color="Red", is_filled=True, radius=5)
circle.describe()
print(circle.color)
print(circle.filled)
print(circle.radius)

