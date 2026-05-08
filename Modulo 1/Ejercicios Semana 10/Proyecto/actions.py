import utilities #import de las utilidades
student_list = [] #lista para guardar a los estudiantes 

student_porfile = { # template de informacion a pedir para agregar un estudiante
        'Nombre' , 'Seccion' ,'Espanol','Ingles','Sociales','Ciencias', 'Promedio'
    }



def add_student():#funcion para agregar un estudiante
    closure = 0#variable para manejar la continuidad con respecto a querer agregar mas estudiantes o no
    option = ""#variable para saber si el usuario desea continuar o no agregando mas estudiantes 
    while(closure == 0):
        name = utilities.ask_info(("\nIngrese el nombre del estudiante: "),utilities.name_format)#pregunta al usuario sobre el nombre del estudiante
        classroom = utilities.ask_info(("\nIngrese la seccion del estudiante(4 digitos): "),utilities.seccion_format)#pregunta al usuario sobre la seccion 
        spanish_grade = utilities.ask_info(("\nIngrese la nota de español: "),utilities.grade_format)#pregunta al usuario sobre la nota de español
        english_grade = utilities.ask_info(("\nIngrese la nota de ingles: "),utilities.grade_format)#pregunta al usuario sobre la nota de ingles
        history_grade = utilities.ask_info(("\nIngrese la nota de sociales: "),utilities.grade_format)#pregunta al usuario sobre la nota de sociales
        science_grade = utilities.ask_info(("\nIngrese la nota de ciencias: "),utilities.grade_format)#pregunta al usuario sobre la nota de ciencias

        new_student = { #diccionario para crear un nuevo estudiante
            "Nombre" : name,
            "Seccion" : classroom,
            "Espanol" : spanish_grade,
            "Ingles" : english_grade,
            "Sociales" : history_grade,
            "Ciencias" : science_grade,
            "Promedio" : (int(spanish_grade)+int(english_grade)+int(history_grade)+int(science_grade))/4 #calculo del promedio del estudiante 
        }
        student_list.append(new_student)#instancia para agregar un estudiante nuevo a la lista

        print("\nNuevo estudiante agregado\n")

        while(option != "N" or option != "Y"):#validacion para continuar o no agregando mas estudiantes
            option = input("\nDesea agregar uno nuevo? Y/N: ")
            if(option == "Y"):
                break
            elif(option == "N"):
                closure = 1
                break
            else:
                print("La opcion agregada no es valida")


def view_students():#funcion para revisar la lista de estudiantes
    for students in student_list:
        print(students)

def get_top_3_average():#funcion para revisar los top 3 mejores promedios
    stored_students = sorted(student_list, key=lambda x: x['Promedio'], reverse=True)#creacion de una nueva lista, con filtros para que la key promedio sea la que se use como referencia
    top3 = stored_students[:3]#creacion de una nueva lista que solo tenga los primeros 3 puestos de la lista anteriormente creada
    for students in top3:
        print(students)

def get_total_average():#funcion para revisar el promedio total de todos los estudnates 
    result = 0#variable que contiente el resultado final de la formula
    total_average = 0#varaible para saber el total de la suma de todos los promedios
    for student in student_list:
        total_average = total_average + student.get('Promedio')#formula para calcular la suma de todos los promedios
    result = total_average / (len(student_list))#formula para calcular el promedio de todos los estudiantes 
    print (f'{result}')
