#imports para funcionalidades 
import random

numero_usuario = int (input("Ingrese su numero, por favor: ")) #Peticion al usuario para que agregue el numero a comparar
numero_random = random.randint(1, 10)#Generacion de un numero random del 1 al 10

while(numero_usuario != numero_random):#While para repetir el proceso hasta que el numero ingresado por el usuario es el mismo que el numero random generado
    numero_usuario = int(input ("El numero acutal no es el numero secreto, ingrese uno nuevo: "))

#Prints
print("Si, es el numero correcto!!!")



