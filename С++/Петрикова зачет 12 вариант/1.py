def krat17(numbers):
    result_list = []
    for number in numbers:
        if number % 17 == 0:
            result_list.append(number)     
    
    return result_list

mylist = (359, 2839, 17, 230, 394, 293)
print(krat17(mylist))