def catch_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('error')
            return "error"
    return wrapper

@catch_error
def divide(a, b):
    return a / b

result = divide(4, 0) 
