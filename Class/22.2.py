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
        

class Admin(User):
    
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ['добавлять сообщения','удалять пользователей', 'банить пользователей']
    
    def show_privileges(self):
        print(f'Администратор может: ')
        for privilege in self.privileges:
            print(f'{privilege}')
            
admin = Admin('Никита', 'Суворов', '42', 'Нижний Новгород')
admin.describe_user()
admin.greet_user()
admin.show_privileges()