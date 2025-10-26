def caching_fibonacci() -> callable:
    cache = {0: 0, 1: 1}  # initiation of default cache values

    def fibonacci(n: int) -> int:
        if n < 0:
            return 0  # base case as per task requirements
        if n in cache:
            return cache[n]  # return cached value
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # recursive calc
            return cache[n]

    return fibonacci


# Example usage
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610
print(fib(0))  # 0
print(fib(-10))  # 0



