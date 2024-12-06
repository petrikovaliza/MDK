def repeat(n):
    def decorator(input_func):
        def wrapper(*args, **kwards):
            return "\n".join(input_func(*args, **kwards) for _ in range(n))
        return wrapper        
    return decorator
        
        
@repeat(5)
def print_greeting(greeting, name):
    return (f'{greeting}, {name}')
    
print(print_greeting('hello', 'liza'))