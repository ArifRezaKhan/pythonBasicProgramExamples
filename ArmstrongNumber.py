# Function to calculate order of the number
def order(x):
    # Variable to store the number of digits
    n = 0
    while x != 0:
        x % 10
        x = x // 10
        n += 1
    return n


# Function to check whether the given number is
# Armstrong number or not
def isArmstrong(x):
    n = order(x)
    sum1 = 0
    while x != 0:
        r = x % 10
        sum1 += r ** n
        x = x // 10

    # If condition satisfies
    return sum1 == z


# Driver Program
z = 153
print("Armstrong Number:", isArmstrong(z))
