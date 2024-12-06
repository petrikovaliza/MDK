#1

def divide_numbers(a,b):
    try:
        result = a / b
        print('Result:', result)
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
        
numerator = 100
denominator = 0
divide_numbers(numerator,denominator)

#2

def integer_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print('Неверный ввод, введите целое число')
        
n = integer_input('Введите целое число: ')
print('Введенное число: ', n)

#3

def get_numbers(a,b):
    try:
        first_numb = int(input(a))
        second_numb = int(input(b))
        return first_numb, second_numb
    except ValueError:
        print('Неверно, введите число!')

s = get_numbers('Введите первое число: ', 'Введите второе число:')
print('Введенные числа: ', s)

    