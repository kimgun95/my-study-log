# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 스택에 자식 쌍을 하나의 규칙으로 넣어주는 것 -> 이 문제의 근본 해결책이 된다(dynamic programming)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            # 두 값이 모두 null이면 비교할 것이 없으니 다음 스택 진행
            if left is None and right is None:
                continue
            # 하나만 null이면 false 반환
            if left is None or right is None:
                return False
            # 둘 다 값일 때 비교
            # 같다면 스택 추가, 이때 스택에 아래와 같은 쌍으로 넣어야 함 -> dp 개념
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        # 모든 비교가 잘 끝났다면 true 반환
        return True
