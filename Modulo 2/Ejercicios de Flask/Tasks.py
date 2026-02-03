from flask import Flask, request, jsonify
from Persistency import write_file, read_file
from Validation import body_validations

app = Flask(__name__)

@app.route("/tasks")

def get():
    tasks = read_file('Tasks.json')
    filtered_shows = tasks
    genre_filter = request.args.get("state")
    if genre_filter:
        filtered_shows = list(
            filter(lambda show: show["state"] == genre_filter, filtered_shows)
        )

    return {"data": filtered_shows}

@app.route("/tasks", methods=["POST"])
def create():
    tasks = read_file('Tasks.json')
    request_body = request.json
    id_validation = False
    try: 
        if not request_body:
            raise ValueError ("No se agrego ningun entry para agregar")
        for task in tasks:
            if task["id"] == request_body["id"]:
                id_validation = True
        if (id_validation == False):
            body_validations(request_body)
            tasks.append(request_body)
            write_file('Tasks.json' ,tasks)
            return "Task agregado", 200
        else:
            raise ValueError("El id agregado ya existe")
    except ValueError as ex:
        return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
                
    

@app.route("/tasks/<id_task>", methods=["PUT"])
def edit(id_task):
    tasks = read_file('Tasks.json')
    request_body = request.json
    id_validation = False
    try:
        if not request_body:
            raise ValueError ("No se agrego ningun entry para modificar")
        for task in tasks:
            if task["id"] == str(id_task):
                id_validation = True
        if (id_validation == True):
            body_validations(request_body)
            task["title"] = request_body["title"]
            task["description"] = request_body["description"]
            task["state"] = request_body["state"]
            write_file('Tasks.json', tasks)
            return {"Task modificado: " : request_body}, 200
        else:
            raise ValueError ("El id que intentas modificar no existe")
    except ValueError as ex:
                return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500

@app.route("/tasks/<id_task>", methods=["DELETE"])
def delete(id_task):
    tasks = read_file('Tasks.json')
    request_body = request.json
    try:
        if not request_body:
            raise ValueError ("No se agrego ningun entry para modificar")
        
        for i, task in enumerate(tasks):
            if task["id"] == str(id_task):
                del tasks[i]
                write_file('Tasks.json', tasks)
                return "Task eliminada", 200
            
        raise ValueError ("El id que intentas modificar no existe")
    
    except ValueError as ex:
                return jsonify(message=str(ex)), 404
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    
    
if __name__ == "__main__":
    app.run(host="localhost", debug=True)

