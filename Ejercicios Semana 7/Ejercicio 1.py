

def calculadora(opcion, numero_actual):
    validador = False
    if int(opcion) == 0 :      
        while(validador == False):
            numero = input('Ingrese el numero que desea sumar: ')
            try:
                numero_actual = numero_actual + int(numero)
                return (numero_actual)
                validador = True
            except:
                print('Ingrese un valor numerico adecuado')
    elif int(opcion) == 1: 
        while(validador == False):
            numero = input('Ingrese el numero que desea restar: ')
            try:
                numero_actual = numero_actual - int(numero)
                return (numero_actual)
                validador = True
            except:
                print('Ingrese un valor numerico adecuado')
    elif int(opcion) == 2: 
        while(validador == False):
            numero = input('Ingrese el numero que desea multiplicar: ')
            try:
                numero_actual = numero_actual * int(numero)
                return (numero_actual)
                validador = True
            except:
                print('Ingrese un valor numerico adecuado')
    elif int(opcion) == 3: 
        while(validador == False):
            numero = input('Ingrese el numero que desea dividir: ')
            try:
                numero_actual = numero_actual / int(numero)
                return (numero_actual)
                validador = True
            except:
                print('Ingrese un valor numerico adecuado')
    elif int(opcion) == 4: 
        print ('Valor inicial establecido')
        numero_actual = 0
        return (numero_actual)



def main():
    numero_actual = 0
    opcion = 0
    while(opcion != 5):
        try:
            print ("0 - Suma")
            print ("1 - Resta")
            print ("2 - Multiplicacion")
            print ("3 - Division")
            print ("4 - Borrar resultado")
            print ("5 - Cerrar")
            opcion = input('Ingrese la opcion que desea: ')
            if (int(opcion)<=4):
                numero_actual = calculadora(opcion, numero_actual)
                print(f'\nValor actual: {numero_actual}\n')
            elif(int(opcion)==5):
                print('Cerrando programa')
                break
            elif(int(opcion)>=6):
                print('Numero invalido, ingrese un numero valido para la lista(0-5)')
        except Exception as ex: 
            print('Valor ingresado erroneo, ingrese un numero valido para la lista(0-5)')

main()