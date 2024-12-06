def get_even(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i

list_of_nums = [1, 2, 5, 6, 11]
print("До фильтрации: " + str(list_of_nums))
print("Только четные числа: ", end = " ")
for i in get_even(list_of_nums):
    print(i, end = " ")