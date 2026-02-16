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
    