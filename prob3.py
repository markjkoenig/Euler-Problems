'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def findPrime(n):
    for i in range(2,int(n**0.5)+1): # parse thru lefthand factors
        if n%i==0:
            return i 
    return n


def findLargestPrime(n):
    while True: 
        k = findPrime(n)
        if k < n:
            n = n/k
        else:
            return int(n)

if __name__ == "__main__":
    print(findLargestPrime(600851475143))
