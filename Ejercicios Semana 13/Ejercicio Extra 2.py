user_is_loged = False

def requiers_login(func):
    def wrapper (*args):
        if user_is_loged == False:
            raise TypeError ("Usuario no autenticado")
        return func(*args)
    return wrapper

@requiers_login
def view_porfile():
    print ("Mostrando perfil del usuario")


view_porfile()