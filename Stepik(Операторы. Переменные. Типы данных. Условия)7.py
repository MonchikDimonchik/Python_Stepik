n = input()
a = [int(x) for x in n[:3]]
b = [int(x) for x in n[3:]]
if sum(a) == sum(b):
    print('Счастливый')
else:
    print('Обычный')