'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 +...+ 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 +...+ 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def ss(k):
    sumSquares = 0 # I know there is a fancy formula but I don't remember exactly...
    for i in range(k+1):
        sumSquares += i**2

    squareSum = (k*(k+1)/2)**2 # This one I do, though!

    diff = abs(int(sumSquares - squareSum))
    return diff


if __name__ == '__main__':
    print(ss(100))
