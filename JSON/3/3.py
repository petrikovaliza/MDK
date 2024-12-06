import json

with open('user_data.json', 'r') as file:
    data = json.load(file)
    
new_users = {
     "username": "user2",
     "email": "user2@example.com"
}

data['users'].append(new_users)

with open('user_data.json', 'w') as file:
    json.dump(data, file, indent = 4)