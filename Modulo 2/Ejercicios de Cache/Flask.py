from db import DB_Manager
from JWT_Manager_RS256 import JWT_Manager
from flask import Flask, request, Response, jsonify
from Validations import create_product_validation, update_product_validation, create_recipe_validation
from CacheRedis import CacheManager
import json

with open("private_key.pem", "rb") as f:
    private_key = f.read()

with open("public_key.pem", "rb") as f:
    public_key = f.read()

app = Flask("user-service")
db_manager = DB_Manager()
jwt_manager = JWT_Manager(private_key, public_key)
cache_manager = CacheManager( host = "oatmeal-birth-canvas-91552.db.redis.io", port = 13570, password = "aif5uYjnyvJ8mUaSAX9cgwdTCquicNOZ",)


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
    
@app.route('/product/lists', methods=["GET"])
def get_product_list():
    auth_token = request.headers.get('Authorization')
    try:
        if(auth_token is not None):
            test = auth_token.replace("Bearer ","").strip()
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            if(user[2] == "admin"):
                id = request.args.get("id")
                name = request.args.get("name")
                date = request.args.get("date")
                amount = request.args.get("amount")
                keys = cache_manager.get_all_keys()
                cache_data = []
                for key in keys:
                    cache_data.append(json.loads(cache_manager.get_data(f"{key}")))
                filtered_cache_data = []
                if any(v is not None for v in [id, name, date ,amount]):
                    for p in cache_data:
                        if (id and str(id) == str(p.get('id'))) or \
                            (name and name == p.get('name')) or \
                            (date and date == p.get('date')) or \
                            (amount and str(amount) == str(p.get('amount'))):
                                filtered_cache_data.append(p)
                    return {"data": filtered_cache_data}
                else:
                    return {"data": cache_data}
        else:
            return Response(status=403)
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    
@app.route('/product/create', methods=["POST"])
def create_product():
    auth_token = request.headers.get('Authorization')
    request_body = request.json
    try:
        if(auth_token is not None):
            test = auth_token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            if(user[2] == "admin"):
                if not request_body:
                    return jsonify(error="No se agrego ningun entry para agregar") , 422
                create_product_validation(request_body)
                if(db_manager.insert_product(request_body['name'], request_body['date'], request_body['amount']) == True):
                    product = db_manager.get_product(name= request_body['name'], date=request_body['date'], amount=request_body['amount'])
                    for prod in product:
                        cache_manager.store_data(prod['id'] , prod)
                    return "Producto agregado", 201
                else:
                    return jsonify(error="Hubo un error agregando al producto, favor revisar la base de datos" ), 400
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500

@app.route('/product/update', methods=["PATCH"])
def update_product():
    auth_token = request.headers.get('Authorization')
    request_body = request.json
    try:
        if(auth_token is not None):
            test = auth_token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            if(user[2] == "admin"):

                if not request_body:
                    return jsonify(error="No se agrego ningun entry para modificar") , 422
                update_product_validation(request_body)
                if(db_manager.update_product_by_id(request_body['id'], request_body['name'], request_body['date'], request_body['amount']) == True):
                    cache_manager.delete_data(request_body['id'])
                    product = db_manager.get_product(request_body['id'])
                    for prod in product:
                        cache_manager.store_data(prod['id'] , prod)
                    return "Estado del producto fue actualizado", 200
                else:
                    return jsonify(error="Hubo un error actualizando al producto, favor revisar la base de datos" ), 400
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500

@app.route('/product/delete', methods=["DELETE"])
def delete_product():
    auth_token = request.headers.get('Authorization')
    request_body = request.json
    try:
        if(auth_token is not None):
            test = auth_token.replace("Bearer ","")
            decoded = jwt_manager.decode(test)
            user_id = decoded['id']
            user = db_manager.get_user_by_id(user_id)
            if(user[2] == "admin"):

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
