numeros = []#declaracion de la lista de numeros vacia
mayor = 0 #variable para contener el numero mayor de la lista

for index in range(0, 10):#for para recorrer 10 veces 
	numeros.append (input(f'Ingrese el numero {index+1}: '))#peticion al usuario del valor a agregar
	if(int(numeros[index]) >= mayor):#if para determinar si el numero agregado es mayor al numero mayor actual
		mayor = int(numeros[index])#asignacion del numero actual a la variable mayor
print(f'{numeros} El mayor es: {mayor}')#print final de la lista con el resultado 