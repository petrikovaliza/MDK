#Комбинирование областей видимости

def sum_numbers(numbers):
    local_sum = sum(numbers)
    global total
    total = 100 - local_sum
    print('сумма чисел:', local_sum)
    print('Обновленный total: ', total)
    
sum_numbers([10 ,20, 30])