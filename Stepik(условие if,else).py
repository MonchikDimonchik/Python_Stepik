a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print("Это нормально")

if h < a and h < b:
    print("Недосып")

if b < h and h > a:
    print("Пересып")