from datetime import datetime

class User:
    def __init__(self, name, dateofbirth):
        self.name= name
        self.dateofbirth = datetime.strptime(dateofbirth, "%Y/%m/%d")
        self.today = datetime.today()
        pass
    
    @property
    def calculate_age(self):
        return self.today.year - self.dateofbirth.year 


Diego = User("Diego", "2000/04/29")
Manny = User("Manny", "2015/10/31")

def access(User):
    if User.calculate_age < 18 :
        print ("No tiene accesso, es menor de edad")
    else:
        print ("Aceso permitido, es mayor de edad")

access(Diego)
access(Manny)