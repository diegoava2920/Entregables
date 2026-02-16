from sqlalchemy import Column, Integer, String, ForeignKey, update, delete
from EngineConnection import Base, session

class Address(Base):
    __tablename__ = "address"
    __table_args__ = {"schema": "sqalchemy_test"}
    id = Column(Integer(), primary_key=True)
    userid = Column(ForeignKey("sqalchemy_test.users.id"), nullable=False)
    description = Column( String(50), nullable=False, unique=True)

    def __str__(self):
        return (f"{self.id}  {self.userid}  {self.description}")
    
    def create_address(userid, description):
        try: 
            new_address = Address(userid= userid, description=description)
            session.add(new_address)
            session.commit()
            return "Se creo una nueva direccion"
        except Exception as error:
            print("Error adding the car table from the database: ", error)
            return False
        
    def modify_address(p_id, userid, description):
        try: 
            session.execute(update(Address).where(Address.id == p_id).values(userid= userid, description=description))
            session.commit() 
            return "Se modifico la direccion"
        except Exception as error:
            print("Error modifying the address table from the database: ", error)
            return False
        
    def delete_address(p_id):
        try:
            session.execute(delete(Address).where(Address.id == p_id))
            session.commit() 
            return "Se elimino la direccion"
        except Exception as error:
            print("Error deleting the address table from the database: ", error)
            return False
        
    def all_address():
        addresses = session.query(Address).all()

        for address in addresses:
            print(address)

        return addresses