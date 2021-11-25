# N이 0 혹은 1일 때 코드 진행을 하지 않고 바로 정답 출력
# 처음에 dp를 활용하지 않고 탐색을 하니까 '시간초과'가 발생
def solution():
    T = int(input())
    for i in range(T):
        N = int(input())
        if N == 0:
            print(1, 0)
        elif N == 1:
            print(0, 1)
        else:
            dp = [[-1, -1] for _ in range(N + 1)]
            dp[0] = [1, 0]
            dp[1] = [0, 1]

        def fibonacci(num):
            nonlocal dp
            # 이미 계산한 적 있다면 dp값 리턴
            if dp[num][0] != -1:
                return
            fibonacci(num - 1)
            fibonacci(num - 2)
            dp[num] = [dp[num - 1][0] + dp[num - 2][0], dp[num - 1][1] + dp[num - 2][1]]
            return

        if N != 0 and N != 1:
            fibonacci(N)
            print(dp[N][0], dp[N][1])
    return


solution()