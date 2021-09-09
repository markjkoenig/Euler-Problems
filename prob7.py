'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''
from prob5 import GCD

def genPrimes(k): # up to k primes
    primes = [2]
    i = 3
    while len(primes) < k:
        if all(GCD(i, p)==1 for p in primes):
            primes.append(i)
        i += 1

    return primes[-1]


if __name__ == '__main__':
    print(genPrimes(10001))
