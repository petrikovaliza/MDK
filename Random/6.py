import random

number_faces = int(input("Сколько граней у куба: ")) 
number_throws = int(input("Сколько раз бросить: ")) 

for number_throw in range(number_throws):
    print(f"Бросок {number_throw + 1}: случайное число - {random.randint(1, number_faces)}")



     


