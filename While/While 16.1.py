#16.1

prompt = "\nВведите дополнения для пиццы:"
prompt += "\nВведите 'quit', чтобы завершить программу."
message = ""
while message != 'quit':
    message = input("Дополнение включено в заказ")
    message = input(prompt)
    print(message)