def solution(queue1, queue2):
    q = queue1 + queue2
    val = sum(q)
    if val % 2 == 1:
        return -1
    val //= 2
    l = r = 0
    res = q[0]
    while l <= r:
        if res == val:
            break
        if res > val:
            res -= q[l]
            l += 1
        else:
            r += 1
            if r < len(q):
                res += q[r]
            else:
                return -1
    if res != val:
        return -1
    answer = 0
    if r < len(queue1) - 1:
        answer = (r - l + 1) * 2 + (len(queue1) - r - 1) + len(queue2) * 2
        return answer
    for i in range(len(q)):
        if i < l:
            if i < len(queue1):
                answer += 1
            else:
                answer += 2
        elif l <= i <= r:
            if i >= len(queue1):
                answer += 1
    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]	))
print(solution([1, 1], [1, 5]))
print(solution([3, 1, 1], [1, 1, 1]))