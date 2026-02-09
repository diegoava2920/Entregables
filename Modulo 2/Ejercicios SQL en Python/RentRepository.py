class RentRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
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
                "SELECT rent_id, car_id, user_id, rent_date, rent_state FROM lyfter_car_rental.car_rent WHERE 1=1 "
            )

            params = []
            
            if user_id:
                query += " AND user_id = %s" 
                params.append(f"{user_id}")

            if car_id:
                query += " AND car_id = %s"
                params.append(f"{car_id}")

            if rent_date:
                query += " AND rent_date = %s"
                params.append(f"{rent_date}")

            if rent_state:
                query += " AND rent_state = %s"
                params.append(f"{rent_state}")
            
            results = self.db_manager.execute_query(query, tuple(params))
        
            formatted_results = [self._format_rent(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting the rent from the database: ", error)
        return False

    def create_rent(self, car_id, user_id):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.car_rent ( car_id, user_id, rent_state) VALUES (%s, %s, 'ON_GOING')",
                car_id, 
                user_id,
            )
            print("Rent inserted successfully")
            return True
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
    
    