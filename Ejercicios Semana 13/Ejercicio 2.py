def number(func):
    def warpper(*args, **kwargs):

        new_args = []
        new_kwargs = {}

        for arg in args:
            new_args.append(convert_number(arg))

        for k, v in kwargs.items():
            new_kwargs[k] = convert_number(v)

        return func(*new_args, **new_kwargs)
    return warpper
        
def convert_number(value):
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                raise (ValueError(f"Alguno de los valores ({value}) no es un número válido"))

@number
def suma(first, second):
    total = first + second
    return total
    

total = suma (first="2", second="2")
#total = suma (first="1", second="h")
total1 = suma (2, 5)

print (f"{total}")
print (f"{total1}")
