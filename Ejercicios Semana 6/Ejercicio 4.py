def funcion_string_alrevez(string = 'mi mama me mima'):#definicion de la funcion con parametro de string 
    for char in reversed(range (0, len(string))):#for con un reversed para recorrer la cadena al reves
	    print(string [char])#print del string al reves 
print(funcion_string_alrevez())#llamado de la funcion