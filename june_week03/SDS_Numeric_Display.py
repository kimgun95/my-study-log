def main():
    test = int(input())
    for i in range(test):
        num_list = input().split(' ')
        filt = list(input())
        print(num_list)
        print(filt)
        A = list(map(int, list(num_list[0])))
        B = list(map(int, list(num_list[1])))
        for i in range(6 - len(A)):
            A.insert(0, 0)
        for i in range(6 - len(B)):
            B.insert(0, 0)

        for i in range(len(filt)):
            if filt[i] == '+':
                filt[i] = 1
            elif filt[i] == '-':
                filt[i] = -1
            else:
                filt[i] = 0

        filt_rev = [] * len(filt)
        for i in range(len(filt)):
            filt_rev.append(filt[len(filt) - (i + 1)])
        print(A)
        print(B)
        print(filt)
        print(filt_rev)
main()