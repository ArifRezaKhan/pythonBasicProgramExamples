# First way is Recursive and Iterative.
def factorial(n):
    # Single line to find factorial
    # return 1 if (n == 1 or n == 0)  else n * factorial(n - 1)
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return " Negative numbers don't have factorial!"
    else:
        return n * factorial(n-1)


# Driver code
num = float(input("Enter a number:"))
num1 = (round(num))
print("Factorial of", num1, "is", factorial(num1))
