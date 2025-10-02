def manual_add(n):#0(1)
    result = 0#0(1)
    for i in range(1, n + 1):#0(n)
        result += i#0(1)
    return result#0(1)
#0(n)

def add_formula(n):#0(1)
    return n * (n + 1) // 2 #0(1)
#0(1)

#Se usa la segunda opcion, la primera tendria que ejecutar el bucle muchisimas veces