import math as m

def addition_1(e=0.000001) -> float:
    n = 1
    summation = 0
    while True:
        increment = 1 / n
        summation = summation + increment
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return summation

def addition_2(e=0.000001) -> float:
    n = 1
    summation = 0
    while True:
        increment = n / m.pow(n , 2)
        summation = summation + increment
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return summation

def addition_3(e=0.000001) -> float:
    n = 2
    summation = 0
    while True:
        increment = m.log(n) / n
        summation = summation + increment
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return summation

def addition_4(e=0.000001) -> float:
    n = 2
    summation = 0
    while True:
        increment = m.sin(n) / m.log10(n)
        summation = summation + increment
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return summation

def multiplication_5(e=0.000001) -> float:
    n = 2 
    multiplication = 1
    while True:
        increment = 1 / n * m.log(n)
        multiplication = multiplication * (1 + increment)
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return multiplication

def multiplication_6(e=0.000001) -> float:
    n = 2 
    multiplication = 1
    while True:
        increment = n / ((n-1) * (n+2))
        multiplication = multiplication * (1 + increment)
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return multiplication

def multiplication_7(e=0.000001) -> float:
    n = 1
    multiplication = 1
    while True:
        increment = m.cos(n) / m.sin(n**2)
        multiplication = multiplication * (1 + increment)
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return multiplication

def multiplication_8(e=0.000001) -> float:
    n = 1
    multiplication = 1
    while True:
        increment = m.atan(n) / (e*n - m.pi)
        multiplication = multiplication * (1 + increment)
        n = n + 1
        if m.fabs(increment) < e:
            break
    print(f'n = {n}')
    return multiplication

while True:
    choice = int(input('Выберите, что хотите вычислить:\n 1.Сумма 1.\n 2.Сумма 2.\n 3.Сумма 3.\n 4.Сумма 4.\n 5.Произведение 5. \n 6.Произведение 6. \n 7.Произведение 7.\n 8.Произведение 8.\n Введите 99 для выхода.'))
    if choice == 99:
        break
    e = float(input('Введите значение e: '))
    
    if choice == 1:
        try:
            result = addition_1(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть меньше от 0 до 1')
    
    if choice == 2:
        try:
            result = addition_2(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть меньше от 0 до 1')
    
    if choice == 3:
        try:
            result = addition_3(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть больше 0')
    
    if choice == 4:
        try:
            result = addition_4(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть больше 0')
    
    if choice == 5:
        try:
            result = multiplication_5(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть больше 0')
    
    if choice == 6:
        try:
            result = multiplication_6(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть больше 0')
    
    if choice == 7:
        try:
            result = multiplication_7(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть больше 0')
    
    if choice == 8:
        try:
            result = multiplication_8(e)
            print(f"Cумма = {format(result, '9f')}\n")
        except ValueError:
            print('e должно быть меньше от 0 до 1')

