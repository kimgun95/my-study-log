# 탐색은 한 번만 할거야 BFS로
# 해당 위치에 숫자가 0이 아니라면 왼쪽, 위쪽이 0이 아닌지 확인 (이때, 0행과 0열 참조 조심)
# 0이 아니라면 거기에 단지 번호를 매겼을 텐데 그 번호를 가져옴
# 둘 다 0이라면 숫자를 증가시킨 단지 번호를 준다
def attach_number(N):
    s = [] * N
    for i in range(N):
        s[i].append(list(input()))

    print(s)


attach_number(int(input()))