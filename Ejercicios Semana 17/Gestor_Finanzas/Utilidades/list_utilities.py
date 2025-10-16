#Utilidades para convertir listas de un formato a otro segun lo que requiera el programa
import Gestor_Finanzas.Clases.category#Import de la clase categorias 
import Gestor_Finanzas.Clases.movments#Import de la calse movimientos

#Metodo para convertir un directorio de listas en una lista de objetos movment, recibe como parametro el directorio a cambiar
def convert_directory_list_to_movment_list(directory):
    names = directory["Nombre"]#Variable que recibe la lista de los nombres
    amounts = directory["Monto"]#Variable que recibe la lista de los montos
    categories = directory["Categoria"]#Variable que recibe la lista de las categorias
    types = directory["Tipo"]#Variable que recibe la lista de los tipos
    dates = directory["Fecha"]#Variable que recibe la lista de las fecahs
    #Variable que recibe una lista de comprensiones de objetos movment, esta lista recorre cada valor dentro de las tulpas creada 
    #En base a cada iteracion de cada lista que habia dentro del directorio que se recibe como parametro, toma cada valor de la 
    #Iteracion y crea un objeto utilizando esos valores
    object_list = [Gestor_Finanzas.Clases.movments.Movment(name, amount, category, typs, dates) for name, amount, category, typs, dates in zip(names, amounts, categories, types, dates)]
    return object_list#retorna la lsita de objetos movment

def convert_movment_list_to_directory_list(objects):#Metodo para convertir una lista de objetos movment a directorio de listas, recibe como parametro la lista de objetos
    return {#Retorno del directorio
        #Crea un key para el nombre y una lista de comprension, que recorre todos los objetos y guarda los atributos que se llamen 'name'
        'Nombre': [str(obj.name) for obj in objects],
        #Crea un key para el monto y una lista de comprension, que recorre todos los objetos y guarda los atributos que se llamen 'amount'
        'Monto': [obj.amount for obj in objects],
        #Crea un key para la categoria y una lista de comprension, que recorre todos los objetos y guarda los atributos que se llamen 'category'
        'Categoria': [str(obj.category) for obj in objects],
        #Crea un key para el tipo y una lista de comprension, que recorre todos los objetos y guarda los atributos que se llamen 'types'
        'Tipo': [str(obj.types) for obj in objects],
        #Crea un key para la fecha y una lista de comprension, que recorre todos los objetos y guarda los atributos que se llamen 'typdatees'
        'Fecha' : [str(obj.date) for obj in objects]
    }

#Metodo para convertir un directorio de listas en una lista de objetos category, recibe como parametro el directorio a cambiar
def convert_directory_list_to_category_list(directory):
    ids = directory["ID"]#Variable que recibe la lista de los ids
    names = directory["Nombre"]#Variable que recibe la lista de los nombres
    #Variable que recibe una lista de comprensiones de objetos category, esta lista recorre cada valor dentro de las tulpas creada 
    #En base a cada iteracion de cada lista que habia dentro del directorio que se recibe como parametro, toma cada valor de la 
    #Iteracion y crea un objeto utilizando esos valores
    object_list = [Gestor_Finanzas.Clases.category.Category(id, name) for id, name in zip(ids, names)]
    return object_list #Retorno de la lista de objetos category

def convert_category_list_to_directory_list(objects):#Metodo para convertir una lista de objetos category a directorio de listas, recibe como parametro la lista de objetos
    return {#Retorno del directorio 
        'ID': [str(obj.id) for obj in objects],#Crea un key para el id y una lista de comprension, que recorre todos los objetos y guarda los atributos que se llamen 'id'
        'Nombre': [obj.name for obj in objects]#Crea un key para el nombre y una lista de comprension, que recorre todos los objetos y guarda los atributos que se llamen 'name'
    }