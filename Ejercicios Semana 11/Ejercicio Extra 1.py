altura = 0
ancho = 0

class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = (self.width * self.height)
        return area
    
    def get_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter
    
while True:
    try:
        altura = float(input("Ingresa la altura (no negativo): "))
        if altura < 0:
            print("El número no puede ser negativo. Intenta de nuevo.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")

while True:
    try:
        ancho = float(input("Ingresa el ancho (no negativo): "))
        if ancho < 0:
            print("El número no puede ser negativo. Intenta de nuevo.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")

rectangulo = Rectangle(ancho, altura)
print (rectangulo.get_area())
print (rectangulo.get_perimeter())