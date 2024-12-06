import math as m

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

D = m.pow(b, 2) - (4 * a * c)
print(D)

if D == 0:
    print('Уравнение имеет 1 корень {x}')
    print(x = -b / (2 * a))
elif D < 0:
    print('Уравнение не имеет корней((')
else:
    x1 = (-b + m.sqrt(D)) / (2 * a)
    x2 = (-b - m.sqrt(D)) / (2 * a)
    print('Уравнение имеет 2 корня: {x1}, {x2}')
    
