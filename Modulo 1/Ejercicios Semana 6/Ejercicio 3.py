def suma_lista(numeros = [1, 4, 5, 6,  7, 8]):#definicion de la funcion con parametro de una lista
    total = 0#variable para llevar la cuenta de los totales
    for index in range(0, len(numeros)):#for para recorrer la lista
        total = total + numeros[index] #suma del valor actual de la variable con el valor actual del objeto de la lista 
    return (total)#return del total

print(suma_lista())#llamado de la funcion 