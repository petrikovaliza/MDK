from keyboard_folder import keyboard

def hotkey_action():
    print('Горячая клавиша Ctrl+Shift+A нажата!')

keyboard.add_hotkey('ctrl+shift+a', hotkey_action)

keyboard.wait('esc')