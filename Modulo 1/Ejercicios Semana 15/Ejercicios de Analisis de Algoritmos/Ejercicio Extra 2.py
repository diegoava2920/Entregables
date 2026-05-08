
def linear_search(my_list, target):#0(n)
    for item in my_list:#0(n)
        if item == target:#0(1)
            return True#0(1)
    return False#0(1)
#0(n) 


def binary_search(my_list, target):#0(log n)
    low = 0#0(1)
    high = len(my_list) - 1#0(1)
    while low <= high:#0(n)
        mid = (low + high) // 2#0(1)
        if my_list[mid] == target:#0(1)
            return True#0(1)
        elif my_list[mid] < target:#0(1)
            low = mid + 1#0(1)
        else:#0(1)
            high = mid - 1#0(1)
    return False#0(1)
#0(log n) el log por que cada uno de los pasos dentro de la funcion esta cortando a la mitad el trabajo necesario para la busqueda

#El primero se utiliza para listas en general, el segundo solo para listas ordenadas

# Si se utilizara el segundo con una lista desordenada, la funcion estaria corriendo sin sentido,
# ya que hace comparaciones sumando y restando valores, al estar desorganizados, hace que el codigo no lo pueda leer apropiadamente


