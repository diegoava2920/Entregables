import csv
import actions

def write_csv_file(file_path, data, headers):#funcion para escribir un file de csv dentro de la pc 
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def read_csv_file(file_path):#funcion para leer un file de csv dentro de la pc 
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for query in reader:
            actions.student_list.append(query)

