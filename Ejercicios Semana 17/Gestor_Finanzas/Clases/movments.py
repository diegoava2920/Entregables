#Clase para crear objetos de movimiento
class Movment():#Definicion de la clase de movment 
    def __init__(self, name, amount, category, types, date):#Definicion del constructor 
        self.name = name #Asignacion del nombre
        self.amount = amount #Asignacion del monto
        self.category = category #Asignacion del categoria
        self.types = types #Asignacion del tipos
        self.date = date #Asignacion del fechas 
        pass