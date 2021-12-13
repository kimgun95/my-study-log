# 유명한 괄포 판별 문제
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                target = stack.pop()
                if (c == ')' and target == '(') or (c == '}' and target == '{') or (c == ']' and target == '['):
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True