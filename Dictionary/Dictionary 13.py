#13.1

glossary = {
'База данных:':'совокупность данных, хранимых в соответствии со схемой данных',
'Алгоритм:':'это полное и точное описание на некотором языке конечной последовательности правил',
'СУБД:':'инструменты, которые помогают управлять базами данных',
'Информационная система:':'специализированная система, которая необходима для того, чтобы хранить, искать и обрабатывать информацию.',
'Ведение БД:':'Деятельность по обновлению, восстановлению и перестройке структуры базы данных\n'}

glossary['print'] = '- функция, которая выводит на экран результат выполнения программы или какой-то ее части.'
glossary['int'] = '- целые числа, с которыми можно выполнять обычные математические операции: например, деление, возведение в степень или сложение.'
glossary['list'] = '- списки. Это аналог массивов, в которых могут находиться данные разных типов.'
glossary['for'] = '- цикл, который повторяет определенное действие до тех пор, пока не произойдет специальное событие для его завершения.'
glossary['tuple'] = '- кортежи. Это те же списки, но с одним исключением — изменить помещенные в них данные нельзя не случайно, не специально.\n'    
print(glossary)

for key in glossary:
    print(f"{key} {glossary[key]}")

#13.2

river = {
'Tiger':'Turkiye',
'Mississippi':'USA',
'Amazonka':'Brazil',}

for key in river:
    print(f"The {key} runs through {river[key]}.\n")
    
for key in river:
    print(key)
    
for country in river.values():
    print(country)

#13.3

user = ['Liza','Anya','Katerina','Margo','Dima','Alice']
new_user =['Liza','Olesya','Margo','Jonh']
print()
for new_user in new_user:
    if new_user in user:
        print(f"Thanks for perticipating, {new_user.title()}\n")
    else:
        print(f"We invite you to take part, {new_user.title()}\n")

#13.4

hobby = {
'Liza':'drawing',
'Anya':'running',
'Katerina':'drawing',
'Margo':'horse riding',
'Katerina':'modeling',
'Dima':'running'}

for hobby in set(hobby.values()):
    print(hobby.title())

#13.5

baza = {
'User_1':'Liza',
'User_2':'Katerina',
'User_3':'Dima',
'User_4':'Alice'}
for user in baza.keys():
    print(user.title())   

user = input("Введите ключ:")
print(f"Ключ:{key}")





