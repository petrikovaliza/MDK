import json

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('file.json', 'w') as json_file:
    json.dumps(person, json_file)

with open('file.Json', 'r') as json_file:
    data = json.load(json_file)
    print(data)
