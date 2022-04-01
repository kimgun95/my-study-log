# 난 이게 three pointer로 해야하는 건가.. 싶어서 엄두도 못냈다
# 그러나 two pointer로 충분히 해결할 수 있었음. 반복문을 잘 생각해서 경우를 따지는 아이디어가 중요했다
def is_valid(l, r, s):
    if r >= s or l < 0:
        return False
    return True


def solution(cookie):
    answer = 0
    length = len(cookie)
    for idx in range(length - 1):
        left, right = idx, idx + 1
        left_size, right_size = cookie[left], cookie[right]
        while True:
            if left_size > right_size:
                right += 1
                if not is_valid(left, right, length):
                    break
                right_size += cookie[right]
            elif left_size < right_size:
                left -= 1
                if not is_valid(left, right, length):
                    break
                left_size += cookie[left]
            else:
                answer = max(answer, left_size)
                left -= 1
                right += 1
                if not is_valid(left, right, length):
                    break
                right_size += cookie[right]
                left_size += cookie[left]
    return answer


print(solution([1,1,2,3]))
print(solution([1,2,4,5]))