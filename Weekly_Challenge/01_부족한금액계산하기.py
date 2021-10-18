def solution(price, money, count):
    total = 0
    for i in range(count):
        total += (i + 1) * price
    answer = money - total
    if answer >= 0:
        return 0
    return -answer

p = 3
m = 20
c = 4
print(solution(p, m, c))