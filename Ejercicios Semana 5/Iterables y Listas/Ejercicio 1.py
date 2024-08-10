Carnes = [#generacion de list de carnes
	'Pollo',
	'Res',
	'Cerdo',
	'Pescado'
]

Vegetales = [#generacion de list de verduraas
	'Papa',
	'Yuca',
	'Zanahoria',
	'Brocoli'
]

for index in range(0, len(Carnes)):#for por indice para revisar uno por uno
	print(f'Carne: {Carnes[index]} | | Vegetales: {Vegetales[index]}')