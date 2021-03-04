a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a <= b and c >= d) < 10:
    for i in range(c, d + 1):
        print('\t', i, end="")
    for i in range(a, b+1):
        print('\n', i, end='')
        for j in range(c, d+1):
            print('\t', i * j, end='')

