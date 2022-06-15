# arr 배열에서 가장 작은 수를 찾아 제거하기
# 빈 배열을 리턴할 때는 -1 리턴하기
def solution(arr):
    answer = []
    min_val = min(arr)
    for i in range(0, len(arr)):
        if arr[i] == min_val:
            answer = arr[:i] + arr[i + 1:]
            break

    if len(answer) == 0:
        return [-1]
    return answer
