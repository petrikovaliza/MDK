# Простой пример областей видимости

x = 10

def local_scope():
    x = 5
    print("Значение x внутри функции local_scopу:", x)
    
local_scope()
print("Значение x вне функции: ", x)