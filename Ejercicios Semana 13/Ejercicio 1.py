
def persona(func):
    def wrapper (user, *args):
        print(f"{user.name} | { user.age}")
        result = func(user, *args)
        return result
    return wrapper
    
class User:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        pass

    @persona
    def saludo(self):
        saludo = "Hola, mucho gusto"
        return saludo


Diego = User("Diego", 25)
print (Diego.saludo())

