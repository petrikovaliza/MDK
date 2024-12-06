def classify_number(number):
    match number:
        case number if number > 0 : print('Положительное число')
        case number if number < 0 : print('Отрицательное число')
        case number if number == 0 : print('Число 0')
        
classify_number(5)
classify_number(0)
classify_number(-9)