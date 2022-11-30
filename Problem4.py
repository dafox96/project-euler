#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(x):
    x = str(x)
    if(x==x[::-1]):
        return True
    return False
i = 999
while i > 0:
    j = i
    k = i
    while j<=999:
        while j<= 999:
            if(is_palindrome(j*k)):
                print(j*k)
                quit()
            j += 1
            k -= 1
        if k%2:
            j = i
            k = i-1
    i -= 1
