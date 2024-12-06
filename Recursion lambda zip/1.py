# Факториал числа

def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(n = 0))
print(factorial(n = 1))
print(factorial(n = 5))
