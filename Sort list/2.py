# В списке содержатся русские и латинские символы. Отсортировать его таким образом,
# чтобы сначала по алфавиту перечислялись русские символы, потом латинские (также по
# алфавиту).
# Пример: [‘я’,‘c’, ‘c’, ‘b’ ,‘a’, ‘ж’] -> [‘ж’, ‘я’, ‘a’, ‘b’ , ‘c’, ‘c’]

def sort_russian_then_latin(characters):

    russian_chars = []
    latin_chars = []
    
    for char in characters:
        if 'а' <= char <= 'я':
            russian_chars.append(char)
        else:
            latin_chars.append(char)
    
    russian_chars.sort()
    latin_chars.sort()
    
    result = russian_chars + latin_chars
    return result

characters = ['я', 'c', 'c', 'b', 'a', 'ж']
sorted_characters = sort_russian_then_latin(characters)
print(sorted_characters)