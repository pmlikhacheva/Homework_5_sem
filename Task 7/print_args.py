def print_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Аргументы:", args, kwargs)
        return result
    return wrapper

@print_args
def example_func(a, b, c=1):
    return a + b + c

example_func(1, 2, c=3)
