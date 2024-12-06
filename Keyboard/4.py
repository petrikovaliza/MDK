from keyboard_folder import keyboard

logs = []
print('Нажмите любые клавиши, для завершения нажмите ESC')

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        logs.append(event.name)
        print(f'Нажата клавиша: {event.name}')
    if event.name == 'esc':
        break
        
with open('key_logs.txt', 'w', encoding='utf-8') as file_object:   
    for key in logs:
        file_object.write(f'{key}n')
        
print(f"Количество нажатий: {len(logs)}. Логи сохранены в key_logs.txt")