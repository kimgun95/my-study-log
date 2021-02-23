from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    visited = [{} for _ in range(200001)]

    # 큐에 브라운의 모든 위치들을 저장할 예정
    queue = deque()
    queue.append(brown_loc)

    # 코니의 위치는 계속 증가함으로 max값을 초과하지 않게 함
    while cony_loc <= 200000:
        # 시간과 코니위치 증가
        time += 1
        cony_loc += time

        # 시간마다 브라운이 갈 수 있는 모든 위치를 찾어 visited와 queue에 저장
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

        # 해당 시간에 코니의 위치가 visited에 저장되어 있다면 time 반환
        if time in visited[cony_loc]:
            return time
    return False


print(catch_me(c, b))  # 5가 나와야 합니다!