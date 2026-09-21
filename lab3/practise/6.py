class prime:
    def is_prime(self,n):
        if n < 2:
            return False
        for i in range(2 , int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    def filter_primes(self,numbers):
        return list(filter(lambda x: self.is_prime(x), numbers))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pf = prime()
primes = pf.filter_primes(numbers)

print(primes) 
    