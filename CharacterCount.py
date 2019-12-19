test_str = "GeeksForGeeks"
char_count = {}
for i in test_str:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print("Character count in the string is : \n" + str(char_count))
