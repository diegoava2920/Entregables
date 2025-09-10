from abc import ABC, abstractmethod
import math
class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio
        super().__init__()
    
    def calculate_area(self):
        area = math.pi * (self.radio**2)
        print (f"\nEl area del circulo es: {area}")
    
    def calculate_perimeter(self):
        perimeter = 2 * self.radio * math.pi 
        print (f"\nEl permitero del circulo es: {perimeter}")

class Square(Shape):
    def __init__(self, side):
        self.side = side
        super().__init__()

    def calculate_area(self):
        area = self.side * self.side
        print (f"\nEl area del cuadrado es: {area}")

    def calculate_perimeter(self):
        perimeter = self.side + self.side + self.side + self.side
        print (f"\nEl permitero del cuadrado es: {perimeter}")

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()
    
    def calculate_area(self):
        area = self.base * self.height
        print (f"\nEl area del rectangulo es: {area}")
    
    def calculate_perimeter(self):
        perimeter = 2*(self.base + self.height)
        print (f"\nEl permitero del rectangulo es: {perimeter}")

ciruclo = Circle(10)
cuadrado = Square(10)
rectangulo = Rectangle(5, 5 )

ciruclo.calculate_area()
ciruclo.calculate_perimeter()

cuadrado.calculate_area()
cuadrado.calculate_perimeter()

rectangulo.calculate_area()
rectangulo.calculate_perimeter()

