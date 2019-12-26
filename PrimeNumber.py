# To print all prime numbers in an interval
start = 4
end = 30
for val in range(start, end+1):
    if val > 1:
        for n in range(2, val):
            if val % n == 0:
                break
        else:
            print(val)

