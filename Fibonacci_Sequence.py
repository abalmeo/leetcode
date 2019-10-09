from functools import lru_cache


def fibonacciOne(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacciOne(n-1) + fibonacciOne(n-2)
# if not using memoization, then repeatedly being called
# # for n in range(1, 11):
# #     print(n, ":", fibonacciOne(n))
# for n in range(1, 101):
#     print(n, ":", fibonacciOne(n))


fibonacci_cache = {}


def fibonacciTwo(n):
  # if we have cached value, return it otherwise compute Nth term
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacciTwo(n-1) + fibonacciTwo(n-2)
    fibonacci_cache[n] = value
    return value


# for n in range(1, 1000):
#     print(n, ":", fibonacciTwo(n))


# using internal tool
@lru_cache(maxsize=1000)
def fibonacciThree(n):
  # Check input is positive inter
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacciThree(n-1) + fibonacciThree(n-2)


for n in range(1, 501):
    print(n, ":", fibonacciThree(n))
