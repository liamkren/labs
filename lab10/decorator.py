def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

import time

def test_fibonacci(n):
    start = time.time()
    result = fibonacci(n)
    end = time.time()
    print(f"Fibonacci({n}) = {result}")
    print(f"Time taken: {end - start:.6f} seconds")

if __name__ == "__main__":
    n = 35
    print("Testing Fibonacci without memoization...")
    test_fibonacci(n)
