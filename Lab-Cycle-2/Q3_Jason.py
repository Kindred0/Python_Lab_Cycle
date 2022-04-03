import json

with open('iris.json') as f:
    data=json.load(f)

print(data)