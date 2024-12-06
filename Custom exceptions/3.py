class InvalidAgeError(Exception):
    
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return f'{self.message} - недопустимый возраст'
   
class User():
    
    def __init__(self, name, age):
        self.name = name
        if 0 < age < 150:
            self.age = age
        else:
            raise InvalidAgeError('InvalidAgeError')
           
    def hello_user(self):
        print(f"Добро пожаловать, {self.name}")
         
try:
    user = User('Алекса', 25)
    user.hello_user()
    user = User('Дорька', 156)
    user.hello_user()
    user = User('Андрей', 0)
    user.hello_user()
    
except InvalidAgeError as e:
    print(e)