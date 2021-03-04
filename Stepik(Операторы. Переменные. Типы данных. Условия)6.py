n = int(input())
if n // 10 % 10 == 1 or n % 10 == 0 or n % 10 >= 5:
    print(n, 'программистов')
elif n % 10 == 1:
    print(n, 'программист')
else:
    print(n, 'программиста')