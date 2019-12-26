# Using Dynamic Programming with Space Optimization


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


# Driver program
num = int(input(" Enter a number: "))
print("The Fibonacci Number is ", fibonacci(num))
