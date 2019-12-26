# Method 1: Recursive program
# Function for nth Fibonacci number


def fibonacci(n):
    if n <= 0:
        print(" Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci Number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Driver Code
num = int(input(" Enter a number: "))
print("The Fibonacci Number is ", fibonacci(num))
