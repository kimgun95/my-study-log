input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


# memo에 기록하는 행위(메모이제이션)를 통해 큰 값이라도 run time error없이 결과를 도출해낼 수 있게 한다
def fibo_dynamic_programming(n, fibo_memo):
    # input값인 n이 memo에 기록되어 있다면 바로 반환
    if n in fibo_memo:
        return fibo_memo[n]

    # memo에 기록되어 있지 않다면 어쩔 수 없이 재귀 호출로 계산을 해준다
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    # 대신 계산시 마다 memo에 기록을 해준다
    fibo_memo[n] = nth_fibo

    return nth_fibo


print(fibo_dynamic_programming(input, memo))