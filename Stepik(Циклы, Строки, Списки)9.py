a = int(input())
b = 0
c = 0
x = 1
while x != 0:
    b = b + a
    c = a ** 2 + c
    if b == 0:
        print(c)
        break
    a = int(input())