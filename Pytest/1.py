def uppercase(input_func):
    def wrapper(*args, **kwards):
        result = input_func(*args, **kwards)
        return result.upper()
    return wrapper

@uppercase
def print_greeting(greeting, name):
    return (f'{greeting}, {name}')


print(print_greeting('hello', 'liza'))
    