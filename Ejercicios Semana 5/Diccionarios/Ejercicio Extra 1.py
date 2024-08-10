ventas = [ #generacion de la lista de clientes y articulos
    {
        'fecha' : '5/6/2024',
        'email_cliente' : 'd-vargas08@hotmail.com',
        'articulo' :[
            {
                'nombre' : 'crema',
                'codigo' : 'CM542',
                'precio' : 255
            },
            {
                'nombre' : 'pasta de dientes',
                'codigo' : 'PT274',
                'precio' : 144
            },
            {
                'nombre' : 'cepillo de dientes',
                'codigo' : 'CP987',
                'precio' : 150
            }
        ],
    },
    {
        'fecha' : '5/6/2024',
        'email_cliente' : 'sergioooo0606@gmail.com',
        'articulo' :[
            {
                'nombre' : 'crema',
                'codigo' : 'CM542',
                'precio' : 255
            },
            {
                'nombre' : 'esmalte',
                'codigo' : 'EM242',
                'precio' : 100
            },
        ],
    },
    {
        'fecha' : '5/6/2024',
        'email_cliente' : 'mmoreira272004@hotmail.com',
        'articulo' : [
            {
                'nombre' : 'toallas humedas',
                'codigo' : 'TH557',
                'precio' : 300
            },
            {
                'nombre' : 'pasta de dientes',
                'codigo' : 'PT274',
                'precio' : 144
            },
            {
                'nombre' : 'esmalte',
                'codigo' : 'EM242',
                'precio' : 100
            },
        ],
    },
]

total_por_codigo = { #generacion de el diccionario
        'EM242' : 0,
        'PT274' : 0,
        'TH557': 0,
        'CM542': 0,
        'CP987': 0,
    } 

for recorrido_ventas in range(0, len(ventas)):#for para recorrer todos los objetos dentro de ventasa
    for recorrido_articulos in range (0, len(ventas[recorrido_ventas]['articulo'])):#  for para recorrer todos los articulos dentro de la venta
        for cod, precio in total_por_codigo.items():# for para recorrer todos los objetos dentro del diccionario
            if(cod == ventas[recorrido_ventas]['articulo'][recorrido_articulos]['codigo']):#if para diferenciar los codigos de articulos 
                total_por_codigo[f'{cod}'] = total_por_codigo[f'{cod}'] + ventas[recorrido_ventas]['articulo'][recorrido_articulos]['precio']# asignacion del precio
                

print (total_por_codigo)#print del diccionario