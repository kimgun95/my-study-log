def solution(n):
    answer = 0
    col = [True for _ in range(n)] # 세로 체크
    visit = [[True for _ in range(n)] for _ in range(n)] # 대각선 체크

    def checkVisit(v, size, idx):
        board = []
        for i in range(n): # board에 v를 deepcopy
            board.append(v[i][:])
        left = idx
        right = idx
        while size < n: # 대각선 요소들을 방문 처리
            left -= 1
            right += 1
            if 0 <= left < n:
                board[size][left] = False
            if 0 <= right < n:
                board[size][right] = False
            size += 1
        return board

    def search(depth, visited):
        nonlocal answer
        if depth > n - 1: # 한가지 경우의 수 추가
            answer += 1
            return
        for i in range(n):
            if not col[i]: # 세로로 이미 있을 때
                continue
            if visited[depth][i]: # 놓을 수 있을 때
                col[i] = False
                # 대각선 좌우 이동 visit 체크
                search(depth + 1, checkVisit(visited, depth + 1, i))
                col[i] = True
        return

    search(0, visit)
    return answer


print(solution(4)) # 2
print(solution(8)) # 92