from collections import deque

balanced_parentheses_string = "()))((()"


def get_correct_parentheses(balanced_parentheses_string):
    if len(balanced_parentheses_string) == 0:
        return balanced_parentheses_string
    left, right = 0, 0
    u_string = ""
    v_string = ""
    result_string = ""

    # 균형잡힌 괄호 문자열 찾기
    for i in range(len(balanced_parentheses_string) + 1):
        if i == 0:
            if balanced_parentheses_string[i] == "(":
                left = 1
            else:
                right = 1
        # 괄호 갯수가 같을 때 break
        elif left == right:
            break
        elif balanced_parentheses_string[i] == "(":
            left += 1
        else:
            right += 1

    # 문자열을 2개로 나눈다
    u_string = balanced_parentheses_string[0:i]
    v_string = balanced_parentheses_string[i:len(balanced_parentheses_string)]

    queue = deque()
    check = 1
    # 올바른 괄호 문자열인지 체크
    for i in range(len(u_string)):
        if u_string[i] == "(":
            queue.append("(")
        elif queue and queue.pop() == "(":
            continue
        else:
            check = 0

    # 올바른 괄호 문자열이 아니라면 아래 과제 수행
    if check == 0:
        empty_string = "("
        empty_string += get_correct_parentheses(v_string)
        empty_string += ")"
        # 앞, 뒤 문자 제거
        u_string = u_string[1:-1]
        # (, )를 서로 바꾸는 과정
        replaced_u_string = ""
        for j in range(len(u_string)):
            if u_string[j] == "(":
                replaced_u_string += ")"
            else:
                replaced_u_string += "("
        empty_string += replaced_u_string
        return empty_string

    # 올바른 괄호 문자열이면 결과 문자열에 저장 및 뒤 문자열 탐색
    result_string += u_string
    result_string += get_correct_parentheses(v_string)

    return result_string


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
