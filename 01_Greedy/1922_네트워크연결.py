import sys


def solution():
    n = int(sys.stdin.readline().split()[0])
    m = int(sys.stdin.readline().split()[0])
    costs = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    # kruskal을 활용하기 위해 가중치 기준으로 정렬
    costs.sort(key=lambda x: x[2])
    # union-find를 위한 자료구조 초기화
    parent = dict()
    rank = dict()
    for i in range(1, n + 1):
        parent[i] = i
        rank[i] = 0

    def find(vertice):
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1, vertice2):
        root1 = find(vertice1)
        root2 = find(vertice2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    total_cost = 0
    for cost in costs:
        node1, node2, money = cost
        if find(node1) != find(node2) and node1 != node2:
            union(node1, node2)
            total_cost += money
    return total_cost


print(solution())