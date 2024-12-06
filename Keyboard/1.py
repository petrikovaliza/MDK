from keyboard_folder import keyboard

def hotkey_action():
    print(11, 13, 25, 33)

keyboard.add_hotkey('enter', hotkey_action)

keyboard.wait('esc')