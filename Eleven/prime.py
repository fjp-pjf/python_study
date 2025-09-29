def is_prime(num):
    if num < 2:  # 0 and 1 are not prime
        return False
    for i in range(2, int(num**0.5) + 1):  # check divisors up to sqrt(num)
        if num % i == 0:
            return False
    return True

is_prime(43)