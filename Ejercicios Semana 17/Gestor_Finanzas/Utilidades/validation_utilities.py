#Utilidades para validar la entrada de datos por parte de los usuarios
import re #Importacion del re
import PySimpleGUI as sg #Importacion del pysimplegui
from datetime import datetime #Importacion de datetime

name_format = r'^[a-zA-Z\s]+$' #Formato para el nombre
amount_format = r'^\d+(\.\d{1,2})?$' #Formato para el monto
date_format = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$' #Formato para la fecha
today = datetime.today() #Formato para la fecha

#Funcion para pedir informacion al usuario por medio de un popup y hacer revision de formatos y duplicados, recibiendo de parametro 
# el mensaje que se le va a enviar, el titulo del popup, el formato a revisar y la lista con la que se va a revisar el duplicado
def ask_info_popup(message, new_title, format , list):

    while True:#While que se mantiene corriendo mientras que sea verdadero
        new_info = sg.popup_get_text(message, new_title)#Variable que recibe del popup_text el texto que se va a revisar
        entry = new_info.strip()
        if entry is None:#Si el texto agregado no existe o no se agrego nada
            sg.popup("No se ingreso nueva entrada")#Se genera un popup con mensaje de error
            return None#Retorna un non
        if re.match(format, entry):#if para comparar que el formato de la linea agregada sea compatible con el formato ya establecido
            for list_index in list:#For para recorrer toda la lista 
                if entry == list_index:#Si el entry agregado en el texto es igual a el valor de la lista en el que se encuentra el for
                    sg.popup_ok("No pueden haber 2 valores con el mismo nombre, ingrese un nombre diferente")#Generea un popop de error
                    entry = None#Convierte el dato de entrada en none
                    return entry#Retorna el dato de entrada
                else:#Si no es igual
                    pass#El codigo sigue
            return entry#Retora el entry
        else:#Si el entry no cumple con el formato requerido
            sg.popup_ok("La entrada no cumple con el formato requerido")#Envia un popop de error 
            return None #Retorna none

#Funcion revisar la informacion agregada por el usuario en inputs, validar que la informacion agregada cumpla con los 
# formatos y que no este vacio, recibe como parametro el valor a analiza, el patron del formato y el nombre del key del input
#Puede retornar o un string o un none
def ask_info_input(new_info, format_pattern, field_name) -> str | None:
    value = new_info.strip()
    if not value:#Si el valor esta vacio
        sg.popup_ok(f"No se ingresó ningún valor para {field_name}.")#Generea un popop de error
        return None#Retoran un none
    if re.match(format_pattern, value):#if para comparar que el formato de la linea agregada sea compatible con el formato ya establecido
        return value#Retorna el valor en caso de que si lo cumpla
    else:#Si no cumple con el formato
        sg.popup_ok(f"El valor '{value}' no cumple con el formato requerido para {field_name}.")#Generea un popop de error
        return None#Retorna none

#Funcion que revisa si un combo dentro del programa esta vacio o no
#Puede retornar o un string o un none
def ask_info_combo(value, field_name) -> str | None :
    if not value:#Si el valor no existe o es None
        sg.popup_ok(f"No se selecionon ningún valor para {field_name}.")#Generea un popop de error
        return None#Retorna un none
    else:#En caso que si tenga valor
        return value#Retorna el valor

#Funcion revisar la informacion agregada por el usuario en inputs de fecha, validar que la informacion agregada cumpla con los 
# formatos agregados y que la fecha agregada no sea una fecha posterior a la fecha actual, recibe como parametro el valor de la fecha
# el patron del formato de la fecha 
def ask_info_date(value, format_pattern) -> str | None:
    if not value:#Si el valor de la fecha no existe o es none
        sg.popup_ok(f"No se ingresó ningún valor para la fecha.")#Generea un popop de error
        return None #Retorna none
    if re.match(format_pattern, value):#Si el valor de la fecha cumple con el patron agregado
        entered_date = datetime.strptime(value, "%d/%m/%Y")
        if entered_date > today:#Si la fecha ingresa es una fecha posterior a la fecha acutal del dia de hoy
            sg.popup(f"La fecha {value} es una fecha posterior a la fecha actual, no puede ser ingresada")#Generea un popop de error
            return None#Retorna none
        else:#Si la fecha no es posterior a la fecha de hoy
            return datetime.strptime(value,"%d/%m/%Y")#Se retorna la fecha ingresada con el formato de dd/mm/yyyy
    else:#Si la fecha no cumple con el formato agregado
        sg.popup_ok(f"La fecha '{value}' no cumple con el formato requerido (use dd/mm/yyyy).")#Generea un popop de error
        return None#Retorna none
    

    
    