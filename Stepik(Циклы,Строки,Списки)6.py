dnk = input().lower()
counter = -1
counter2 = 1
for i in dnk:
    counter += 1
    if len(dnk) > counter + 1:
        if i == dnk[counter + 1]:
            counter2 += 1
            continue
        if len(dnk) == counter + 1:
            counter2 += 1
            print(i + str(counter2), end='')
            break
        else:
            print(i + str(counter2), end='')
            counter2 = 1
    else:
        print(i + str(counter2), end='')