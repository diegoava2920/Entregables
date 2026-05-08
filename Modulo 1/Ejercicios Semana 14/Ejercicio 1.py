class Node:#Creacion de la clase nodo
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack():#Creacion de la clase Stack
    head: Node

    def __init__(self):
        self.head = None
    
    def push(self, value):#Metodo push para agregar objetos nuevos al stack
        new_node= Node(value)#Instanciacion de un nuevo nodo
        new_node.next = self.head#El valor del next se cambia para que sea el head actual
        self.head = new_node#El valor del head actual se cambia para que sea el nuevo nodo agregado
    
    def pop(self):#Metodo pop para retirar el ultimo objeto agregado al stack 
        value = self.head.data#Instanciacion de variable value para que almacene la informacion del head actual
        self.head = self.head.next#El valor del head actual se cambia por el del next
        return value

    def print_structure(self):
        current_node = self.head#Instanciacion de la variable curren node para almacenar el valor del head actual
        while current_node is not None:#While que recorre hasta que el current node no sea None
            print(current_node.data)
            current_node = current_node.next


stack = Stack()
stack.push("Diego")
stack.push("Soy")
stack.push("Hola")

print("Contenido del stack:")
stack.print_structure()

print("Pop:")
print (f"{stack.pop()}")
print("Despues de pop:")
stack.print_structure()