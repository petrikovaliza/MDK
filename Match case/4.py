def analyze_list(number):
    match number:
        case[] : print('Список пуст')
        case number if len(number) == 1 : print('В списке одно число: ', *number )
        case number if len(number) == 2 : print('В списке два числа: ', *number )
        case number if len(number) > 2 : print('В списке много чисел, всего: ', *number )
        
analyze_list([])
analyze_list([5])
analyze_list([3, 7])
analyze_list([1, 2, 3, 4])
analyze_list([])



# {number}