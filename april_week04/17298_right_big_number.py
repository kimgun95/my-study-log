# 백만이라는 큰 수가 들어와 2중 for문을 돌릴수가 없는 상황
# 하나의 for문으로 해결을 해야 한다.
def right_big_number(num):
    a = list(map(int, input().split()))
    # 결과 값은 마지막 수는 -1 고정이기에 -1로 애초에 모두 초기화
    res = [-1 for _ in range(len(a))]
    # 스택의 기능을 활용하기 위해 list를 대체로 사용
    s = []
    # 한 번의 for문, 뒤에 나오는 while문은 s를 이용한 비교를 하는 데 s는 num만큼만 append 되기에 while문을 정확히 num번 만큼만 작동
    for i in range(num):
        while len(s) != 0 and a[i] > a[s[-1]]:
            res[s[-1]] = a[i]
            s.pop()
        s.append(i)

    for i in range(num):
        print(res[i], end='')
        print(' ', end='')


right_big_number(int(input()))