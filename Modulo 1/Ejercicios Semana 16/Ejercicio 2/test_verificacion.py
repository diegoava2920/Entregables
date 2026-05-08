from Verificacion import lista_numeros_primos
from Verificacion import verificacion_numeros_primos

def test_verificacion_numero_primo_recognize_prime_number():
    assert verificacion_numeros_primos(3) == 2
    assert verificacion_numeros_primos(5) == 2

def test_lista_numero_primos_no_prime_numbers():
    #AAA
    #Aranmgent
    list_test = [4, 6, 8, 10, 12]
    #Argument
    result = lista_numeros_primos(list_test)
    #Assert
    assert result == []

def test_lista_numero_primos_prime_numbers_big_list():
    #AAA
    #Aranmgent
    list_test = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10 ,11, 12 , 13 ,14 ,15 ,16 ,17 ,18 ,19 ,20]
    #Argument
    result = lista_numeros_primos(list_test)
    #Assert
    assert result == [2, 3, 5, 7, 11, 13, 17, 19 ]

