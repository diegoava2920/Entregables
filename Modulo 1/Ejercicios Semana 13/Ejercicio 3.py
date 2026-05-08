from datetime import datetime

class User:
    def __init__(self, name, dateofbirth):
        self.name= name
        self.dateofbirth = datetime.strptime(dateofbirth, "%Y/%m/%d")
        pass
    
    @property
    def calculate_age(self):
        today = datetime.today()
        years = today.year - self.dateofbirth.year
        if (today.month, today.day) < (self.dateofbirth.month, self.dateofbirth.day):
            years = years -1
        return years

def adult_check(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, User) and arg.calculate_age < 18:
                raise ValueError ("El usuario debe ser mayor de edad")
        
        for val in kwargs.values():
            if isinstance(val, User) and val.calculate_age < 18:
                raise ValueError("El usuario debe ser mayor de edad")
            
        return func(*args, **kwargs)
    return wrapper


@adult_check
def access(User):
    print (f"Felicidades usuario {User.name}, tienes acceso")


Diego = User("Diego", "2000/04/29")
Manny = User("Manny", "2007/10/31")

access(Diego)
access(Manny)