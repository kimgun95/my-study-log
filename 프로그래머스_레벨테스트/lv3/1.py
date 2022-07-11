# 삼각형 모양의 트리에서 노드에서 내려갈 때 가장 최대로 만들 수 있는 합의 경로를 찾는 문제
def solution(triangle):
    answer = 0
    size = len(triangle)
    visit = []
    for i in range(size):
        visit.append([-1 for _ in range(len(triangle[i]))])


    def checkMax(num, idx):
        if visit[num][idx] != -1: # 백 트래킹 탐색
            return visit[num][idx]
        nonlocal size
        if num + 1 >= size:
            return triangle[num][idx]
        visit[num][idx] = max(checkMax(num+1, idx), checkMax(num+1, idx+1)) + triangle[num][idx]
        return visit[num][idx]

    answer = checkMax(0, 0)
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))