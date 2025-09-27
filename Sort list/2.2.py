# В списке содержатся латинские символы и цифры. Отсортировать его таким образом,
# чтобы сначала по алфавиту перечислялись латинские символы, потом цифры (в порядке
# возрастания).
# Пример: [‘5’,‘c’, ‘c’, ‘b’ ,‘a’, ‘2’] -> [‘a’, ‘b’ , ‘c’, ‘c’, ‘2’,‘5’]

def custom_sort(lst):
    letters = []
    digits = []
    
    for item in lst:
        if item.isalpha():
            letters.append(item)
        elif item.isdigit():
            digits.append(int(item))
            
    letters.sort()
    digits.sort()
    digits = list(map(str, digits))
    result = letters + digits
    return result

lst = ['5','c', 'c', 'b' ,'a', '2']
sorted_lst = custom_sort(lst)
print(sorted_lst)