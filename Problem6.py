#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(x):
    sum = 0
    for y in range(1, x+1):
        sum += y*y
    return sum

def square_sum(x):
    square = 0
    for y in range(1,x+1):
        square+=y
    square = square*square
    return square

print(square_sum(100)-sum_squares(100))