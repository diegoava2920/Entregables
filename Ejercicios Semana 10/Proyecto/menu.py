import actions
import csv
import data


def main_menu():#funcion del menu principal 
    opcion = 0#variable que controla la opcion a elegir
    while(opcion != "7"):#while para repetir la lista hasta que el resultado sea 7 (osea la opcion de cerrado)
        try:#try para tomar cualquier error que aparezca y enviar in mensaje dependiendo de cual sea
            #Lista de opciones
            print("Bienvenido al Sistema de Control de Estudiantes!")
            print("Menu:\n")
            print("1- Agregar estudiante\n")
            print("2- Ver estudiantes\n")
            print("3- Top 3 mejores promedios\n")
            print("4- Promedio total de todos los estudiantes\n")
            print("5- Exportar archivo\n")
            print("6- Importar archivo\n")
            print("7- Salir\n")
            opcion = input("Ingrese la opcion que dese usar: ")

            #Opciones y sus respectivos calls de funciones depenediendo de cual opcion eliga
            if(int(opcion) == 1) :
                actions.add_student()
            elif(int(opcion)== 2) :
                actions.view_students()
                input ("\nPresione Enter para seguir\n")
            elif(int(opcion) == 3):
                actions.get_top_3_average()
                input ("\nPresione Enter para seguir\n")
            elif(int(opcion) == 4):
                actions.get_total_average()
                input ("\nPresione Enter para seguir\n")
            elif(int(opcion) == 5):
                data.write_csv_file("student_list.csv", actions.student_list, actions.student_porfile)
                print ("\nDatos guradados en archivo student_list.csv\n")
                input ("\nPresione Enter para seguir\n")
            elif(int(opcion) == 6):
                data.read_csv_file("student_list.csv")
                print ("\nDatos cargados desde el archivo student_list.csv\n")
                input ("\nPresione Enter para seguir\n")
            elif(int(opcion) == 7):
                print("\nAdios!\n")
            else:
                print("\nEl valor agregado es incorrecto, agregue uno nuevo (Opciones entre el 1-7)\n")
                input ("\nPresione Enter para seguir\n")
        except ValueError:#catch de error de ValueError por si el usuario intenta usar algo que no sea un numero
            print("\nEl valor agregado es incorrecto, agregue uno nuevo (Opciones entre el 1-7)\n")
            input ("\nPresione Enter para seguir\n")
        except FileNotFoundError:#catch de error de FileNotFoundError en caso de que el usuario intente cargar datos al programa sin un archivo anterirormente colocado en la carpeta
            print("\nNo hay lista disponible en el directorio que se encuentra\n")
            input ("\nPresione Enter para seguir\n")
