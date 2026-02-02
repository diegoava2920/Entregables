def body_validations(body_dir):
    if "title" not in body_dir:
        raise ValueError("No hay nombre en el body")
    if "description" not in body_dir:
        raise ValueError("No hay descripcion en el body")
    if "state" not in body_dir:
        raise ValueError("No hay estado en el body")
    if body_dir["state"] not in ["on going", "in progress", "completed"]:
        raise ValueError("El estado no es una de las opciones correctas, por favor modifiquelo")