#1

# def sum(a, b):
#     s = a + b
#     return s

# print(sum(25, 4))

#2

def get_even(numbers):
    even_nums = [num for num in numbers if not num % 2]
    print(even_nums)
    return even_nums

get_even([1, 2, 3, 4, 5, 6])

#3

def mean(sample):
    print(sample)
    a = sum(sample) / len(sample)
    print(a)
    return a


mean([1, 2, 3, 4])

#4

string1 = 'Techies'

for value in string1:
    if value == 'h':
        pass
    else:
        print('Value: ', value)
    