def funcion_mayusuculas_y_minusculas(string = 'Mi Mama Me Mima'):#definicion de la funcion con un string como parametro 
    mayuscula = 0#variable contadro de mayusculas
    minuscula = 0#variable contadro de minusculas
    for char in string:#for para recorrer el string letra por letra
        if(char.isupper()):#if para verificar si la letra que esta en el string es mayuscula
            mayuscula += 1 #agregar +1 al contador de mayusculas
        elif(char.islower()):#elif para verificar si la letra que esta en el string es minuscula
            minuscula += 1#agregar +1 al contador de minusculas
    print (f'{string} || Mayusculas = {mayuscula} || Minusculas = {minuscula}')#print de la informacion del recorrido del string

print(funcion_mayusuculas_y_minusculas())#llamado de la funcion

