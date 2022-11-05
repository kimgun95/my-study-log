def solution(n, student, point):
    answer = 0
    rank = []
    for i in range(n):
        rank.append([0, -(i+1)])
    length = len(student)
    for i in range(length):
        studentIdx = student[i]
        studentPoint = point[i]
        beforeIdx = -1
        for j in range(n):
            if -studentIdx == rank[j][1]:
                beforeIdx = j
                break
        rank[beforeIdx][0] += studentPoint
        rank.sort(reverse=True)
        if beforeIdx < n//2:
            for j in range(n//2,n):
                if -studentIdx == rank[j][1]:
                    answer+=1
        else:
            for j in range(n//2):
                if -studentIdx == rank[j][1]:
                    answer+=1
    return answer



print(solution(6, [6, 1, 4, 2, 5, 1, 3, 3, 1, 6, 5], [3, 2, 5, 3, 4, 2, 4, 2, 3, 2, 2]))
print(solution(10, [3, 2, 10, 2, 8, 3, 9, 6, 1, 2], [3, 2, 2, 5, 4, 1, 2, 1, 3, 3]))