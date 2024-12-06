import math as m

AB = int(input('Введите сторону AB: '))
BC = int(input('Введите сторону BC: '))
AC = int(input('Введите сторону AC: '))


if (AB + BC) > AC and (AB + AC) > BC and (AC + BC) > AB:
    print("Треугольник существует")
else:
    print('Треугольника не существует')