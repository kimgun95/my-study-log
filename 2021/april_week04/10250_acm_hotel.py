def acm_hotel(num):
    for i in range(num):
        H, W, N = map(int, input().split())
        if N % H == 0:
            result = H * 100 + N//H
        else:
            result = N % H * 100 + N // H + 1
        print(result)


acm_hotel(int(input()))