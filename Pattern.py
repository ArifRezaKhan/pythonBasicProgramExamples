for i in range(4):
    for j in range (4):
        print("#", end=" ")
    print()
print(" New Pattern")

for i in range(4):
    for j in range(i + 1):
        print("#", end=" ")
    print()

print(' Another New Pattern')
for i in range(4):
    for j in range(4 - i):
        print("#", end=" ")
    print()
