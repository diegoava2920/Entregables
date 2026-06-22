def bubble_sort(list):#0(1) Ya que la definicion no tiene costo por si mismo

    for other_index in range (0, len (list) -1 ):#0(n)

        for index in range (0, len (list) -1):#0(n^2)

            current_element = list[index]#0(1) La posicion de la lista en Python es cosntante 
            next_element = list[index+1]#0(1) La posicion de la lista en Python es cosntante

            print (f"Iteracion {other_index}:{index} | Elemento actual: {current_element} | Elemento siguiente: {next_element}")#0(1)

            if current_element > next_element:#0(n)
                print(f"Elemento actual es mayor al siguiente, cambiandolos de lugar")#0(n)
                list[index] = next_element#0(1)
                list[index+1] = current_element#0(1)
    
new_list = [-4, 9, 7, 1, -8 , 4]#0(1)
bubble_sort(new_list)#0(n^2) Ya que tiene 2 ciclos sucediendo dentro de si

print(new_list)#0(1)