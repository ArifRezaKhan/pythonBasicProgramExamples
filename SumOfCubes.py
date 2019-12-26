# The sum of cubes of n natural numbers is given "(n(n+1) / 2) ** 2"
# For optimizing overflow we are using if conditions


def sum_of_cubes(n):
    x = 0
    if n >= 0:
        if n % 2 == 0:
            x = (n/2) * (n+1)
        else:
            x = n * ((n+1)/2)
        return int(x * x)
    else:
        print(" Please enter a NATURAL number")


# Driver Code
p = int(input(" Sum of cubes of 'n' natural nos. Enter n:"))
print(sum_of_cubes(p))
