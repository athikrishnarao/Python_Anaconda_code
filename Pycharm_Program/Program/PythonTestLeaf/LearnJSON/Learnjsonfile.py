# Python to JSON
data = {
    'name':'Athi',
    'Exp':'5+',
    'value':None,
    'is nothing': True,
    'hobbies':('always sleeping....','always slepping')
    }

import json
# dumps: convert python data to JSON
print(type(data))
j = json.dumps(data,indent=4)
print(j)

# dump: write the json file
with open('py_to_json.json','w')as file:
    json.dump(j,file,indent=4)

