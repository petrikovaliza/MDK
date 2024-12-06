import time

def timer(input_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции : {end_time - start_time:.2f} секунд")
        return result
    return wrapper

@timer
def func():
    time.sleep(3)
    return 1

func()
        
        