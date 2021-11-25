def sort_number(num):
    a = []
    for i in range(num):
        x = int(input())
        a.append(x)
    a.sort()
    for i in range(num):
        print(a[i])


sort_number(int(input()))