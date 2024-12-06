import numpy as np
a = np.array([1, 2, 3, 4, 5])

for i in a:
    print(f'{i}')
    
for i in range(len(a)):
    a[i] *= 3

print(f'Второе состояние: {a}')
summa = np.sum(a)
print(f'Общая сумма: {summa}')
dlina = len(a)
print(f'Общая длина: {dlina}')


 