filename = 'reason_book.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("Почему тебе нравится программировать? ")
        if name == 'quit':
            break
        else:
            file_object.write(f"{name.rstrip()}\n")