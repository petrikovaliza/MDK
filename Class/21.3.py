class User:
    
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        
    def describe_user(self):
        print(f"Имя: {self.first_name}, Фамилия: {self.last_name}, Возвраст: {self.age}, Город: {self.city}")
        
    def greet_user(self):
        print(f"Привет {self.first_name}!")
        
User1 = User('Аня', 'Сахарова', '25', 'Москва')
User2 = User('Миша', 'Бурченко', '23', 'Челябинск')
User3 = User('Витя', 'Семенов', '28', 'Лондон')

User1.describe_user()
User1.greet_user()

User2.describe_user()
User2.greet_user()

User3.describe_user()
User3.greet_user()
