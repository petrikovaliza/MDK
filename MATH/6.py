import math as m

def addition_1(n: int) -> float:
    summation = 0
    for i in range(1, n+1):
        summation = summation + m.sqrt(m.fabs(m.pow(2, i) * m.log(i+1) * m.log(i+2, 3)))
    return summation

def addition_2(n: int) -> float:
    summation = 0
    for i in range(n+1):
        summation = summation + m.log(i) + m.factorial(i) * m.log**2(i+1, 5) * m.log(i, 2)
    return summation

def addition_3(n: int) -> float:
    summation = 0
    for i in range(1, n+1):
        summation = summation + m.pow(m.sqrt(m.log(i, 2) * m.pow(3, i-1) + i * m.log(2)), 3)
    return summation

def addition_4(n: int) -> float:
    summation = 0
    for i in range(n+1):
        summation = summation + m.log(i+1) / (m.log10(i+2) * m.log(i+3, 7))
    return summation

def addition_5(n: int) -> float:
    summation = 0
    for i in range(1, n+1):
        summation = summation + m.pow(m.exp(i) + m.log(i) * m.log(i+2, 5), 2)
    return summation

def multiplication_6(n: int) -> float:
    multiplication = 1
    for i in range(1, n+1):
        multiplication = multiplication * (m.pow(2, -i) * m.log(i+1) + m.pow(1.2, i/12) * m.log10(i+2))
    return multiplication

def multiplication_7(n: int) -> float:
    multiplication = 1
    for i in range(1, n+1):
        multiplication = multiplication * (3 * m.log(i+2, 2) - m.exp(-i) / m.log10(i+1) + m.pow(2, 1-2*i))
    return multiplication

def multiplication_8(n: int) -> float:
    multiplication = 1
    for i in range(1, n+1):
        multiplication = multiplication * (m.sqrt(m.fabs(m.pow(5, i+1)) / m.pow(i, 3) + m.log(i*2) - m.factorial(i)))
    return multiplication

def multiplication_9(n: int) -> float:
    multiplication = 1
    for i in range(1, n+1):
        summation = 0
        for k in range(1, i+3):
            summation = summation + 1/k
        multiplication = multiplication * (m.log(i+1) * m.exp(i/7) * summation)
    return multiplication

def multiplication_10(n: int) -> float:
    multiplication = 1
    for i in range(1, n+1):
        summation = 0
        for k in range(1, i+3):
            summation = summation
            multiplication = multiplication * summation
        multiplication = multiplication * ((m.log(k+1)) * m.log(i+2, 2))
    return multiplication

while True:
    choice = int(input('Выберите, что хотите вычислить:\n 1.Сумма 1.\n 2.Сумма 2.\n 3.Сумма 3.\n 4.Сумма 4.\n 5.Сумма 5.\n 6.Произведение 6.\n 7.Произведение 7.\n 8.Произведение 8.\n 9.Произведение 9.\n 10.Произведение 10.\n Введите 99 для выхода.'))
    if choice == 99:
        break
    n = int(input('Введите значение n: '))
    
    if choice == 1:
        result = addition_1(n)
        print(f"Cумма = {format(result, '6f')}\n")
    
    if choice == 2:
        try:
            result = addition_2(n)
            print(f"Cумма = {format(result, '6f')}\n")
        except ValueError:
            print('n должно быть меньше 0')
    
    if choice == 3:
        result = addition_3(n)
        print(f"Cумма = {format(result, '6f')}\n")
    
    if choice == 4:
        try:
            result = addition_4(n)
            print(f"Cумма = {format(result, '6f')}\n")
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
    
    if choice == 5:
        result = addition_5(n)
        print(f"Cумма = {format(result, '6f')}\n")
    
    if choice == 6:
        result = multiplication_6(n)
        print(f"Произведение = {format(result, '6f')}\n")

    
    if choice == 7:
        result = multiplication_7(n)
        print(f"Произведение = {format(result, '6f')}\n")

    
    if choice == 8:
        result = multiplication_8(n)
        print(f"Произведение = {format(result, '6f')}\n")
                  
    if choice == 9:
        result = multiplication_9(n)
        print(f"Произведение = {format(result, '6f')}\n")
        
    if choice == 10:
        result = multiplication_10(n)
        print(f"Произведение = {format(result, '6f')}\n")
        
