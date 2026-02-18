from sqlalchemy import Column, Integer, String, ForeignKey, update, delete
from EngineConnection import SessionM, Base, inspector


class Car(Base):
    __tablename__ = "cars"
    __table_args__ = {"schema": "sqalchemy_test"}
    id = Column(Integer(), primary_key=True)
    userid = Column(ForeignKey("sqalchemy_test.users.id"))
    brand = Column( String(50), nullable=False, unique=True)

    def __str__(self):
        return (f"{self.id}  {self.userid}  {self.brand}")
    

    if (inspector.has_table('cars', schema="sqalchemy_test")):
        print ("Ya existe la tabla de carros")
    else:
        print ("Se creo exitosamente la tabla de carros")
    

    def create_car(self, userid, brand):
        try:
            with SessionM() as session:    
                new_user = Car(userid= userid, brand=brand)
                session.add(new_user)
                session.commit()
                print(f"Se creo un nuevo carro: {brand}")
                return True
        except Exception as error:
            print("Error adding the car table from the database: ", error)
            return False

    def modify_car(self, id, userid, brand):
        try:
            with SessionM() as session:  
                session.execute(update(Car).where(Car.id == id).values(userid= userid, brand=brand))
                session.commit()
                print(f"Se modifico el carro {id}: {userid} , {brand}")
                return True
        except Exception as error:
            print("Error modifying the car table from the database: ", error)
            return False


    def delete_car(self, id):
        try:
            with SessionM() as session:  
                session.execute(delete(Car).where(Car.id == id))
                session.commit()
                print(f"Se elimino el carro: {id}")
                return True
        except Exception as error:
            print("Error deleting the car table from the database: ", error)
            return False


    def add_user_to_car(self, p_id, userid):
        try:
            with SessionM() as session:
                session.execute(update(Car).where(Car.id == p_id).values(userid = userid))
                session.commit()
                print(f"Se agrego el usuario al carro: Usuario {userid} para Carro {p_id}")
                return True
        except Exception as error:
            print("Error modifying the car table from the database: ", error)
            return False


    def all_cars(self):
        print("\nCarros:")
        with SessionM() as session:
            cars = session.query(Car).all()

            for car in cars:
                print(car)

            return cars