def Fib_Gen(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b
n = int(input("Введите N: "))
fib = Fib_Gen(n)

for num in fib:
    print(num)