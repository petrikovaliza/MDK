from regi import *
from auth import *

def start_menu():
    while True:
        start_input = input('If you first time here/want to enter to your account(R/A)')
        if start_input == 'R':
            registration()
            break
        elif start_input == 'A':
            authorization()
            break
        else:
            print('Incorrect input, please try again')