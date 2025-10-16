import sys, os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, root_dir)
from unittest.mock import patch

from datetime import datetime
from Gestor_Finanzas.Utilidades import validation_utilities

def test_ask_info_date_valid():
    # Simulamos entrada válida
    date_str = "15/10/2024"
    result = validation_utilities.ask_info_date(date_str, validation_utilities.date_format)
    assert isinstance(result, datetime)
    assert result == datetime(2024, 10, 15)

def test_ask_info_date_invalid():
    # Entrada inválida
    result = validation_utilities.ask_info_date("2024-10-15", validation_utilities.date_format)
    assert result is None

def test_ask_info_input_valid():
    with patch('Gestor_Finanzas.Utilidades.validation_utilities.sg.popup_ok') as mock_popup:
        result = validation_utilities.ask_info_input("Alimentos", validation_utilities.name_format, "Nombre")
        assert result == "Alimentos"
        mock_popup.assert_not_called()

def test_ask_info_combo_empty():
    with patch('Gestor_Finanzas.Utilidades.validation_utilities.sg.popup_ok') as mock_popup:
        result = validation_utilities.ask_info_combo(None, "Categoría")
        assert result is None
        mock_popup.assert_called_once_with("No se selecionon ningún valor para Categoría.")

def test_ask_info_date_invalid_format():
    with patch('Gestor_Finanzas.Utilidades.validation_utilities.sg.popup_ok') as mock_popup:
        result = validation_utilities.ask_info_date("2025-10-15", validation_utilities.date_format)
        assert result is None
        mock_popup.assert_called_once_with("La fecha '2025-10-15' no cumple con el formato requerido (use dd/mm/yyyy).")

def test_ask_info_popup_duplicate():
    with patch('Gestor_Finanzas.Utilidades.validation_utilities.sg.popup_get_text', return_value="Comida"), \
        patch('Gestor_Finanzas.Utilidades.validation_utilities.sg.popup_ok') as mock_popup:
        result = validation_utilities.ask_info_popup("Ingrese categoría", "Añadir", validation_utilities.name_format, ["Comida"])
        assert result is None
        mock_popup.assert_called_once()