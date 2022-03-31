# 10억이라는 큰 입력 값에 의해 런타임 에러, 시간 초과가 계속 발생했다
# 1. 처음엔 다익스트라로 weight를 계산하며 풀었다. (실패)
# 2. 위 해결법이 시간이 좀 걸릴 것 같아 (현재위치 * 2)들을 반복하며 dp를 채워보았다. (실패)
# 3. 그냥 해당 위치를 2로 나누며 나머지 값을 cost로 추가하면 되었다.
def solution(n):
    cost = 0
    while n > 0:
        q, r = divmod(n, 2)
        cost += r
        n = q
    return cost


print(solution(5))