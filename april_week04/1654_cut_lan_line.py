def cut_lan_line():
    K, N = map(int, input().split())
    line = []
    sum = 0
    for i in range(K):
        line.append(int(input()))
        sum += line[i]
    # N개로 만들 수 있는 길이의 최대, 최소값을 정의
    high = sum // N
    low = 1
    # 이분 탐색, 최소와 최대의 중간 값을 넣어주면서 범위를 줄여나감.
    # 단순히 1증가, 감소로 반복문을 진행하면 시간초과가 발생
    while low <= high:
        cnt = 0
        mid = (high + low) // 2
        for l in line:
            cnt += l // mid
        if cnt >= N:
            low = mid + 1
        else:
            high = mid - 1
    return high


print(cut_lan_line())