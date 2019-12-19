num = int(input("Enter a number to check if it's narcissistic or not: "))


def order(temp=num):
    count = 0
    while temp > 0:
        temp % 10
        temp //= 10
        count += 1
    return count


def determine(temp=num):
    count = order(temp)
    sum1 = 0
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** count
        temp //= 10
    if num == sum1:
        print(num, " is an ARMSTRONG Number")
    else:
        print(num, "NOT an Armstrong number")


# Driver Code
determine(num)
