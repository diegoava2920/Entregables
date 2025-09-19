from datetime import datetime

def log_call(func):
    def wrapper (*args):
        date = datetime.now()
        result = func(*args)
        return print(f"| {func.__name__} | {args} | {date} |  \n| {result} |")
    return wrapper

def number(func):
    def warpper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError ("Todos los parametros deben de ser numeros")
        return func(*args)
    return warpper

@number
@log_call
def multiply(first, second):
    total = first * second
    return total

multiply("h",2)

