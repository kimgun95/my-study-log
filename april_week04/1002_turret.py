import math


def turret(num):
    for i in range(num):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        # 두 점이 같은 경우
        if x1 == x2 and y1 == y2:
            if r1 == r2:
                print(-1)
            else:
                print(0)
        # 두 점이 서로의 반경에 포함되지 않는 경우
        elif distance > r1 and distance > r2:
            if distance < r1 + r2:
                print(2)
            elif distance == r1 + r2:
                print(1)
            else:
                print(0)
        # 한 점이 상대방의 반경에 포함되는 경우
        else:
            if distance == abs(r1 - r2):
                print(1)
            elif distance < abs(r1 - r2):
                print(0)
            else:
                print(2)


turret(int(input()))