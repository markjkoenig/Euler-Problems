'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def GCD(x, y): # Euclidian algorithm for two nums
    if  y == 0:
        return x
    else:
        return GCD(y, x%y)


def LCM(x, y): # LCM eqn for two nums
    lcm = int(x*y / GCD(x,y))
    return lcm


def induct(foo, k): 
# Induct a function up to k arguments (lcm(x1, x2,..., xk) = lcm(lcm(x1, x2), x3,..., xk) = ...)
    S = [i for i in range(1, k+1)]
    while len(S) != 1:
        S[0] = foo(S[0], S[1])
        del(S[1])
    return(S[0])

if __name__ == '__main__':
    print(induct(LCM, 20))
