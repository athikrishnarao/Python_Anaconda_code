import json

# Loads: Convert JSON file to Python format
pythonObj = json.loads('{"Name":"GN","active":false,"Value":null}')
print(pythonObj)

# Load: Load the JSON file
with open('py_to_json.json','r') as file:
    data = json.load(file)
    fo = json.loads(data)
print(fo)
