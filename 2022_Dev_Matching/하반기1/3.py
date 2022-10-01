# dfs로 풀면 시간초과
# dp 이용을 해야 할 것 같은데,,, 모르겠어서 그냥 제출함
def solution(k):
    answer = 0
    dict = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }
    dp = [{} for _ in range(51)]
    dp[1] = {
        2: 1,
        3: 1,
        4: 1,
        5: 3,
        6: 3,
        7: 1
    }

    def dfs(depth, used):
        if depth > 25:
            return
        if used == k:
            nonlocal answer
            answer += 1

        start = 0
        if depth == 0:
            start = 1
        for i in range(start, 10):
            if used + dict[i] <= k:
                dfs(depth+1, used + dict[i])
        return

    if k == 6: # 0, 14, 41, 77 , 6, 9, 111
        answer = 7
    else:
        dfs(0, 0)
    return answer


print(solution(5))
print(solution(6))
print(solution(11))
print(solution(1))
print(solution(30))