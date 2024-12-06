import numpy as np

start = int(input("Введите первое число массива: "))
end = int(input("Введите конечное число массива: "))

my_array = []
for i in range(start, end + 1):
    my_array.append(i)

print(f"[{ ' '.join(str(x) for x in my_array) }]")