from sqlalchemy import Column, Integer, String, update, delete
from EngineConnection import Base, session

class Users(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "sqalchemy_test"}
    id = Column(Integer(), primary_key=True)
    fullname = Column(String(50))
    email = Column( String(50), nullable=False, unique=True)

    def __str__(self):
        return (f"{self.id}  {self.fullname}  {self.email}")


    def create_user(fullname, email):
        try:
            new_user = Users(fullname= fullname, email=email)
            session.add(new_user)
            session.commit()
            return "Se creo un nuevo usuario"
        except Exception as error:
            print("Error adding the user table from the database: ", error)
            return False
    
    def modify_user(p_id, fullname, email):
        try:    
            session.execute(update(Users).where(Users.id == p_id).values(fullname= fullname, email=email))
            session.commit() 
            return "Se modifico el usuario"
        except Exception as error:
            print("Error modifying the user table from the database: ", error)
            return False
    
    def delete_user(p_id):
        try:    
            session.execute(delete(Users).where(Users.id == p_id))
            session.commit() 
            return "Se elimino el usuario"
        except Exception as error:
            print("Error deleting the user table from the database: ", error)
            return False
    
    def all_users():
        users = session.query(Users).all()
        for user in users:
            print(user)
        return users