#Manejo de las persistencias, lectura y escritura de los archivos .csv, con modificaciones para que cuando se ingresen o escriban 
# archivos lo hagan de manera que el programa los lea sin problema
import csv#import de los archivos de csv


#Metodo para escribir archivos csv, recibe como parametro el path que se va a escribir y la lista que se va a ingresar y modificar 
# para que entre en formato de csv
def write_csv_file(file_path, list_to_change):
    #Variable que recibe lista de comprension, en base a una lista de directorios que se obtuvo de los parametros
    #Por cada valor que tenga la tulpa generada por el desempaque de los valores de la lista de directorios, se crea un 
    # directorio utilizando la key que se encuentre revisando y el valor revisado
    data_to_write = [dict(zip(list_to_change.keys(), values)) for values in zip(*list_to_change.values())]
    headers = list(list_to_change.keys())#Variable que contiene una lista creada a base de los keys dentro de la lista
    # Abrir los archivos de csv, utiliza el path agregado y le da formato al file
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)#Variable que guarda el file escreito
        writer.writeheader()#Escribe los headers del file
        writer.writerows(data_to_write)#Escrible las columnas del file

def read_csv_file(file_path):
    rows = {}#Diccionario vacio para guardar los datos por columnas
    with open(file_path, 'r', encoding='utf-8') as file:#Abre el archivo cvs y le da formato
        reader = csv.DictReader(file)#Variable que lee el archivo y lo asigna a una varialbe
        for header in reader.fieldnames:#Crea una lista por cada columna que haya en el archivo
            rows[header] = []#Crea una lista para los encabezados 
        for row in reader:#Recorre cada fila del archivo
            for key, value in row.items():#Recorre cada key y cada valor dentro de la fila del archivo
                rows[key].append(value)#Crea un dicionario de listas por cada key, agregandole el valor que encuentre
    return rows#Devuelve el dicionario de listas 


