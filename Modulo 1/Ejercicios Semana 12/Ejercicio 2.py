from abc import ABC, abstractmethod
import math
class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio
        super().__init__()
    
    def calculate_area(self):
        area = math.pi * (self.radio**2)
        return area
    def calculate_perimeter(self):
        perimeter = 2 * self.radio * math.pi 
        return perimeter

class Square(Shape):
    def __init__(self, side):
        self.side = side
        super().__init__()

    def calculate_area(self):
        area = self.side * self.side
        return area

    def calculate_perimeter(self):
        perimeter = self.side + self.side + self.side + self.side
        return perimeter

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()
    
    def calculate_area(self):
        area = self.base * self.height
        return area
    
    def calculate_perimeter(self):
        perimeter = 2*(self.base + self.height)
        return perimeter

ciruclo = Circle(10)
cuadrado = Square(10)
rectangulo = Rectangle(5, 5 )

print(ciruclo.calculate_area())
print(ciruclo.calculate_perimeter())

print(cuadrado.calculate_area())
print(cuadrado.calculate_perimeter())

print(rectangulo.calculate_area())
print(rectangulo.calculate_perimeter())

