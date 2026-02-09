from Persistency import read_file
class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        pass

    def _format_car(self, car_record):

        return{
            "car_id": car_record[0],
            "brand":car_record[1],
            "model":car_record[2], 
            "fab_year":car_record[3],
            "car_state": car_record[4]
        }
    
    def create_new_car_table(self):
        try:
            self.db_manager.execute_query(
                "CREATE TABLE lyfter_car_rental.cars( car_id SERIAL PRIMARY KEY NOT NULL, brand VARCHAR(25) NOT NULL, model VARCHAR(25)NOT NULL, fab_year VARCHAR(4) NOT NULL, car_state VARCHAR(30)NOT NULL);",
            )
            car_list = read_file('cars.json')
            for car in car_list:
                self.create_car(car["brand"], car["model"], car["fab_year"], car["car_state"])
            return True
        except Exception as error:
            print("Error getting the car table from the database: ", error)
            return False
    
    def create_car(self, brand, model, fab_year, car_state):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (brand, model, fab_year, car_state) VALUES (%s, %s, %s, %s)",
                brand, 
                model, 
                fab_year, 
                car_state,
            )
            print("Car inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a car into the database: ", error)
            return False
    
    def validate_an_available_car(self, car_id):
        try:
            results = self.db_manager.execute_query(
                "SELECT car_id, brand, model, fab_year, car_state FROM lyfter_car_rental.cars WHERE car_state = 'AVAILABLE' AND car_id = %s;",
                car_id
            )
            if(not results):
                raise ValueError("No hay carros disponibles con ese id")
            return True
        except Exception as error:
            print("Error validating the cars from the database: ", error)
            return False
        
    def update_car_status(self, car_id, car_state):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_state = %s WHERE car_id = %s",
                car_state,
                car_id,
            )
            print("Car updated successfully")
            return True
        except Exception as error:
            print("Error updating a car from the database: ", error)
            return False
        

    def get_available_car(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT car_id, brand, model, fab_year, car_state FROM lyfter_car_rental.cars WHERE car_state = 'AVAILABLE';",
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting the car from the database: ", error)
            return False
    
    def get_rented_car(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT car_id, brand, model, fab_year, car_state FROM lyfter_car_rental.cars WHERE car_state = 'IN_RENT';"
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting the car from the database: ", error)
            return False

    def get_a_car(self, carid):
        try:
            results = self.db_manager.execute_query(
                "SELECT car_id, brand, model, fab_year, car_state FROM lyfter_car_rental.cars WHERE car_id = %s",
                carid
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting the car from the database: ", error)
            return False
        
    def get_all_car(self, car_id=None, brand=None, model=None, fab_year=None, car_state=None):
        try:
            query = (
                "SELECT car_id, brand, model, fab_year, car_state FROM lyfter_car_rental.cars WHERE 1=1 "
            )

            params = []
            
            if car_id:
                query += " AND car_id = %s"
                params.append(f"{car_id}")

            if brand:
                query += " AND brand = %s"
                params.append(f"{brand}")

            if model:
                query += " AND model = %s"
                params.append(f"{model}")

            if fab_year:
                query += " AND fab_year = %s"
                params.append(f"{fab_year}")

            if car_state:
                query += " AND car_state = %s"
                params.append(f"{car_state}")

            results = self.db_manager.execute_query(query, tuple(params))
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting the car from the database: ", error)
            return False
        