import math as m

def logarith_1(x: float) -> float:
    return m.log(x+3) + m.exp(x-2) - m.log10(m.exp(x-3)) / (2*x-1)

def logarith_2(x: float) -> float:
    return m.fabs(m.log(m.factorial(int(x)))) + m.sqrt(m.log(x+2, 2))**4 - 1 / m.sqrt(m.log(x))

def logarith_3(x: float) -> float:
    return m.log10(x**2 + 1) * (1 / m.exp(x-1)) - (1 / m.pow(x, m.log(x+2)))

def logarith_4(x: float) -> float:
    return m.log((x+1),5) / m.sqrt(m.exp(x-2)) - m.log10(3*x / 2*m.pow(x, 3) - 1)

def trigonometry_5(x: float) -> float:
    return (m.sin(x)**3 * m.cos(2*x)) / m.fabs(m.tan(x/2) **2) + (1/m.tan(3*x))**2

def trigonometry_6(x: float) -> float:
    return m.sqrt(m.fabs(m.sin(3*x)**2) + m.cos(x)**2) / (m.cos(2*x) - 1) * m.exp(m.sin(2*x+1) * 1/m.tan(x-1))

def trigonometry_7(x: float) -> float:
    return (m.asin(x)**2 + m.exp(m.acos(x)-1)) / (m.sqrt(m.fabs(m.pi/2 -m.atan(x/2))) * round(m.pi, 2)) * m.asin(m.fabs(x)) / x - round(m.pi, 2)

def trigonometry_8(x: float) -> float:
    return (m.exp(m.fabs(m.pi/2 -m.atan(x))) - round(m.pi, 2)) / (m.sqrt(m.acos(x)**2) + 1) - m.exp(x**2) / (round(m.pi, 2) + 3*(m.pi/2 -m.atan(x)**2))

while True:
    choice = int(input('Выберите, что хотите вычислить:\n 1.Первый логарифм.\n 2.Второй логарифм.\n 3.Третий логарифм.\n 4.Четвертый логарифм.\n 5.Тригонометрия пятая.\n 6.Тригонометрия шестая.\n 7.Тригонометрия седьмая.\n 8.Тригонометрия восьмая.\n Введите 99 для выхода.'))
    if choice == 99:
        break
    x = float(input('Введите значение x: '))
    
    if choice == 1:
        result = logarith_1(x)
        print(f"f(x) = {format(result, '6f')}\n")
    
    if choice == 2:
        result = logarith_2(x)
        print(f"f(x) = {format(result, '6f')}\n")
    
    if choice == 3:
        result = logarith_3(x)
        print(f"f(x) = {format(result, '6f')}\n")
    
    if choice == 4:
        result = logarith_4(x)
        print(f"f(x) = {format(result, '6f')}\n")
    
    if choice == 5:
        try:
            result = trigonometry_5(x)
            print(f"f(x) = {format(result, '6f')}\n")
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except ValueError:
            print('X должно быть от -1 до 1')
    
    if choice == 6:
        try:
            result = trigonometry_6(x)
            print(f"f(x) = {format(result, '6f')}\n")
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except ValueError:
            print('X должно быть от -1 до 1')
    
    if choice == 7:
        try:
            result = trigonometry_7(x)
            print(f"f(x) = {format(result, '6f')}\n")
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except ValueError:
            print('X должно быть от -1 до 1')
    
    if choice == 8:
        try:
            result = trigonometry_8(x)
            print(f"f(x) = {format(result, '6f')}\n")
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except ValueError:
            print('X должно быть от -1 до 1')