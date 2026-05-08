Colores = [#declaracion de lista de colores
	'Azul',
	'Verde',
	'Morado',
	'Anaranjado',
	'Rojo',
	'Rosado',
	'Cafe',
	'Negro',
	'Blanco',
    'Celeste'
]
primer_espacio = ''#declaracion de variable para contener el primer valor de la lista
ultimo_espacio = ''#declaracion de variable para contener el ultimo valor de la lista

for index in range(0, len(Colores)):#for en indice para recorrer y seleccionar objetos dentro de la lista

    if(index == 0):#if apuntando al primer objeto de la lista para asignarle su valor a la variable primer_espacio y setear el ultimo valor como el primero
        primer_espacio = Colores[index]
        Colores[index] = Colores[len(Colores)-1]

    if(index == len(Colores)-1):#if apuntando al ultimo objeto de la lista para asignarle su valor a la variable ultimo_espacio y setear el primer valor como ultimo
        ultimo_espacio = Colores[index]
        Colores[index] = primer_espacio        
    print(f'Record {index}: {Colores[index]}')#print de toda la lista 

