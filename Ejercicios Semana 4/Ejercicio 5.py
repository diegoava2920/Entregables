#Declarar variables
cantidad_notas = int(input('Ingrese cuantas notas va a agregar: ')) #Peticion sobre la cantidad de notas que se van a agregar
contador = 1 #Contador del while 
promedio_total = 0 #Promedio total de las notas agregadas
promedio_aprobadas = 0#Promedio total de las notas aprobadas
promedio_reprobadas = 0#Promedio total de las notas reprobadas
reprobadas = 0#Total de notas reprobadas
aprobadas = 0#Total de notas aprobadas

#While para pedir las notas y agregarlas a su respectiva seccion
while (contador <= cantidad_notas):
    nota = int(input(f'Ingrese la nota {contador}: '))# Peticion al usuario de la nota que se va a agregar
    promedio_total = promedio_total + nota #Suma total de todas las notas juntas
    if(nota >= 70): #If para verificar si la nota es aprobada o reprobada
        aprobadas = aprobadas + 1#Suma +1 a contador de notas aprobadas
        promedio_aprobadas = promedio_aprobadas + nota#Suma total de todas las notas aprobadas juntas
    else:
        reprobadas = reprobadas + 1#Suma +1 a contador de notas reprobadas
        promedio_reprobadas = promedio_reprobadas + nota#Suma total de todas las notas reprobadas juntas
    contador = contador + 1#Contador +1 para ir cerrando el ciclo

#Verificacion de que las notas no sean 0 y calculo de los promedios
if(aprobadas == 0):
    promedio_aprobadas = 0
else:    
    promedio_aprobadas = promedio_aprobadas / aprobadas #Calculo del promedio de las notas aprobadas

if(reprobadas == 0):
    promedio_reprobadas = 0
else:
    promedio_reprobadas = promedio_reprobadas / reprobadas #Calculo del promedio de las notas reprobadas

promedio_total = promedio_total / cantidad_notas  #Calculo del promedio de las notas totales

#Prints de toda la informacion agregada
print (f'Aprobadas: {aprobadas}')
print (f'Reprobadas: {reprobadas}')
print (f'Promedio aprobadas: {promedio_aprobadas}')
print (f'Promedio reprobadas: {promedio_reprobadas}')
print (f'Promedio total: {promedio_total}')
