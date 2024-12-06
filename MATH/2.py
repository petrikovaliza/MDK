import math as m

AB = int(input('Введите длину первого катета: '))
AC = int(input('Введите длину второго катета: '))
BC = m.pow((m.pow(AB, 2)) + m.pow(AC, 2), 2)
print(BC)

S =  (AB * AC) / 2
P = AB + AC + BC
print(f'Площадь {S}, Периметр: {P}')


