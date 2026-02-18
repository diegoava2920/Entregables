from Persistency import read_file
class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        pass

    def _format_user(self, user_record):

        return{
            "user_id": user_record[0],
            "fullname":user_record[1],
            "email":user_record[2],
            "username":user_record[3],
            "passwrd":user_record[4],
            "bday":user_record[5],
            "account_state": user_record[6]
        }
    
    def create_new_user_table(self):
        try:
            self.db_manager.execute_query(
                "CREATE TABLE lyfter_car_rental.users( user_id SERIAL PRIMARY KEY NOT NULL, fullname VARCHAR(50) NOT NULL, email VARCHAR(30) NOT NULL, username VARCHAR(30) NOT NULL, passwrd VARCHAR(30) NOT NULL, bday DATE NOT NULL, account_state VARCHAR(30) NOT NULL);",
            )
            user_list = read_file('users.json')
            for user in user_list:
                self.create_user(user["fullname"], user["email"], user["username"], user["passwrd"], user["bday"], user["account_state"])
            return True
        except Exception as error:
            print("Error getting the rent table from the database: ", error)
            return False

    def create_user(self, fullname, email, username, passwrd, bday, account_state):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (fullname, email, username, passwrd, bday, account_state) values (%s,%s,%s,%s,%s,%s)", 
                fullname, 
                email, 
                username, 
                passwrd, 
                bday, 
                account_state
            )
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False
        
    
    
    def update_user_status(self, user_id, account_state):
        try:
            self.db_manager.execute_query(
                "UPDATE  lyfter_car_rental.users SET account_state = %s WHERE user_id = %s",
                account_state,
                user_id, 
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False
    
    def validate_an_active_user(self, userid_renting):
        try:
            results = self.db_manager.execute_query(
                "SELECT user_id, fullname, email, username, passwrd, bday, account_state FROM lyfter_car_rental.users WHERE account_state = 'ACTIVE' AND user_id = %s;",
                userid_renting
            )
            if(not results):
                raise ValueError("No hay usuarios disponibles con ese id")
            return True
        except Exception as error:
            print("Error getting the user from the database: ", error)
            return False
        
    def get_all_users(self, user_id=None, username=None, email=None, state=None):
        try:
            query = (
                "SELECT user_id, fullname, email, username, passwrd, bday, account_state FROM lyfter_car_rental.users WHERE 1=1"
            )
            params = []
            
            if user_id:
                query += " AND user_id = %s"
                params.append(f"{user_id}")

            if username:
                query += " AND username = %s"
                params.append(f"{username}")

            if email:
                query += " AND email = %s"
                params.append(f"{email}")

            if state:
                query += " AND account_state = %s"
                params.append(f'{state}')
            print(params)
            results = self.db_manager.execute_query(query, tuple(params))

            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False