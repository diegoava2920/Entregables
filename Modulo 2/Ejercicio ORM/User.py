from sqlalchemy import Column, Integer, String, update, delete
from EngineConnection import Base, SessionM, inspector

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "sqalchemy_test"}
    id = Column(Integer(), primary_key=True)
    fullname = Column(String(50))
    email = Column( String(50), nullable=False, unique=True)

    def __str__(self):
        return (f"{self.id}  {self.fullname}  {self.email}")
    
    if (inspector.has_table('users', schema="sqalchemy_test")):
        print ("Ya existe la tabla de usuarios")
    else:
        print ("Se creo exitosamente la tabla de usuarios")


    def create_user(self, fullname, email):
        try:
            with SessionM() as session:
                new_user = User(fullname= fullname, email=email)
                session.add(new_user)
                session.commit()
                print(f"Se creo un nuevo usuario: {fullname}")
                return True
        except Exception as error:
            print("Error adding the user table from the database: ", error)
            return False


    def modify_user(self, p_id, fullname, email):
        try:
            with SessionM() as session:    
                session.execute(update(User).where(User.id == p_id).values(fullname= fullname, email=email))
                session.commit()
                print(f"Se modifico el usuario {fullname}")
                return True
        except Exception as error:
            print("Error modifying the user table from the database: ", error)
            return False


    def delete_user(self, p_id):
        try:
            with SessionM() as session:    
                session.execute(delete(User).where(User.id == p_id))
                session.commit()
                print(f"Se elimino el usuario: {p_id}")
                return True
        except Exception as error:
            print("Error deleting the user table from the database: ", error)
            return False


    def all_users(self):
        print("\nUsuarios:")
        with SessionM() as session:
            users = session.query(User).all()
            for user in users:
                print(user)
            return users