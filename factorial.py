def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        total = 1
        while x > 1:
            total *= x
            x -= 1
        return total