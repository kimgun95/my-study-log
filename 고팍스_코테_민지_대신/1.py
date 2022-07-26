def solution(A, B):
    num = (A+B)//4
    while num > 0:
        cnt = (A // num) + (B // num)
        if cnt >= 4:
            break
        num -= 1
    return num

print(solution(10,21))
print(solution(13,11))
print(solution(2,1))
print(solution(1,8))