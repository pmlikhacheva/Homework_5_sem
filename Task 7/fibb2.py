import time
from functools import lru_cache

# Функция для вычисления числа Фибоначчи через циклы
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Функция для вычисления числа Фибоначчи через рекурсию без использования @cache
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Функция для вычисления числа Фибоначчи через рекурсию с использованием @cache
@lru_cache(maxsize=None)
def fibonacci_recursive_cached(n):
    if n <= 1:
        return n
    return fibonacci_recursive_cached(n-1) + fibonacci_recursive_cached(n-2)

# Сравнение скорости работы функций
n = 30

start_time = time.perf_counter()
fibonacci_iterative(n)
end_time = time.perf_counter()
print("Число Фибоначчи (Циклы)")
print(f"Время: {end_time - start_time:.8f} секунд")

start_time = time.perf_counter()
fibonacci_recursive(n)
end_time = time.perf_counter()
print("Число Фибоначчи (Рекурсия)")
print(f"Время: {end_time - start_time:.8f} секунд")

start_time = time.perf_counter()
fibonacci_recursive_cached(n)
end_time = time.perf_counter()
print("Число Фибоначчи (Рекурсия и @cache)")
print(f"Время: {end_time - start_time:.8f} секунд")

