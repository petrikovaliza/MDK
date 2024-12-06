#17.1

sandwich_orders = ['American sub','Bacon, egg and cheese','Baked bean','Barros Jarpa']
finished_sandwiches = []
print(sandwich_orders)

for sandwich in sandwich_orders:
    print(f"I made your {sandwich.title()} sandwich.\n")
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"Verifying sandwich: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nMade sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
    
#17.2

sandwich_orders = ['American sub','With cheese','Bacon, egg and cheese','With cheese','Baked bean','Barros Jarpa','With cheese']
print("No more with cheese")

while 'With cheese' in sandwich_orders:
   sandwich_orders.remove('With cheese') 
print(sandwich_orders)
        
#17.3

responses = {}
polling_active = True

while polling_active:
    name = input("\nКак вас зовут?")
    response = input("Где бы вы хотели провести отпуск?")
    responses[name] = response

    repeat = input("Продолжить опрос?(Да/нет)")
    if repeat == 'Нет':
        polling_active = False

print("\n - - - Результаты опроса - - -")
for name, response in responses.items():
    print(f"{name} хочет отправиться в отпуск в {response}.")