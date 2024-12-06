# Фильтрация строк по длине

name = ['liza','dora', 'moiva','fo']
length_filter = filter(lambda x: len(x) < 3, name)
print(list(length_filter))