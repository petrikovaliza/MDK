#16.3 вторая часть

prompt = "\nВведите дополнения для пиццы:"
prompt += "\nВведите 'quit', чтобы завершить программу."
while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print("Дополнение включено в заказ")