def solution(board, arrows, threshold):
    n = len(board)
    for i in range(len(arrows)): # 방향 입력 수 만큼 수행
        a = arrows[i]
        if 0 < a <= n: # 1. 아래로 움직일 때
            a -= 1
            for p in range(n - 1, -1, -1): # 맨 아래부터 이동
                if board[p][a] == 1: # 돌이 있을 때
                    if p == n - 1: # 인덱스를 벗어나는 돌 일 때
                        cnt = 0 # 얼마나 쌓였는지
                        idx = p - 1
                        while idx >= 0:
                            if board[idx][a] == 0: # 부시지 못함
                                break
                            cnt += 1
                            if cnt >= threshold: # 부시기
                                board[n - 1][a] = 0
                                break
                            idx -= 1
                    else:
                        if board[p + 1][a] == 0: # 앞이 비어있다면 돌 이동
                            board[p + 1][a] = 1
                            board[p][a] = 0
        elif n < a <= 2 * n: # 2. 좌로 움직일 때
            a -= 1
            a %= n
            for p in range(n): # 맨 왼쪽부터 이동
                if board[a][p] == 1: # 돌이 있을 때
                    if p == 0: # 인덱스를 벗어나는 돌 일 때
                        cnt = 0 # 얼마나 쌓였는지
                        idx = p + 1
                        while idx < n:
                            if board[a][idx] == 0: # 부시지 못함
                                break
                            cnt += 1
                            if cnt >= threshold: # 부시기
                                board[a][0] = 0
                                break
                            idx += 1
                    else:
                        if board[a][p - 1] == 0: # 앞이 비어있다면 돌 이동
                            board[a][p - 1] = 1
                            board[a][p] = 0

        elif 2 * n < a <= 3 * n: # 3. 위로 움직일 때
            a -= 1
            a %= n
            a += 1
            a = n - a
            for p in range(n): # 맨 위부터 이동
                if board[p][a] == 1: # 돌이 있을 때
                    if p == 0: # 인덱스를 벗어나는 돌 일 때
                        cnt = 0 # 얼마나 쌓였는지
                        idx = p + 1
                        while idx < n:
                            if board[idx][a] == 0: # 부시지 못함
                                break
                            cnt += 1
                            if cnt >= threshold: # 부시기
                                board[0][a] = 0
                                break
                            idx += 1
                    else:
                        if board[p - 1][a] == 0: # 앞이 비어있다면 돌 이동
                            board[p - 1][a] = 1
                            board[p][a] = 0
        elif 3 * n < a <= 4 * n: # 우로 움직일 때
            a -= 1
            a %= n
            a += 1
            a = n - a
            for p in range(n - 1, -1, -1): # 맨 오른쪽부터 이동
                if board[a][p] == 1:  # 돌이 있을 때
                    if p == n - 1:  # 인덱스를 벗어나는 돌 일 때
                        cnt = 0  # 얼마나 쌓였는지
                        idx = p - 1
                        while idx >= 0:
                            if board[a][idx] == 0:  # 부시지 못함
                                break
                            cnt += 1
                            if cnt >= threshold:  # 부시기
                                board[a][n - 1] = 0
                                break
                            idx -= 1
                    else:
                        if board[a][p + 1] == 0:  # 앞이 비어있다면 돌 이동
                            board[a][p + 1] = 1
                            board[a][p] = 0

    return board


# [[0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0]]
print(solution([[0,0,0,1,0,0], [0,0,0,0,0,0], [0,0,1,1,0,0], [0,1,0,1,0,0,], [0,0,0,1,0,0],[1,1,1,1,0,0]],[19,16,15],5))
# [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(solution([[0,0,0,0,0], [1,1,0,1,1], [0,0,0,0,0], [0,0,0,0,0,], [0,0,0,0,0]],[7,7,7,7,7,7,7,7,7],1))