def main():
    test = int(input())
    # test 크기만큼 반복
    for i in range(test):
        N = int(input())
        camels = [] * N
        camels = list(map(int, input().split(' ')))

        arrive = [] * N
        time = 0
        if len(camels) == 1:
            time = camels[0]
        else:
            # 낙타를 우선 정렬 후 최솟값 1,2를 key로 저장해둔다
            camels.sort()
            k1 = camels[0]
            k2 = camels[1]
            # 비어있지 않다면 낙타를 계속 옮긴다
            while len(camels) > 1:
                # 옮기지 않은 낙타 무리에 key 1,2가 모두 있다면 이 둘을 옮긴다
                if k1 in camels and k2 in camels:
                    arrive.insert(0, k2)
                    arrive.insert(0, k1)
                    camels.remove(k2)
                    camels.remove(k1)
                    time += k2
                else:
                    max_num1 = camels[-1]
                    max_num2 = camels[-2]
                    arrive.append(max_num2)
                    arrive.append(max_num1)
                    camels.remove(max_num1)
                    camels.remove(max_num2)
                    time += max(max_num1, max_num2)
                # 아직 낙타가 남았다면 돌아간다
                if len(camels) > 0:
                    num = min(arrive)
                    camels.insert(0, num)
                    arrive.remove(num)
                    time += num
        print('#{0} {1}'.format(i + 1, time))




main()