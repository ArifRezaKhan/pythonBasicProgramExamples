# Function to calculate x raised to the power y
def power(x, y):
    if y == 0:
        return 1
    elif int(y % 2) == 0:
        return power(x, int(y / 2)) * power(x, int(y / 2))
    else:
        return x * power(x, int(y / 2)) * power(x, int(y / 2))


# Driver Code
x = 3
y = 2
print(power(x, y))
