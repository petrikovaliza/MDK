filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("Введите имя:")
        if name == 'quit':
            break
        else:
            file_object.write(f"Привет, {name.rstrip()}\n")