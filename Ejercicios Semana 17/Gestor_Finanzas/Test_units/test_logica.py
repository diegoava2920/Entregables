import sys, os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, root_dir)
from unittest.mock import patch

from Gestor_Finanzas.Utilidades import list_utilities
from Gestor_Finanzas.Clases import movments
from Gestor_Finanzas.Clases import category

def test_convert_category_list_to_directory_list_work_properly():
    category_list = [
        category.Category(1, 'Alimentos'),
        category.Category(2, 'Transporte')
    ]
    result = list_utilities.convert_category_list_to_directory_list(category_list)
    assert result == {
        'ID': ['1', '2'],
        'Nombre': ['Alimentos', 'Transporte']
    }

def test_convert_movment_list_to_directory_list_works_properly():
    movment_test = [
        movments.Movment("Café", "1000", "Alimentos", "Gasto", "01/01/2024"),
        movments.Movment("Salario", "50000", "Trabajo", "Ingreso", "05/01/2024")
    ]

    result = list_utilities.convert_movment_list_to_directory_list(movment_test)

    assert result["Nombre"] == ["Café", "Salario"]
    assert result["Monto"] == ["1000", "50000"]
    assert result["Tipo"] == ["Gasto", "Ingreso"]

