def fib(n):
    """Return a list containing a fibonnaci series upto n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


number = int(input("Please enter a number: "))
print(fib(number))
