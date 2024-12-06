import numpy as np

my_array = [1, 2, 3, 4, 5]

print(" ".join(str(x) for x in my_array))
for i in range(len(my_array)):
    print(i + 1)

new_array = [x * 3 for x in my_array]

print(f"Второе состояние массива: {' '.join(str(x) for x in new_array)}")
print(f"Общая сумма: {sum(my_array)}")
print(f"Общая длина: {len(my_array)}")
print(f"Общая сумма * 3: {sum(new_array)}")
print(f"Общая длина * 3: {len(new_array)}")

 