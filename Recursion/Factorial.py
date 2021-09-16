def factorial(n):
    #    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n >= 0:
        return 1 if (n == 0 or n == 1) else n * factorial(n - 1)
print(factorial(-10))
