fruits = ['mango', 'banana', 'orange']
letters = ''.join(fruit[0] for fruit in fruits)
fruits_length = [len(fruit) for fruit in fruits]
filtered_fruits = [fruit for fruit in fruits if len(fruit) < 3]

print(f"Первые буквы: [{', '.join(letters)}]")
print(f"Длины строк: {fruits_length}")
print(f"Фрукты с длиной строки < 3: {filtered_fruits}")