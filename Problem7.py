#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import math

def is_prime(x):
    if(x<=1):
        return False
    if(x==2 or x == 3):
        return True
    if(x%2 ==0 or x%3 == 0):
        return False 
    for y in range(5,math.floor(math.sqrt(x))+1,6):
        if(x%y == 0 or x%(y+2) == 0):
            return False
    return True

primes_found = 2
largest = 3

find = 10001

n = 0

while(primes_found < find):
    n+=1
    if(is_prime(6*n-1)):
        primes_found +=1
        largest = 6*n-1
    if(primes_found < find):
        if(is_prime(6*n+1)):
            primes_found += 1
            largest = 6*n+1

print(largest)