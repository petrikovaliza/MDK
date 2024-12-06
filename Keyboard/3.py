from keyboard_folder import keyboard

lst = [1, 2, 3]

def auth_keys():
    lst.append(lst[-1] + 1)
    print(f'Список: {lst}')

keyboard.add_hotkey('p', auth_keys, suppress=True)
keyboard.wait('esc')
            