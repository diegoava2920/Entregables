libreria = ['libro','lapiz','regla']#lista de objetos no relacionados

restaurante = { #diccionario de objetos relacionados a un restaurante
    'libro' : 'el principito',
    'plato principal' : 'haburgesa',
    'fresco' : 'malteada de vainilla',
    'lapiz' : 'carbon B5',
    'acompañamiento' : 'papas',
    'regla' : '20cm'
}
#eliminacion de elementos no relacionados del diccionario
restaurante.pop(libreria[0])
restaurante.pop(libreria[1])
restaurante.pop(libreria[2])

#print del diccionario
print(restaurante)
