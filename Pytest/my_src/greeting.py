class Text_Greeting():
    
    def greeting(self, name):
        name = input()
        return f"My name {name}"
    
    def empty_string(self, arg):
        arg = input()
        return True if len(arg) > 0 else False
    
    def register_check(self, arg: str):
        arg = input()
        return arg.upper()
            
    def long_check(self,arg):
        arg = input()
        return True if len(arg) < 10 else False
        
    def string_type(self,arg):
        arg = input() 
        return True if type(arg) !=str else False