# Sum of squares of natural numbers up to n is given by the formula n(n+1)(2n+1)/6
# To optimize overflow we can divide (n * (n + 1)) by 2 and (2n+1) by 3


def sum_of_squares(n):
    if n >= 0:
        return (n * (n + 1)) / 2 * (2 * n + 1) / 3
    else:
        print(" n must be a natural number.")


# Driver Code
a = float(input("Enter a number up to which you want to find sum of squares: "))
x = int(a)
print(sum_of_squares(x))
