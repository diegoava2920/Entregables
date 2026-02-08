from UserRepository import UserRepository
from CarRepository import CarRepository

class RentRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.user_repo = UserRepository(db_manager)
        self.car_repo = CarRepository(db_manager)
        pass

    def _format_rent(self, rent_record):
        return{
            "rent_id":rent_record[0],
            "car_id":rent_record[1],
            "user_id":rent_record[2],
            "rent_date":rent_record[3],
            "rent_state":rent_record[4]
        }
    
    def create_new_rent_table(self):
        try:
            self.db_manager.execute_query(
                "CREATE TABLE lyfter_car_rental.car_rent( rent_id SERIAL PRIMARY KEY NOT NULL, car_id INT REFERENCES lyfter_car_rental.cars(car_id), user_id INT REFERENCES lyfter_car_rental.users(user_id), rent_date DATE DEFAULT CURRENT_DATE, rent_state VARCHAR (30))",
            )
            return True
        except Exception as error:
            print("Error getting the rent table from the database: ", error)
            return False
    
    def get_a_rent(self, rent_id):
        try:
            results = self.db_manager.execute_query(
                "SELECT rent_id, car_id, user_id, rent_date, rent_state FROM lyfter_car_rental.car_rent WHERE rent_id = %s;",
                rent_id,
            )
            formatted_results = [self._format_rent(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting the rent from the database: ", error)
            return False
        
    def get_all_rents(self, user_id=None, car_id= None, rent_date=None, rent_state=None):
        try:
            query = (
                "SELECT rent_id, car_id, user_id, rent_date, rent_state FROM lyfter_car_rental.car_rent WHERE 1=1"
            )

            params = []
            
            if user_id:
                query += " AND user_id = %s"
                params.append(f"%{user_id}%")

            if car_id:
                query += " AND user_id = %s"
                params.append(f"%{car_id}%")

            if rent_date:
                query += " AND rent_date = %s"
                params.append(f"%{rent_date}%")

            if rent_state:
                query += " AND rent_state = %s"
                params.append(f"%{rent_state}%")
            
            results = self.db_manager.execute_query(query, tuple(params))
        
            formatted_results = [self._format_rent(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting the rent from the database: ", error)
        return False

    def create_rent(self, car_id, user_id):
        try:
            print(car_id)
            print(user_id)
            if(self.user_repo.validate_an_active_user(user_id) == True and self.car_repo.validate_an_available_car(car_id)==True):
                self.db_manager.execute_query(
                    "INSERT INTO lyfter_car_rental.car_rent ( car_id, user_id, rent_state) VALUES (%s, %s, 'ON_GOING')",
                    car_id, 
                    user_id,
                )
                self.car_repo.update_car_status(car_id, 'IN_RENT')
                print("Rent inserted successfully")
                return True
            else:
                raise ValueError("El usuario o el auto que agrego no esta disponible para ser alquilado, por favor verifique")
        except Exception as error:
            print("Error inserting the rent into the database: ", error)
            return False
        
    def update_rent_status(self, rent_id, rent_state):
        try:
            self.db_manager.execute_query(
                "UPDATE  lyfter_car_rental.car_rent SET rent_state = %s WHERE rent_id = %s",
                rent_state,
                rent_id, 
            )
            print("Rent updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False
    
    def car_devolution(self, rent_id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.car_rent SET rent_state = 'COMPLETEDE' WHERE rent_id = %s",
                rent_id,
            )
            carid = self.get_a_rent(rent_id)
            self.car_repo.update_car_status(carid[0]['car_id'], 'AVAILABLE')
            print("Car devolution completed")
            return True
        except Exception as error:
            print("Error while processing devolution from the database: ", error)
            return False
    
    def set_defaulter(self, rent_id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.car_rent SET rent_state = 'IN_DEBT' WHERE rent_id = %s",
                rent_id,
            )
            userid = self.get_a_rent(rent_id)
            self.user_repo.update_user_status(userid[0]['user_id'], 'DEFAULTER')
            carid = self.get_a_rent(rent_id)
            self.car_repo.update_car_status(carid[0]['car_id'], 'IN_DEBT')
            print("Defaulter set completed")
            return True
        except Exception as error:
            print("Error while processing defaulter from the database: ", error)
            return False