def solution(A, B):
    answer = 0
    length = len(A)
    C = [-1 for _ in range(length)]
    for i in range(length):
        if A[i] == B[i]:
            C[i] = A[i]
        elif A[i] > B[i]:
            C[i] = A[i]
        else:
            C[i] = B[i]
    C.sort()
    if C[0] != 1:
        answer = 1
    else:
        flag = 0
        for i in range(length-1):
            if C[i+1] - C[i] >= 2:
                answer = C[i] + 1
                flag = 1
                break
        if flag == 0:
            answer = C[-1] + 1
    return answer

print(solution([1,2,4,3],[1,3,2,3]))
print(solution([3,2,1,6,5],[4,2,1,3,3]))
print(solution([1,2],[1,2]))
