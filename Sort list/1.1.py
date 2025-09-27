# В списке содержатся слова, содержащие цифры. Отсортировать его так, чтобы слова
# располагались в порядке возрастания количества цифр, кратных 3.
# Пример: [‘s23c’, ‘aa6op9’, ‘2rt2t’] -> [‘2rt2t’, ‘s23c’, ‘aa6op9’,]

def count_digits_divisible_by_3(word):

    return sum(1 for char in word if char.isdigit() and int(char) % 3 == 0)


words = ['s23c', 'aa6op9', '2rt2t']
sorted_words = sorted(words, key=count_digits_divisible_by_3)
print(sorted_words)