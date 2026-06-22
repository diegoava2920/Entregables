from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass
    def has_permission(self):
        pass

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
    
    def get_role(self):
        print ("Usuario Admin")

    def has_permission(self, permission):
        print("El usuario Admin tiene permiso")
    
class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        print ("Usuario Regular")

    def has_permission(self, permission):
        if permission == ("read"):
            print("El usuario tiene permiso")
        else:
            print("El usuario no tiene permiso")

user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

user1.has_permission("delete")
user2.has_permission("delete")

