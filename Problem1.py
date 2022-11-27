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