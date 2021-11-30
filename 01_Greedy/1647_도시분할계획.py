# kruskal algorithm 을 활용해 풀었다.
# prim algorithm 을 대충 이해하고 구현해서 풀었더니 '시간초과'가 발생했다
# kruskal을 많이 활용하는 것 같아서 공부를 했고 꽤 어려웠다
import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    cost = []
    for i in range(m):
        road = list(map(int, sys.stdin.readline().split()))
        cost.append(road)
    # 1. 가중치를 기준으로 간선 정렬
    cost.sort(key=lambda x: x[2])

    # 2. make set(Union-Find 알고리즘을 위한 초기화)
    parent = dict()
    rank = dict()
    for i in range(1, n + 1):
        parent[i] = i
        rank[i] = 0

    # 3. Find(두 node가 서로 같은 그래프인지 판별)
    def find(vertice):
        # path compression(Find 함수를 실행한 노드는 root 노드에 바로 연결) -> 시간복잡도 낮추는 역할
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    # 4. Union(두 트리를 하나의 트리로 합침)
    def union(vertice1, vertice2):
        root1 = find(vertice1)
        root2 = find(vertice2)
        # union-by-rank 기법(높이가 작은 트리를 높이가 큰 트리에 붙임): O(N)를 O(logN)으로 낮춤
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    total_cost, max_cost = 0, 0
    # 5. 사이클 없는 간선 연결
    for c in cost:
        node1, node2, money = c
        if find(node1) != find(node2):
            union(node1, node2)
            total_cost += money
            max_cost = max(max_cost, money)

    # 이 문제는 마을 분리를 한 번해야하기에 가중치가 가장 큰 간선을 빼주면 된다
    return total_cost - max_cost


print(solution())