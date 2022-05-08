from itertools import permutations

loc = []
graph = []
go = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = 0


def dfs(ex):
    for i in range(len(loc)):
        graph[loc[i][0]][loc[i][1]] = ex[i]
    h, w = len(graph), len(graph[0])
    visit = [[0] * w for _ in range(h)]
    total = []
    check = set()
    for y in range(h):
        for x in range(w):
            if visit[y][x] == 1:
                print('hu')
                continue
            check.add(graph[y][x])
            s = [[y, x, graph[y][x]]]
            while s:
                cur_y, cur_x, val = s.pop()
                if visit[y][x] == 1:
                    continue
                visit[cur_y][cur_x] = 1
                print(visit)

                total.append(val)
                for g in go:
                    ny, nx = cur_y + g[0], cur_x + g[1]
                    if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == val:
                        s.append([ny, nx, val])
                        check.add(val)

    print(total)
    print(check)
    if total == 3 and len(check) == 3:
        return 1

    return 0


def make_case(arr, size):
    if len(arr) == size:
        global answer
        answer += dfs(arr)
        return
    for alpha in ['a', 'b', 'c']:
        arr.append(alpha)
        make_case(arr, size)
        arr.pop()
    return


def solution(grid):
    h, w = len(grid), len(grid[0])

    for g in grid:
        graph.append(list(g))

    for y in range(h):
        for x in range(w):
            if graph[y][x] == '?':
                loc.append([y, x])
    N = len(loc)
    make_case([], N)
    return answer


print(solution(["??b", "abc", "cc?"]))
# print(solution(["abcabcab","????????"]))
# print(solution(["aa?"]))