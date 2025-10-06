

def lista_numeros_primos(test_list):#definicion de la funcion para generar una lista de solo los numeros primos con parametro de una lista ya definida
    nueva_lista = []#variable para contener la nueva lista
    for index in range(0, len(test_list)):#for para recorrer la lista del parametro
        if(verificacion_numeros_primos(test_list[index]) == 2 ):#if para verificar si el numero de la lista es primo o no
            nueva_lista.append(test_list[index])#append para agregar el numero en la lista 
    return(nueva_lista)#return de la funcion con la lista de numeros primos

def verificacion_numeros_primos(numero):#definico de la funcion para verificar si los numeros son primos o no en base a cuantos divisores tiene
    divisores = 0#variable contador para ver la cantidad de divisores que el numero tiene
    for index in range (0, numero):# for para recorrer todos los numeros del 0 hasta el numero que se esta evaluando
        if(numero % (index+1) == 0):#if para verificar si el residuo de la division es 0
            divisores += 1#agregar un +1 al contador de divisores

    return(divisores)#return con la cantidad de divisores que tiene un numero
