class NegativeNumberError(Exception):
    
    def __init__(self, message):
        super().__init__(message)
        self.message = message
             
    def __str__(self):
        return f'Ошибка {self.message}, число отрицательное'
    
class AtributeNumber():  
    
    def __init__(self, number: int):
        if number < 0:
            raise NegativeNumberError("NegativeNumberError")
        else:
            self.number = number      
    
    def print_number(self):
        print(f"Число - {self.number}, положительное. ")
        
try:
    number = AtributeNumber(37)
    number.print_number()  
    number = AtributeNumber(-8)
    number.print_number() 

except NegativeNumberError as e:
    print(e)
    