class Calculation():
    
    def sum(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b
    
    def find_palyndrome(self, arg: input) -> str:
        arg = input()
        return arg == arg[::-1]