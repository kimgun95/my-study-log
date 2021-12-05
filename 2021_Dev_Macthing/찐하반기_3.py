def solution(s):
    answer = -1
    alpha = ["qwertyuio", "pasdfghjk", "lzxcvbnm"]
    visit = (1 << 26) - 1
    dp = [[None]] * visit
    INF = float('inf')

    def dfs(depth, idx, visited):
        if depth < 0 or depth >= 3 or idx < 0 or (depth == 2 and idx >= 1):
            return INF
        if dp[visited] is not None:
            return dp[visited]
        if visited & (1 << 4) == 1:
            return 1
        # 상하좌우 이동
        visited = visited & (1 << (9 * depth + idx))
        up = dfs(depth - 1, idx, visited)
        down = dfs(depth + 1, idx, visited)
        left = dfs(depth, idx - 1, visited)
        right = dfs(depth, idx + 1, visited)
        dp[visited] = min(up, down, left, right) + 1
        return dp[visited]

    print(dfs(0, 0, 1 << 0))
    return answer


print(solution("abcc")) # 23
print(solution("tooth")) # 52
print(solution("zzz")) # 0