'''
Multiples of 3 or 5
Show HTML problem content 
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def problem1(n):
#Find sum of all multiples of 3 or 5 below 1000
    x = []
    for i in range(n):
        if n%3 == 0 or n%5 == 0:
            x.append(i)
    return sum(x)

print('Sum of all multiples of 3 or 5 below 1000 is ' + str(problem1(1000)))

