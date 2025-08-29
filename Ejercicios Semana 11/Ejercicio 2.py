
class person:
    def __init__(self, name):
        self.name = name

class bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = []


    
    def add_passengers(self, person):
        if (self.max_passengers > len(self.current_passengers)):
            self.current_passengers.append(person)
            print ("Nuevo pasajero, bienvenid@!")
        else:
            print("Bus lleno")

    def remove_passengers(self, name):
        for passenger in self.current_passengers:
            if passenger.name == name:
                self.current_passengers.remove(passenger)
                print ("Pasajero bajo")
            else: 
                print ("No esta ese pasajero")

bus = bus(2)

person1 = person("Diego")
person2 = person("Sergio")
person3 = person("Manfred")

bus.add_passengers(person1)  
bus.add_passengers(person2) 
bus.add_passengers(person3)

bus.remove_passengers("Diego")