from db import DB_Manager
from JWT_Manager_RS256 import JWT_Manager
from flask import Flask, request, Response, jsonify
from Validations import create_product_validation, update_product_validation, create_recipe_validation
from CacheRedis import CacheManager

with open("private.pem", "rb") as f:
    private_key = f.read()

with open("public.pem", "rb") as f:
    public_key = f.read()

app = Flask("user-service")
db_manager = DB_Manager()
jwt_manager = JWT_Manager(private_key, public_key)
cache_manager = CacheManager( host = "placeholder", port = 00000, password = "Ijxu2xygtt6VZoo4aMk8K7KsRVNhUkZA",)

def generate_cache_products_id_key(id):
    return f'getProduct-id{id}'

@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
    auth_token = request.headers.get('Authorization')
    if(auth_token is not None):
            test = auth_token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            if(user[2] == "admin"):
                data = request.get_json()  # data is empty
                if(data.get('username') == None or data.get('password') == None or data.get('type') == None):
                    return Response(status=400)
                else:
                    result = db_manager.insert_user(data.get('username'), data.get('password'),  data.get('type'))
                    user_id = result[0]

                    token = jwt_manager.encode({'id':user_id})
                    
                    return jsonify(token=token)
            else:
                return Response(status=403) 
    else:
        return Response(status=403)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = db_manager.get_user(data.get('username'), data.get('password'))

        if(result == None):
            return Response(status=401)
        else:
            user_id = result[0]
            token = jwt_manager.encode({'id':user_id})
        
            return jsonify(token=token)

@app.route('/me')
def me():
    try:
        token = request.headers.get('Authorization')
        if(token is not None):
            test = token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            return jsonify(id=user_id, username=user[1])
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/product/<unit>', methods=["GET", "POST", "PATCH", "DELETE"])
def product_manager_system(unit):
    request_body = request.json
    auth_token = request.headers.get('Authorization')
    try:
        if(auth_token is not None):
            test = auth_token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            if(user[2] == "admin"):
                id = request.args.get("id")
                name = request.args.get("name")
                date = request.args.get("date")
                amount = request.args.get("amount")

                valid_units = ("lists", "create", "update", "delete")

                if (unit not in valid_units ):
                    return jsonify(error="PAGE NOT FOUND" ), 404
                
                if(request.method == "GET" and unit == "lists"):                    
                    filtered_shows = db_manager.get_product(id=id, name=name, date=date, amount=amount)
                    for prod in filtered_shows:
                        cache_manager.store_data(prod["id"], prod["name"])
                    return {"data": filtered_shows}
                
                elif(request.method == "POST" and unit == "create"):
                        if not request_body:
                            return jsonify(error="No se agrego ningun entry para agregar") , 422
                        create_product_validation(request_body)
                        if(db_manager.insert_product(request_body['name'], request_body['date'], request_body['amount']) == True):
                            filtered_shows = db_manager.get_product(id=id, name=name, date=date, amount=amount)
                            for prod in filtered_shows:
                                cache_manager.store_data(prod["id"], prod["name"])
                            return "Producto agregado", 201
                        else:
                            return jsonify(error="Hubo un error agregando al producto, favor revisar la base de datos" ), 400
                        
                elif(request.method == "PATCH" and unit == "update"):
                        if not request_body:
                            return jsonify(error="No se agrego ningun entry para modificar") , 422
                        update_product_validation(request_body)
                        if(db_manager.update_product_by_id(request_body['id'], request_body['name'], request_body['date'], request_body['amount']) == True):
                            cache_manager.delete_data(request_body['id'])
                            cache_manager.store_data(request_body['id'], request_body['name'])
                            return "Estado del producto fue actualizado", 200
                        else:
                            return jsonify(error="Hubo un error actualizando al producto, favor revisar la base de datos" ), 400
                        
                elif(request.method == "DELETE" and unit == "delete"):
                        if not request_body:
                            return jsonify(error="No se agrego ningun entry para borrar") , 422
                        if(db_manager.delete_product_by_id(request_body['id']) == True):
                            cache_manager.delete_data(request_body['id'])
                            return "El producto fue eliminado", 200
                        else:
                            return jsonify(error="Hubo un error eliminando al producto, favor revisar la base de datos" ), 400
            else:
                return Response(status=403) 
        else:
            return Response(status=403)        
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500

@app.route('/recipe', methods=["GET"])
def get_recipe_per_user():
    try:
        token = request.headers.get('Authorization')
        if(token is not None):
            test = token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            recipe = db_manager.get_recipe_by_user(user_id)
            return [dict(row._mapping) for row in recipe]
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/sell', methods=["POST"])
def product_sell():
    try:
        token = request.headers.get('Authorization')
        if(token is not None):
            request_body = request.json
            if not request_body:
                return jsonify(error="No se agrego ningun entry para agregar") , 422

            test = token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']                
            create_recipe_validation(request_body)
            if(db_manager.create_recipe(request_body[user_id], request_body['product_id']) == True):
                return "Venta agregado", 201
            else:
                return jsonify(error="Hubo un error haciendo la venta, favor revisar la base de datos" ), 400
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)
if __name__ == "__main__":
    app.run(host="localhost", debug=True)
