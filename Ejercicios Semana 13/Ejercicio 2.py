def number(func):
    def warpper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError ("Todos los parametros deben de ser numeros")
        return func(*args)
    return warpper
        

@number
def suma(first, second):
    total = first + second
    return total
    

total = suma (2,4)
total2 = suma (2, "h")

print (f"{total}")
print(f"{total2}")