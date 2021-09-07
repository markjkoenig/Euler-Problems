'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
digits = [0,1,2,3,4,5,6,7,8,9]


def isPalindrome(n):
    s = str(n)
    sl = list(s)
    #print(sl)
    if len(sl) != 1:    
        for i in range(int((len(sl)+1)/2)+1):
            if sl[i] != sl[-(i+1)]:
                return False
        return True
    else:
        return True
    
'''
print(isPalindrome(2))
print(isPalindrome(121))
print(isPalindrome(122))
print(isPalindrome(135531))
print(isPalindrome(1234421))
'''

def maxDrome():
    dromes = []
    for i in range(100,1000):
        for j in range(100,1000):
            num = i*j
            if isPalindrome(num):
                dromes.append(num)
    return max(dromes)


if __name__ == "__main__":
    print(maxDrome())

    
