#11.1

users = ['Admin','Liza','Anya','Katerina','Margo','Dima','Alice']
for user in users:
    print(f"Hello, {user}.")
    
for user in users:
    if user == 'Admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")
        
#11.2

current_users = ['Admin','Liza','Anya','Katerina','Jonh','Dima','Kira']
new_users = ['Maria','Nastya','Angelina','Kira', 'Jonh']
for new_users in new_users:
    if new_users in current_users:
        print("Выберите другое имя!")
    else:
        print("Супер, имя доступно")
        
#11.3

numb = list(range(1,10))
print(numb)
for numb in numb:
    if numb == 1:
        print(f'{numb}st')
    elif numb == 2:
        print(f'{numb}nd')
    elif numb == 3:
        print(f'{numb}rd')
    else:
        print(f'{numb}th')