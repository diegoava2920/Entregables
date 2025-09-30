def bubble_sort(list):#Creacion de la funcion
    swaps = 0
    for other_index in range (0, len (list) -1 ):#Ciclo para recorrer todos los numeros de la lista

        for index in range (0, len (list) -1):#Ciclo para comparar todos los numeros de la lista con el numero mas bajo
            
            current_element = list[index]#Indice de el numero actual que se quiere mover
            next_element = list[index+1]#Indice de el numero siguiente con el que queremos comparar el actual

            print (f"Iteracion {other_index}:{index} | Elemento actual: {current_element} | Elemento siguiente: {next_element}")

            if current_element > next_element:#Condicional para comparar los numeros, en caso de que sea mayor el numero
                print(f"Elemento actual es mayor al siguiente, cambiandolos de lugar")
                list[index] = next_element
                list[index+1] = current_element
                swaps = swaps + 1

    print(f"Lista ordenada: {list}")
    print(f"Iteraciones: {other_index}")
    print(f"Intercambios: {swaps}")
    
new_list = [-4, 9, 7, 1, -8 , 4]
bubble_sort(new_list)

