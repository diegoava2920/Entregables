from sqlalchemy import Column, Integer, String, ForeignKey, update, delete
from EngineConnection import Base, inspector, SessionM


class Address(Base):
    __tablename__ = "address"
    __table_args__ = {"schema": "sqalchemy_test"}
    id = Column(Integer(), primary_key=True)
    userid = Column(ForeignKey("sqalchemy_test.users.id"), nullable=False)
    description = Column( String(50), nullable=False, unique=True)

    def __str__(self):
        return (f"{self.id}  {self.userid}  {self.description}")
    
    if (inspector.has_table('address', schema="sqalchemy_test")):
        print ("Ya existe la tabla de direcciones")
    else:
        print ("Se creo exitosamente la tabla de direcciones")
    

    def create_address(self, userid, description):
        try: 
            with SessionM() as session:
                new_address = Address(userid= userid, description=description)
                session.add(new_address)
                session.commit()
                print(f"Se creo una nueva direccion {description}")
                return True
        except Exception as error:
            print("Error adding the car table from the database: ", error)
            return False

    def modify_address(self, p_id, userid, description):
        try: 
            with SessionM() as session:
                session.execute(update(Address).where(Address.id == p_id).values(userid= userid, description=description))
                session.commit() 
                print(f"Se modifico la direccion {description}")
                return True
        except Exception as error:
            print("Error modifying the address table from the database: ", error)
            return False

    def delete_address(self, p_id):
        try:
            with SessionM() as session:
                session.execute(delete(Address).where(Address.id == p_id))
                session.commit()
                print(f"Se elimino la direccion {p_id}")
                return True
        except Exception as error:
            print("Error deleting the address table from the database: ", error)
            return False

    def all_address(self):
        print("\nDirecciones:")
        with SessionM() as session:
            addresses = session.query(Address).all()

            for address in addresses:
                print(address)
            return addresses