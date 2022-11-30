#The prime factors of 13195 are 5, 7, 13 and 29. 
#What is the largest prime factor of the number 600851475143 ?

import math

def largest_prime_factor(x):
    factors = []
    if x%2 == 0: 
        factors.append(2)
    i = 3
    while i <= math.floor(math.sqrt(x)):
        if x%i == 0:
            divisible = 0
            for factor in factors:
                if i%factor == 0:
                    divisible = 1
                    break
            if divisible == 0:
                factors.append(i)
        i+=2
    return factors

print(prime_factors(600851475143))