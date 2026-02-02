from flask import Flask, request, jsonify
import json


app = Flask(__name__)

with open('Tasks.json', 'r') as file:
    tasks = json.load(file)
        

@app.route("/get")
def get():
    filtered_shows = tasks
    genre_filter = request.args.get("state")
    if genre_filter:
        filtered_shows = list(
            filter(lambda show: show["state"] == genre_filter, filtered_shows)
        )

    return {"data": filtered_shows}

@app.route("/create", methods=["POST"])
def create():
    request_body = request.json
    if not request_body:
        return "No se agrego ningun entry para modificar"

    for task in tasks:
        if task["id"] == request_body["id"]:
            return "La id que esta agregando ya existe"
        
    try: 
        if "title" not in request_body:
            raise ValueError("No hay nombre en el body")
        if "description" not in request_body:
            raise ValueError("No hay descripcion en el body")
        if "state" not in request_body:
            raise ValueError("No hay estado en el body")
        if request_body["state"] not in ["on going", "in progress", "completed"]:
            raise ValueError("El estado no es una de las opciones correctas, por favor modifiquelo")
        tasks.append(request_body)
        with open('Tasks.json', 'w') as file:
            json.dump(tasks, file)
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500
                
    return "Cambio completado"
    

@app.route("/edit", methods=["POST"])
def edit():
    request_body = request.json
    retorno = ""
    if not request_body:
        retorno = "No se agrego ningun entry para modificar"
    else:
        for task in tasks:
            if task["id"] == request_body["id"]:
                task["title"] = request_body["title"]
                task["description"] = request_body["description"]
                task["state"] = request_body["state"]
                retorno = "Cambio realizado"
                with open("Tasks.json", "w", encoding="utf-8") as file:
                        json.dump(tasks, file, indent=4)
                break
            else:
                retorno = "No se encontro ningun id con ese nombre"
    return retorno
    


@app.route("/delete", methods=["DELETE"])
def delete():
    request_body = request.json
    retorno = ""
    if not request_body:
        retorno = "No se agrego ningun entry para borrar"
    else:
        for i,task in enumerate(tasks):
            if task["id"] == request_body["id"]:
                del tasks[i]
                retorno = "Cambio realizado"
                with open("Tasks.json", "w", encoding="utf-8") as file:
                        json.dump(tasks, file, indent=4)
                break
            else:
                retorno = "No se encontro ningun id con ese nombre"
    return retorno
    
if __name__ == "__main__":
    app.run(host="localhost", debug=True)

