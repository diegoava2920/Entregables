def create_product_validation(body):
    if "name" not in body:
        raise ValueError("No se agrego el nombre")
    if "date" not in body:
        raise ValueError("No se agrego la fecha")
    if "amount" not in body:
        raise ValueError("No se agrego la cantidad")
    
def update_product_validation(body):
    if "id" not in body:
        raise ValueError("No se agrego el id")
    if "name" not in body:
        raise ValueError("No se agrego el nombre")
    if "date" not in body:
        raise ValueError("No se agrego la fecha")
    if "amount" not in body:
        raise ValueError("No se agrego la cantidad")
    
def create_recipe_validation(body):
    if "user_id" not in body:
        raise ValueError("No se agrego el user_id")
    if "product_id" not in body:
        raise ValueError("No se agrego el product_id")