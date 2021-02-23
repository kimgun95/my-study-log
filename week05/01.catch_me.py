from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    visited = [{} for _ in range(200001)]
    queue = deque()
    queue.append(brown_loc)

    while cony_loc < 200000:
        time += 1
        cony_loc += time

        for i in range(0, len(queue)):
            brown_loc = queue.popleft()

            new_position = brown_loc - 1
            if new_position >= 0 and time not in visited[new_position]:
                visited[new_position][time] = True
                queue.append(new_position)

            new_position = brown_loc + 1
            if new_position <= 200000 and time not in visited[new_position]:
                visited[new_position][time] = True
                queue.append(new_position)

            new_position = brown_loc * 2
            if new_position <= 200000 and time not in visited[new_position]:
                visited[new_position][time] = True
                queue.append(new_position)

        if time in visited[cony_loc]:
            return time
    return False


print(catch_me(c, b))  # 5가 나와야 합니다!