#Clase para crear objetos de categoria
class Category():
    _next_id = 1#Contador para llevar la cuenta de los contadores de la categoria
    def __init__(self, id=None, name=None):#Contructor de categoria
        if id is None:#Validacion para revisar que el id ingresado a la categoria es nulo o no, si lo es
            self.id = Category._next_id#Se le asigna el numero actual que tiene el contador
            Category._next_id +=1#El contador se le asigna un mas 1 para el proximo objeto a crear
        else:#Si no es nulo
            self.id = int(id)#Se le asigna al objeto el ID ingresado
            Category._next_id = int(id) +1#Se le asigna mas 1 al contador de categoria
        self.name = name#Asignacion normal del nombre
    pass

