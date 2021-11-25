def main():
    test = int(input())
    # 테스트 케이스 만큼 반복
    for i in range(test):
        # 입력 데이터 정제
        num = list(map(int, input().split(' ')))
        N = num[0]
        K = num[1]
        ling = [[] for i in range(K)]
        for j in range(K):
            ling[j] = list(input())

        save = [([0] * N) for i in range(K)]
        # 각 행, 열에서 1이 될 수 있는 최소 회전 수를 구하여 저장한다
        # 시간 복잡도가 말이 안되어 구현하지 말까 생각했지만 도저히 아이디어가 떠오르지 않아 구현했다
        for a in range(K):
            for b in range(N):
                count = 0
                if ling[a][b] != '1':
                    for c in range(1, K):
                        num = a + c
                        if num >= K:
                            num -= K
                        if ling[num][b] == '1':
                            count = c
                            break
                    for d in range(1, K):
                        num = a - d
                        if num < 0:
                            num += K
                        if ling[num][b] == '1':
                            count = min(count, d)
                            break
                save[a][b] = count

        cal_save = [0] * K
        for a in range(K):
            sum = 0
            for b in range(N):
                sum += int(save[a][b])
            cal_save[a] = sum

        print('#{0} {1}'.format(i + 1, min(cal_save)))



main()