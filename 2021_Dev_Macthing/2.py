def week(name):
    if name == "MON":
        return 5
    elif name == "TUE":
        return 4
    elif name == "WED":
        return 3
    elif name == "THU":
        return 2
    elif name == "FRI":
        return 1
    elif name == "SUN":
        return 6
    return 0


def solution(leave, day, holidays):
    answer = -1
    start = 1
    cal = [0] * 31
    if day == "SUN":
        cal[1] = 1
    start += week(day)
    while start <= 30:
        cal[start] = 1
        if start + 1 <= 30:
            start += 1
            cal[start] = 1
        start += 6
    for i in holidays:
        cal[i] = 1
    print(cal)
    return answer


l = 4
d = "FRI"
h = [6, 21, 23, 27, 28]
print(solution(l, d, h))