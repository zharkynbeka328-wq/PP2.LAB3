def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5, 11, 15, 17]
primes = list(filter(lambda x: is_prime(x), nums))
print("Простые числа:", primes) 


# [2, 3, 5, 11, 17]
