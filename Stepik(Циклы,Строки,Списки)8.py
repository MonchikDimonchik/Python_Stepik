a = sorted([int(i) for i in input().split()])
length = len(a)
counter = -1
counter2 = 0
for i in a:
    counter += 1
    if counter == length - 1:
        if counter2 >= 1:
            print(a[counter - 1])
    else:
        if i == a[counter + 1]:
            counter2 += 1
            continue
        elif counter2 >= 1:
            print(a[counter - 1], end=' ')
            counter2 = 0