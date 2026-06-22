from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import insert, select, update, delete

metadata_obj = MetaData(schema="product_managment")

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(30)),
    Column("type", String(30)),
    Column("password", String),
)

product_table = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(30)),
    Column("date", String(30)),
    Column("amount", Integer),
)

recipie_table = Table(
    "recipe",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("product_managment.users.id")),
    Column("product_id", Integer, ForeignKey("product_managment.products.id"))
    
)
class DB_Manager:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:yiyito2920@localhost:5432/postgres', echo=False)
        metadata_obj.create_all(self.engine)
        
    def insert_user(self, username, password, type):
        stmt = insert(user_table).returning(user_table.c.id).values(username=username, password=password, type=type)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(self, username, password):
        try:
            stmt = select(user_table).where(user_table.c.username == username).where(user_table.c.password == password)
            with self.engine.connect() as conn:
                result = conn.execute(stmt)
                users = result.all()

                if(len(users)==0):
                    return None
                else:
                    return users[0]
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False
        
    def get_user_by_id(self, id):
        stmt = select(user_table).where(user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users[0]
    
    def insert_product(self, name, date, amount):
        stmt = insert(product_table).returning(product_table.c.id).values(name=name, date=date, amount=amount)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return True
    
    def get_product(self, id=None, name=None, date=None, amount=None):
        try:
            stmt = select(product_table)
            filters = []

            if id:
                filters.append(product_table.c.id == id)

            if name:
                filters.append(product_table.c.name == name)
            
            if date:
                filters.append(product_table.c.date == date)
            
            if amount:
                filters.append(product_table.c.amount == amount)
            
            if filters:
                stmt = stmt.where(*filters)

            with self.engine.connect() as conn:
                result = conn.execute(stmt)
                product = result.all()

                if(len(product)==0):
                    return None
                else:
                    return [dict(row._mapping) for row in product]
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False
            
    def update_product_by_id(self, id, name, date, amount):
        stmt = update(product_table).returning(product_table.c.id).where(product_table.c.id == id).values(id = id, name=name, date=date, amount=amount)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            product = result.all()
            conn.commit()
            if(len(product)==0):
                return None
            else:
                return True
            
    def delete_product_by_id(self, id):
        stmt = delete(product_table).returning(product_table.c.id).where(product_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            product = result.all()
            conn.commit()
            if(len(product)==0):
                return None
            else:
                return True
            
    def create_recipe(self, user_id, product_id):
        stmt = insert(recipie_table).returning(recipie_table.c.id).values(user_id=user_id, product_id=product_id)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return True
    
    
    def get_recipe_by_user(self, user_id):
       stmt = select(recipie_table).where(recipie_table.c.user_id == user_id)
       with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users
    
    


