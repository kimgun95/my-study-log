def calculate(cnt, width):
    total = 0
    total += (cnt // (width * 2 + 1))
    if cnt % (width * 2 + 1) != 0:
        total += 1
    return total


def solution(n, stations, w):
    answer = 0
    dp = [0] * (n + 1)
    for s in stations:
        left, right = s - w, s + w
        if left < 1:
            left = 1
        if right > n:
            right = n
        for node in range(left, right + 1):
            dp[node] = 1
    count = 0
    for i in range(1, n + 1):
        if dp[i] == 0:
            count += 1
            if i == n:
                answer += calculate(count, w)
        else:
            answer += calculate(count, w)
            count = 0
    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
