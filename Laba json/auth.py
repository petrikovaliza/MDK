from main_menu import *
from admin_menu import *

def authorization():
    print('\nWelcome to authorization menu')
    username_input = input('Enter your login: ')
    password_input = input('Enter your password: ')
    def my_profile():
        filename = 'user_profile.py'
        with open(filename, 'w') as file_object:
            file_object.write(username_input)
        my_profile()
    for data_user in data["users"]:
        if username_input.lower() == data_user["username"].lower() and password_input.lower() == data_user["password"].lower():
            print(f'\nWelcome back, {username_input}!\n')
            main_menu()          
            print(f'\nGood bye, {username_input}!\n')
        elif username_input.lower() == "admin_" and password_input == "admin_":
            print('Start admin panel. . .')
            admin_menu()
            break
        else:
            pass
    else:
        print('Incorrect data, plese try again')