a = [int(i) for i in input().split()]
b = len(a)
counter = -1
for i in a:
    counter += 1
    if b == 1:
        print(i)
        break
    else:
        if counter == 0:
            c = a[counter+1] + a[-1]
        elif counter == b - 1:
            c = a[counter-1] + a[0]
            print(c)
            break
        else:
            c = a[counter-1] + a[counter+1]
    print(c, end=' ')
