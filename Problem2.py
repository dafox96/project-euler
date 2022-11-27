x = 1
y = 1
z = 2
sum = 0
while z <= 4000000:
    if z%2 == 0:
        sum += z
    x = y
    y = z
    z = x + y
print(sum)