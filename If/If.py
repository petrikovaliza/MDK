foods = ['sushi','soup','pizza']
for food in foods:
    if food =='soup':
        print(food.lower())  
    else:
        print(food.title())  
        
#10.1

colour = 'red'
if colour == 'red':
    print("Остановитесь")

#10.2

age = 24
if 0 <= age <= 2:
    print("Вы младенец")
elif 2 <= age < 4:
    print("Вы малыш")
elif 4 <= age < 13:
    print("Вы ребенок")
elif 13 <= age < 20:
    print("Вы подросток") 
elif 20 <= age < 65:
    print("Вы взрослый")
else:
    print("Вы пожилой человек")
    
#10.3

fruits = ['apple','orange','watermelon']
if 'orange' in fruits:
    print('Orange in list')
if 'apple' in fruits:
    print('Apple in list')
if 'watermellon' in fruits:
    print('Watermelon in list')

#10.4 

fruits_list = ['apple','orange','watermelon']
if 'orange' in fruits:
    print('You really like orange!')
if 'apple' in fruits:
    print('You really like apple!')
if 'watermelon' in fruits:
    print('You really like watermelon!')   
if 'mango' in fruits:
    print('You really like mango!')
if 'melon' in fruits:
    print('You really like melon!')