#16.3 первая часть задания

prompt = "\nВведите дополнения для пиццы:"
prompt += "\nВведите 'quit', чтобы завершить программу."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print("Дополнение включено в заказ")
        
