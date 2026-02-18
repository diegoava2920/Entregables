from EngineConnection import Base, engine
from User import User
from Cars import Car
from Address import Address

Base.metadata.create_all(engine)

new_user = User()
new_car = Car()
new_address = Address()

new_user.create_user("Diego Vargas", "d-vargas08@hotmail.com")
new_user.create_user("Manfred Calvo", "miloantares@hotmail.com")
new_user.create_user("Megan Moreira", "merixmoreira@hotmail.com")
new_user.all_users()
new_user.modify_user(1, "Armando Gonzalez", "a_gonazles80@gmail.com")
new_user.all_users()
new_user.delete_user(1)
new_user.all_users()

new_car.create_car(2, "Hyundai")
new_car.create_car(None ,"Honda")
new_car.all_cars()
new_car.modify_car(2, 2, "Ford")
new_car.all_cars()
new_car.add_user_to_car(2, 2)
new_car.delete_car(2)
new_car.all_cars()

new_address.create_address(2,"Alajuela")
new_address.create_address(3,"Heredia")
new_address.all_address()
new_address.modify_address(2, 2, "Cartago")
new_address.all_address()
new_address.delete_address(1)
new_address.all_address()


