from UserRepository import UserRepository
from CarRepository import CarRepository
from RentRepository import RentRepository

class SpecialServices:

    def __init__(self, db_manager):
            self.db_manager = db_manager
            pass

    def car_devolution(self, rent_id):
            car_repo = CarRepository(self.db_manager)
            rent_repo = RentRepository(self.db_manager)
            try:
                self.db_manager.execute_query(
                    "UPDATE lyfter_car_rental.car_rent SET rent_state = 'COMPLETED' WHERE rent_id = %s",
                    rent_id,
                )
                carid = rent_repo.get_a_rent(rent_id)
                car_repo.update_car_status(carid[0]['car_id'], 'AVAILABLE')
                print("Car devolution completed")
                return True
            except Exception as error:
                print("Error while processing devolution from the database: ", error)
                return False
        
    def set_defaulter(self, rent_id):
        car_repo = CarRepository(self.db_manager)
        user_repo = UserRepository(self.db_manager)
        rent_repo = RentRepository(self.db_manager)
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.car_rent SET rent_state = 'IN_DEBT' WHERE rent_id = %s",
                rent_id,
            )
            userid = rent_repo.get_a_rent(rent_id)
            user_repo.update_user_status(userid[0]['user_id'], 'DEFAULTER')
            carid = rent_repo.get_a_rent(rent_id)
            car_repo.update_car_status(carid[0]['car_id'], 'IN_DEBT')
            print("Defaulter set completed")
            return True
        except Exception as error:
            print("Error while processing defaulter from the database: ", error)
            return False