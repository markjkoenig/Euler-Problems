'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

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
    
def maxDrome():
    drome = 0
    for i in range(100,1000):
        for j in range(100,1000):
            num = i*j
            if isPalindrome(num) and num > drome:
                drome = num
    return drome


if __name__ == "__main__":
    print(maxDrome())

    
