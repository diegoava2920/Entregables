import csv
import actions
from Student import Student

def write_csv_file(file_path, data, headers):#funcion para escribir un file de csv 
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        dictionary = []#lista que contendra los dicionarios
        for item in data:#ciclo que crea un dicionarion en caso que lo agregado sea un objecto, si es una lista, lo deja tal cual es
            if hasattr(item, 'create_directory'):# condicional que revisa si el item, en este caso el objeto, tiene un metodo "create_directory"
                dictionary.append(item.create_directory())#se le agrega a la lista el objeto pasado por el metodo para cambiarlo a dicionario
            else:
                dictionary.append(item)#se le agrega el dicionario a la lista 
        writer.writerows(dictionary)

def read_csv_file(file_path):#funcion para leer un file de csv dentro de la pc 
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for query in reader:
            newStudent = Student(query['Nombre'],query['Seccion'],query['Espanol'],query['Ingles'],query['Sociales'],query['Ciencias'])
            actions.student_list.append(newStudent)

