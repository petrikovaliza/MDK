from keyboard_folder import keyboard

def on_key_event(event):
    print(f'"key {"pressed" if event.event_type == "down" else "released"}')

keyboard.hook(on_key_event)

keyboard.wait('esc')