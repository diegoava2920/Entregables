from UserRepository import UserRepository
from CarRepository import CarRepository


def body_user_validations(body_dir):
    if "fullname" not in body_dir:
        raise ValueError("No se agrego el nombre")
    if "email" not in body_dir:
        raise ValueError("No se agrego el e-mail")
    if "username" not in body_dir:
        raise ValueError("No se agrego el username")
    if "passwrd" not in body_dir:
        raise ValueError("No se agrego la contraseña")
    if "bday" not in body_dir:
        raise ValueError("No se agrego el cumpleaños")
    if "account_state" not in body_dir:
        raise ValueError("No se agrego el estado de la cuenta")


def body_car_validations(body_dir):
    if "brand" not in body_dir:
        raise ValueError("No se agrego la marca")
    if "model" not in body_dir:
        raise ValueError("No se agrego el modelo")
    if "fab_year" not in body_dir:
        raise ValueError("No se agrego el año de fabricacion")
    if "car_state" not in body_dir:
        raise ValueError("No se agrego el estado del carro")
    

def body_rent_validations(body_dir, db_manager):
    user_repo = UserRepository(db_manager)
    car_repo = CarRepository(db_manager)
    if "car_id" not in body_dir:
        raise ValueError("No se agrego el carro")
    if "user_id" not in body_dir:
        raise ValueError("No se agrego el usuario")
    print(body_dir['user_id'])
    print(body_dir['car_id'])
    if(user_repo.validate_an_active_user(body_dir['user_id']) == False or car_repo.validate_an_available_car(body_dir['car_id'])== False):
        raise ValueError("El usuario o el auto agregado no estan disponibles")
    
def change_state_user_validation(state):
    if "account_state" not in state:
        raise ValueError("No se agrego el estado nuevo")
    if 'user_id' not in state:
        raise ValueError("No se agrego el id del usuario")
    
def change_state_car_validation(state):
    if "car_state" not in state:
        raise ValueError("No se agrego el estado nuevo")
    if 'car_id' not in state:
        raise ValueError("No se agrego el id del auto")
    
def change_state_rent_validation(state):
    if "rent_state" not in state:
        raise ValueError("No se agrego el estado nuevo")
    if 'rent_id' not in state:
        raise ValueError("No se agrego el id de la renta")   