def ordenar_string(string = 'cafe-verde-marron-turquesa-negro-azul'):#definicion de la funcion con parametro de string
    ordenar = string.split('-')#variable a la que se le asigna el string como lista y dividida con funcion split para separalas usando '-' como punto de separacion
    lista_ordenada = sorted(ordenar)#variable para tomar la lista anteriormente modificada y ordenarla en orden alfabetico
    return print('-'.join(lista_ordenada))#return print con .join para generar un string nuevo en base a la lista y que cada objeto este separado por '-'

ordenar_string()#llamado a la funcion