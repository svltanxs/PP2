def is_prime(n):
    if(n < 2):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if(n % 2 == 0):
            return False
    return True
def filter(numbers):
    for i in numbers:
        if is_prime(i):
            return i
numbers = input().split

primes = filter_prime(numbers)
print(primes)
