# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    # root node를 queue에 추가
    queue_list = [start_node]
    visited = []

    # queue의 요소가 모두 pop될 때 까지 반복
    while queue_list:
        # queue의 첫 번째 요소를 pop하여 visited에 추가
        node = queue_list.pop(0)
        visited.append(node)

        # visited에 추가한 요소의 인접 노드를 queue에 추가
        for adj_node in adj_graph[node]:
            if adj_node not in visited:
                queue_list.append(adj_node)
    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!