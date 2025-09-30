def bubble_sort(list):#Creacion de la funcion

    for other_index in range (0, len (list) -1 ):#Ciclo para recorrer todos los numeros de la lista

        for index in range (0, len (list) -1):#Ciclo para comparar todos los numeros de la lista con el numero mas bajo

            current_element = list[index]#Indice de el numero actual que se quiere mover
            next_element = list[index+1]#Indice de el numero siguiente con el que queremos comparar el actual

            print (f"Iteracion {other_index}:{index} | Elemento actual: {current_element} | Elemento siguiente: {next_element}")

            if current_element > next_element:#Condicional para comparar los numeros, en caso de que sea mayor el numero
                print(f"Elemento actual es mayor al siguiente, cambiandolos de lugar")
                list[index] = next_element
                list[index+1] = current_element

def validation_list(list):
    if not list:
        print ("La lista esta vacia")
        return
    for index in range (0 , len (list)):
        current_number = list[index]
        if not isinstance (current_number, (int, float)):
            print(f"El valor {current_number} no es numerico")
            return
    bubble_sort(list)
    print(list)

test1 = []
test2 = [1, 2, 3, 4 , "a"]
test3 = [9,5,8,2,1,4,6]

validation_list(test1)
validation_list(test2)
validation_list(test3)
