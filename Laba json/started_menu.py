from reg import(registration)
from auth import(authorization)

def start_menu():
    while True:
        start_input = input('IF you first time here/want to enter to your account (R/A)')
        if start_input is 'R':
            registration()
            break
        elif start_input is 'A':
            authorization()
            break
        else:
            print('Incorrect input, plese try again.')
start_menu()