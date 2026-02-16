from EngineConnection import Base, inspector, engine, session
from Users import Users
from Cars import Car
from Address import Address
from TableCreation import validate_tables

validate_tables(inspector)

Base.metadata.create_all(engine)

