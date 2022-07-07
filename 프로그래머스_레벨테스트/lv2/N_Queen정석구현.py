n = int(input())
# index와 value 관계 -> queen이 index행,value열에 있다.
queen = [-1 for _ in range(n)]
count = 0


def check(idx, d): # 퀸을 배치할 수 있는지 체크
    for i in range(d):
        if queen[i] == queen[d]: # 세로 방향 비교
            return False
        if queen[i] - queen[d] == i - d: # 좌 대각선 방향 비교
            return False
        if queen[i] - queen[d] == d - i: # 우 대각선 방향 비교
            return False
    return True


def nQueen(depth):
    global count
    if depth >= n: # 모두 배치했다면 카운트 +1
        count += 1
        return
    for i in range(n):
        queen[depth] = i
        if check(i, depth):
            nQueen(depth + 1)
    return


nQueen(0)
print(count)