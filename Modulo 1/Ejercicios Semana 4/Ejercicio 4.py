#Declarar variables
lista_numeros = [1 , 2 , 3] #Contador de los 3 numeros
mayor = 0 #Checkpoint del numero mayor
#For para recorrer la lista de los 3 numeros
for contador in lista_numeros :
    numero = int (input ( f'ingrese el numero {contador} :'))#Peticion del dato del numero al usuario
    if (numero > mayor):#If para determinar si el numero agregado es mayor al numero mayor actual o no
        mayor = numero
#Prints
print(f'El numero mayor es: {mayor} ')