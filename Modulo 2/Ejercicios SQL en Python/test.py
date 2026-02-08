from PgManager import PgManager
from Persistency import read_file
from UserRepository import UserRepository
from CarRepository import CarRepository
from RentRepository import RentRepository

user_list = read_file("users.json")
car_list = read_file("cars.json")

db_manager = PgManager(db_name="postgres", user="postgres", password="yiyito2920", host="localhost")
user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rent_repo = RentRepository(db_manager)

#user_repo.create_new_user_table()
#car_repo.create_new_car_table()
#rent_repo.create_new_rent_table()


rent_repo.create_rent(1, 4)