from Upper_and_lower import funcion_mayusuculas_y_minusculas

def test_upper_and_lower_counting_properly(capsys):
    #AAA
    #Aranmgent
    string_test = 'Mi Mama Me Mima'
    #Argument
    funcion_mayusuculas_y_minusculas(string_test)
    captured = capsys.readouterr() 
    #Assert
    assert "Mayusculas = 4" in captured.out
    assert "Minusculas = 8" in captured.out

def test_upper_and_lower_counting_no_string(capsys):
    #AAA
    #Aranmgent
    string_test = ''
    #Argument
    funcion_mayusuculas_y_minusculas(string_test)
    captured = capsys.readouterr() 
    #Assert
    assert "Mayusculas = 0" in captured.out
    assert "Minusculas = 0" in captured.out  



def test_upper_and_lower_counting_no_alphabetic(capsys):
    #AAA
    #Aranmgent
    string_test = '8D12a4F2we9'
    #Argument
    funcion_mayusuculas_y_minusculas(string_test)
    captured = capsys.readouterr() 
    #Assert
    assert "Mayusculas = 2" in captured.out
    assert "Minusculas = 3" in captured.out  
