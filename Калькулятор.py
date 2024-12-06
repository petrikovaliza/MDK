def calculator(x,y):
    if operation == "+":
        result = x + y
        return result
    elif operation == "-":
        result = x - y
        return result
    elif operation == "*":
        result = x * y
        return result
    elif operation == "/":
        try:
            return x / y
        except ZeroDivisionError:
            print("На ноль делить нельзя")
    else:
        print("Ошибка: неверный ввод!")
        result = None

operation = input("Введите операцию (+, -, *, /): ")
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

print(f"Результат: {calculator(x,y)}")