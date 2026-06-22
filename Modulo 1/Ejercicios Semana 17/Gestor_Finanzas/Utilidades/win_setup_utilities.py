#Utilidades relacionadas a los llamados de las ventanas del programa
import PySimpleGUI as sg#import de pysimplegui
import Gestor_Finanzas.Persistencias.persistency#Import de las persistencias #import de la clase persistencia
from datetime import datetime#import de la clase datetime
today = datetime.today()#asignacion del dia de hoy

def get_main_window(movment_table):#Metodo que retorna la configuracion de  la pantalla principal, recibe como paramtero un diccionario de listas con la informacion para llenar la tabla
    return [
            [sg.Text('Bienvenido a su gestor de finanzas', font='Default 18', justification='left')],#Texto de bienvenida
                [sg.Text('Moviminetos: ', font='Default 15')],#Texto de informacion sobre la pantalla
                #Tabla de informacion, los valores de la tabla vienen de una lista de tuplas, resultado del desempaque de los 
                # valores del diccionario de listas  y los encabezados son sus respectivos keys
                [sg.Table(values=list(zip(*movment_table.values())), headings=list(movment_table.keys()), justification='center',expand_x=True, size=(40, 20))], 
                [sg.Btn('Añadir Ingreso'), sg.Btn('Añadir Gasto'), sg.Btn('Añadir Categoria')],#Botones para añadir ingresos, gastos y categorias
                [sg.Text('Fecha Inicio'), sg.Input(key='-INICIO-')], [sg.Text('Fecha Fin'), sg.Input(key='-FIN-')],#Inputs para filtrar por fechas
                [sg.Btn('Filtrar'), sg.Btn('Limpiar Filtro')],#Botones para filtrar segun los inputs y limpiar el filtrado
                [sg.Push(), sg.Btn('Salir')]#Boton de salida
                
        ]

def get_categorias_window(): #Metodo que retorna la configuracion de  la pantalla de categorias
    category_table = Gestor_Finanzas.Persistencias.persistency.read_csv_file(r"Gestor_Finanzas\Persistencias\Categorias.csv")#Variable que contiene la lista de diccionarios con los valores de la tabla de categorias
    return [
            [[sg.Text('Categorias', font='Default 15', justification='left')],#Texto de informacion sobre la pantalla
                #Tabla de informacion, los valores de la tabla vienen de una lista de tuplas, resultado del desempaque de los 
                # valores del diccionario de listas  y los encabezados son sus respectivos keys
                [sg.Table(values=list(zip(*category_table.values())), headings=list(category_table.keys()), justification='center',expand_x=True, size=(40, 20))],
                [sg.Btn('Añadir Categoria'), sg.Btn('Volver')]#Botnoes de añadir una categoria y para volver a la pantalla principal
            ]
        ]

def get_movement_window(movment): #Metodo que retorna la configuracion de la pantalla de movimientos, que recibe de parametro el tipo de movimiento
    return [
            [ 
                [sg.Text(f"Agregar {movment}", font='Default 15', justification='left')],#Texto de informacion sobre la pantalla
                [sg.Text('Tipo: '), sg.Text(movment)],#Texto de informacion sobre la pantalla sobre su tipo de movimiento
                [sg.Text('Nombre'), sg.Input(key='-NOMBRE-') ],#Input para pedir el nombre de la categoria
                [sg.Text('Monto'), sg.Input(key='-MONTO-')],#Input para pedir el monto de la categoria
                #Combobox que contiene las categorias que ya fueron ingresadas, lee el file donde se encuentran las listas de directorios
                # de categorias, lee y llena el combo con todo bajo el key de nombre 
                [sg.Text('Categoria'),sg.Combo(Gestor_Finanzas.Persistencias.persistency.read_csv_file(r"Gestor_Finanzas\Persistencias\Categorias.csv")['Nombre'],key='-CATEGORIA-' ,readonly=True)],
                #Input para agregar la fecha, el texto por defecto es la fecha de hoy
                [sg.Text('Fecha (Formato dd/mm/yyyy)'), sg.Input(default_text= f'{today.strftime("%d/%m/%Y")}', key='-FECHA-', )],
                #Botnoes de añadir una categoria y para volver a la pantalla principal
                [sg.Btn(f'Añadir {movment}'), sg.Btn('Volver')]
            ]
        ]