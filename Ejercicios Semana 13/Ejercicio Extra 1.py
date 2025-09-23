def repeat_twice(func):
    def wrapper (*args):
        result1 = func(*args)
        result2 = func(*args)
        return result2
    return wrapper


@repeat_twice
def hello_name(name):
    print (f"Hola {name}")

diego = hello_name("Diego")