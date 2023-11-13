def reverse_args(func):
    def wrapper(*args, **kwargs):
        args = list(args)
        args.reverse()
        return func(*args, **kwargs)
    return wrapper

@reverse_args
def foo(a, b):
    print(a, b)

foo(4, 5)