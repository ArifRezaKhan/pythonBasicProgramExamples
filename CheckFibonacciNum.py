# Python program to check if a no is Fibonacci number or not!
import math


# Utility function that returns true if x is a perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


# Returns true if n is a Fibonacci Number or else False
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


# Utility function to test
for i in range(1, 11):
    if isFibonacci(i):
        print(i, " is a FIBONACCI Number.")
    else:
        print(i, "No NOT fibonacci")
