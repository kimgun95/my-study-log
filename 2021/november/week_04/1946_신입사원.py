# 1. 생각: 내가 생각하기에는 반례가 있는데 왜 사람들이 쉽게 접근해서 풀었지? 라는 생각을 오래했다.
# 2. 착오: 선발할 수 있는 최대 인원에 나는 집중을 했고 그렇게 선발된 인원들끼리 순위 비교를 했을 때 조건을 만족하면 된다고 생각했다.
#           하지만 지원자 전체에 대한 조건이 만족했어야 했고 여기서 쉽게 아이디어를 떠오르면 다음과 같다.
# 3. 아이디어: 서류 1등과, 면접 1등은 무조건 선발이 될 것이다. 따라서 서류를 기준으로 오름차순 정렬 후 면접을 기준으로 사람들을 뽑아 나가면 되었다.
#           서류 1등의 면접 점수를 시작으로 내림차순의 면접 점수를 뽑다보면 면접 1위까지 가게 될 것이다.
#           이렇게 서류기준 오름차순, 면접기준 내림차순 조건을 만족하면 선발을 할 수 있게 된다.
import sys


def solution():
    T = int(input())
    # 테스트 케이스만큼 입력 받고 출력
    for i in range(T):
        N = int(input())
        rank = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        # 서류 기준으로 순위 오름차순 정렬
        rank.sort(key=lambda x: x[0])

        count = 1
        criterion = rank[0][1]
        # 면접 기준으로 순위 비교하며 내림차순이 만족되는 것은 count up
        for j in range(1, N):
            if rank[j][1] < criterion:
                count += 1
                criterion = rank[j][1]
        print(count)
    return


solution()