import json
import auth
  
with open('user_data.json', 'r') as json_file:
    data = json.load(json_file)

print(data)
user = data["users"][0]
username = user["username"]
user_password = user["password"]
print(username)
print(user_password)

def main_menu():
    print(f'//MAIN MENU')
    
# start_menu()

if __name__ == "__main__":
    print('\n DEBUG^ Script is run in this document')
else:
    print('Script is imported')