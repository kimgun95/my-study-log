from collections import deque

input = "abcabcabcabcdededededede"


def string_compression(string):
    # 앞 문자열 부터 주어진 길이로 잘라 반복되는 횟수를 저장
    queue = deque()
    # 문자열 안에서 문자가 최대 크기로 반복될 수 있는 크기
    size = (len(string) // 2) + 1
    result = [0] * size
    # 문자열의 최소길이를 찾기 위함
    min = 1000

    # 문자열을 1 ~ size 길이로 잘라본다
    for i in range(1, size):
        j = 0
        # 문자열을 i 크기로 자르면서 j는 +i를 통해 반복
        while j < len(string):
            # 문자열의 남은 길이가 i보다 작은 것 처리
            if j + i > len(string):
                queue.append((string[j: len(string)], 1))
                break
            # 첫 문자열 자를 때 처리
            if j == 0:
                queue.append((string[j:j + i], 1))
            # 첫 문자열 아닐 때
            else:
                alpha, count = queue.pop()
                # 이전 문자열과 같을 때
                if alpha == string[j:j + i]:
                    queue.append((alpha, count + 1))
                # 같지 않을 때
                else:
                    queue.append((alpha, count))
                    queue.append((string[j:j + i], 1))
            j += i

        # 자른 문자열과 반복 횟수를 저장한 queue를 pop을 통해 결과 도출
        while queue:
            alpha, count = queue.popleft()
            if count == 1:
                result[i] += len(alpha)
            else:
                result[i] += (len(alpha) + (count // 10) + 1)
        # 최솟값 갱신
        if min > result[i]:
            min = result[i]

    return min


print(string_compression(input))  # 14 가 출력되어야 합니다!
