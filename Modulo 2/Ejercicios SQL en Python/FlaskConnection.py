from flask import Flask, request, jsonify
from PgManager import PgManager
from Validations import body_user_validations, body_car_validations, body_rent_validations, change_state_car_validation, change_state_user_validation, change_state_rent_validation
from UserRepository import UserRepository
from CarRepository import CarRepository
from RentRepository import RentRepository

db_manager = PgManager(db_name="postgres", user="postgres", password="yiyito2920", host="localhost")
user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rent_repo = RentRepository(db_manager)

app = Flask(__name__)

@app.route("/RentACar/<unit>/lists", methods=["GET"])
def get_all_units(unit):
    try: 
            user_id = request.args.get("user_id")
            username = request.args.get("username")
            email = request.args.get("email")
            state = request.args.get("state")
            car_id = request.args.get("car_id")
            brand = request.args.get("brand")
            model = request.args.get("model")
            fab_year = request.args.get("fab_year")
            car_state = request.args.get("car_state")
            rent_state = request.args.get("rent_state")
            rent_date = request.args.get("rent_date")
            match (unit):
                case 'users':
                    filtered_shows = user_repo.get_all_users(user_id = user_id, username=username, email=email, state=state)
                case 'cars':
                    filtered_shows = car_repo.get_all_car(car_id=car_id, brand=brand, model=model, fab_year=fab_year, car_state=car_state)
                case 'rents':
                    filtered_shows = rent_repo.get_all_rents(user_id=user_id, car_id=car_id, rent_state=rent_state, rent_date=rent_date)
                case _:
                    raise ValueError("No existe una unidad para listar")
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500

    return {"data": filtered_shows}


@app.route("/RentACar/<unit>/create", methods=["POST"])
def create_new_unit(unit):
    request_body = request.json
    try: 
            if not request_body:
                raise ValueError ("No se agrego ningun entry para agregar")
            match (unit):
                case 'user':
                    body_user_validations(request_body)
                    if(user_repo.create_user(request_body['fullname'], request_body['email'], request_body['username'], request_body['passwrd'], request_body['bday'], request_body['account_state']) == True):
                        return "Usuario agregado", 200
                    else:
                        raise ValueError("Hubo un error agregando al usuario, favor revisar la base de datos")
                case 'car':
                    body_car_validations(request_body)
                    if(car_repo.create_car(request_body['brand'], request_body['model'], request_body['fab_year'], request_body['car_state'])==True):
                        return "Auto agregado", 200
                    else:
                        raise ValueError("Hubo un error creando la nueva renta, favor revisar la base de datos")
                case 'rent':
                    body_rent_validations(request_body)
                    if(rent_repo.create_rent(int(request_body['car_id']), int(request_body['user_id'])) == True ):
                        return "Rentra creada", 200
                    else:
                        raise ValueError("Hubo un error creando la nueva renta, favor revisar la base de datos")
                case _:
                    raise ValueError("No existe una unidad modificable con ese nombre")
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    


@app.route("/RentACar/<unit>/update_status", methods=["PATCH"])
def update_unit(unit):
    request_body = request.json
    try: 
            if not request_body:
                raise ValueError ("No se agrego ningun entry para agregar")
            match (unit):
                case 'user':
                    change_state_user_validation(request_body)
                    if(user_repo.update_user_status(request_body['user_id'], request_body['account_state']) == True):
                        return "Estado de usuario actualizado", 200
                    else:
                        raise ValueError("Hubo un error actualizando al usuario, favor revisar la base de datos")
                case 'car':
                    change_state_car_validation(request_body)
                    if(car_repo.update_car_status(request_body['car_id'], request_body['car_state']) == True):
                        return "Estado de auto actualizado", 200
                    else:
                        raise ValueError("Hubo un error actualizando al usuario, favor revisar la base de datos")
                case 'rent':
                    print(request_body)
                    change_state_rent_validation(request_body)
                    if(rent_repo.update_rent_status(request_body['rent_id'], request_body['rent_state']) == True):
                        return "Estado de renta actualizado", 200
                    else:
                        raise ValueError("Hubo un error actualizando al usuario, favor revisar la base de datos")
                case _:
                    raise ValueError("No existe una unidad modificable con ese nombre")
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    

@app.route("/RentACar/rent/completed_rent", methods=["PATCH"])
def completed_rent():
    request_body = request.json
    try: 
            if not request_body:
                raise ValueError ("No se agrego ningun entry para agregar")
            if 'rent_id' not in request_body:
                raise ValueError("No se agrego el id de la renta")
            if(rent_repo.car_devolution(request_body['rent_id']) == True):
                return "Carro devuelto", 200
            else:
                raise ValueError("Hubo un error en la devolucion del auto, favor revisar la base de datos")
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    
@app.route("/RentACar/rent/new_defaulter", methods=["PATCH"])
def new_defaulter():
    request_body = request.json
    try: 
            if not request_body:
                raise ValueError ("No se agrego ningun entry para agregar")
            if 'rent_id' not in request_body:
                raise ValueError("No se agrego el id de la renta")
            if(rent_repo.set_defaulter(request_body['rent_id']) == True):
                return "Moroso agregado", 200
            else:
                raise ValueError("Hubo un error en la devolucion del auto, favor revisar la base de datos")
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    

    

if __name__ == "__main__":
    app.run(host="localhost", debug=True)

