def caching_fibonacci():
    cache_dict = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache_dict:
            return cache_dict[n]

        cache_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache_dict[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

