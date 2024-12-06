# Числа Фибоначчи

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))
