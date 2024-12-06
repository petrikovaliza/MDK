from keyboard_folder import keyboard
import threading
import time

print("Нажмите 'q' для выхода.")

while True:
    if keyboard.is_pressed('q'):
        break
    keyboard.press('a')
    print("Нажата клавиша 'а' ")
    time.sleep(1)