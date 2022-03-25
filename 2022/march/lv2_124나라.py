def solution(n):
    if n <= 3:
        return '124'[n - 1]
    # n - 1을 하는 이유: 0부터가 아닌 1부터 시작하기 때문에 크기를 1 줄이고 3으로 나눠준다
    return solution((n - 1) // 3) + '124'[(n - 1) % 3]


print(solution(10))