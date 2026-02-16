from sqlalchemy import Column, Integer, String, ForeignKey, update, delete
from EngineConnection import session, Base


class Car(Base):
    __tablename__ = "cars"
    __table_args__ = {"schema": "sqalchemy_test"}
    id = Column(Integer(), primary_key=True)
    userid = Column(ForeignKey("sqalchemy_test.users.id"))
    brand = Column( String(50), nullable=False, unique=True)

    def __str__(self):
        return (f"{self.id}  {self.userid}  {self.brand}")
    

    def create_car(userid, brand):
        try:    
            new_user = Car(userid= userid, brand=brand)
            session.add(new_user)
            session.commit()
            return "Se creo un nuevo carro"
        except Exception as error:
            print("Error adding the car table from the database: ", error)
            return False
    
    def modify_car(id, userid, brand):
        try:  
            session.execute(update(Car).where(Car.id == id).values(userid= userid, brand=brand))
            session.commit() 
            return "Se modifico el carro"
        except Exception as error:
            print("Error modifying the car table from the database: ", error)
            return False
    
    def delete_car(id):
        try:  
            session.execute(delete(Car).where(Car.id == id))
            session.commit() 
            return "Se elimino el carro"
        except Exception as error:
            print("Error deleting the car table from the database: ", error)
            return False

    def add_user_to_car(p_id, userid):
        try:
            session.execute(update(Car).where(Car.id == p_id).values(userid = userid))
            session.commit()
            return "Se agrego el usuario al carro"
        except Exception as error:
            print("Error modifying the car table from the database: ", error)
            return False
    
    def all_cars():
        cars = session.query(Car).all()

        for car in cars:
            print(car)

        return cars