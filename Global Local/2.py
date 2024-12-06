#Использование enclosing scope

def outer_function():
    y = 20
    print(y)
    
    def inner_function():
        nonlocal y
        y = 24
        print(y)
    
    inner_function()
    
outer_function()

