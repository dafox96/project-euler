#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
i = 3
while i < 1000:
    total += i
    print(i)
    print(total)
    i += 3

i = 5
while i < 1000:
    total += i
    print(i)
    print(total)
    if (i+5)%3!=0:
        i+=5
    else:
         i+=10

print(total)