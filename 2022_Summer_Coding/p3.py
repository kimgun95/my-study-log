def solution(line):
    answer = []
    left_y, left_x = 1, 0
    right_y, right_x = 1, 9

    def location(c):
        if '0' <= c <= '9':
            if c == '0':
                return [0, 9]
            return [0, int(c) - 1]
        if c == 'Q':
            return [1, 0]
        if c == 'W':
            return [1, 1]
        if c == 'E':
            return [1, 2]
        if c == 'R':
            return [1, 3]
        if c == 'T':
            return [1, 4]
        if c == 'Y':
            return [1, 5]
        if c == 'U':
            return [1, 6]
        if c == 'I':
            return [1, 7]
        if c == 'O':
            return [1, 8]
        if c == 'P':
            return [1, 9]

    for l in line:
        y, x = location(l)
        l_x, r_x = abs(x - left_x), abs(x - right_x)
        l_dist = abs(y - left_y) + l_x
        r_dist = abs(y - right_y) + r_x
        if l_dist < r_dist:
            answer.append(0)
            left_y, left_x = y, x
        elif l_dist > r_dist:
            answer.append(1)
            right_y, right_x = y, x
        else:
            if l_x < r_x:
                answer.append(0)
                left_y, left_x = y, x
            elif l_x > r_x:
                answer.append(1)
                right_y, right_x = y, x
            else:
                if x <= 4:
                    answer.append(0)
                    left_y, left_x = y, x
                else:
                    answer.append(1)
                    right_y, right_x = y, x
    return answer



print(solution("Q4OYPI"))