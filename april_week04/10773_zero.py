def zero(num):
    a = []
    for i in range(num):
        x = int(input())
        if x == 0:
            if len(a) > 0:
                a.pop()
        else:
            a.append(x)
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    print(sum)


zero(int(input()))