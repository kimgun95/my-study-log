def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                answer = False
                break
            top = stack.pop()
            if top != '(':
                answer = False
                break
    if len(stack) != 0 or not answer:
        return False
    return True