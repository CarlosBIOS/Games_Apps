import time

# Write your code below 👇


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f'{function.__name__} run speed: {end_time - start_time}')
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


slow_function()
fast_function()

print('*' * 80)

# The challenge:
inputs = eval(input())
# TODO: Create the logging_decorator() function 👇


def logging_decorator(function):
    def calculate(*args):
        result = function(args[0], args[1], args[2])
        print(f'You called {function.__name__}{args}\nIt returned: {result}')
    return calculate


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
