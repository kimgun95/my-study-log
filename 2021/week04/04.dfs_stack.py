# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    # root 노드를 stack에 추가
    stack_list = [start_node]
    visited = []

    # stack에 요소들이 모두 pop 될 때 까지 반복
    while stack_list:
        # stack에서 pop한 node를 visited에 추가
        node = stack_list.pop()
        visited.append(node)
        # node의 인접 노드를 stack에 추가
        for adjacent_node in adjacent_graph[node]:
            if adjacent_node not in visited:
                stack_list.append(adjacent_node)
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!