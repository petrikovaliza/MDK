import main_menu 
import admin_menu 
import json

with open('user_data.json', 'r') as json_file:
    data = json.load(json_file)

def authorization():
    print('\nWelcome to authorization menu')
    username_input = input('Enter your login: ')
    password_input = input('Enter ypur password: ')
    for data_user in data["users"]:
        if username_input.lower() == data_user["username"].lower() and password_input() == data_user["password"].lower():
            print(f'\nWelcome back, {username_input}!')
            main_menu()
            break
        elif username_input.lower() == "admin_" and password_input == "admin_":
            print('Start admin panel...')
            admin_menu()
            break
        else:
            pass
    else:
        print('Incorrect data, please try again')