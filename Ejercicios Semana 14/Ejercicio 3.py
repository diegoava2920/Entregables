#Es importante tomar en cuenta que para los arboles, se utiliza mucha recursividad del metodo, osea, correr el mismo metodo dentro de la
#Misma funcion, asi se va llendo mas arriba en el arbol para recorrer todo lo posible

class Node:#Instanciacion del nodo
    def __init__(self, data):
        self.data = data 
        self.leftChild = None # Atributo para gestionar los hijos derechos (menores)
        self.rightChild = None# Atributo para gestionar los hijos derechos (mayores)

    def insert_node(self, data):# Metodo para insterar un nodo dentro de otro nodo
        if data < self.data:# Validacion para verificar si el valor ingresado es menor al valor actual del nodo
            if self.leftChild is None:# Si es menor y ademas no tiene hijo menor
                self.leftChild = Node(data)# El valor ingresado se vuelve el hijo menor
            else:#Si no
                self.leftChild.insert_node(data)# Vuelve a correr el metodo para hacer una asignacion recursiva al hijo menor
        else:#Si el valor ingresado no es menor al valor actual 
            if self.rightChild is None:#Verifica si el hijo mayor, osea el de la derecha, existe o no, si existe
                self.rightChild = Node(data)#El valor ingresado se vuelve el hijo mayor
            else:#Si no
                self.rightChild.insert_node(data)#Vuelve a correr el metodo para hacer una asignacion recursiva al hijo mayor

class BinaryTree:# Instanciacion del arbol binario
    def __init__(self, root_value=None):
        if root_value is None:#Validacion de que el valor agregado no sea None, si lo es 
            self.root = None#La raiz sigue siendo None
        else:#Si no lo es
            self.root = Node(root_value)#La raiz se vuelve igual al valor agregado  

    def insert_tree(self, value):#Metodo para insertar un nodo dentro de un arbol
        if self.root is None:#Validacion para ver si la raiz del arbol esta vacia, si lo esta
            self.root = Node(value)#El valor de la raiz se vuelve un nodo hecho en base al valor agregado a la raiz
        else:#Si no
            self.root.insert_node(value)#El metodo se vuelve a correr a si mismo, utilizando el valor agregado hasta llegar a una raiz vacia
    
    def print(self):
        self._print_node(self.root, "")

    def _print_node(self, node, prefix):
        print(prefix + str(node.data))
        if node.leftChild is not None:
            self._print_node(node.leftChild, prefix + "L-")
        if node.rightChild is not None:
            self._print_node(node.rightChild, prefix + "R-")

tree = BinaryTree(10)
tree.insert_tree(5)
tree.insert_tree(15)
tree.insert_tree(3)
tree.insert_tree(7)
tree.insert_tree(12)
tree.insert_tree(18)
tree.insert_tree(17)
tree.insert_tree(2)
tree.insert_tree(6)
tree.print()
        