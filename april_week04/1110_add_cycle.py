def add_cycle(number):
    count = 0
    before = number
    while True:
        if before < 10:
            cal_num = before
        else:
            cal_num = before // 10 + before % 10
        after = before % 10 * 10 + cal_num % 10
        count += 1
        before = after
        if number == after:
            return count


# 26은 4, 1은 60 출력
print(add_cycle(int(input())))