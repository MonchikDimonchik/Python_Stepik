s = [0, 0, 1]
while s[2]:
    i = int(input())
    s = [s[0] + i, s[1] + i ** 2, s[0] + i]
print(s[1])