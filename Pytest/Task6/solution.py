def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x%2 == 0:
        return False
    i = 3
    while i ** 2 <= x:
        if x%i == 0:
            return False
        i += 2
    return True    