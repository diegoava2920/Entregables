from flask import Flask, request, jsonify
from PgManager import PgManager
from Validations import body_user_validations, body_car_validations, body_rent_validations, change_state_car_validation, change_state_user_validation, change_state_rent_validation
from UserRepository import UserRepository
from CarRepository import CarRepository
from RentRepository import RentRepository
from SpecialServices import SpecialServices

db_manager = PgManager(db_name="postgres", user="postgres", password="yiyito2920", host="localhost")

app = Flask(__name__)

@app.route("/users/<unit>", methods=["GET", "POST", "PATCH"])
def users_manage_system(unit):
    user_repo = UserRepository(db_manager)
    request_body = request.json
    try: 
            user_id = request.args.get("user_id")
            username = request.args.get("username")
            email = request.args.get("email")
            state = request.args.get("state")

            valid_units = ("lists", "create", "update")

            if (unit not in valid_units ):
                return jsonify(error="PAGE NOT FOUND" ), 404
            
            if(request.method == "GET" and unit == "lists"):
                filtered_shows = user_repo.get_all_users(user_id = user_id, username=username, email=email, state=state)
                return {"data": filtered_shows}
            
            elif(request.method == "POST" and unit == "create"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                body_user_validations(request_body)
                if(user_repo.create_user(request_body['fullname'], request_body['email'], request_body['username'], request_body['passwrd'], request_body['bday'], request_body['account_state']) == True):
                    return "Usuario agregado", 201
                else:
                    return jsonify(error="Hubo un error agregando al usuario, favor revisar la base de datos" ), 400
                    
                
            elif(request.method == "PATCH" and unit == "update"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                change_state_user_validation(request_body)
                if(user_repo.update_user_status(request_body['user_id'], request_body['account_state']) == True):
                    return "Estado de usuario actualizado", 200
                else:
                    return jsonify(error="Hubo un error actualizando al usuario, favor revisar la base de datos" ), 400
            else:
                return jsonify(error="PAGE NOT FOUND" ), 404
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500



@app.route("/cars/<unit>", methods=["GET", "POST", "PATCH"])
def cars_manage_system(unit):
    car_repo = CarRepository(db_manager)
    request_body = request.json
    try: 
            car_id = request.args.get("car_id")
            brand = request.args.get("brand")
            model = request.args.get("model")
            fab_year = request.args.get("fab_year")
            car_state = request.args.get("car_state")

            valid_units = ("lists", "create", "update")

            if (unit not in valid_units ):
                return jsonify(error="PAGE NOT FOUND" ), 404
            
            if(request.method == "GET" and unit == "lists"):
                filtered_shows = car_repo.get_all_car(car_id=car_id, brand=brand, model=model, fab_year=fab_year, car_state=car_state)
                return {"data": filtered_shows}
            
            elif(request.method == "POST" and unit == "create"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                body_car_validations(request_body)
                if(car_repo.create_car(request_body['brand'], request_body['model'], request_body['fab_year'], request_body['car_state'])==True):
                    return "Auto agregado", 201
                else:
                    return jsonify(error="Hubo un error creando la nueva renta, favor revisar la base de datos"), 400
                
            elif(request.method == "PATCH" and unit == "update"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                change_state_car_validation(request_body)
                if(car_repo.update_car_status(request_body['car_id'], request_body['car_state']) == True):
                    return "Estado de auto actualizado", 200
                else:
                    return jsonify(error="Hubo un error actualizando al usuario, favor revisar la base de datos"), 400
                
            else:
                return jsonify(error="PAGE NOT FOUND" ), 404
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    


@app.route("/rents/<unit>", methods=["GET", "POST", "PATCH"])
def rents_manage_system(unit):
    request_body = request.json
    rent_repo = RentRepository(db_manager)
    special_services = SpecialServices(db_manager)
    try: 
            rent_state = request.args.get("rent_state")
            rent_date = request.args.get("rent_date")
            car_id = request.args.get("car_id")
            user_id = request.args.get("user_id")

            valid_units = ("lists", "create", "update" , "completed_rent", "new_defaulter")

            if (unit not in valid_units ):
                return jsonify(error="PAGE NOT FOUND" ), 404
            
            if(request.method == "GET" and unit == "lists"):
                filtered_shows = rent_repo.get_all_rents(user_id=user_id, car_id=car_id, rent_state=rent_state, rent_date=rent_date)
                return {"data": filtered_shows}
            
            elif(request.method == "POST" and unit == "create"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                body_rent_validations(request_body, db_manager)
                if(rent_repo.create_rent(int(request_body['car_id']), int(request_body['user_id'])) == True ):
                        return "Rentra creada", 201
                else:
                    return jsonify(error="Hubo un error creando la nueva renta, favor revisar la base de datos" ), 400
                
            elif(request.method == "PATCH" and unit == "update"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                change_state_rent_validation(request_body)
                if(rent_repo.update_rent_status(request_body['rent_id'], request_body['rent_state']) == True):
                    return "Estado de renta actualizado", 200
                else:
                    return jsonify(error="Hubo un error actualizando al usuario, favor revisar la base de datos"), 400
                
            elif(request.method == "PATCH" and unit == "completed_rent"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                if 'rent_id' not in request_body:
                    return jsonify(error="No se agrego el id de la renta"), 422
                if(special_services.car_devolution(request_body['rent_id']) == True):
                    return "Carro devuelto", 200
                else:
                    return jsonify(error="Hubo un error en la devolucion del auto, favor revisar la base de datos" ), 400
            
            elif(request.method == "PATCH" and unit == "new_defaulter"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                if 'rent_id' not in request_body:
                    return jsonify(error="No se agrego el id de la renta"), 422
                if(special_services.set_defaulter(request_body['rent_id']) == True):
                    return "Moroso agregado", 200
                else:
                    return jsonify(error="Hubo un error en la generacion de morosos, favor revisar la base de datos" ), 400
                
            else:
                return jsonify(error="PAGE NOT FOUND"), 404
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500

if __name__ == "__main__":
    app.run(host="localhost", debug=True)

