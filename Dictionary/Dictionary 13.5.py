#13.5

baza = {
'User_1':'Liza',
'User_2':'Katerina',
'User_3':'Dima',
'User_4':'Alice'}
for user in baza.keys():
    print(user.title()) 
         
user = input("Введите ключ:")
if user in baza.keys():
    print(f"Ключ: {user}, Значение: {baza[user]}")
    
answer = input("Изменить значение ключа? (Да/Нет)")
if answer == 'Да':
    answer_1 = input("Ввведите значение для вашего нового ключа: ") 
    baza[user] = answer_1.title()
    answer_2 = input(f"Значение {user} обновлен на : {answer_1}")
print(baza)

