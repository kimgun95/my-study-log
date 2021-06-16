def main():
    test = int(input())
    # 테스트 케이스 만큼 반복
    for t in range(test):
        # 입력값 받기
        num_list = input().split(' ')
        filt = list(input())
        # A, B, filter, filter_rev 데이터 정제
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

        # 카운트 초기화
        count = 0
        # 좌 -> 우 방향으로 filter를 적용할 수 있는 한도 내 숫자를 먼저 계산
        for i in range(6 - len(filt) + 1):
            if A[i] != B[i]:
                diff = abs(A[i] - B[i])
                if A[i] > B[i]:
                    if filt[0] == -1:
                        for j in range(len(filt)):
                            A[i + j] += (filt[j] * diff)
                        count += diff
                    elif filt_rev[0] == -1:
                        for j in range(len(filt)):
                            A[i + j] += (filt_rev[j] * diff)
                        count += diff
                else:
                    if filt[0] == 1:
                        for j in range(len(filt)):
                            A[i + j] += (filt[j] * diff)
                        count += diff
                    elif filt_rev[0] == 1:
                        for j in range(len(filt)):
                            A[i + j] += (filt_rev[j] * diff)
                        count += diff
        # 계산 결과로 A가 허용 범위를 벗어났다면 count = -1
        for num in A:
            if num > 9 or num < 0:
                count = -1
        # 우 -> 좌 방향으로 마지막 정리를 한다
        if count != -1:
            for i in range(len(filt) - 1):
                num = 6 - (i + 1)
                if A[num] != B[num]:
                    diff = abs(A[num] - B[num])
                    if A[num] > B[num]:
                        if filt[-1] == -1:
                            for j in range(len(filt)):
                                A[num + j - len(filt) + 1] += (filt[j] * diff)
                            count += diff
                        elif filt_rev[-1] == -1:
                            for j in range(len(filt)):
                                A[num + j - len(filt) + 1] += (filt_rev[j] * diff)
                            count += diff
                    else:
                        if filt[-1] == 1:
                            for j in range(len(filt)):
                                A[num + j - len(filt) + 1] += (filt[j] * diff)
                            count += diff
                        elif filt_rev[-1] == 1:
                            for j in range(len(filt)):
                                A[num + j - len(filt) + 1] += (filt_rev[j] * diff)
                            count += diff
        # 계산 결과로 A가 허용 범위를 벗어났다면 count = -1
        for num in A:
            if num > 9 or num < 0:
                count = -1
        print('#{0} {1}'.format(t + 1, count))
main()