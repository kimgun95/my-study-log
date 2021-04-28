stack_DFS = []
stack_BFS = []


def DFS(N, start, st, visited):
    visited[start] = 1
    stack_DFS.append(start)
    for i in range(1, N + 1):
        if visited[i] == 0 and st[start][i] == 1:
            DFS(N, i, st, visited)


def BFS(N, start, st, visited):
    visited[start] = 1
    queue = [start]
    while queue:
        num = queue[0]
        stack_BFS.append(num)
        del queue[0]
        for i in range(1, N + 1):
            if visited[i] == 0 and st[num][i] == 1:
                queue.append(i)
                visited[i] = 1


def sol():
    N, M, V = map(int, input().split())
    st = [[0] * (N + 1) for i in range(N + 1)]
    visited = [0 for i in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        st[x][y] = 1
        st[y][x] = 1

    DFS(N, V, st, visited)
    visited = [0 for i in range(N + 1)]
    BFS(N, V, st, visited)
    print(" ".join(map(str, stack_DFS)))
    print(" ".join(map(str, stack_BFS)))


sol()