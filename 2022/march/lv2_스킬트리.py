def solution(skill, skill_trees):
    answer = 0
    s = list(skill)
    for sk in skill_trees:
        word = ""
        for idx in range(len(sk)):
            if sk[idx] in s:
                word += sk[idx]
        length = len(word)
        if skill[:length] == word:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))