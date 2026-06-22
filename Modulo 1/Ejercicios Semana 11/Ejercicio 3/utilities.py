import re
name_format = r'^[a-zA-Z\s]+$'#formato para agregar estudiantes 
grade_format = r'^(?:[1-9]|[1-9][0-9]|100)$'#formato para agregar notas
seccion_format = r'^.{4}$'#formato para agregar una seccion

def ask_info(message, format):#funcion para pedir informacion al usuario y hacer revision de formatos
    while True:
        entry = input(message)
        if re.match(format, entry):#if para comparar que el formato de la linea agregada sea compatible con el formato ya establecido
            return entry
        else:
            print("Error: La entrada no cumple con el formato requerido. Inténtelo de nuevo.")
