frutas = ['manzana','naranja','mora','pera'] #Definicion de la lista de frutas
colores = ['rojo','anarnajado','morado','verde']#Definicion de la lista de colores

frutas_y_colores =  { #Definicion del diccionario 
        frutas[0] : colores[0],
        frutas[1] : colores[1],
        frutas[2] : colores[2],
        frutas[3] : colores[3]
    }


for frutas, colores in frutas_y_colores.items():# for para recorrer el diccionario
    print(f'{frutas} : {colores}')# print de los valores