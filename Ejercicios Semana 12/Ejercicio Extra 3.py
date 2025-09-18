class Vehicle():
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
        pass

    def get_info(self):
        print (f"Marca: {self._brand} \n Año: {self._year}")

class Car(Vehicle):
    def __init__(self, brand, year , doors):
        self._brand = brand
        self._year = year
        self.doors = doors

    def get_info(self):
        print (f"Marca: {self._brand} \n Año: {self._year} \n Puertas: {self.doors}\n")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, types):
        self._brand = brand
        self._year = year
        self.type = types
    
    def get_info(self):
        print (f"Marca: {self._brand} \n Año: {self._year} \n Tipo: {self.type} \n")

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

vehicle1.get_info()  # Toyota (2020) - 4 puertas
vehicle2.get_info()  # Yamaha (2022) - Tipo: Deportiva