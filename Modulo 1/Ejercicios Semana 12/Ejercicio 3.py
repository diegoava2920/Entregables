class Cajero:
    def __init__(self, name):
        self.name = name
        pass
    def atencion_cliente(self):
        print ("Hola, como lo puedo ayudar?")

        
class Bodegero:
    def __init__(self, name):
        self.name = name
        pass

    def manejo_producto(self):
        print ("Hay 20 manzanas")

class Acomodador:
    def __init__(self, name):
        self.name = name
        pass

    def revision_estantes(self):
        print ("Estante de comida lleno")

class Empleado(Cajero, Bodegero, Acomodador):
    def __init__(self, name):
        super().__init__(name)
        print (f"Mi nombre es {self.name}")

empleado1 = Empleado("Erick")

empleado1.manejo_producto()
empleado1.atencion_cliente()
empleado1.revision_estantes()

