def solution(S, C):
    answer = 0
    length = len(S)
    idx = 0

    def calculate(start, end):
        maxValue = max(C[start:end+1])
        flag = 0
        cost = 0
        for index in range(start,end+1):
            if C[index] != maxValue or flag == 1:
                cost += C[index]
            else:
                flag = 1
        return cost

    while idx < length-1:
        # print("idx", idx)
        if S[idx] == S[idx+1]:
            j = idx
            while j < length-1:
                # print("j", j)
                if S[j] == S[j+1]:
                    j += 1
                else:
                    break
            answer += calculate(idx, j)
            idx = j + 1
        else:
            idx += 1
    return answer

print(solution('abccbd', [0,1,2,3,4,5]))
print(solution('aabbcc', [1,2,1,2,1,2]))
print(solution('aaaa', [3,4,5,6]))
print(solution('ababa', [10,5,10,5,10]))