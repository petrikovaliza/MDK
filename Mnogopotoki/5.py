import threading

def sum_list(list):
    sum_numbers = sum(list)
    print(f'Сумма элементов списка: {sum_numbers}')

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [8, 9, 10, 11, 12, 13, 14, 15]

thread1 = threading.Thread(target = sum_list, args = (list1,))
thread2 = threading.Thread(target = sum_list, args = (list2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()