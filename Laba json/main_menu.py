import json
import random

with open('user_data.json', 'r') as json_file:
    data = json.load(json_file)

print(data)
user = data["users"][0]
username = user["username"]
user_password = user["password"]
print(username)
print(user_password)


def main_menu():
    print(f'//MAIN MENU\n')
    cube()
    
    if __name__ == "__main__":
        print('\n DEBUG: Script is run in this document')
    else:
        print('Script is imported')

def cube():
        while True:
            entry = input("Бросить кубик? (да/нет): ")
            if entry.lower() == "да":
                def roll_dice():
                    return random.randint(1, 6)
                result = roll_dice()
                print(f"Выпало: {result}")
            elif entry.lower() == "нет":
                print("До свидания!")
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
            return entry