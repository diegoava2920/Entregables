import json
lista_pokemones = []

with open('lista_pokemones.json', 'r') as file:
    lista_pokemones = json.load(file)

def revisar_lista():
    return (f'\n{lista_pokemones}')

def agregar_pokemon():
    nombre = input("Ingrese el nombre del Pokémon: \n")
    tipo = input("Ingrese el tipo del Pokémon: \n")
    hp = input("Ingrese la vida base: \n")
    att = input("Ingrese ataque base: \n")
    defn = input("Ingrese defensa base: \n")
    sp_att = input("Ingrese ataque especial base: \n")
    sp_defn = input("Ingrese defensa especial base: \n")
    vel = input("Ingrese velocidad base: \n")
    
    nuevo_pokemon = {
        'Nombre': {
            "Nombre": nombre,
            "Tipo": tipo,
            "Base":{
                "HP" : hp,
                "Att" : att,
                "Defn" : defn,
                "Sp_att" : sp_att,
                "Sp_def" : sp_defn,
                "Vel" : vel
            }
        }
    }
    lista_pokemones[nombre] = (nuevo_pokemon) 
    with open('lista_pokemones.json', 'w') as file:
        json.dump(lista_pokemones, file)

def main():
    print('\nBienvenido a la Pokedex: \n')    
    opcion = 0
    while(int(opcion) != 3):

        print('Seleccione la opcion que desea realizar: \n')
        opcion = input('1. Revisar la lista de Pokemones \n2. Agregar nuevo Pokemon \n3. Cerrar el programa: \n\n' )
        if(int(opcion) == 1):
            print (f'{revisar_lista()}\n')
        elif(int (opcion) == 2):
            agregar_pokemon()
        elif(int(opcion) == 3):
            print('\nEl programa se cerrara\nGracias por usar la Pokedex\n')
        elif():
            print('\nEl numero ingresado no es correcto, agregue un numero apropiado\n')

main() 