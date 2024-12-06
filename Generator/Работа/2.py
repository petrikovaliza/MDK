def fibonacci_generator():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
print(type(fib_gen))
for num in fib_gen:
    print(num)