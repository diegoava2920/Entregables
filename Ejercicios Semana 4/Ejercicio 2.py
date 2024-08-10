nombre = input('Ingrese su nombre: ')#Peticion a ingresar el nombre al usuairo
apellido = input('Ingrese su apellido: ')#Peticion a ingresar el apellido al usuairo
edad = int(input('Ingrese su edad: ')) #Peticion a ingresar la edad al usuairo

#If de comparativa de edades para verificar bajo que categoria cae la persona ingresada
if(edad >=65) :
    print("es un adulto mayor")
elif(edad >= 25 and edad <65 ) :
    print("es un adulto")
elif(edad >= 18 and edad <25 ) :
    print("es un adulto joven")
elif(edad >= 13 and edad <18 ) :
    print("es un adolecente")
elif(edad >= 10 and edad <13 ) :
    print("es un preadolecente")
elif(edad >= 3 and edad <10 ) :
    print("es un niño")
else:
    print("es un bebe")
