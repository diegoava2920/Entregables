#Metodo que maneja las interfaces de las pantallas, piden los datos, maneja los botones, llena las listas
import PySimpleGUI as sg#Import de pysimeplegui
import Gestor_Finanzas.Utilidades.validation_utilities#Import de las utilidades de validacion
import Gestor_Finanzas.Persistencias.persistency#Import de las persistencias 
import Gestor_Finanzas.Clases.category#Import de la clase categorias 
import Gestor_Finanzas.Clases.movments#Import de la calse movimientos
import Gestor_Finanzas.Utilidades.list_utilities#Import de las utilidades de listas
from datetime import datetime#Import del datetime
import Gestor_Finanzas.Utilidades.win_setup_utilities#Import de las utilidades para el seteo de las pantallas
today = datetime.today()#Variable que recible la fecah de hoy como valor

#Definicion de la pantalla principal 
def main_windows_show():
    #Variable que recibe la lista de diccionarios creada en base a la lectura del archivo .csv de gestiones
    movment_table = Gestor_Finanzas.Persistencias.persistency.read_csv_file(r"Gestor_Finanzas\Persistencias\Gestion.csv")
    #Variable que contiene la pantalla principal, utilizando las utilidades de la pantalla, que reciben la lista 
    # de diccionarios para setear todos los botones, inputs y tablas con la informacion necesaria 
    window_main = sg.Window('Gestor de Finanzas', Gestor_Finanzas.Utilidades.win_setup_utilities.get_main_window(movment_table), size=(600, 600), resizable=True, finalize=True)
    while True:#While para mantener la ventana abierta
        event, values = window_main()#variables de eventos y valores que reciben las entradas de lo que suceda en la ventana
        if event in (sg.WIN_CLOSED, 'Salir'):#Si el evento es la X de salir o el boton de Salir
            break#Cierra el programa
        elif event == 'Añadir Categoria':#Si el evento es añadir categoria
            window_main.close()#Cierra la pantalla principal
            categories_windows_show()#Abre la ventana de categorias
            return#Retorna nada
        elif event == 'Añadir Ingreso':#Si el evento es añadir ingreso
            window_main.close()#Cierra la pantalla principal
            movement_windows_show('Ingreso')#Abre la ventana de movimiento con el parametro de su respectivo movimiento
            return #Retorna nada
        elif event == 'Añadir Gasto':#Si el evento es añadir gasto
            window_main.close()#Cierra la pantalla principal
            movement_windows_show('Gasto')#Abre la ventana de movimiento con el parametro de su respectivo movimiento
            return#Retorna nada
        elif event == f'Filtrar':#Si el evento es filtrar, que se encarga de filtrar por fechas
            #Variables que reciben las fechas iniciales y finales, validadas para ser apropiadas y que se utilizan para filtrar 
            start = Gestor_Finanzas.Utilidades.validation_utilities.ask_info_date(values['-INICIO-'], Gestor_Finanzas.Utilidades.validation_utilities.date_format)
            end = Gestor_Finanzas.Utilidades.validation_utilities.ask_info_date(values['-FIN-'], Gestor_Finanzas.Utilidades.validation_utilities.date_format)
            #Variable que guarda los index filtrados que se encuentran dentro de la key Fecha del directorio de listas creado al principo.
            #Esta lista de comprenciones recorre los valores de la lista asignada a la key Fecha, los enumera para generar un indice ,
            #los junta en tulpas y guarda los indices solo si el valor asignado de ese indice es mayor al start y menor al end
            filtred_directories = [list_index for list_index, list_value in enumerate(movment_table['Fecha']) if start <= datetime.strptime(list_value ,"%d/%m/%Y") <= end]
            #Variable que guarda una compresion de directorios con una comprension de listas dento de ella, esta comprension primero crea un 
            # key por cada conjunto de keys + valor que haya en el directorio de listas original, estas tiene como valor el resultado de
            # una lista de comprensiones, la cual guarda un elemento de la lista original, recorriendo unicamente los index guardados dentro de la 
            # variable creada anteriormente para filtrar
            filtred_list = {list_key: [list_value[list_index] for list_index in filtred_directories] for list_key, list_value in movment_table.items()}
            window_main.close()#Cierra la pantalla principal
            #Llamado a la pantalla principal, la configuracion de la tabla ahora recibe el directorio de listas con las fechas filtradas
            window_main = sg.Window('Gestor de Finanzas', Gestor_Finanzas.Utilidades.win_setup_utilities.get_main_window(filtred_list), size=(600, 600), resizable=True, finalize=True)
        elif event == f'Limpiar Filtro':# Si el evento es limpiar filtro
            window_main.close()# Se cierra la pantalla principal actual
            #Se llama a la pantalla principal original, con toda la info que hay en el archivo csv
            window_main = sg.Window('Gestor de Finanzas', Gestor_Finanzas.Utilidades.win_setup_utilities.get_main_window(movment_table), size=(600, 600), resizable=True, finalize=True)

#Llamado a la pantalla de categorias
def categories_windows_show():
    table_category_data= Gestor_Finanzas.Persistencias.persistency.read_csv_file(r"Gestor_Finanzas\Persistencias\Categorias.csv")#Variable que recibe el directorio de listas con las categorias
    #Variable que recibe la lista de objetos categorias hecha en base al directorio de listas creado anteriormente
    category_list = Gestor_Finanzas.Utilidades.list_utilities.convert_directory_list_to_category_list(table_category_data)
    #Creacion de la pantalla de categorias
    window_category = sg.Window('Categorias', Gestor_Finanzas.Utilidades.win_setup_utilities.get_categorias_window(), size=(500, 500), resizable=True, finalize=True )
    while True:#While para mantener la pantalla creada 
        event, value = window_category()#Asignacion de los eventos y valores de la pantalla
        if event in (sg.WIN_CLOSED, 'Volver'):#If en caso de que se presion le X o el boton de volver
            window_category.close()#Se cierra la pantalla actual
            main_windows_show()#Se abre la pantalla principal nuevamente
            break#Se rompe el while
        elif event == 'Añadir Categoria' :#Si se presiona el boton añadir categoria
            validation_check = False#Variable para manejar el while
            while validation_check == False:#Mientas que la variable sea falsa 
                #Variable que recibe como valor el texto agregado en el popup, habiendo hecho revision de formatos y existencia
                new_category = Gestor_Finanzas.Utilidades.validation_utilities.ask_info_popup("Ingrese el nombre de la categoria", "Añadir Categoria", Gestor_Finanzas.Utilidades.validation_utilities.name_format, table_category_data['Nombre'])
                if not new_category:#Si la variable no tiene valor
                    validation_check = True#La validacion se vuelve verdadera para cerrar el ciclo
                else:#Si la variable si tiene valor
                    new_category_object = Gestor_Finanzas.Clases.category.Category(None, new_category)#Se crea un nuevo objeto categoria
                    category_list.append(new_category_object)#A la lista de categorias se le agrega el objeto nuevo creado
                    #Se actualiza la informacion de la tabla de categorias, convirtiendo la lista de objetos en un directorio de listas
                    table_category_data.update (Gestor_Finanzas.Utilidades.list_utilities.convert_category_list_to_directory_list(category_list))
                    #Se guarda la tabla actualizada dentro de el archivo de categorias.csv
                    Gestor_Finanzas.Persistencias.persistency.write_csv_file(r"Gestor_Finanzas\Persistencias\Categorias.csv" , table_category_data)
                    validation_check = True#La validacion se vuelve verdadera para cerrar el ciclo
            window_category.close()#Se cierra la pantalla actual
            #Se genera una nueva pantalla de categorias con la informacion updeteada
            window_category = sg.Window('Categorias', Gestor_Finanzas.Utilidades.win_setup_utilities.get_categorias_window(), size=(500, 500), resizable=True, finalize=True )
    

def movement_windows_show(movment):#Llamado a la pantalla de movimineto, recibe como parametro el tipo de movimiento 
    movment_table_data = Gestor_Finanzas.Persistencias.persistency.read_csv_file(r"Gestor_Finanzas\Persistencias\Gestion.csv")#Variable que recibe el directorio de listas con las gestiones
    #Variable que recibe la lista de objetos movimiento hecha en base al directorio de listas creado anteriormente
    movment_list = Gestor_Finanzas.Utilidades.list_utilities.convert_directory_list_to_movment_list(movment_table_data)
    #Creacion de la pantalla de movimientos
    window_movment = sg.Window(f'{movment}', Gestor_Finanzas.Utilidades.win_setup_utilities.get_movement_window(movment), size=(500, 500), resizable=True, finalize=True )
    while True:#While para mantener la pantalla creada 
        event, values = window_movment()#Asignacion de los eventos y valores de la pantalla
        if event in (sg.WIN_CLOSED, 'Volver'):#If en caso de que se presion le X o el boton de volver
            window_movment.close()#Se cierra la pantalla actual
            main_windows_show()#Se abre la pantalla principal nuevamente
            break#Se rompe el while
        elif event == f'Añadir {movment}':#Si se presiona el boton añadir movimiento
            validation_check = False#Variable para manejar el while
            while validation_check == False :#Mientas que la variable sea falsa 
                #Variables que manejan la informacion del nombre, cantidad, categoria y fecha del objeto, cada una pasando por su 
                #Respectiva validacion de formatos, informacion legitima y existencia de la informacion
                name = Gestor_Finanzas.Utilidades.validation_utilities.ask_info_input(values['-NOMBRE-'], Gestor_Finanzas.Utilidades.validation_utilities.name_format, "Nombre")
                amount = Gestor_Finanzas.Utilidades.validation_utilities.ask_info_input(values['-MONTO-'], Gestor_Finanzas.Utilidades.validation_utilities.amount_format, "Monto")
                category = Gestor_Finanzas.Utilidades.validation_utilities.ask_info_combo(values['-CATEGORIA-'], 'Categoria')
                date = Gestor_Finanzas.Utilidades.validation_utilities.ask_info_date(values['-FECHA-'],Gestor_Finanzas.Utilidades.validation_utilities.date_format)
                if not all([name, amount, category, date]):#Si de todos las variables anteriormente generadas, alguna no tiene un valor
                    validation_check = True#La validacion se vuelve verdadera para cerrar el ciclo
                    window_movment.close()#Se cierra la pantalla actual
                    #Creacion de la pantalla de movimientos
                    window_movment = sg.Window(f'{movment}', Gestor_Finanzas.Utilidades.win_setup_utilities.get_movement_window(movment), size=(500, 500), resizable=True, finalize=True )
                else:#Si todas las variables tienen valor
                    #Se crea un nuevo objeto 
                    new_movment = Gestor_Finanzas.Clases.movments.Movment(values['-NOMBRE-'], values['-MONTO-'], values['-CATEGORIA-'], movment, values['-FECHA-'])
                    movment_list.append(new_movment)#A la lista de movimients se le agrega el objeto nuevo creado
                    #Se actualiza la informacion de la tabla de movimientos, convirtiendo la lista de objetos en un directorio de listas
                    movment_table_data = Gestor_Finanzas.Utilidades.list_utilities.convert_movment_list_to_directory_list(movment_list)
                    #Se guarda la tabla actualizada dentro de el archivo de gestiones.csv
                    Gestor_Finanzas.Persistencias.persistency.write_csv_file(r"Gestor_Finanzas\Persistencias\Gestion.csv", movment_table_data)
                    validation_check = True#La validacion se vuelve verdadera para cerrar el ciclo
                    window_movment.close()#Se cierra la pantalla actual

main_windows_show()








