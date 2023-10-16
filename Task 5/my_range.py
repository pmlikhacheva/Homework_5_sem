
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    if step > 0:
        if start > stop:
            raise Exception("step is positive but stop is less than start")
        curr = start
        while curr < stop:
            yield curr
            curr += step
    elif step < 0:
        if start < stop:
            raise Exception("step is negative but start is less than stop")
        curr = start
        while curr > stop:
            yield curr
            curr += step
    else:
        raise ValueError("Step cannot be zero")

for i in my_range(10, 2, -2):
    print(i)

for i in my_range(0, 10, -1):
    print(i)