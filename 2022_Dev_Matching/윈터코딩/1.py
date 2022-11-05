def solution(line):
    answer = ''
    idx = 0
    length = len(line)
    while idx < length:
        if idx == length - 1 or line[idx] != line[idx+1]:
            answer += line[idx]
        else:
            while idx < length-1 and line[idx] == line[idx+1]:
                if idx+1 == length:
                    break
                idx += 1
            answer += line[idx] + '*'
        idx += 1

    return answer



print(solution("aabbbc"))
print(solution("aabbbccccc"))
print(solution("hellllllo"))
print(solution("wonderful"))