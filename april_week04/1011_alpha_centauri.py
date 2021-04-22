import math


def alpha_centauri(number):
    for i in range(0, number):
        start, end = map(int, input().split())
        distance = end - start
        sqrt_num = int(math.sqrt(distance))
        if distance == math.pow(sqrt_num, 2):
            print(sqrt_num * 2 - 1)
        elif distance >= (math.pow(sqrt_num, 2) + 1) and (distance <= math.pow(sqrt_num, 2) + sqrt_num):
            print(sqrt_num * 2)
        else:
            print(sqrt_num * 2 + 1)


alpha_centauri(int(input()))