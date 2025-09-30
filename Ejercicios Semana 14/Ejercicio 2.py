#Es importante ver los double ended stackts como meter bolitas por un tubo que tiene los dos lados abiertos. 
#Considerando que la izquierda es la entrada principal o de adelante (Head) y la derecha la entrada secundario o de atras (Tail)
#Si lo vemos asi, podemos ver por ejemplo que tenemos 1 bolita dentro del tubo,, luego, se ingresaron 2 bolitas, cada una por cada lado
#Tomando como referencia la bolita del medio, la bolita que entro por la izquierda es su anterior (prev) y la que entro por su derecha
#Es la next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        pass

class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None
        pass
    
    def push_left(self, data):#Metodo para agregar desde la izquierda
        new_node = Node(data) #Se instancia un nuevo nodo 
        if self.head is None: #if que revisa si el head esta vacio
            self.head = self.tail = new_node #Le asigna al head y al tail el valor del nodo instanciado al principio (new_node = Node(data))
        else:
            new_node.next = self.head# Se le asigna el valor del head actual al .next, ya que el nuevo nodo debe de reconcer al head actual como su next por orden(next por que se ingreso desde la izquierda)
            self.head.prev = new_node# Se le asigna el valor del new node al prev del head actual, ya que al agregarse un nuevo nodo, el .prev se actualiza de None a tener el valor del nodo recientemente agregado
            self.head = new_node# Se le asigna el valor del new node al head, para volverlo el head actual

    def push_right(self, data):#Metodo para agregar desde la derecha
        new_node = Node(data) #Se instancia un nuevo nodo 
        if self.tail is None: #if que revisa si el tail esta vacio
            self.head = self.tail = new_node #Le asigna al head y al tail el valor del nodo instanciado al principio (new_node = Node(data))
        else:
            new_node.prev = self.tail# Se le asigna el valor del tail actual al .prev, ya que el nuevo nodo debe de reconcer al tail actual como su prev por orden(prev por que se ingreso desde la derecha)
            self.tail.next = new_node# Se le asigna el valor del new node al next del head actual, ya que al agregarse un nuevo nodo, el .next se actualiza de None a tener el valor del nodo recientemente agregado 
            self.tail = new_node# Se le asigna el valor del new node al tails, para volverlo el tail actual
    
    def pop_left(self):#Metodo para retirar desde la izquierda
        value = self.head.data#Se instancia una variable value para el output
        self.head = self.head.next#Al head actual se le asigna el valor del next, para que se vuelva el primero del lado izquierdo
        if self.head is not None:#Condicional en caso de que no haya ningun objeto agregado al stack
            self.head.prev = None#Al prev se le asigna none, al ya que al retirar el ultimo objeto agregado del stack, no queda nada en el puesto anteriror a el (prev por que es el izquierdo)
        else:
            self.tail = None#Al tail se le agrega el none, ya que no hay ningun objeto en el stack
        
        return value

    def pop_right(self):#Metodo para retirar desde la derecha
        value = self.tail.data#Se instancia un variable vaule para el ouput
        self.tail = self.tail.prev#Al tail actual se le asigna su valor prev, para que se vuelva el primero del lado derecho
        if self.tail is not None:#Condicional en caso de que no haya ningun objeto agregado al stack
            self.tail.next = None#Al next se le asigna none, al ya que al retirar el ultimo objeto agregado del stack, no queda nada en el puesto posteriror a el (next por que es el derecho)
        else:
            self.head = None#Al head se le agrega el none, ya que no hay ningun objeto en el stack
        return value
        
    
    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next



Double = Dequeue()
Double.push_left("Soy")
Double.push_left("Hola")
Double.push_right("Diego")
Double.push_right("Mucho Gusto")

print("Contenido del Stack:")
Double.print_structure()

print("\nPop left:", Double.pop_left())
print("Pop right:", Double.pop_right())

print("\nDespués de los pops:")
Double.print_structure()


