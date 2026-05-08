
def persona(func):
    def wrapper (*args, **kwargs):
        print(f"Funcion: {func.__name__} | Arguments: {args} | Keyword Arguments: {kwargs}")
        result = func(*args, **kwargs)
        print (f"El retorno de la funcion va a ser: {result}")
        return result
    return wrapper
    

@persona
def saludo(name, age, pais):
        saludo = (f"Hola, mucho gusto, soy {name}, tengo {age} años y soy de {pais}")
        return saludo

print (saludo("Diego", 25, pais="CostaRica" ))

