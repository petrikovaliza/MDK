class TooManyAttemptsError(Exception):
    
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return f'Ошибка {self.message} - больше 3 попыток входа с неверным паролем'
    
class Login():
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.attempts = 0
        
    def check_password(self, pasword):
        self.attempts += 1
        if self.attempts >3:
            raise TooManyAttemptsError