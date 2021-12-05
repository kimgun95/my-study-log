def solution(drum):
    answer = 0
    length = len(drum)

    def go(depth, idx, star):
        if depth >= length:
            nonlocal answer
            answer += 1
            return
        if idx < 0 or idx >= length:
            return
        if drum[depth][idx] == '#':
            go(depth + 1, idx, star)
        elif drum[depth][idx] == '>':
            go(depth, idx + 1, star)
        elif drum[depth][idx] == '<':
            go(depth, idx - 1, star)
        elif star == 1:
            return
        else:
            go(depth + 1, idx, star + 1)

    for i in range(length):
        go(0, i, 0)

    return answer


print(solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"]))