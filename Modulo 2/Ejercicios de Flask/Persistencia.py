import json

def readFile(json_file):
    with open(json_file, 'r') as file:
        directory = json.load(file)
    return directory

def writeFile(json_file, directory):
    with open(json_file, 'w') as file:
            json.dump(directory, file)
        