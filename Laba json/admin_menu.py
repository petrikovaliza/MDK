import json
from main_menu import(data)

def admin_menu():
    with open("user_data.json") as f:
        data = json.load(f)
    while True:
        print('Admin menu is successfully started!')
        print('For admin commands check please !help')
        admin_input = input('Choose what you wanna do: ')
        match admin_input:
            case '!delete':
                delete_user_input = input('Which you want to delete from users? (Enter name): ')
                users = data.get('users', [])
                new_users = [user for user in users if user['username'] != delete_user_input]

                data['users'] = new_users
                with open('user_data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)

            case '!delete_all':
                delete_all_user_input = input('You wipe all users account, are you sure? ')
                if delete_all_user_input.lower() == 'yes':
                    data["users"] = []  # Очищаем список пользователей
                    print("All users successfully deleted.")
                    with open('user_data.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                else:
                    print("Deletion canceled.")

            case '!help':
                print('In these block you can watch your commands, now available: !help, !delete, !delete_all, !show_users, !add_user, !count_users, !return (for return to menu), !unlogin (for back to register)')

            case '!exit':
                print('Close the program...')
                break

            case '!unlogin':
                pass

            case '!show_users':
                show_users(data)

            case '!add_user':
                add_user(data)

            case '!count_users':
                count_users(data)

            case '!return':
                break
            case _:
                print('Incorrect data, please try again')

def show_users(data):
    print("\nСписок пользователей:")
    for user in data["users"]:
        print(f"Имя пользователя: {user['username']}")

def add_user(data):
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    data["users"].append({"username": username, "password": password})
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Пользователь успешно добавлен!")

def count_users(data):
    print(f"Количество зарегистрированных пользователей: {len(data['users'])}")

if __name__ == "__main__":
    admin_menu()