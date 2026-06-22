import csv


lista_juegos_tab = [
	{
		'Nombre': 'Nier: Automata',
		'Genero': 'RPG',
		'Desarollador': 'PLatinum Games',
		'ESRB': 'M',
	},
	{
		'Nombre': 'MegaMan Zero',
		'Genero': 'Plataformas',
		'Desarollador': 'Capcom',
		'ESRB': 'E',
	},
	{
		'Nombre': 'Jak 3',
		'Genero': 'Aventura',
		'Desarollador': 'Naughty Dogs',
		'ESRB': 'T',
	},
]

titulos_juegos = (
	'Nombre',
	'Genero',
	'Desarollador',
	'ESRB',
)

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

write_csv_file('lista_juegos_tab', lista_juegos_tab, titulos_juegos)