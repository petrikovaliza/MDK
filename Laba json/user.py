import json
from main_menu import *
from auth import authorization

def main_menu():
    while True:
        print("Основное меню")
        print("1. Редактировать профиль")
        print("2. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            edit_profile()
        elif choice == "2":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

def edit_profile():
    with open("user_data.json") as f:
        data = json.load(f)

    username = input("Введите имя пользователя: ")
    user = next((user for user in data["users"] if user["username"] == username), None)

    if user:
        print("Текущие данные профиля:")
        for key, value in user.items():
            print(f"{key.capitalize()}: {value}")

        while True:
            print("\nЧто вы хотите изменить?")
            print("1. Email")
            print("2. Дата рождения")
            print("3. Номер телефона")
            print("4. Вернуться в главное меню")
            choice = input("Выберите действие: ")

            if choice == "1":
                new_email = input("Введите новый email: ")
                user["email"] = new_email
            elif choice == "2":
                new_date_of_birth = input("Введите новую дату рождения (YYYY-MM-DD): ")
                user["date_of_birth"] = new_date_of_birth
            elif choice == "3":
                new_phone_number = input("Введите новый номер телефона: ")
                user["phone_number"] = new_phone_number
            elif choice == "4":
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        with open("user_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Профиль успешно обновлен!")
    else:
        print("Пользователь не найден.")

if __name__ == "__main__":
    authorization()
    main_menu()