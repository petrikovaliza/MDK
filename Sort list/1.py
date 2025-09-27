# В списке содержатся слова, содержащие цифры. Отсортировать его так, чтобы слова
# располагались в порядке убывания суммы цифр в слове.
# Пример: [‘s23c’, ‘aa1op9’, ‘2rt2t’] -> [‘aa1op9’, ‘s23c’, ‘2rt2t’]

def sum_of_digits(word):
    return sum(int(digit) for digit in word if digit.isdigit())

words = ['s23c', 'aa1op9', '2rt2t']
sorted_words = sorted(words, key=sum_of_digits, reverse=True)
print(sorted_words)