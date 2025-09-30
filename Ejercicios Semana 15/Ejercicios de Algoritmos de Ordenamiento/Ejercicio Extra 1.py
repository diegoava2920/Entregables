class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def node_list(self):#Metodo para crear una lista 
        nodes = []#Variable para alacenar la lista
        current_node = self.head#Pointer para recorrer la lista desde el inicio
        while current_node is not None:#Mientras el current node no sea None
            nodes.append (current_node)#A la variable que alacena las listas, se le agrega el nodo actual
            current_node = current_node.next#El nodo actual se vuelve el siguiente nodo y se reinicia el ciclo
        return nodes 

forth_node = Node(4)
third_node = Node(5, forth_node)
second_node = Node(3, third_node)
first_node = Node(7, second_node)

linked_list = LinkedList(first_node)

def bubble_sort(list):#Creacion de la funcion

    for other_index in range (0, len (list) -1 ):#Ciclo para recorrer todos los numeros de la lista

        for index in range (0, len (list) -1):#Ciclo para comparar todos los numeros de la lista con el numero mas bajo

            current_element = list[index]#Indice de el numero actual que se quiere mover
            next_element = list[index+1]#Indice de el numero siguiente con el que queremos comparar el actual

            print (f"Iteracion {other_index}:{index} | Elemento actual: {current_element.data} | Elemento siguiente: {next_element.data}")

            if current_element.data > next_element.data:#Condicional para comparar los numeros, en caso de que sea mayor el numero
                print(f"Elemento actual es mayor al siguiente, cambiandolos de lugar")
                list[index] = next_element
                list[index+1] = current_element

bubble_sort(linked_list.node_list())