class Animal:
    def __init__(self):
        pass

    def speak():
        print ("Hace un sonido")

class Perro(Animal):
    def __init__(self):
        super().__init__()
    pass

    def speak(self):
        return "Ladra"
    

class Gato(Animal):
    def __init__(self):
        super().__init__()
    pass

    def speak(self):
        return "Maulla"
    
fido = Perro()
michi = Gato()

print (fido.speak())
print (michi.speak())