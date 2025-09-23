from datetime import datetime
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        date = datetime.now()
        result = func(*args, **kwargs)
        if args:
            print(f"Argumentos: {args}")
        if kwargs:
            print(f"Arhumentos Keyword: {kwargs}")

        print(f"| {func.__name__} | Ejecutado en: {date} | Resultado: {result} |\n")
        return result

    return wrapper

def number(func):
    @wraps(func)
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
@log_call
def multiply(first, second):
    total = first * second
    return total


multiply(2,2)
multiply(first=2, second=2)
