numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]#generacion de lista de numeros del 1 al 20

for index in range(0, len(numeros)):#for para recorrer toda la lista
	if((numeros[index]%2) == 0 ):#if para separar los numeros pares de los impraes segun su reciduo
	    print(f'{numeros[index]}')#print de la lista 