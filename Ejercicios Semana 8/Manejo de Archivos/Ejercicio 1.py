entradas = [] #Lista para manejar las entradas de datos
with open("Canciones.txt") as file: #open con with para abrir y cerrar directamente el file una vez usado(lista original)
    entradas = file.readlines() #agregar los datos a la lista, usando el readlines para que cada linea sea leida como un objeto de la lista
    entradas = [canciones.strip() for canciones in entradas]#strip de cada una de las lineas de la lista para remover cualquer espacio inecesario entre el inicio y el final del entry

print (f'Sin ordenar: {entradas}')#print para revisar la lista antes de ordenarla
entradas.sort()#sort para ordenar la lista por orden alfabetico
print (f'Ordenado: {entradas}')#print para revisar la lista despues de ordenarla

with open("Canciones_ordenadas.txt" , 'w') as file:#open con with para abrir y cerrar directamente el file una vez usado(lista modificada)
    for cancion in entradas:#iteracion para revisar cada entry en la lista
        file.write(cancion + '\n')#agregar un entry por linea al nuevo file
    print('Se guardo adecuadamente')#print para confirmar que todo se agrego bien
