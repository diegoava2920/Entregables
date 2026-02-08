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
    

def body_rent_validations(body_dir):
    if "car_id" not in body_dir:
        raise ValueError("No se agrego el carro")
    if "user_id" not in body_dir:
        raise ValueError("No se agrego el usuario")
    
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