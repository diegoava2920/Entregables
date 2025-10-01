def bubble_sort(added_list):#Creacion de la funcion

    for other_index in range (0, len (added_list) -1 ):#Ciclo para recorrer todos los numeros de la lista
        changes = False
        for index in range (0, len (added_list) -1 - other_index):#Ciclo para comparar todos los numeros de la lista con el numero mas bajo

            current_element = added_list[index]#Indice de el numero actual que se quiere mover
            next_element = added_list[index+1]#Indice de el numero siguiente con el que queremos comparar el actual

            print (f"Iteracion {other_index}:{index} | Elemento actual: {current_element} | Elemento siguiente: {next_element}")

            if current_element > next_element:#Condicional para comparar los numeros, en caso de que sea mayor el numero
                print(f"Elemento actual es mayor al siguiente, cambiandolos de lugar")
                added_list[index] = next_element
                added_list[index+1] = current_element
                changes = True

        if not changes:
            return

    
new_list = [-8, 12, 9, 6, 3, 0, -3, 8, 7]
new_list2 = [1, 2 , 5, 4, 6, 3, 8, 7, 9]
bubble_sort(new_list2)
bubble_sort(new_list)

print(new_list2)
print(new_list)